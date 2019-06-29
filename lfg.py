import os
import sys
import requests

while True:
	liceName = input('Which license would you like to use? (Type "LIST" for a list of the available commands): ')

	if liceName == "LIST": 
		#Lists all the licenses and available and their commands
		print("\n-------------\n  LICENSES\n-------------\n")
		print("LICENSE                    COMMAND\n")
		print("General Public License v3 = 'gpl'\nApache License = 'al'\nBSD 2 = 'bsd2'\nBSD 3 = 'bsd3'\nMIT = 'mit'\nUnlicense = 'ul'\nMozilla Public License v2 = 'mpl'\n")

		continue

	elif liceName == 'gpl' or liceName == 'al' or liceName == 'bsd2' or liceName == 'bsd3' or liceName == 'ul' or liceName == 'mit' or liceName == 'mpl': 
		repoPath = input('Please type the path to the repository: ') 
		liceFile = 'https://raw.githubusercontent.com/Lich42/LFG_Licenses/master/' + liceName + '.txt' #Gets the url of the users desired license
		data = requests.get(liceFile)

		os.chdir(repoPath) #Changes the directory to the user's specified one

		with open("LICENSE", "w+") as text_file: 
			text_file.write(data.text) 
	
		print("Success!") 
		sys.exit() 

	else:
		print("\nTHAT IS NOT A VALID COMMAND, PLEASE TRY AGAIN\n")
		continue