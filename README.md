# tomcatlog_parser
Simple Python based log parser for tomcat logs. It describes the number of times endpoints on the server were called and average response time.

## Steps to execute the script
1. Make sure that you have Python 3.x installed (>2.7 should also work in theory).
2. Clone/Download the repository on Windows or Linux and navigate to the project directory (*tomcatlog_parser*) via terminal (or command-prompt for windows).
3. Run the script and provide it with a tomcat log file

### Linux
```bash
./parse_tomcat.py <Log File>
```
### Windows
```bash
parse_tomcat.py <Log File>
```

## Script Details
The script takes a Tomcat log file as input and searches for calls to call server endpoints. Based on the initial task description and the followup clarification by Artur, I understand that the script has to locate endpoint calls which also have a response time associated with them (e.g., *<endpoint> was answered with statusCode=200 took t=30ms*) and ignoring others. For this purpose, I open the file and read it line by line. I locate the log lines that contain both endpoint (*requests*) and the average response time to finish the call. I identify these lines by checking for "Request to URL" and "took t" attributes.

I then use regexps to extract the endpoint name and response time. UUIDS is endpoints are also anonymized. I then use python dictionary [*O(n) for iteration, get and set*], to store the extracted values in the form **{key:value} = {<endpoint>:[no. of invocations, sum of response time]}**. The code searches the dictionary for endpoint, if the endpoint is not found (case for first iteration), it is appended to the dictionary with endpoint name as dictionary and a list containing no. of invocations (1) and sum of response time. IF the endpoint is already in the dictionary. The list is updated by adding + 1 to the no. of invocations and adding the response time. 

Finally the dictionary is printed with endpoint name, total the number of times it was invoked in the log and average response time which is sum of response time/ # of invocations



 
