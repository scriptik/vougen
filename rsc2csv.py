#### Convert the rsc File to csv 
#### PEZHMAN SHAFIGH  2019
import os
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
for i in range (5,lni,5):
    #print(words[i])
    #print(words[i+1])
    #print(words[i+2])
    #print(words[i-1])
    print(words[i]+words[i+1]+words[i+2]+words[i-1])
print(len(words))
#num_date = len(words)+1
#num_time = len(words)+8
#x = range(1, num_date, 9)
#y = range(8, num_time, 9)
#
#log_time = []
#kb = []
#for i in x:
#    log_time.append(words[i])
#for j in y:
#    kb.append(words[j])
#z = range(0, num_lines)

#now = datetime.datetime.now()
##filename=str(now.year)+str(now.month)+str(now.day)
#filename=now.strftime("%Y_%m_%d")+"RouterLOG"+".csv"
##outputFile = open('output.csv', 'w', newline='')
#outputFile = open(filename, 'w', newline='')
#outputWriter = csv.writer(outputFile)
#outputWriter.writerow(['Year', 'Month', 'Day', 'Hour', 'Byte'])
#
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
