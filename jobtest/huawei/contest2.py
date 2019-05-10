def getResult(input):
    # input = list(input)
    stack = []
    num_stack = []
    tmp = ""
    result = ""
    length = len(input)
    my_dict = {')':'(',']':'[','}':'{'}

    for i in range(length):
        # print(stack)
        # print(num_stack)
        if input[i] == '(':
            stack.append(input[i])
        elif input[i] in my_dict.keys():
            pop = ""
            while stack and stack[-1]!=my_dict[input[i]] :
                pop+=stack.pop()
            pop = pop[::-1]
            stack.pop()
            num = num_stack.pop()
            for i in range(num):
                for j in pop:
                    stack.append(j)


        elif ord("0") < ord(input[i]) <= ord("9"):
            num_stack.append(int(input[i]))
        else:
            stack.append(input[i])


    return "".join(stack[::-1])

if __name__ == '__main__':

    inputs = input().strip()
    res = getResult(inputs)

    print(res)
