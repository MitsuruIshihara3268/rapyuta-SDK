from __future__ import print_function
import subprocess


def speedtest_cli_check():
    command6 = ['./librespeed-cli-linux-amd64', '--local-json', 'run.json']
    # cwd option need to be changed according to environment
    subprocess.call(command6, cwd='/home/mitsuruishihara/speedtest-cli/out')


if __name__ == '__main__':
    speedtest_cli_check()