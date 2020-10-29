def memory(n):
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f


def group_by(s, fn):
    grouped = {}
    for e in s:
        key = fn(e)
        
        if key in grouped.keys() :
            # print('if called')
            values= grouped[key]
            values.append(e)
        else:
            # print('else called')
            grouped[key] = [e]
    return grouped
        
        
def add_this_many(x, el, s):
   s_len=len(s)
   idx=0
   while idx<s_len:
       if s[idx]==x:
           s.append(el)
       idx+=1


def filter(iterable, fn):
    for i in iterable:
        if fn(i):
            yield i


def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1

def merge(a, b):
    yield next(a)