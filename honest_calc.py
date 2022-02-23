def check_number(number):
    return all([i in "1234567890." for i in number]) \
           and number.count(".") <= 1 \
           and number.count("-") <= 1 \
           or number == "M"


def check_ops(operand):
    return operand in "*/+-" and len(operand) == 1


def check_division_by_zero(operand, number):
    if number == "M":
        number = str(memory)
    return False if operand == "/" and number == "0" else True


def convert_to_num(number: str):
    if number == "M":
        return memory
    else:
        return float(number)


def one_digit(number):
    return float(number) == int(float(number)) and -10 < float(number) < 10


def check(number_1, ops, number_2):
    if number_1 == "M":
        number_1 = memory
    if number_2 == "M":
        number_2 = memory
    msg = ""
    if one_digit(number_1) and one_digit(number_2):
        msg += msg_6
    if (float(number_1) == 1 or float(number_2) == 1) and ops == "*":
        msg += msg_7
    if (float(number_2) == 0 or float(number_1) == 0) and ops in "*+-":
        msg += msg_8
    if msg != "":
        print(msg_9 + msg)


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


print(msg_0)
result = input().split()
memory = 0
while True:
    while True:
        check(*result)
        if not check_number(result[0]) or not check_number(result[2]):
            print(msg_1)
        elif not check_ops(result[1]):
            print(msg_2)
        elif not check_division_by_zero(result[1], result[2]):
            print(msg_3)
        else:
            break
        print(msg_0)
        result = input().split()
    num_1, num_2 = convert_to_num(result[0]), convert_to_num((result[2]))
    if result[1] == "+":
        answer = num_1 + num_2
    elif result[1] == "-":
        answer = num_1 - num_2
    elif result[1] == "*":
        answer = num_1 * num_2
    else:
        answer = num_1 / num_2
    print(answer)
    question_1 = input(msg_4)
    if question_1 == "y" and not one_digit(answer):
        memory = answer
    elif one_digit(answer) and question_1 == "y":
        res_1 = input(msg_10)
        if res_1 == "y":
            res_2 = input(msg_11)
            if res_2 == "y":
                res_3 = input(msg_12)
                if res_3 == "y":
                    memory = answer
    question_2 = input(msg_5)
    if question_2 == "n":
        break
    print(msg_0)
    result = input().split()
