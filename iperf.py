#!/usr/bin/env python

from __future__ import print_function
import subprocess
import os
import time


# sever and client information need to be changed according to environment
def iperf_check():
    DEVNULL = open(os.devnull, 'wb')

    print('startinng server iperf')
    iperf_server_cmd = ['ssh', 'mitsuru@192.168.56.101', 'iperf', '-s']
    subprocess.Popen(iperf_server_cmd, stdout=DEVNULL)

    time.sleep(5)

    print('starting client iperf')
    iperf_client_cmd = ['iperf', '-c', '192.168.56.101']
    subprocess.call(iperf_client_cmd)

    kill_server_iperf = ['ssh', 'mitsuru@192.168.56.101', 'pkill', 'iperf']
    subprocess.call(kill_server_iperf)
    print('--------------------------\n killed iperf server process')


if __name__ == '__main__':
    iperf_check()