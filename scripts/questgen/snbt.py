"""Minimal SNBT writer in FTB Quests' layout (tabs, bare keys, typed numbers)."""
import hashlib
import re


class D(float):
    """double -> 1.0d"""


class F(float):
    """float -> 1.0f"""


class L(int):
    """long -> 1L"""


class B(int):
    """byte -> 1b"""


def qid(key: str) -> str:
    """Stable 16-hex id from a readable key, so regenerating keeps player progress."""
    h = hashlib.sha1(f"hearthandhollow:{key}".encode()).hexdigest()[:16].upper()
    return ("0123456789ABCDEF"[int(h[0], 16) & 7]) + h[1:]


_BARE = re.compile(r"^[A-Za-z0-9_.+-]+$")


def _key(k: str) -> str:
    return k if _BARE.match(k) else '"' + k.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def dump(v, ind=0) -> str:
    t = "\t"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, D):
        return f"{float(v)}d"
    if isinstance(v, F):
        return f"{float(v)}f"
    if isinstance(v, L):
        return f"{int(v)}L"
    if isinstance(v, B):
        return f"{int(v)}b"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return f"{v}d"
    if isinstance(v, str):
        return _str(v)
    if isinstance(v, list):
        if not v:
            return "[ ]"
        if all(isinstance(x, str) for x in v):
            if len(v) == 1:
                return "[" + _str(v[0]) + "]"
            inner = "\n".join(t * (ind + 1) + _str(x) for x in v)
            return "[\n" + inner + "\n" + t * ind + "]"
        inner = "\n".join(t * (ind + 1) + dump(x, ind + 1) for x in v)
        return "[\n" + inner + "\n" + t * ind + "]"
    if isinstance(v, dict):
        if not v:
            return "{ }"
        lines = [t * (ind + 1) + _key(k) + ": " + dump(v[k], ind + 1) for k in sorted(v)]
        return "{\n" + "\n".join(lines) + "\n" + t * ind + "}"
    raise TypeError(type(v))


def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(obj) + "\n")
