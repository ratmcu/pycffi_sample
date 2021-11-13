from sample_build import ffibuilder

from cffi import FFI
import os

extended_ffibuilder = FFI()

extended_ffibuilder.include(ffibuilder)


extended_ffibuilder.cdef("""
    int do_more_stuff(point_t p);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
extended_ffibuilder.set_source("_extended_cffi",
"""
     #include "./sample/sample.h"   // the C header of the library
     #include "stdio.h"
     int do_more_stuff(point_t p);

""",
     library_dirs=['./sample','./extended'],
     include_dirs=['./sample'],
     libraries=['sample', 'extended'],
     extra_link_args=['-Wl,-rpath=' + os.path.abspath('./sample')+',-rpath=' + os.path.abspath('./extended')])   # library name, for the linker

if __name__ == "__main__":
    extended_ffibuilder.compile(verbose=True)
