import os
import sys


def createFiles(folderName_):
   if not os.path.exists(folderName_):
      os.makedirs(folderName_)

   for x in range(1,20):
      f = open( "./" + folderName_ + "/test" + str(x), 'w')
      f.write(str(x))
      f.close()


