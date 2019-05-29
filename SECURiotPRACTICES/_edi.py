#!/usr/bin/python coding=utf-8

# Author : Édi Aires

# Work in Progress ...
# TO-DO -> Constrution of the final report : adding security guides

import os
from markdown import markdown
from xhtml2pdf import pisa
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


version = 1

# list that contains to answers in the written file
input_list = []

# add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
answers_list=[]
comments_list=[]
table_for_report=[]



# TO-DO -> a dict is unordered so the questions will appear in different order
# maybe better use OrderedDict ( from collection import OrderedDict )

# create a dictionairy to store the answers to the questions
questions_and_answers = {
	"Q1": "",
	"Q2": "",
	"Q3": "",
	"Q4": "",
	"Q5": "",
	"Q6": "",
	"Q7": "",
	"Q8": "",
	"Q9": "",
	"Q10": "",
	"Q11": "",
	"Q12": ""
}

# Questions
# Q1   -> Architeture
# Q2   -> Has a DB
# Q3   -> Type of data storage
# Q4   -> Which db
# Q5   -> Type of data
# Q6   -> Authentication
# Q7   -> User Registration
# Q8   -> Way of user registration
# Q9   -> Programming Languages
# Q10  -> Input Forms
# Q11  -> Upload Files
# Q12  -> Logs


# TO -DO -> in case of answer "others" (user input), 
# at the time of execution add to respective dict

question_1 = {
	"1" : "Web Application",
	"2" : "Web Service",
	"3" : "Desktop Application",
	"4" : "Mobile Application",
	"5" : "ClientServer > Client Component",
	"6" : "ClientServer > Server Component ",
	"7" : "API Service",
	"8" : "Embedded System",
	"9" : ""
}

question_2 = {
	"1" : "Yes",
	"2" : "No"
}

question_3 = {
	"1" : "SQL",
	"2" : "NoSQL",
	"3" : "Local Storage",
	"4" : "Distributed Storage"
}

question_4 = {
	"1" : "SQL Server",
	"2" : "MySQL",
	"3" : "PostgreSQL",
	"4" : "SQLite",
	"5" : "OracleDB",
	"6" : "MariaDB",
	"7" : "MongoDB",
	"8" : "CosmosDB",
	"9" : "DynamoDB",
	"10" : "Cassandra",
	"11" : ""
}

question_5 = {
	"1" : "Personal Information",
	"2" : "Confidential Data",
	"3" : "Critical Data",
	"4" : ""
}

question_6 = {
	"1" : "No Authentication",
	"2" : "Username and Password",
	"3" : "Social Networks / Google",
	"4" : "SmartCard",
	"5" : "Biometrics",
	"6" : "Two Factor Authentication",
	"7" : "Multi Factor Authentication"
}

question_7 = {
	"1" : "Yes",
	"2" : "No"
}

question_8 = {
	"1" : "The users will register themselves",
	"2" : "Will be a administrator that will register the users"
}

question_9 = {
	"1" : "C#",
	"2" : "C / C++",
	"3" : "Java",
	"4" : "Javascript",
	"5" : "PHP",
	"6" : "Python",
	"7" : "Ruby",
	"8" : ""
}

question_10 = {
	"1" : "Yes",
	"2" : "No",
}

question_11 = {
	"1" : "Yes",
	"2" : "No",
}


question_12 = {
	"1" : "Yes",
	"2" : "No"
}


'''
>template para as perguntas
def NAME():
	print("  : ")
	print("")
	print( "  1 -   ")
	print( "  2 -   ")
	print( "  3 -   ")
	print( "  4 -   ")
	print("")
'''

# ----------------------------------------------------------------------------
def readInputFromFile():

	# user inputs the file name and checks if the file exists
	while True:
		filepath = validateInput(2)
		if not os.path.isfile(filepath):
			print("File path {} does not exist...".format(filepath))
		else:
			break


	with open(filepath,'r') as file:
		line = file.readline()
		while line:

			# print (line.strip())
			# print (line.split('#')[0].strip() )

			# read line until character '#' which means after that is a comment
			input_list.append(line.split('#')[0].strip())
			line = file.readline()





# ----------------------------------------------------------------------------
# funtion to validate input and implemts dynamic arguments:
# if one argument is pass, it means what to validate
# if two arguments are pass it means that is to valide a int and
# there is a number of options to put in range

# means of arguments respectively
# arg(1) what to validate -> if it is to validate a int or a string (1 or 2)
# arg(2) n_options -> number of options in the question (==range)

def validateInput(*arg):

    # print("i was called with", len(arg),"arguments:",arg)
    # print (arg[0])
    # print (arg[1])

    while True:

        # validate a int
        if arg[0] == 1:
            try:
                user_input = input("  > ")

            # syntax error, name error
            except (SyntaxError, NameError, TypeError):
                print("  Not a valid answer!  ")
                print("")
                continue
            else:
                if (type(user_input) is int) and (user_input in range(0, arg[1])):
                    break
                else:
                    print("  Not a valid answer!  ")
                    print("")


        # validate a string
        if arg[0] == 2:
            try:
                user_input = input("  > ")

            # syntax error, name error
            except (SyntaxError, NameError, TypeError):
                print("  Not a valid answer!  ")
                print("")
                continue
            else:
                if type(user_input) is str:
                    break
                else:
                    print("  Not a valid answer!  ")
                    print("")

    return user_input


# ----------------------------------------------------------------------------
def arqui(version):
	print("---")
	print("")
	if version==1:
		print("  **Which will be the architecture of the system ?**  ")
	else:
		print("  **What is the architecture of the system ?**  ")

	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - Web Application  ")
	print( "  2 - Web Service  ")
	print( "  3 - Desktop Application  ")
	print( "  4 - Mobile Application  ")
	print( "  5 - Client-Server > Client Component  ")
	print( "  6 - Client-Server > Server Component  ")
	print( "  7 - API Service  ")
	print( "  8 - Embedded System  ")
	print( "  9 - Others  ")
	print("")

	# function input() interprets the input
	# get user input differs from python 2.x and 3.x --> input() = version 3 | raw_input() = version 2.x
	# TO-DO change this funtion input (to enter a string it needs quotes)
	# maybe getting the python version and adapt the funtions or just using input() and enter string with quotes (current version)
 

	while(1):
		# validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
		value=validateInput(1,10)
		if value == 0:
			return 
		if value == 9:
			print( "  Please specify the architeture: (name between quotes)  ")			
			value2=validateInput(2)
			# question_1["9"] = str(value2)
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value2) + ";"

		else:
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value) + ";"
		


# ----------------------------------------------------------------------------
def hasDB(version):	
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will use a Database ?**  ")
	else:
		print("  **The system use a Database ?**  ")
	print("")
	print( "  1 - Yes  ")	
	print( "  2 - No  ")
	print("")

	value=validateInput(1,3)
	questions_and_answers["Q2"]=str(value)
	
	
	if value == 1:
		typeOfDatabase(version)
		whichDatabase(version)
		sensitiveData(version)

	else:
		questions_and_answers["Q3"]="N/A"
		questions_and_answers["Q4"]="N/A"
		questions_and_answers["Q5"]="N/A"
		return


# ----------------------------------------------------------------------------
def typeOfDatabase(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print("  **Which will be type of data storage ?**  ")
	else:
		print("  **What is type of data storage ?**  ")
	print("")
	print( "  1 - SQL  ")	
	print( "  2 - NoSQL  ")
	print( "  3 - Local Storage  ")
	print( "  4 - Distributed Storage  ")
	print("")

	value = validateInput(1,5) 
	questions_and_answers["Q3"]=str(value)


# ----------------------------------------------------------------------------
def whichDatabase(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which Database will be used ?**  ")
	else:
		print("  **What is the Database used ?**  ")
	
	print("")
	print( "  1 - SQL Server  ")	
	print( "  2 - MySQL  ")
	print( "  3 - PostgreSQL  ")
	print( "  4 - SQLite  ")
	print( "  5 - OracleDB  ")
	print( "  6 - MariaDB  ")
	print( "  7 - MongoDB  ")
	print( "  8 - CosmosDB  ")
	print( "  9 - DynamoDB  ")
	print( "  10 - Cassandra  ")
	print( "  11 - Other  ")
	print("")
	
	value=validateInput(1,12)
	if value == 11:
		print( "  Please specify the name of database: (name between quotes)  ")
		value2=validateInput(2)
		questions_and_answers["Q4"]=str(value2)
	else:
		questions_and_answers["Q4"]=str(value)


# ----------------------------------------------------------------------------
def sensitiveData(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which type of data will be stored ?**  ")
	else:
		print("  **What is the type of data stored ?**  ")

	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - Personal Information (Names, Address,...)  ")
	print( "  2 - Confidential Data  ")
	print( "  3 - Critical Data  ")
	print( "  4 - Other  ")
	print("")
	
	while(1):
		value=validateInput(1,5)
		if value == 0:
			return 
		if value == 4 :
			print( "  Please specify the architeture: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			#question_5["4"] = str(value2)
			questions_and_answers["Q5"]=questions_and_answers["Q5"] + str(value2) + ";"

		else:
			questions_and_answers["Q5"]=questions_and_answers["Q5"] + str(value) + ";"


# ----------------------------------------------------------------------------
def authentication(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which type of authentication will be implemented ?**  ")
	else:
		print("  **What is the type of authentication implemented in the system ?**  ")
	print("")
	print( "  1 - No Authentication  ")
	print( "  2 - Username and Password  ")
	print( "  3 - Social Networks / Google  ")
	print( "  4 - SmartCard  ")
	print( "  5 - Biometrics  ")
	print( "  6 - Two Factor Authentication  ")
	print( "  7 - Multi Factor Authentication  ")
	print("")

	value = validateInput(1,8)
	questions_and_answers["Q6"]=str(value)


# ----------------------------------------------------------------------------
def userRegist(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print("  **There will be a user registration ?**  ")
	else:
		print("  **There is a user registration ?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q7"]=str(value)

	if value == 1 :
		typeOfUserRegist(version)
	else:
		questions_and_answers["Q8"] = "N/A"


# ----------------------------------------------------------------------------
def typeOfUserRegist(version):
	print("")
	print("---")
	print("")
	if version == 1 :
		print(" **Which way of user registration will be used ?**  ")
	else:
		print(" **Which way of user registration it's used ?**  ")
	print("")
	print( "  1 - The users will register themselves  ")
	print( "  2 - Will be a administrator that will register the users  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q8"]=str(value)


# ----------------------------------------------------------------------------
def languages(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **Which programming languages will be used in the implementation of the system ?**  ")	
	else:
		print("  **What is the programming languages used in the implementation of the system ?**  ")	
	
	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print( "  1 - C#  ")
	print( "  2 - C / C++  ")
	print( "  3 - Java  ")
	print( "  4 - Javascript  ")
	print( "  5 - PHP  " )
	print( "  6 - Python  " )
	print( "  7 - Ruby  ")
	print( "  8 - Other / Property Language  ")
	print("")

	while(1):
		value=validateInput(1,9)
		if value == 0:
			return 
		if value == 8:
			print( "  Please specify the programming language: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			# question_9["8"]  = str(value2)
			questions_and_answers["Q9"]=questions_and_answers["Q9"] + str(value2) + ";"

		else:
			questions_and_answers["Q9"]=questions_and_answers["Q9"] + str(value) + ";"


# ----------------------------------------------------------------------------
def inputForms(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will allow user input forms ?**  ")
	else:
		print("  **The system has user input forms ?**  ")
	print("")
	print( "  1 -Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q10"]=str(value)


# ----------------------------------------------------------------------------
def allowUploadFiles(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will allow upload files ?**  ")
	else:
		print("  **The system allow upload files ?**  ")
	print("")
	print( "  1 - Yes  ")	
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q11"]=str(value)


# ----------------------------------------------------------------------------
def systemLogs(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will have a regist of logs?**  ")
	else:
		print("  **The system has a logging regist?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q12"]= str(value) 



##############################################################################################


# function to use graph easy to make the schematic using a call to the system
def designWithGraphEasy():
	# v=1
	sInput = ("design_schemes.txt")

	'''
	sOutput = "design_schemes" + str(v) 
	sOutput_html = "design_schemes" + str(v) + ".html")

	
	cmd1 = "graph-easy --input " + sInput + " > " + sOutput 
	cmd2 = "graph-easy --as=ascii " + sInput + " > " + sOutput
	cmd3 = "graph-easy --as=boxart " + sInput + " > " + sOutput
	cmd4 = "graph-easy --as=html " + sInput + " > " + sOutput_html
	
	'''
	cmd = ("graph-easy --as=svg " + sInput +" > design_schemes.svg")
	#print( cmd)
	# cmd2 = "graph-easy --as=ascii " + sInput + " > " + sOutput + ".txt")
	# print( cmd2
	
	os.system(cmd)
	# os.system(cmd2)

	# convert img svg to PNG
	drawing = svg2rlg("design_schemes.svg")
	renderPM.drawToFile(drawing, "design_schemes.png", fmt="PNG")


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def convertReport():
	# input_filename = ("guides/example_report.md")
	# input_filename = "some_markdown.md")
	input_filename = ("FINAL_REPORT.md")

	output_filename = ("FINAL_REPORT.html")

	with open(input_filename,"r" ) as f:
		html_text= markdown(f.read(), extensions=[ 'markdown.extensions.tables','markdown.extensions.sane_lists'])  
	

	out= open(output_filename,"w")
	out.write(html_text)

	# writing in pdf file, the html content

	resultFile = open("FINAL_REPORT.pdf", "w+b")
	pisa.CreatePDF(html_text, dest=resultFile)
	# print( pisastatus)


# ----------------------------------------------------------------------------
def printData():

	generate_file = open("ans.txt", "w")	

	list_aux = []		
	# it is a multiple question

	# find if the answer correspond to option "others" (means that is user input text) OR fix this buy make it simple, verify if it the answer has only letters xD
	# find if the first caracter is a letter and if the answer has no more options
	if questions_and_answers["Q1"][0].isdigit() == False and questions_and_answers["Q1"].find(";") == -1 :
		list_aux.append( questions_and_answers["Q1"])

	else:

		# variable aux is a list that contains the answers chosen by the user to the question in cause
		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q1"].split(";")

		#delete last item (= None)
		aux = aux[:-1]
		# print(aux)

		# iterate the answers chosen by the user
		for item in aux:

			# iterate the options of the question and check what the chosen answers match
			for option in question_1:
				if item == option:
					list_aux.append( question_1[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)


	# print(list_aux)
	print("{:22} {:3} {:40} ".format("Architeture", ":", ' ; '.join(list_aux) ) )
	table_for_report.append([ "Architeture" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q1"])
	comments_list.append(' ; '.join(list_aux))

	
	# --------------------------------------------
	for n in question_2:
		item = questions_and_answers["Q2"]		
		if  item == n:
			# print( "Has DB {:>18} ".format(":     ") + question_2[n])
			print("{:22} {:3} {:40} ".format("Has DB", ":" , question_2[n]) )

			table_for_report.append( [ "Has DB" , question_2[n] ])

			answers_list.append(questions_and_answers["Q2"])
			comments_list.append(question_2[n])


	# --------------------------------------------
	item = questions_and_answers["Q3"]
	# case this question is not answered, and the answer it will be "N/A"
	if questions_and_answers["Q3"].isdigit() == False :
		print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  item) )

		table_for_report.append(["Type of data storage",  item ])

		answers_list.append(questions_and_answers["Q3"])
		comments_list.append(item)
	
	else:

		for n in question_3:					
			if  item == n:
				print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  question_3[n]) )

				table_for_report.append([ "Type of data storage", question_3[n] ])

				answers_list.append(questions_and_answers["Q3"])
				comments_list.append(question_3[n])

	# --------------------------------------------

	item = questions_and_answers["Q4"]	
	for n in question_4:		
		if  item == n :
			print("{:22} {:3} {:40} ".format( "Which DB", ":", question_4[n]) )

			table_for_report.append( [ "Which DB",  question_4[n] ])
	
			answers_list.append(questions_and_answers["Q4"])
			comments_list.append(question_4[n])

	# case of user input text
	if item.isdigit() == False: 
		print("{:22} {:3} {:40} ".format( "Which DB", ":", item ) )

		table_for_report.append( [ "Which DB", item ])

		answers_list.append(questions_and_answers["Q4"])
		comments_list.append(item)


	# --------------------------------------------	
	list_aux = []	
	# it is a multiple question

	# find if the answer correspond to option "others" (means that is user input text) or not answered
	if questions_and_answers["Q5"][0].isdigit() == False and questions_and_answers["Q5"].find(";") == -1:
		list_aux.append( questions_and_answers["Q5"])

	else:

		# variable aux is a list that contains the answers chosen by the user to the question in cause
		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q5"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

		for item in aux:
			for option in question_5:		
				if  item == option:
					list_aux.append( question_5[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)

	print("{:22} {:3} {:40} ".format("Type of data stored" , ":" , ' ; '.join(list_aux) ) )

	table_for_report.append( ["Type of data stored" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q5"])
	comments_list.append(' ; '.join(list_aux))



	# --------------------------------------------
	for n in question_6:
		item = questions_and_answers["Q6"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("Authentication", ":" , question_6[n]) )

			table_for_report.append( [ "Authentication" , question_6[n] ])

			answers_list.append(questions_and_answers["Q6"])
			comments_list.append(question_6[n])


	# --------------------------------------------
	for n in question_7:
		item = questions_and_answers["Q7"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("User Registration", ":" , question_7[n]) )

			table_for_report.append( ["User Registration" , question_7[n] ])

			answers_list.append(questions_and_answers["Q7"])
			comments_list.append(question_7[n])


	# --------------------------------------------
	item = questions_and_answers["Q8"]
	if questions_and_answers["Q8"].isdigit() == False:
		print("{:22} {:3} {:40} ".format("Type of Registration", ": " , item) )

		table_for_report.append( ["Type of Registration", item ])

		answers_list.append(questions_and_answers["Q8"])
		comments_list.append(item)

	else :
		for n in question_8:
			if  item == n:
				print("{:22} {:3} {:40} ".format("Type of Registration", ": " , question_8[n]) )

				table_for_report.append( [ "Type of Registration", question_8[n] ])

				answers_list.append(questions_and_answers["Q8"])
				comments_list.append(question_8[n])


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	
	# find if the answer correspond to option "others" (means that is only user input text)
	if questions_and_answers["Q9"][0].isdigit() == False and questions_and_answers["Q9"].find(";") == -1:
		list_aux.append( questions_and_answers["Q9"])

	else:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q9"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

			
		for item in aux:
			for option in question_9:		
				if  item == option:
					list_aux.append( question_9[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)
	
	print("{:22} {:3} {:40} ".format("Programming Languages" , ":" , ' ; '.join(list_aux) ) )
	
	table_for_report.append( [ "Programming Languages" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q9"])
	comments_list.append(' ; '.join(list_aux))


	# --------------------------------------------
	for n in question_10:
		item = questions_and_answers["Q10"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Input Forms" , ":" , question_10[n]) )

			table_for_report.append( ["Input Forms" , question_10[n] ])

			answers_list.append(questions_and_answers["Q10"])
			comments_list.append(question_10[n])
			


	# --------------------------------------------
	for n in question_11:
		item = questions_and_answers["Q11"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Upload Files" , ":" , question_11[n]) )

			table_for_report.append( [ "Upload Files" , question_11[n] ])

			answers_list.append(questions_and_answers["Q11"])
			comments_list.append(question_11[n])

	# --------------------------------------------
	for n in question_12:
		item = questions_and_answers["Q12"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("The system has logs" , ":" , question_12[n]) )

			table_for_report.append( [ "The system has logs" , question_12[n] ])

			answers_list.append(questions_and_answers["Q12"])
			comments_list.append(question_12[n])






	# -------------------------------------------
	# write / generate a file with all answers
	for i in range(0,len(answers_list)):
		generate_file.write( "{:20}{:3}{:20}\n".format(answers_list[i] , " # " , comments_list[i] ) )

		

	generate_file.close()

#############################################################################################################

# Information Capture main function
def informationCapture():

	print("---")
	print("")	
	print( "  **What is the status of development of the system ?**  ")
	print("")
	print("  1 - The system is yet to be developed.  ")
	print("  2 - The system is already developed.  ")
	print("")
	version=validateInput(1,3)
	print("")


	print("---")
	print("")	
	print( "  **Which way do you want to run this tool ?**  ")
	print("")
	print("  1 - Answer the questions one by one.  ")
	print("  2 - Use a text file with the answers already written.  ")
	print("")

	input_choice = validateInput(1,3)
	print("")

	# answer the qustions by hand
	if input_choice == 1:
		
		arqui(version)
		hasDB(version)

		authentication(version)
		userRegist(version)
		languages(version)
		inputForms(version)
		allowUploadFiles(version)
		systemLogs(version)



	# answers already written in the input file	
	else:
		print("---")
		print("")
		print("  **What is the name of the input file ?**  ")
		print("")
		readInputFromFile()
	
		questions_and_answers["Q1"] = input_list[0]	
		questions_and_answers["Q2"] = input_list[1]
		questions_and_answers["Q3"] = input_list[2]
		questions_and_answers["Q4"] = input_list[3]
		questions_and_answers["Q5"] = input_list[4]
		questions_and_answers["Q6"] = input_list[5]
		questions_and_answers["Q7"] = input_list[6]
		questions_and_answers["Q8"] = input_list[7]
		questions_and_answers["Q9"] = input_list[8]
		questions_and_answers["Q10"] = input_list[9]
		questions_and_answers["Q11"] = input_list[10]
		questions_and_answers["Q12"] = input_list[11]



#############################################################################################################

# Processing Information main function
def processingInformation():
	print("")
	print("  Processing information.....")
	print("")

	printData()



	report = open("FINAL_REPORT.md", "w")
	report.write("# Final Report  " +'\n')
	report.write("\n")
	

	report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|","" ,"|" ) )
	report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|" , ":---------", "|" ) )

	'''
	for i in range( 0,len(table_for_report) ):
		report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
	'''	
	for i in range( 0,len(table_for_report) ):
		report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0] , "|" , table_for_report[i][1] , "|" ) )

	report.write("\n")
	
	

	# constrution of the system model (achiteture)
	# file to write code that will design the schematics
	designFile = open("design_schemes.txt", "w")

	designFile.write("[.]")


	if questions_and_answers["Q1"].find("1") != -1:
		designFile.write("<-- -->[Client] <-- https --> [Server]")

	if questions_and_answers["Q1"].find("2") != -1:
		designFile.write("<-- -->[Web Service]")
	
	if questions_and_answers["Q1"].find("3") != -1:
		designFile.write("<-- -->[Desktop App]")

	if questions_and_answers["Q1"].find("4") != -1:
		designFile.write("<-- -->[Mobile]")
	
	if questions_and_answers["Q1"].find("5") != -1:
		designFile.write("<-- -->[Cliente Component]")
	
	if questions_and_answers["Q1"].find("6") != -1:
		designFile.write("<-- -->[Server Component]")
	
	if questions_and_answers["Q1"].find("7") != -1:
		designFile.write("<-- -->[API Service]")

	if questions_and_answers["Q1"].find("8") != -1:
		designFile.write("<-- -->[Embedded System]")

	# ---------------------------------------------------
	if questions_and_answers["Q2"].find("1") != -1:
		designFile.write("[.]<-- -->[Database]")


	 #designFile.write("<-- -->[..]")
	designFile.close()
	designWithGraphEasy()
	
	# escrever o esquema no report
	report.write("![alt text](design_schemes.png)")
	report.write("\n")
	report.write("\n")

	



	# write authentication guide
	report.write( open("guides/Authentication_guide.md","r").read() )	
	

	# check if embebbed systems are chosen
	if questions_and_answers["Q1"].find("8") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides/IOT_Security_guide.md","r").read() )	


	# check if database is choosed
	if questions_and_answers["Q2"].find("1") != -1:
		report.write("\n")
		report.write("\n")

		# write SQL injection guide
		report.write( open("guides/SQL_Injection_guide.md","r").read() )	

	
	# check if web service are chosen
	if questions_and_answers["Q1"].find("2") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides/Web_Service_guide.md","r").read() )	
	
	
	# check if API service are chosen
	if questions_and_answers["Q1"].find("7") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides/API_guide.md","r").read() )	
	

	# check if input forms is used	
	if questions_and_answers["Q10"].find("1") != -1:
		report.write("\n")
		report.write("\n")

		# write input validation guide
		report.write( open("guides/Input_Validation_guide.md","r").read() )	


	if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1 : 
		
		report.write("\n")
		report.write("\n")
		
		# Session Management guide
		report.write( open("guides/Session_Management_guide.md","r").read() )	
		report.write("\n")
		report.write("\n")

		# write XSS guide
		report.write( open("guides/Cross_Site_Scripting_guide.md","r").read() )	




	report.write("\n")
	report.write("\n")

	# write Cryptography guide
	report.write( open("guides/Cryptography_guide.md","r").read() )	



	if questions_and_answers["Q7"].find("1") != -1 :

		report.write("\n")
		report.write("\n")

		# write Access Control guide
		report.write( open("guides/Access_Control_guide.md","r").read() )	
		

	

	if questions_and_answers["Q11"].find("1") != -1 :

		# check if file upload are chosen

		report.write("\n")
		report.write("\n")
		report.write( open("guides/File_Upload_guide.md","r").read() )	

	
	# logging info
	if questions_and_answers["Q12"].find("1") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides/Logging_guide.md","r").read() )	
		




	report.close()
	convertReport()

	
 	


if __name__ == "__main__":

	print("---")
	print("")
	print("#  Welcome to ")
	print("")
	print("#  SECURiotPRACTICES")
	print("")
	print ("  The **SECURiotPRACTICES** is a custom made program.") 
	print("  This program implements a questionnaire about the development")
	print("  of a system and generate a report with secure development guides.")
	print("  It is part of the outputs of project Project SECURIoTESIGN, with funding  ")
	print("  with funding by FCT-Fundação para a Ciência e Tecnologia (Portugal)  ")
	print("  through the research grant SFRH//BD//133838//2017.")
	print("")
	print("## License")
	print("")
	print("  Developed by Edi Aires and Pedro R. M. Inácio")
	print("  Department of Computer Science")
	print("  Universidade da Beira Interior")
	print("")
	print("  Copyright 2019 Edi Aires and Pedro R. M. Inácio")
	print("")
	print("  SPDX-License-Identifier: Apache-2.0")
	print("")

	
	informationCapture()
	processingInformation()	


	print("")
	print("#############################################################") # after this is for debugging xD

	print("")
	print("")
	print("")

	
	
	exit(1)


# license Apache-2.0
