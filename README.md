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
The script takes a Tomcat log file as input and searches for calls to call server endpoints. It then extracts the endpoint (URL), calculates the number of times it was invoked and finally it calculates the average response time for the calls in the entire log. It also anonymizes the UUIDS used in services.
