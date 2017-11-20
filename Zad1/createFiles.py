import os
import sys

folderName = sys.argv[1] # Argument przekazany do skryptu

if not os.path.exists(folderName): 
   os.makedirs(folderName)

for x in range(1,20):
   f = open( "./" + folderName + "/test" + str(x), 'w')
   f.write(str(x))
   f.close()


