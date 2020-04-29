"""
This program simulates two-stack algorithm. 

Assumption: the expression is fully parentesized!!
"""

def cal_helper(value1, value2, operator):
    if operator=="+":
        return value1+value2
    elif operator=="*":
        return value1*value2
    elif operator=="-":
        return value1-value2
    else:
        raise ValueError("Invalid oeprator")

def calculator(expression):
    operator_stack=[]
    number_stack = []

    for char in expression:
        if char in ["+", "-", "*"]:
            operator_stack.append(char)
        elif char=="(":
            pass
        elif char==")":
            value1 = number_stack.pop()
            value2 = number_stack.pop()
            operator = operator_stack.pop()
            result = cal_helper(value1, value2, operator)
            number_stack.append(result)
        else:
            number_stack.append(int(char))
    
    return number_stack[0]


if __name__ == "__main__":
    print(calculator("((1+2)*(4+5))"))
