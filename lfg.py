import os
import sys

while True:
	liceName = input('Which license would you like to use? (Type "LIST" for a list of the available commands): ')

	if liceName == "LIST": 
		#Lists all the licenses and available and their commands
		print("\n-------------\n  LICENSES\n-------------\n")
		print("LICENSE                    COMMAND\n")
		print("General Public License v3 = 'gpl'\nApache License = 'al'\nBSD 2 = 'bsd2'\nBSD 3 = 'bsd3'\nMIT = 'mit'\nUnlicense = 'ul'\nMozilla Public License v2 = 'mpl'\n")

		continue

	elif liceName == 'gpl' or liceName == 'al' or liceName == 'bsd2' or liceName == 'bsd3' or liceName == 'ul' or liceName == 'mpl': 
		repoPath = input('Please type the path to the repository: ') 
		liceFile = 'licenses/' + liceName + '.txt' #Gets the file path of the users desired license

		f = open(liceFile, 'r') #Opens the license file
		os.chdir(repoPath) #Changes the directory to the user's specified one

		with open("LICENSE.md", "w+") as text_file: 
			text_file.write(f.read()) 
	
		print("Success!") 
		sys.exit() 

	else:
		print("\nTHAT IS NOT A VALID COMMAND, PLEASE TRY AGAIN\n")
		continue