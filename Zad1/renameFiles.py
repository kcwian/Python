import os
import sys

path = sys.argv[1] 	  	# Argument przekazany do skryptu - nazwa/sciezka katalogu
newFileName = sys.argv[2] 	# Argument przekazany do skryptu - nowa nazwa plikow

files = os.listdir(path)	# Lista plikow w danym katalogu
i = 1

# Dokoncz program tak aby zmienial nazwy utworzonych plikow w podanym katalogu
