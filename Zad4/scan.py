import subprocess
import re

### Wywolac skrypt ping.sh oraz zapsać rezultat do zmiennej pingResult

pingResult = 
###

ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", pingResult)
print ip
