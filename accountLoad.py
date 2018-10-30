# Python Script to parse logs

import re
import csv

log_file_path = r"C:\Users\smarshall\Desktop\python\logs\171213_01_accountload.log"

## Regexs ##
datetime = '([0-9]{4}-[0-9]{2}-[0-9]{2})(?:T)([\d]{1,2}:[\d]{1,2}:[\d]{1,2})'
time = '((?=\w)[\d]{1,2}:[\d]{1,2}:[\d]{1,2})'
target = r'(?!\b Source\s latency\s\b)[0-9]{1,2}(?=\s\bseconds\s)'
source = r'(?!\b Target\s latency\s\b)[0-9]{1,2}(?=\s\bseconds,)'


regexs = [datetime,target,source]



# List for columns.......
match_list=[[]]

headers = "datetime,targetLatency,sourceLatency"

def readwrite(i):
        with open(log_file_path, "r") as file:
            with open(r'C:\Users\smarshall\Desktop\python\splitlogAccountLoad.csv', 'w') as outfile:
                outfile.write(headers+"\n")
            ###  For line in the log file match up the regex and chuck it in a list... then write a row
                for line in file:
                    for r in regexs:
                        for match in re.finditer(r, line, re.S):
                            match_text = match.group()
                            match_list[i].append(match_text)

                    item = map(str,match_list[i])
                    line = ",".join(item)

                    if line is not None:
                        outfile.write(line.strip("[]")+"\n")
                    i += 1
                    match_list.append([])



def writerows():
    for item in match_list:
        with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w') as outfile:
            columnhead = ["date", "time"]
            # writer=csv.DictWriter(outfile,fieldnames=columnhead)
            outfile.write(item+"\n")




readwrite(0)





# You have a csv file with some columns and some data...












