from cffi import FFI
import os

ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    typedef struct { int x, y; } point_t;
    int do_stuff(point_t p);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_sample_cffi",
"""
     #include "sample.h"   // the C header of the library
""",
     library_dirs=['./sample'],
     include_dirs=['./sample'],
     libraries=['sample'],
     extra_link_args=['-Wl,-rpath=' + os.path.abspath('./')])   # library name, for the linker

# if __name__ == "__main__":
#     ffibuilder.compile(verbose=True)
