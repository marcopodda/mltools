import time
from functools import wraps


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %  (f.__name__, args, kw, te-ts))
        return result
    return wrap


def to_hms(secs):
    return time.strftime('%H:%M:%S', time.gmtime(secs))