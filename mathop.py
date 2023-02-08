def divide(first_num, second_num):
    try:

        return first_num / second_num

    except Exception as e:
        raise e


def multiply(first_num, second_num):
    try:

        return first_num * second_num

    except Exception as e:
        raise e


def subtract(first_num, second_num):
    try:

        return first_num - second_num

    except Exception as e:
        raise e


def add(first_num, second_num):
    try:

        return first_num + second_num

    except Exception as e:
        raise e


def raise_nums(first_num, second_num):
    try:

        return first_num ** second_num

    except Exception as e:
        raise e


def floor_division(first_num, second_num):
    try:

        return first_num // second_num

    except Exception as e:
        raise e


def multi_division(stack: list):
    try:

        result = float(stack[0])

        for num in stack[1:]:

            result /= float(num)

        return result

    except Exception as e:
        raise e


def multi_multiply(stack: list):
    try:

        result = float(stack[0])

        for num in stack[1:]:

            result *= float(num)

        return result

    except Exception as e:
        raise e


def anti_sum(stack: list):
    try:

        result = float(stack[0])

        for num in stack[1:]:

            result -= float(num)

        return result

    except Exception as e:
        raise e


def multi_raise(stack: list):
    try:

        result = float(stack[0])

        for num in stack[1:]:
            result **= float(num)

        return result

    except Exception as e:
        raise e


def multi_floor_division(stack: list):
    try:

        result = float(stack[0])

        for num in stack[1:]:

            result //= float(num)

        return result

    except Exception as e:
        raise e

