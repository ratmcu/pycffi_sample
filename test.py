import _sample_cffi
from _sample_cffi.lib import do_stuff

def get_point_t(x, y):
    p =  _sample_cffi.ffi.new('point_t[]',1)
    p[0].x = x
    p[0].y = y
    return p[0]

p = get_point_t(1, 2)
print(do_stuff(p))


