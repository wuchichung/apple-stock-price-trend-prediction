import csv,sys,os,re
import numpy as np

MONTH ={}
MONTH["Jan"] = 1
MONTH["Feb"] = 2
MONTH["Mar"] = 3
MONTH["Apr"] = 4
MONTH["May"] = 5
MONTH["Jun"] = 6
MONTH["Jul"] = 7
MONTH["Aug"] = 8
MONTH["Sep"] = 9
MONTH["Oct"] = 10
MONTH["Nov"] = 11
MONTH["Dec"] = 12

def get_bloomberg_time(row_string):
	time_search = re.search(r"\s([\w,]+)\s+([\w]+),\s([\w]+)",row_string)
	if (time_search):
		month = MONTH[time_search.group(1)]
		day = time_search.group(2)
		year = time_search.group(3)		
		time = str(month)+"/"+str(day)+"/"+str(year)
		return time

def get_guardian_time(row_string):
	time_search = re.search(r'"([\w]+)\s([\w]+),([\w]+)"',row_string)
	if (time_search):
		month = MONTH[time_search.group(1).title()]
		day = time_search.group(2)
		year = time_search.group(3)		
		time = str(month)+"/"+str(day)+"/"+str(year)
		return time


if __name__ == "__main__":
	csv_file = sys.argv[1]
	out_csv = sys.argv[2]
	
	clean_rows=[]
	with open(csv_file, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=";", quotechar='|')
		
		for row in spamreader:
			row_string= ', '.join(row)
			time = get_bloomberg_time(row_string)
			if time:
				clean_row=[]
				clean_row.append(time)
				
				title_string_search = re.search(r'"(,[\w,]+)$',row_string)
				if(title_string_search):
					words = re.findall(r",([\w]+)",title_string_search.group(1))
					print title_string_search.group(1)
					print words
					clean_row += words
					clean_rows.append(clean_row)
	
	with open(out_csv,'w') as ccf:
		writer = csv.writer(ccf)
		for clean_row in clean_rows:
			writer.writerow(clean_row)


