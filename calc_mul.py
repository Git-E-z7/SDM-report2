#!/usr/bin/python3

import re

def calc(A, B):
        # Accept only integers in [1, 999]. Otherwise return -1.
        # Note: bool is a subclass of int in Python, so exclude it explicitly.
        if isinstance(A, bool) or isinstance(B, bool):
                return -1
        if not isinstance(A, int) or not isinstance(B, int):
                return -1
        if not (1 <= A <= 999) or not (1 <= B <= 999):
                return -1
        return A * B


def main ():
        matchstring = ''
        while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                # keep interactive mode usable: try parse to int, otherwise pass raw (then calc returns -1)
                try:
                        A_in = int(A)
                        B_in = int(B)
                except Exception:
                        A_in = A
                        B_in = B
                print ('input A * input B = ', calc(A_in, B_in))

if __name__ == '__main__':
        main()

