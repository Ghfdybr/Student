def divide(first, second):
    '''На ноль делить можно!!!'''
    from math import inf
    if second == 0:
        return inf
    else:
        return(first/second)