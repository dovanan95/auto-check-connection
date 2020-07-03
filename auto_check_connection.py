import easygui
import socket
import os
import subprocess
from datetime import datetime
import threading
import time

n = 1

#m= input('nhap so lan ping: ')
#m1 = int(m)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
now = datetime.now()

cr_now = now.strftime('%b-%d-%Y-%H-%M-%S')

path = easygui.fileopenbox()

with open(path, 'r') as f:
    data = f.read()
    #print (data)
    data_arr = data.split('\n')
    #print (data_arr[0])
    filelog = open("ping_logging "+ str(cr_now) +".txt","w")
    #filelog.write('hello')
    #filelog.close()
    while(True):
        #filelog = open("ping_logging "+ str(cr_now) +".txt","w")
        for line in data_arr:
            #filelog = open("ping_logging "+ str(cr_now) +".txt","w")
            server_ip = line
            #print(server_ip)
                #rep = os.system('ping -n ' + str(n) + " " + server_ip)
                #command = ['ping -n ', str(n), server_ip]
            command_2 = 'ping ' + server_ip
                #p = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                filelog = open("ping_logging "+ str(cr_now) +".txt","a")
                now_loop = datetime.now()

                cr_now_loop = now_loop.strftime('%b-%d-%Y-%H-%M-%S')
                q = subprocess.check_output(command_2, shell=True)
                #q = subprocess.Popen(command,stdout = subprocess.PIPE).communicate()[0]
                q_result = q.decode("utf-8")
                q_anal = q_result.split('\n')
                q_string = q_anal[2]
                q_string_anal = q_string.split(' ')
                byte = q_string_anal[3]
                time = q_string_anal[4]
                TTL = q_string_anal[5]
                if('bytes' in byte or 'time' in time or 'TTL' in TTL):    
                    q_result_out = (str(cr_now_loop)+ ": "+ server_ip + " " + byte+ " " +time+ " "+TTL +" OK \n" )
                else:
                    q_result_out = (str(cr_now_loop)+ ": "+ server_ip + " " + byte+ " " +time+ " "+TTL +" NG \n" )

                filelog.write(q_result_out)
                print(q_result_out)
                filelog.close() 
                     
            except:
                filelog = open("ping_logging "+ str(cr_now) +".txt","a")
                filelog.write(str(cr_now_loop)+ ": "+ server_ip + ' request time out '+ " NG" '\n')
                print(str(cr_now_loop)+ ": "+ server_ip + ' request time out '+ " NG" '\n')
                filelog.close() 

   
