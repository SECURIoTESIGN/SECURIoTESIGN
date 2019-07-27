#!/usr/bin/python coding=utf-8

# Author : Francisco Chimuco

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
	"Q12": "",
	"Q13": "",
	"Q14": "",
	"Q15": "",
	"Q16": "",
	"Q17": "",
	"Q18": "",
	"Q19" : ""
}


# Questions
# Q1   -> Architeture
# Q2   -> Application Domain Type
# Q3   -> Authentication
# Q4   -> Has a DB
# Q5   -> Type of data storage
# Q6   -> Which db
# Q7   -> Type of data
# Q8   -> User Registration
# Q9  -> Way of user registration
# Q10  -> Programming Languages
# Q11  -> Input Forms
# Q12  -> Upload Files
# Q13  -> Logs
# Q14  -> System Regular Updates
# Q15  -> Third-part Software
# Q16  -> System Cloud Environment
# Q17  -> Hardware Specifications
# Q18  -> Hardware Auth
# Q19  -> Hardware Communications





# TO -DO -> in case of answer "others" (user input), 
# at the time of execution add to respective dict

question1 = {
	"1" : "Android App",
	"2" : "iOS App",
	"3" : "Hongmeng OS App",
	"4" : "Hybrid Application",
	"5" : "Tizen Application",
        "6" : "Ubuntu Touch Application",
        "7" : "Web Application",
        "8" : "Embedded System",
        "9" : ""
}

question2 = {
       "1" : "Entertainment",
       "2" : "Mobile Game",
       "3" : "m-Commerce ",
       "4" : "m-Health",
       "5" : "m-Learning",
       "6" : "m-Payment",
       "7" : "m-Social Networking",
       "8" : "Multi User Collaboration",
       "9" : "m-Tourism",
      "10" : "Smart Agriculture",
      "11" : "Smart Air Quality",
      "12" : "Smart Healthcare",
      "13" : "Smart Home",
      "14" : "Smart Manufacturing",
      "15" : "Smart Transportation",
      "16" : "Smart Waste Monitoring",
      "17" : "Smart Wearables"
}

question3 = {
	"1" : "No Authentication",
	"2" : "Username and Password",
	"3" : "Social Networks / Google",
	"4" : "SmartCard",
	"5" : "Biometrics",
	"6" : "Two Factor Authentication",
	"7" : "Multi Factor Authentication"
}

question4 = {
	"1" : "Yes",
	"2" : "No"
}

question5 = {
	"1" : "SQL",
	"2" : "NoSQL",
	"3" : "Local Storage",
	"4" : "Distributed Storage"
}

question6 = {
	"1" : "SQL Server",
	"2" : "MySQL",
	"3" : "PostgreSQL",
	"4" : "SQLite",
	"5" : "OracleDB",
	"6" : "MariaDB",
	"7" : "Cassandra",
	"8" : "CosmosDB",
	"9" : "DynamoDB",
       "10" : "JADE",
       "11" : "HBase",
       "12" : "Neo4J",
       "13" : "Redis",
       "14" : ""
}

question7 = {
	"1" : "Personal Information",
	"2" : "Confidential Data",
	"3" : "Critical Data",
	"4" : ""
}


question8 = {
	"1" : "Yes",
	"2" : "No"
}

question9 = {
	"1" : "The users will register themselves",
	"2" : "Will be a administrator that will register the users"
}

question10 = {
	"1" : "C#",
	"2" : "C/C++/Objective C",
	"3" : "HTML5",
	"4" : "Java",
	"5" : "Javascript",
	"6" : "PHP",
	"7" : "Python",
	"8" : "Ruby",
    	"9" : "Kotlin",
       "10" : ""
}

question11 = {
	"1" : "Yes",
	"2" : "No"
}

question12 = {
	"1" : "Yes",
	"2" : "No"
}


question13 = {
	"1" : "Yes",
	"2" : "No"
}

question14 = {
	"1" : "Yes",
	"2" : "No"
}

question15 = {
	"1" : "Yes",
	"2" : "No"
}

question16 = {
	"1" : "Community Cloud",
	"2" : "Hybrid Cloud",
	"3" : "Private Cloud",
	"4" : "Public Cloud",
	"5" : "Virtual Private Cloud"
 }

question17 = {
	"1" : "Yes",
	"2" : "No"
}

question18 = {
	"1" : "No Authentication",
	"2" : "Symmetric Key",
	"3" : "Basic Authentication (user/pass)",
	"4" : "Certificates (X.509) ",
	"5" : "TPM (Trusted Platform Module)"
}

question19 = {
	"1" : "4G / LTE",
	"2" : "3G",
	"3" : "GSM (2G)",
	"4" : "Radio Frequency",
	"5" : "Bluetooth ",
	"6" : "Wi-Fi ",
	"7" : "GPS ",
	"8" : "RFID ",
	"9" : "NFC"
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
                user_input = int(user_input)

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
	print( "  1 - Android Application  ")
	print( "  2 - iOS Application  ")
	print( "  3 - Hongmeng OS  ")
	print( "  4 - Hybrid Application  ")
	print( "  5 - Tizen Application  ")
	print( "  6 - Ubuntu Touch Application  ")
	print( "  7 - Web Application  ")
	print( "  8 - Embedded System  ")
	print( "  9 - Others  ")
	print("")

	# function input() interprets the input
	# get user input differs from python 2.x and 3.x --> input() = version 3 | raw_input() = version 2.x
	# TO-DO change this funtion input (to enter a string it needs quotes)
	# maybe getting the python version and adapt the funtions or just using input() and enter string with quotes (current version)
 

	while(1):
		# validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
		value=validateInput(1,16)
		if value == 0:
			return 
		if value == 15:
			print( "  Please specify the architeture: (name between quotes)  ")			
			value2=validateInput(2)
			# question_1["9"] = str(value2)
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value2) + ";"

		else:
			questions_and_answers["Q1"]=questions_and_answers["Q1"] + str(value) + ";"
		

# ----------------------------------------------------------------------------

def domain(version):
	print("---")
	print("")
	if version == 1:
		print("  **Which will be the domain of the system ?**  ")
	else:
		print("  **What is the domain of the system ?**  ")

	print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
	print("")
	print("  1 - Entertainment ")
	print("  2 - Mobile Game ")
	print("  3 - m-Commerce ")
	print("  4 - m-Health ")
	print("  5 - m-Learning ")
	print("  6 - m-Payment ")
	print("  7 - m-Social Networking ")
	print("  8 - Mult User Collaboration ")
	print("  9 - m-Tourism ")
	print(" 10 - Smart Agriculture ")
	print(" 11 - Smart Air Quality ")
	print(" 12 - Smart Healthcare ")
	print(" 13 - Smart Home ")
	print(" 14 - Smart Manufacturing ")
	print(" 15 - Smart Transportation ")
	print(" 16 - Smart Waste Monitoring ")
	print(" 17 - Smart Wearables ")
	print("")

	value = validateInput(1,18)
	questions_and_answers["Q2"] = str(value)
		

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
	questions_and_answers["Q3"]=str(value)


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
	questions_and_answers["Q4"]=str(value)
	
	
	if value == 1:
		typeOfDatabase(version)
		if questions_and_answers["Q5"] == '1' or questions_and_answers["Q5"] == '2':
			whichDatabase(version)
		sensitiveData(version)

	else:
		questions_and_answers["Q5"]="N/A"
		questions_and_answers["Q6"]="N/A"
		questions_and_answers["Q7"]="N/A"
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
	questions_and_answers["Q5"]=str(value)


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

	if questions_and_answers["Q5"] == '1':
		print( "  1 - SQL Server  ")	
		print( "  2 - MySQL  ")
		print( "  3 - PostgreSQL  ")
		print( "  4 - SQLite  ")
		print( "  5 - OracleDB  ")
		print( "  6 - MariaDB  ")
		

	if questions_and_answers["Q5"] == '2':
		print( "  7 - Cassandra ")
		print( "  8 - CosmosDB  ")
		print( "  9 - DynamoDB  ")
		print( " 10 - JADE      ")
		print( " 11 - HBase     ")
		print( " 12 - Neo4j     ")
		print( " 13 - Redis     ")
		print( " 14 - Other     ")
		print("")
	value=validateInput(1,15)
	if value == 14:
		print( "  Please specify the name of database: (name between quotes)  ")
		value2=validateInput(2)
		questions_and_answers["Q6"]=str(value2)
	else:
		questions_and_answers["Q6"]=str(value)


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
			questions_and_answers["Q7"]=questions_and_answers["Q7"] + str(value2) + ";"

		else:
			questions_and_answers["Q7"]=questions_and_answers["Q7"] + str(value) + ";"

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
	questions_and_answers["Q8"]=str(value)

	if value == 1 :
		typeOfUserRegist(version)
	else:
		questions_and_answers["Q9"] = "N/A"


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
	questions_and_answers["Q9"]=str(value)


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
	print( "  2 - C/C++/Objective C" )
	print( "  3 - HTML5  ")
	print( "  4 - Java  ")
	print( "  5 - Javascript  ")
	print( "  6 - PHP  " )
	print( "  7 - Python  " )
	print( "  8 - Kotlin  ")
	print( "  9 - Ruby  " )
	print( " 10 - Other/Property Language  ")
	print("")

	while(1):
		value=validateInput(1,11)
		if value == 0:
			return 
		if value == 9:
			print( "  Please specify the programming language: (name between quotes)  ")
			# TO-DO change this funtion input
			value2=validateInput(2)
			# question_9["8"]  = str(value2)
			questions_and_answers["Q10"]=questions_and_answers["Q10"] + str(value2) + ";"

		else:
			questions_and_answers["Q10"]=questions_and_answers["Q10"] + str(value) + ";"


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
	questions_and_answers["Q11"]=str(value)


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
	questions_and_answers["Q12"]=str(value)


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
	questions_and_answers["Q13"]= str(value) 

# ----------------------------------------------------------------------------
def allowUpdateSystem(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will allow regular updates?**  ")
	else:
		print("  **The system has a regular updates?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q14"]= str(value) 

# ----------------------------------------------------------------------------
def allowThirdParty(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **The system will use third-party apps?**  ")
	else:
		print("  **The system uses third-party apps?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q15"]= str(value) 

# ----------------------------------------------------------------------------
def cloudPlataform(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **What is the environment in which the app will be used?**  ")
	else:
		print("  **What is the environment in which the system is used?** ")
	print("  1 - Community Cloud (Remote connection) ")
	print("  2 - Hybrid Cloud (Mix connection) ")
	print("  3 - Private Cloud (Local connection) ")
	print("  4 - Public Cloud (Remote connection)")
	print("  5 - Virtual Private Cloud")
	print("")

	value = validateInput(1,6)
	questions_and_answers["Q16"]= str(value) 

# ----------------------------------------------------------------------------
def hardwareSpecs(version):
	print("")
	print("---")
	print("")
	print("  **Do you want to further specify hardware details concerning the system ?**  ")
	print("")
	print( "  1 - Yes  ")
	print( "  2 - No  ")
	print("")

	value = validateInput(1,3)
	questions_and_answers["Q17"]= str(value) 

	if value == 1:
		hardwareAuth(version)
		hardwareComunication(version)
	else:
		questions_and_answers["Q18"] = "N/A"
		questions_and_answers["Q19"] = "N/A"

# ----------------------------------------------------------------------------
def hardwareAuth(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **What will be the type of authentication implemented in hardware?**  ")
	else:
		print("  **What is the type of authentication implemented in hardware?**  ")
	print("")
	print( "  1 - No Authentication   ") 
	print( "  2 - Symmetric Key   ")
	print( "  3 - Basic Authentication (user/pass)  ")	
	print( "  4 - Certificates (X.509)   ")
	print( "  5 - TPM (Trusted Platform Module)  ")
	print("")

	value = validateInput(1,6)
	questions_and_answers["Q18"]= str(value) 

# ----------------------------------------------------------------------------
def hardwareComunication(version):
	print("")
	print("---")
	print("")
	if version == 1:
		print("  **What will be the wireless tecnologies presents in hardware?**  ")
	else:
		print("  **What are the wireless tecnologies presents in hardware**  ")
	print("")
	print( "  1 - 4G / LTE ")
	print( "  2 - 3G  ")
	print( "  3 - GSM (2G)  ") 
	print( "  4 - Radio Frequency  ")
	print( "  5 - Bluetooth  ")
	print( "  6 - Wi-Fi  ")
	print( "  7 - GPS  ")
	print( "  8 - RFID  ")
	print( "  9 - NFC  ")
	print("")

	value = validateInput(1,10)
	questions_and_answers["Q19"]= questions_and_answers["Q19"] + str(value) + ";" 



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
			for option in question1:
				if item == option:
					list_aux.append( question1[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)


	# print(list_aux)
	print("{:22} {:3} {:40} ".format("Architeture", ":", ' ; '.join(list_aux) ) )
	table_for_report.append([ "Architeture" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q1"])
	comments_list.append(' ; '.join(list_aux))

	
    	# --------------------------------------------
	for n in question2:
		item = questions_and_answers["Q2"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("Application domain type", ":" , question2[n]) )

			table_for_report.append( [ "Application domain type" , question2[n] ])

			answers_list.append(questions_and_answers["Q2"])
			comments_list.append(question2[n])


    	# --------------------------------------------
	for n in question3:
		item = questions_and_answers["Q3"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("Authentication", ":" , question3[n]) )

			table_for_report.append( [ "Authentication" , question3[n] ])

			answers_list.append(questions_and_answers["Q3"])
			comments_list.append(question3[n])

	# --------------------------------------------
	for n in question4:
		item = questions_and_answers["Q4"]		
		if  item == n:
			# print( "Has DB {:>18} ".format(":     ") + question_2[n])
			print("{:22} {:3} {:40} ".format("Has DB", ":" , question4[n]) )

			table_for_report.append( [ "Has DB" , question4[n] ])

			answers_list.append(questions_and_answers["Q4"])
			comments_list.append(question4[n])


	# --------------------------------------------
	item = questions_and_answers["Q5"]
	# case this question is not answered, and the answer it will be "N/A"
	if questions_and_answers["Q5"].isdigit() == False :
		print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  item) )

		table_for_report.append(["Type of data storage",  item ])

		answers_list.append(questions_and_answers["Q5"])
		comments_list.append(item)
	
	else:

		for n in question5:					
			if  item == n:
				print( "{:22} {:3} {:40} ".format("Type of data storage", ":",  question5[n]) )

				table_for_report.append([ "Type of data storage", question5[n] ])

				answers_list.append(questions_and_answers["Q5"])
				comments_list.append(question5[n])

	# --------------------------------------------

	item = questions_and_answers["Q6"]	
	for n in question6:		
		if  item == n :
			print("{:22} {:3} {:40} ".format( "Which DB", ":", question6[n]) )

			table_for_report.append( [ "Which DB",  question6[n] ])
	
			answers_list.append(questions_and_answers["Q6"])
			comments_list.append(question6[n])

	# case of user input text
	if item.isdigit() == False: 
		print("{:22} {:3} {:40} ".format( "Which DB", ":", item ) )

		table_for_report.append( [ "Which DB", item ])

		answers_list.append(questions_and_answers["Q6"])
		comments_list.append(item)


	# --------------------------------------------	
	list_aux = []	
	# it is a multiple question

	# find if the answer correspond to option "others" (means that is user input text) or not answered
	if questions_and_answers["Q7"][0].isdigit() == False and questions_and_answers["Q7"].find(";") == -1:
		list_aux.append( questions_and_answers["Q7"])

	else:

		# variable aux is a list that contains the answers chosen by the user to the question in cause
		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q7"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

		for item in aux:
			for option in question7:		
				if  item == option:
					list_aux.append( question7[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)

	print("{:22} {:3} {:40} ".format("Type of data stored" , ":" , ' ; '.join(list_aux) ) )

	table_for_report.append( ["Type of data stored" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q7"])
	comments_list.append(' ; '.join(list_aux))


	# --------------------------------------------
	for n in question8:
		item = questions_and_answers["Q8"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("User Registration", ":" , question8[n]) )

			table_for_report.append( ["User Registration" , question8[n] ])

			answers_list.append(questions_and_answers["Q8"])
			comments_list.append(question8[n])


	# --------------------------------------------
	item = questions_and_answers["Q9"]
	if questions_and_answers["Q9"].isdigit() == False:
		print("{:22} {:3} {:40} ".format("Type of Registration", ": " , item) )

		table_for_report.append( ["Type of Registration", item ])

		answers_list.append(questions_and_answers["Q9"])
		comments_list.append(item)

	else :
		for n in question9:
			if  item == n:
				print("{:22} {:3} {:40} ".format("Type of Registration", ": " , question9[n]) )

				table_for_report.append( [ "Type of Registration", question9[n] ])

				answers_list.append(questions_and_answers["Q9"])
				comments_list.append(question9[n])


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	
	# find if the answer correspond to option "others" (means that is only user input text)
	if questions_and_answers["Q10"][0].isdigit() == False and questions_and_answers["Q10"].find(";") == -1:
		list_aux.append( questions_and_answers["Q10"])

	else:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q10"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

			
		for item in aux:
			for option in question10:		
				if  item == option:
					list_aux.append( question10[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)
	
	print("{:22} {:3} {:40} ".format("Programming Languages" , ":" , ' ; '.join(list_aux) ) )
	
	table_for_report.append( [ "Programming Languages" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q10"])
	comments_list.append(' ; '.join(list_aux))


	# --------------------------------------------
	for n in question11:
		item = questions_and_answers["Q11"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Input Forms" , ":" , question11[n]) )

			table_for_report.append( ["Input Forms" , question11[n] ])

			answers_list.append(questions_and_answers["Q11"])
			comments_list.append(question11[n])
			


	# --------------------------------------------
	for n in question12:
		item = questions_and_answers["Q12"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Upload Files" , ":" , question12[n]) )

			table_for_report.append( [ "Upload Files" , question12[n] ])

			answers_list.append(questions_and_answers["Q12"])
			comments_list.append(question12[n])

	# --------------------------------------------
	for n in question13:
		item = questions_and_answers["Q13"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("The system has logs" , ":" , question13[n]) )

			table_for_report.append( [ "The system has logs" , question13[n] ])

			answers_list.append(questions_and_answers["Q13"])
			comments_list.append(question13[n])
    

    # --------------------------------------------
	for n in question14:
		item = questions_and_answers["Q14"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("The system has regular updates" , ":" , question14[n]) )

			table_for_report.append( [ "The system has regular updates" , question14[n] ])

			answers_list.append(questions_and_answers["Q14"])
			comments_list.append(question14[n])


    # --------------------------------------------
	for n in question15:
		item = questions_and_answers["Q15"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("The system has third-party" , ":" , question15[n]) )

			table_for_report.append( [ "The system has third-party" , question15[n] ])

			answers_list.append(questions_and_answers["Q15"])
			comments_list.append(question15[n])
    

     # --------------------------------------------
	for n in question16:
		item = questions_and_answers["Q16"]		
		if  item == n:
			print("{:22} {:3} {:40}".format("System Cloud Environments", ":" , question16[n]) )

			table_for_report.append( [ "System Cloud Environments" , question16[n] ])

			answers_list.append(questions_and_answers["Q16"])
			comments_list.append(question16[n])

	# --------------------------------------------
	for n in question17:
		item = questions_and_answers["Q17"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("Hardware Specification" , ":" , question17[n]) )

			table_for_report.append( [ "Hardware Specification" , question17[n] ])

			answers_list.append(questions_and_answers["Q17"])
			comments_list.append(question17[n])

	# --------------------------------------------
	for n in question18:
		item = questions_and_answers["Q18"]		
		if  item == n:
			print("{:22} {:3} {:40} ".format("HW Authentication" , ":" , question18[n]) )

			table_for_report.append( [ "HW Authentication" , question18[n] ])

			answers_list.append(questions_and_answers["Q18"])
			comments_list.append(question18[n])


	# --------------------------------------------
	list_aux = []	
	# it is a multiple question
	
	# find if the answer correspond to option "others" (means that is only user input text)
	if questions_and_answers["Q19"][0].isdigit() == False and questions_and_answers["Q19"].find(";") == -1:
		list_aux.append( questions_and_answers["Q19"])

	else:

		# cut the string in the delimitator ";" 
		aux = questions_and_answers["Q19"].split(";")

		#delete last item (= None)
		aux = aux[:-1]

			
		for item in aux:
			for option in question19:		
				if  item == option:
					list_aux.append( question19[option] )

			# case of user input text
			if item.isdigit() == False: 
				list_aux.append (item)
	
	print("{:22} {:3} {:40} ".format("HW Wireless Tech" , ":" , ' ; '.join(list_aux) ) )
	
	table_for_report.append( [ "HW Wireless Tech" , ' ; '.join(list_aux) ])

	answers_list.append(questions_and_answers["Q19"])
	comments_list.append(' ; '.join(list_aux))





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
		domain(version)
		authentication(version)
		hasDB(version)
		userRegist(version)
		languages(version)
		inputForms(version)
		allowUploadFiles(version)
		systemLogs(version)
		allowUpdateSystem(version)
		allowThirdParty(version)
		cloudPlataform(version)
		hardwareSpecs(version)


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
		questions_and_answers["Q13"] = input_list[12]
		questions_and_answers["Q14"] = input_list[13]
		questions_and_answers["Q15"] = input_list[14]
		questions_and_answers["Q16"] = input_list[15]
		questions_and_answers["Q17"] = input_list[16]
		questions_and_answers["Q18"] = input_list[17]
		questions_and_answers["Q19"] = input_list[18]




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
		designFile.write("<-- -->[Android Device] <-- https --> [Cloud]")

	if questions_and_answers["Q1"].find("2") != -1:
		designFile.write("<-- -->[iOS Device] <-- https --> [Cloud]")
	
	if questions_and_answers["Q1"].find("3") != -1:
		designFile.write("<-- -->[Hongmeng Device] <-- https --> [Cloud]")

	if questions_and_answers["Q1"].find("4") != -1:
		designFile.write("<-- -->[Mobile Device] <-- https --> [Cloud]")
	
	if questions_and_answers["Q1"].find("5") != -1:
		designFile.write("<-- -->[Tizen Device] <-- https --> [Cloud]")
	
	if questions_and_answers["Q1"].find("6") != -1:
		designFile.write("<-- -->[Ubuntu Touch Device] <-- https --> [Cloud]")
	
	if questions_and_answers["Q1"].find("7") != -1:
		designFile.write("<-- -->[Client] <-- https --> [Server]")
	
	if questions_and_answers["Q1"].find("8") != -1:
		designFile.write("<-- -->[Embedded System]")


	# ---------------------------------------------------
	if questions_and_answers["Q4"].find("1") != -1:
		designFile.write("[.]<-- -->[Database]")


	 #designFile.write("<-- -->[..]")
	designFile.close()
	designWithGraphEasy()
	
	# escrever o esquema no report
	report.write("![alt text](design_schemes.png)")
	report.write("\n")
	report.write("\n")

	

	# write authentication guide
	report.write( open("guides1/Authentication_guide.md","r").read() )	
	

	# check if embebbed systems are chosen
	if questions_and_answers["Q1"].find("8") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/IOT_Security_guide.md","r").read() )	


	# check if database is choosed
	if questions_and_answers["Q4"].find("1") != -1 and questions_and_answers["Q5"].find("1"):
		report.write("\n")
		report.write("\n")

		# write SQL injection guide
		report.write( open("guides1/SQL_Injection_guide.md","r").read() )	

	
	# check if language program are chosen
	if (questions_and_answers["Q1"].find("1") != -1 and (questions_and_answers["Q10"].find("1") != -1 or questions_and_answers["Q10"].find("4") != -1)):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Java_C#_guide.md","r").read() )
	
	
	# check if API service are chosen
	#if questions_and_answers["Q1"].find("7") != -1:
	#	report.write("\n")
	#	report.write("\n")
	#	report.write( open("guides/API_guide.md","r").read() )	
	

	# check if input forms is used	
	if questions_and_answers["Q11"].find("1") != -1:
		report.write("\n")
		report.write("\n")

		# write input validation guide
		report.write( open("guides1/Input_Validation_guide.md","r").read() )	


	if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("7") != -1 : 
		
		report.write("\n")
		report.write("\n")
		
		# Session Management guide
		report.write( open("guides1/Session_Management_guide.md","r").read() )	
		report.write("\n")
		report.write("\n")

		# write XSS guide
		report.write( open("guides1/Cross_Site_Scripting_guide.md","r").read() )

		report.write("\n")
		report.write("\n")

        # write HTML5 guide
		report.write(open("guides1/HTML_Secure_guides.md","r").read())
        #report.write(open("guides1/HTML_Secure_guides.md","r").read()) 	


	report.write("\n")
	report.write("\n")

    # write Buffer Overflows guide
	if questions_and_answers["Q10"].find("2") != -1:
		report.write(open("guides1/Buffer_overflows_guides.md","r").read())

	# write Cryptography guide
	report.write( open("guides1/Cryptography_guide.md","r").read() )	

	# write SSL/TLS guide
	if ((questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("7") != -1) and (questions_and_answers["Q6"].find("2") != -1 or questions_and_answers["Q6"].find("3") != -1)):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/TLS_guide.md","r").read() )


	if questions_and_answers["Q4"].find("1") != -1  and (questions_and_answers["Q6"].find("2") != -1 or questions_and_answers["Q6"].find("3") != -1):

		report.write("\n")
		report.write("\n")

		# write Access Control guide
		report.write( open("guides1/Access_Control_guide.md","r").read() )	
		

	if questions_and_answers["Q11"].find("1") != -1 :

		# check if file upload are chosen

		report.write("\n")
		report.write("\n")
		report.write( open("guides1/File_Upload_guide.md","r").read() )	

	
	# logging info
	if questions_and_answers["Q12"].find("1") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Logging_guide.md","r").read() )

	# Update info
	if questions_and_answers["Q13"].find("1") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/App_Update_guide.md","r").read() )


	# Third-party info
	if questions_and_answers["Q14"].find("1") != -1:
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/App_Third_Party_guide.md","r").read() )	
	

	# Database use and community and private cloud environment 
	if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("1") != -1 or questions_and_answers["Q16"].find("3") != -1):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Risk1_guide.md","r").read() )
	
	# Database use and public cloud environment 
	if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("4") != -1 ):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Risk2_guide.md","r").read() )
	
	# Database use and Hybrid cloud environment 
	if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("2") != -1 ):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Risk3_guide.md","r").read() )
	
	# Database use and VPC environment 
	if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("5") != -1 ):
		report.write("\n")
		report.write("\n")
		report.write( open("guides1/Risk4_guide.md","r").read() )
		
	report.close()
	convertReport()


if __name__ == "__main__":

	print("---")
	print("")
	print("#  Welcome to ")
	print("")
	print("#  SECUREloudMobilePRACTICES")
	print("")
	print("  The **SECURECloudMobilePRACTICES** is a custom made program.") 
	print("  This program implements a questionnaire about the development")
	print("  of mobile cloud-based application and generate a report with secure development guides.")
	print("  It is part of the outputs of project PHD Thesis entitled Systematization of the ")
	print("  Security Engineering Process in the Cloud and Mobile Ecosystem ")
	print("")
	print("## License")
	print("")
	print("  Developed by Francisco T. Chimuco and Pedro R. M. Inácio")
	print("  Department of Computer Science")
	print("  Universidade da Beira Interior")
	print("")
	print("  Copyright 2019 Francisco T. Chimuco and Pedro R. M. Inácio")
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

	
	
	exit(0)


# license Apache-2.0
