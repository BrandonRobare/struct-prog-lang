def evaluate(ast, env):
    if ast["tag"] == "program":
        for stmt in ast["statements"]:
            evaluate(stmt, env)
    elif ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "string":
        return ast["value"]
    elif ast["tag"] == "identifier":
        return env[ast["value"]]
    elif ast["tag"] == "assign":
        env[ast["target"]["value"]] = evaluate(ast["value"], env)
    elif ast["tag"] == "print":
        values = [evaluate(arg, env) for arg in ast["arguments"]["values"]]
        print(*values)
    elif ast["tag"] == "brobare":
        env["_kentid_"] = "brobare@kent.edu"
    elif ast["tag"] == "block":
        for stmt in ast["statements"]:
            evaluate(stmt, env)
    elif ast["tag"] == "if":
        condition = evaluate(ast["condition"], env)
        if condition:
            evaluate(ast["then"], env)
        elif ast["else"]:
            evaluate(ast["else"], env)
    return None