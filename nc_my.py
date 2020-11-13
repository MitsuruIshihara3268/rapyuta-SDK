#!/usr/bin/env python

from __future__ import print_function
import subprocess
import datetime



def nc_check():

    haproxy = {'name': 'haproxy', 'ip': '104.46.219.63', 'ports': ['80', '443']}
    salt_fallback = {'name': 'salt_fallback', 'ip': '13.78.30.255', 'ports': ['4505', '4506']}
    salt_main = {'name': 'Salt_Main', 'ip': '104.46.218.87', 'ports': ['4505', '4506']}
    webssh_1_fallback = {'name': 'Webssh_1_fallback', 'ip': '13.78.44.90', 'ports': ['10022']}
    webssh_2_fallback = {'name': 'Webssh_2_fallback', 'ip': '13.78.9.249', 'ports': ['10022']}
    webssh_2_primary = {'name': 'Webssh_2_primary', 'ip': '104.46.218.87', 'ports': ['10022']}
    router_2 = {'name': 'Router_2', 'ip': '40.115.155.91', 'ports': ['80', '443', '4505', '4506', '10022']}
    hitachi_reserve_basic2 = {'name': 'hitachi_reserve_basic2', 'ip': '13.78.23.215', 'ports': ['80', '443', '4505', '4506', '10022']}

    #destinations = [router_2, hitachi_reserve_basic2]
    destinations = [haproxy, salt_fallback, salt_main, webssh_1_fallback, webssh_2_fallback, webssh_2_primary, router_2, hitachi_reserve_basic2]


    with open('nc_check.log', 'a') as f:

        f.write('\n' + str(datetime.datetime.now()) + '\n')

        for destination in destinations:
            ip_address = destination['ip']
            des_name = destination['name']

            f.write('\n')

            for port in destination['ports']:

                nc_tcp_cmd = ['nc', '-z', ip_address, port, '-w' '10']
                nc_udp_cmd = ['nc', '-z', '-u', ip_address, port, '-w', '10']


                try:
                    f.write('checking for ' + str(des_name) + ' tcp ' + str(port) + '\n')
                    subprocess.check_call(nc_tcp_cmd, stdout=f)
                    f.write('success\n')

                except:
                    f.write('###nc for ' + str(des_name) + ' tcp ' + str(port) + ' failed###\n')


                try:
                    f.write('checking for ' + str(des_name) + ' udp ' + str(port) + '\n')
                    subprocess.check_call(nc_udp_cmd, stdout=f)
                    f.write('success\n')

                except:
                    f.write('###nc for ' + str(des_name) + ' udp ' + str(port) + ' failed###\n')



                """
                print('checking for', des_name, 'tcp port')
                command_tcp = subprocess.call(nc_tcpf.write)  #later POPEN


                if command_tcp != 0:            # exit code is in subprocess.call itself
                    print('---------\n checkinng tcp failed\n ---------')

                print('checking for', des_name, 'udp port')
                command_udp = subprocess.call(nc_udp)

                if command_udp != 0:
                    print('---------\n checkinng udp failed\n---------')

                """




    """
    # server - server   from froklift  
    command4 = ['ssh', 'aifl@@192.168.10.202', 'iperf', '-s', '&']
    subprocess.call(command4)

    command5 = ['iperf', '-c', '192.168.10.202']
    subprocess.call(command5)

    command6 = ['ssh', 'aifl@192.168.10.202', 'pkill', 'iperf']
    subprocess.call(command6)
    print('--------------------------\n killed iperf server process')
    
    """

if __name__ == '__main__':
    nc_check()




"""
with open('test.log', 'a') as t:
    proc = subprocess.call(['nc', '-vz', '40.115.155.91', '80'])
    t.write(str(proc))

with open('test2.log', 'a') as l:
    subprocess.call(['ls', '-la'], stdout=l)

subprocess.call('ls')


cmd = subprocess.check_output(['ls'])
print(cmd)

"""