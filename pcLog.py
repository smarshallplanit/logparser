# Python Script to parse logs

import re
import csv

log_file_path = r"C:\Users\smarshall\Desktop\python\logs\pclog.log"
# regex = '(<property name="(.*?)">(.*?)<\/property>)'



## Regexs ##
date = '([0-9]{4}-[0-9]{2}-[0-9]{2}(?=\s\d{1,2}))'
time = '([\d]{1,2}:[\d]{1,2}:[\d]{1,2}.[\d]{1,3})'
datetime = '([0-9]{4}-[0-9]{2}-[0-9]{2})\s([\d]{1,2}:[\d]{1,2}:[\d]{1,2},\d{1,3})'
timefraction = r'(,\d{1,3})'
workqueue = r'(\bWorkqueue\sDWM\W\sSending\smessage\W\sWorkflow\b)'


regexs = [datetime,timefraction,workqueue]



# List for columns.......
match_list=[[]]

headers = "datetime,txn"

def readwrite(i):
    with open(log_file_path, "r") as file:
        with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w') as outfile:
            outfile.write(headers + "\n")
            ###  For line in the log file match up the regex and chuck it in a list... then write a row
            for line in file:
                for r in regexs:
                    for match in re.finditer(r, line, re.S):
                        match_text = match.group()

                        if match is not None:
                            match_list[i].append(match_text)

                row =str(match_list[i]).replace("'","")
                commaCount = row.count(',')



                if commaCount > len(regexs)-1:
                    outfile.write(row.strip("[]") +"\n")
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












