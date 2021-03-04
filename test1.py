def str_check():
    text = "123+345-123"
    str_list = []
    str_list = text.split("+")
    str_list.append("+")
    print(str_list)

    #逆ポーランド記法による計算
    s = ["123","345","123","*","+"]
    stack = []
    for i in range(len(s)):
        if s[i] == '+':
            stack.append(stack.pop() + stack.pop())
        elif s[i] == '-':
            stack.append(-(stack.pop() - stack.pop()))
        elif s[i] == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(s[i]))
    return stack[-1]



if __name__ == "__main__":
    list1 = str_check()
    print(list1)