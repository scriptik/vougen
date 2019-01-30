#### Convert the rsc File to csv 
#### PEZHMAN SHAFIGH  2019
import os
import re
import csv
import datetime

filename = 'users.rsc'
num_lines = sum(1 for line in open(filename))
with open(filename) as file_object:
     string = ''
     for line in file_object:
         #print(line.rstrip())
         string += line.rstrip() +"\n"

print(num_lines)
num_id = num_lines-1
num_id = num_lines-1
lni = num_id*5 #last name id
words = (string.split())
#print(words)
print(len(words))
start = '='
end = ','
for i in range (5,lni,5):
    #print(words[i])
    #print(words[i+1])
    #print(words[i+2])
    #print(words[i-1])
    #print((words[i].split(start))[1].split(end)[0])
    name = ((words[i].split(start))[1].split(end)[0])
    password = ((words[i+1].split(start))[1].split(end)[0])
    server = ((words[i+2].split(start))[1].split(end)[0])
    litime = ((words[i-1].split(start))[1].split(end)[0])
    instr = (name+","+password+","+server+","+litime)
    #print(words[i]+","+words[i+1]+","+words[i+2]+","+words[i-1])
    #instr = (words[i]+","+words[i+1]+","+words[i+2]+","+words[i-1])
    print(instr)

#outputFile = open('output.csv', 'w', newline='')
#outputWriter = csv.writer(outputFile)
#outputWriter.writerow(['Name', 'Password', 'Server', 'UpTime'])
#outputWriter.writerow(instr)
#for k in z:
#    #print((log_time[k])[0:10]+','+(log_time[k])[11:19]+','+kb[k])
#    csv_year = (log_time[k])[0:4]
#    csv_month = (log_time[k])[5:7]
#    csv_day = (log_time[k])[8:10]
#    csv_hour = (log_time[k])[11:13]
#    csv_kb = kb[k]
#    outputWriter.writerow([csv_year ,csv_month ,csv_day ,csv_hour ,csv_kb])
#
#outputFile.close()
