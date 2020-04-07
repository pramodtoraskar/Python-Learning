from datetime import datetime

inputDate1 = input("Input date1 in yyyy,mm,dd format: ")
inputDate2 = input("Input date1 in yyyy,mm,dd format: ")

date_format = "%Y,%m,%d"
date1 = (datetime.strptime(inputDate1, date_format))
date2 = (datetime.strptime(inputDate2, date_format))

delta = date2 - date1
print(delta.days)
