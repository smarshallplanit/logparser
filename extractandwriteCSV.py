# Python Script to parse logs

import re
import csv

log_file_path = r"C:\Users\smarshall\Desktop\python\logs\pclog.log"
# regex = '(<property name="(.*?)">(.*?)<\/property>)'



## Regexs ##
date = '([0-9]{4}-[0-9]{2}-[0-9]{2}(?=\s\d{1,2}))'
time = '([\d]{1,2}:[\d]{1,2}:[\d]{1,2}.[\d]{1,3})'

regexs = [date,time]
#SfbRegex = '([A-Za-z]+\[0-9:A-Za-z]+\])'


# List for columns.......
match_list=[[]]



# Loop through file and use Regex to extract data to write to rows....
def writeheaders():
    with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w', newline='') as outfile:
        for h in columnhead:
            fieldnames = [h]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()


def readlog(i):
        with open(log_file_path, "r") as file:
            with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w') as outfile:
            ###  For line in the log file match up the regex and chuck it in a list... then write a row
                for line in file:
                    for r in regexs:
                        for match in re.finditer(r, line, re.S):
                            match_text = match.group()
                            match_list[i].append(match_text)
                   # print(match_list[i])

                    item = str(match_list[i])
                    if item != "[]":
                        outfile.write(item.strip('[]')+"\n")
                    i += 1
                    match_list.append([])



def writerows():
    for item in match_list:
        with open(r'C:\Users\smarshall\Desktop\python\splitlog.csv', 'w') as outfile:
            columnhead = ["date", "time"]
            # writer=csv.DictWriter(outfile,fieldnames=columnhead)
            outfile.write(item+"\n")








readlog(0)
# writerows()
#writeheaders()



# readwrite(date,"date")
# readwrite(time,"time")




# You have a csv file with some columns and some data...












