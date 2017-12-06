class SeqLike(object):
    def __init__(self):
        print('init a SeqLike')
        return

    def __iter__(self):
        yield 1
        yield 99
        raise StopIteration

if __name__ == '__main__':
    n = SeqLike()
    a, b = n
    print('a=',a)
    print('b=',b)
