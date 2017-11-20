import subprocess
import re

### Należy wywolac skrypt ping.sh oraz zapisać rezultat do zmiennej pingResult

pingResult = 
###

ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", pingResult)
print ip
