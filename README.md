## pycffi to use c c++ code in python

Purpose of this repo is to give a sample boiler plate to build a wrapping in python for a c or c++ code. 
more documentation on pycffi: https://cffi.readthedocs.io/en/latest/

# pycffi_sample
how to use a c/c++ shared library with in python using cffi


## building c library

`cmake .`

`make`

## requirements

`python -m pip install cffi`

## building c backend

`python main_builder.py`

`python extended_builder.py`

## testing

`python test.py`

`python e_test.py`
