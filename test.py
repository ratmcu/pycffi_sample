from _sample_cffi import ffi, lib
from _sample_cffi.lib import do_stuff

def get_point_t(x, y):
    p = ffi.new('point_t[]',1)
    p[0].x = x
    p[0].y = y
    return p[0] 


print(do_stuff(get_point_t(1, 2)))