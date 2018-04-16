#!/usr/bin/python
import sys
import argparse


def extract_vars(log_line):
        return url, num, t

parser = argparse.ArgumentParser(description='This program processes Tomcat logs')
parser.add_argument("filename", help="The name of the log file")
args = parser.parse_args()
#print args.filename
#TODO check if it's a tomcat log file or some other stuff

log_file = open(args.filename,"r")
for line in log_file:
        if "Request to url" in line:
#               print line
                vars = extract_vars(line)
log_file.close()
