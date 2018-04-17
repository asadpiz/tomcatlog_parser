#!/usr/bin/python
import sys
import argparse
import re
# INFO  @ 24 Oct 2013 08:00:55,770 @ io.payworks.api.web.interceptor.ExecuteTimeInterceptor - Request to url='/status' was answered with statusCode='200' took t='1ms'
# INFO  @ 24 Oct 2013 07:51:44,493 @ io.payworks.api.web.interceptor.ExecuteTimeInterceptor - Request to url='/v2/merchants/e0cf059a-5080-40a5-aaf1-67eb866aa48f/secretKey' was answered with statusCode='400' took t='6ms'

def extract_vars(log_line):
# dict.has_key(key)
	timeval = re.search(r't=(\'[0-9]*)ms\'',log_line)
	if timeval:
		responsetime = re.sub(r't=\'(\d+)ms\'',r"\1", timeval.group()) #TODO probably should do stripping for urlval in one step !!! Check if time other than "ms" is detected
		#print responsetime
	else:
		print "Warning: No response time found\n"
	urlval = re.search(r'url=(\'\/[\S]*\'\s)',log_line)
	if urlval:
		# TODO: Better to use capturing group and backreference but avoiding unnecessary dict lookups for now
		# Replacing UUIDS (and flattened UUIDS) with character *, second sub is stripping the "url=" string to get the endpoint value
		endpoint = re.sub(r'[a-f0-9]{8}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{4}-?[a-f0-9]{12}',"*",urlval.group())
		endpoint = re.sub(r'url=\'',"",endpoint) #Strip front
		endpoint = re.sub(r"\'\s","",endpoint)   #Strip end + whitespace
		#print endpoint
	else:
		print "Warning: No endpoint found\n"
        return endpoint, responsetime

parser = argparse.ArgumentParser(description='This program processes Tomcat logs')
parser.add_argument("filename", help="The name of the log file")
args = parser.parse_args()
#print args.filename
#TODO check if it's a tomcat log file or some other stuff

log_stats = {} #empty dictionary for population in the loop

log_file = open(args.filename,"r")
for line in log_file:
        if "Request to url" in line:
                #print line
                variables = extract_vars(line)
		if variables[0] in log_stats:
			#update counters
			log_stats[variables[0]] = [log_stats[variables[0]][0]+1,log_stats[variables[0]][1]+int(variables[1])]
		else:
			log_stats[variables[0]] = [1,int(variables[1])] # new endpoint with counter and response time
print "Printing Log Stats\n"
print ("Endpoint", "No. of Inovations", "Avg. Response Time")
for item in log_stats:
	print (item, log_stats[item][0],float(log_stats[item][1]/log_stats[item][0])) # total response time / no of invocations
log_file.close()
