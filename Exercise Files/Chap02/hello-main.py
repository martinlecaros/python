#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

    x = "una serpiente"
    z = "un lenguage de p"
    print('Python es {}'.format(x))
    print(f'Python es {z}')
    
    if False:
        print('true')
    else:
        print('not true')

if __name__ == '__main__': main()
