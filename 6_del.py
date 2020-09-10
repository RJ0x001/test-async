def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():

    counter = 0
    summ = 0
    average = 0

    while True:
        try:
            x = yield
        except StopIteration:
            # print('Ku-Ku')
            break
        else:
            counter += 1
            summ += x
            average = round(summ / counter, 2)
    return average


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)
