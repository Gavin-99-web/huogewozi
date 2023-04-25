def cal(a, b, c):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a in range(-99, 100) and b in range(-99, 100):
            if c == "+":
                return a+b
            elif c == "-":
                return a-b
            elif c == "*":
                return a*b
            elif c == "/":
                return a/b
        else:
            return "计算的数字超过-99到99范围"
    else:
        return "输入的值存在非数字"

if __name__ == '__main__':
    a = input("请输入第一个数字（范围为-99到99）:")
    b = input("请输入第二个数字（范围为-99到99）:")
    c = input("请输入运算符号（+、-、*、、/、）:")
    num = cal(a, b, c)
    print(num)