#!usr/bin/python

import shutil
import os

allnames = []
allnamePaths = []

count = 0
moveCount = 1
folderSize = fS = 17568


fileExt = ".jpg"

inputDir = 		"NAVARRE_1920_slice"
destination = 	"NAVARRE_1920_Slicebatch"

folder_One = 	'000001-017568'
folder_Two =	'017569-035136'
folder_Three = 	'035137-052704'
folder_Four =	'052705-070272'
folder_Five =	'070273-087840'
folder_Six =	'087841-105408'
folder_Seven =	'105409-122976'
folder_Eight =	'122977-140544'
folder_Nine =	'140545-158112'
folder_Ten = 	'158113-175680'
folder_Eleven =	'175681-193248'
folder_Twelve =	'193249-210816'
folder_Thirteen = '210817+++++'


for root, dirs, files in os.walk(inputDir):
    for name in files:
            
        if name.endswith(fileExt):

            allnames.append(name)           #list of filenames - basename only
            allnamePaths.append(os.path.join(root,name))    #list of all names with directory paths appended

            count = count + 1



for name in allnamePaths:

	if moveCount <= fS:
		if os.path.isdir(destination + '/' + folder_One) != 1:
			os.mkdir(destination + '/' + folder_One)

		newdestination = destination +'/' + folder_One
		shutil.move(name, newdestination)
		

		print "first move"

	if (moveCount > fS and moveCount <= (2*fS)):
		if os.path.isdir(destination + '/' + folder_Two) != 1:
			os.mkdir(destination + '/' + folder_Two)

		newdestination = destination +'/' + folder_Two
		shutil.move(name, newdestination)
		
		print "second move"


	if (moveCount > (2*fS) and moveCount <= (3*fS)):
		if os.path.isdir(destination + '/' + folder_Three) != 1:
			os.mkdir(destination + '/' + folder_Three)
		
		newdestination = destination +'/' + folder_Three
		shutil.move(name, newdestination)

		print "third move"


	if (moveCount > (3*fS) and moveCount <= (4*fS)):
		if os.path.isdir(destination + '/' + folder_Four) != 1:
			os.mkdir(destination + '/' + folder_Four)
		
		newdestination = destination +'/' + folder_Four
		shutil.move(name, newdestination)

		print "fourth move"


	if (moveCount > (4*fS) and moveCount <= (5*fS)):
		if os.path.isdir(destination + '/' + folder_Five) != 1:
			os.mkdir(destination + '/' + folder_Five)
		
		newdestination = destination +'/' + folder_Five
		shutil.move(name, newdestination)

		print "fifth move"


	if (moveCount > (5*fS) and moveCount <= (6*fS)):
		if os.path.isdir(destination + '/' + folder_Six) != 1:
			os.mkdir(destination + '/' + folder_Six)
		
		newdestination = destination +'/' + folder_Six
		shutil.move(name, newdestination)

		print "sixth move"


	if (moveCount > (6*fS) and moveCount <= (7*fS)):
		if os.path.isdir(destination + '/' + folder_Seven) != 1:
			os.mkdir(destination + '/' + folder_Seven)
		
		newdestination = destination +'/' + folder_Seven
		shutil.move(name, newdestination)

		print "seventh move"


	if (moveCount > (7*fS) and moveCount <= (8*fS)):
		if os.path.isdir(destination + '/' + folder_Eight) != 1:
			os.mkdir(destination + '/' + folder_Eight)
		
		newdestination = destination +'/' + folder_Eight
		shutil.move(name, newdestination)

		print "eighth move"


	if (moveCount > (8*fS) and moveCount <= (9*fS)):
		if os.path.isdir(destination + '/' + folder_Nine) != 1:
			os.mkdir(destination + '/' + folder_Nine)
		
		newdestination = destination +'/' + folder_Nine
		shutil.move(name, newdestination)

		print "ninth move"


	if (moveCount > (9*fS) and moveCount <= (10*fS)):
		if os.path.isdir(destination + '/' + folder_Ten) != 1:
			os.mkdir(destination + '/' + folder_Ten)
		
		newdestination = destination +'/' + folder_Ten
		shutil.move(name, newdestination)

		print "tenth move"


	if (moveCount > (10*fS) and moveCount <= (11*fS)):
		if os.path.isdir(destination + '/' + folder_Eleven) != 1:
			os.mkdir(destination + '/' + folder_Eleven)
		
		newdestination = destination +'/' + folder_Eleven
		shutil.move(name, newdestination)

		print "eleventh move"


	if (moveCount > (11*fS) and moveCount <= (12*fS)):
		if os.path.isdir(destination + '/' + folder_Twelve) != 1:
			os.mkdir(destination + '/' + folder_Twelve)
		
		newdestination = destination +'/' + folder_Twelve
		shutil.move(name, newdestination)

		print "twelth move"


	if moveCount > (12*fS):
		if os.path.isdir(destination + '/' + folder_Thirteen) != 1:
			os.mkdir(destination + '/' + folder_Thirteen)
		
		newdestination = destination +'/' + folder_Thirteen
		shutil.move(name, newdestination)

		print "thirteenth move"



	moveCount = moveCount +1


















		







