#!/usr/bin/python3

import cgi, cgitb
import json
import os
import time

cgitb.enable() 


form = cgi.FieldStorage()

result_data = form.getvalue("result_data")




while(os.path.isfile("write.lock")):
	time.sleep(100)

open("write.lock", 'a').close()

with open("result_data.csv","a") as result_file:
	for line in result_data.split("*"):
		result_file.write(line+"\n")

os.remove("write.lock")

data={'stored':"1"}

print ('Content-Type: application/json\n\n')
print (json.dumps(data))