TOOLS = ["parse", "compare"]
WRITES = ("email", "reject", "hire",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    have = set(s.lower() for s in payload.get("skills") or []); need = set(s.lower() for s in payload.get("required") or []); result = sorted(need - have)
    return {"refused": False, "tools": TOOLS, "missing": result, "wrote": False, "applied": False}
