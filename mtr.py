#!/usr/bin/env python

from __future__ import print_function
import subprocess


def mtr_check():
    mtr_cmd = ['mtr', '-rw', 'console.rapyuta.io']
    with open('mtr_output.log', 'a') as f:
        subprocess.call(mtr_cmd, stdout=f)



if __name__ == '__main__':
    mtr_check()