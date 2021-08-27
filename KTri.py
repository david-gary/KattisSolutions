a, b, c = map(int, input().split())
def equation(a, b, c):
    if a + b == c:
        return str(a) + "+" + str(b) + "=" + str(c)
    elif a - b == c:
        return str(a) + "-" + str(b) + "=" + str(c)
    elif a / b == c:
        return str(a) + "/" + str(b) + "=" + str(c)
    elif a * b == c:
        return str(a) + "*" + str(b) + "=" + str(c)
    elif b + c == a:
        return str(a) + "=" + str(b) + "+" + str(c)
    elif b - c == a:
        return str(a) + "=" + str(b) + "-" + str(c)
    elif b / c == a:
        return str(a) + "=" + str(b) + "/" + str(c)
    elif b * c == a:
        return str(a) + "=" + str(b) + "*" + str(c)
    else:
        return None
print(equation(a, b, c))