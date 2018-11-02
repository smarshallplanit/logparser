# Python Script to parse logs

import re
import csv

log_file_path = r"C:\Users\smarshall\Desktop\python\logs\pclog.log"
# regex = '(<property name="(.*?)">(.*?)<\/property>)'



## Regexs ##
date = '([0-9]{4}-[0-9]{2}-[0-9]{2}(?=\s\d{1,2}))'
time = '([\d]{1,2}:[\d]{1,2}:[\d]{1,2}.[\d]{1,3})'
datetime = r'([0-9]{4}-[0-9]{2}-[0-9]{2})\s([\d]{1,2}:[\d]{1,2}:[\d]{1,2})'
# timefraction = r'((?:,)(\d{1,3})\s\s)'
timefraction = r',(\d[0-9].)'
workqueue = r'(\bWorkqueue\sDWM\W\sSending\smessage\W\sWorkflow\b)'


regexs = [workqueue]



# List for columns.......
match_list=[[]]
match_dict={}
headers = "datetime,txn"
c = ','

def readwrite(i):
    with open(log_file_path, "r") as file:
        with open(r'C:\Users\smarshall\Desktop\python\splitlog2.csv', 'w') as outfile:
            outfile.write(headers + "\n")
            ###  For line in the log file match up the regex and chuck it in a list... then write a row
            for line in file:
                match_dict["datetime"]= re.findall(datetime,line)
                match_dict["timefraction"]= re.findall(timefraction,line)

                for r in regexs:
                    match_dict["txn"]=re.findall(r,line)


                if match_dict["txn"]:
                    print(match_dict.values())



                #
                # row = match_dict.get("datetime")+'.'+match_dict.get("timefraction")+ c + match_dict.get("txn") + "\n"
                # outfile.write(row)
                # i += 1



def writerows():
    for item in match_list:
        with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w') as outfile:
            columnhead = ["date", "time"]
            # writer=csv.DictWriter(outfile,fieldnames=columnhead)
            outfile.write(item+"\n")




readwrite(0)



# You have a csv file with some columns and some data...












