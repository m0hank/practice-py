def dispatch_if(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mul":
        return x * y
    elif operator == "div":
        return x / y
    else:
        return None

print(dispatch_if('mul', 10, 4))