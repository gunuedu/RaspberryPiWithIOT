#!/usr/bin/env python3
enable_debug = True # or False
def debug(f):
    if enable_debug:
        def callf(*args,**parms):
            value = f(*args,**parms)
            print("debug: %s" % value)
            return value
        return callf
    else:
        return f

@debug
def incr(x):
    return x + 1

print( "incr(5) : %d" % incr(5) )

