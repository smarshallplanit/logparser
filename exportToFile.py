import re
import time
from collections import OrderedDict
import csv
from itertools import count
from time import strftime

from pip._vendor.msgpack.fallback import xrange

log_file_path = r"C:\Users\smarshall\Desktop\python\sfbios.log"
export_file_path = r"C:\Users\smarshall\Desktop\logs\filtered"

time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

file = "\\" + "Parser Output " + time_now + ".txt"
export_file = export_file_path + file

regex = '(<property name="(.*?)">(.*?)<\/property>)'
dateRegex = '(^[0-9]{4}-[0-9]{2}-[0-9]{2})'
timeRegex = '([\d]{1,2}:[\d]{1,2}:[\d]{1,2}.[\d]{1,3})'
read_line = False

with open(log_file_path,"r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(timeRegex,line,re.S):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)



    else:
        data = file.read()
        for match in re.finditer(timeRegex, data, re.S):
            match_text = match.group()
            match_list.append(match_text)

file.close()


with open(export_file,"w+") as file:
    file.write("Exported Data:\n")
    match_list_clean = list(set(match_list))
    for item in xrange(0,len(match_list_clean)):
        print(match_list_clean[item])
        file.write(match_list_clean[item]+"\n")
file.close()
