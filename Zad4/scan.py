import subprocess
import re

proc = subprocess.Popen('./ping.sh', stdout=subprocess.PIPE)
tmp = proc.stdout.read()
ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", tmp)
print ip
