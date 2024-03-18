def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass

@coroutine
def subgen():
    while True:
        try:
            massege = yield
        except BlaBlaException:
            print('Ku-ku!!!')
        else:
            print('.......', massege)

@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except BlaBlaException as e:
            g.throw(e)

sg = subgen()
g = delegator(sg)

g.send('OK')
g.throw(BlaBlaException)

















