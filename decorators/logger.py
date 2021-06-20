from datetime import datetime


def first_logging(old):
    time_now = datetime.now()

    def foo(*args, **kwargs):
        with open('logs.txt', 'a') as logs:
            result = old(*args, **kwargs)
            foo_list = [f'Date: {time_now}\n',
                        f'Name: {old.__name__}\n',
                        f'Args: {args}, {kwargs}\n',
                        f'Return: {result}\n\n']
            [logs.write(f'{f}') for f in foo_list]
        return result

    return foo


def logging_fabric(path):

    def second_logging(old):
        time_now = datetime.now()

        def foo(*args, **kwargs):
            if path:
                logs_path = path
            else:
                logs_path = 'logs.txt'
            with open(logs_path, 'a') as logs:
                result = old(*args, **kwargs)
                foo_list = [f'Date: {time_now}\n',
                            f'Name: {old.__name__}\n',
                            f'Args: {args}, {kwargs}\n',
                            f'Return: {result}\n\n']
                [logs.write(f'{f}') for f in foo_list]
            return result

        return foo

    return second_logging


# Tests

# №1
# @first_logging
# def first_test(a, test):
#     return a, test
#
#
# first_test(1, test=123)


# №2
# @logging_fabric(path='logs.txt')
# def second_test(test):
#     return test
#
#
# second_test(test=321)

