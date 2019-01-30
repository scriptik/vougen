#### Convert the (vougen)rsc File to csv 
#### PEZHMAN SHAFIGH  2019
import os
import re
import csv
import datetime

file_in = 'users.rsc'
file_ou = 'users.csv'
num_lines = sum(1 for line in open(file_in))
with open(file_in) as file_object:
     string = ''
     for line in file_object:
         string += line.rstrip() +"\n"

#print(num_lines)
num_id = num_lines-1
num_id = num_lines-1
lni = num_id*5 #last name id
words = (string.split())
#print(len(words))
with open(file_ou, 'w') as file_out:
    file_out.write("Name,Password,Server,UpTime\n")
start = '='
end = ','
for i in range (5,lni,5):
    name = ((words[i].split(start))[1].split(end)[0])
    password = ((words[i+1].split(start))[1].split(end)[0])
    server = ((words[i+2].split(start))[1].split(end)[0])
    litime = ((words[i-1].split(start))[1].split(end)[0])
    instr = (name+","+password+","+server+","+litime)
    #print(instr)
    with open(file_ou, 'a') as file_out:
         file_out.write(instr+"\n")

