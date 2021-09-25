#!/usr/bin/python coding=utf-8
# !/bin/bash

# Author : Francisco Chimuco

# Work in Progress ...
# TO-DO -> Constrution of the final report : adding security guides

import os
from markdown import markdown
from xhtml2pdf import pisa
from switch import Switch
from goto import with_goto
from PyPDF2 import PdfFileMerger
1
version = 1

# list that contains to answers in the written file
input_list = []

# add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
answers_list = []
comments_list = []
table_for_report = []

# TO-DO -> a dict is unordered so the questions will appear in different order
# maybe better use OrderedDict ( from collection import OrderedDict )

# create a dictionairy to store the answers to the questions
# question_and_answers as qans
qans = {
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
    "Q19": "",
    "Q20": "",
    "Q21":""
}

# Questions
# Q1   -> Mobile Plataform
# Q2   -> Application Domain Type
# Q3   -> Authentication 
# Q4   -> Authentication Schemes
# Q5   -> Has a DB
# Q6   -> Type of data storage
# Q7   -> Which db
# Q8   -> Type of data
# Q9   -> User Registration
# Q10  -> Way of user registration
# Q11  -> Programming Languages
# Q12  -> Input Forms
# Q13  -> Upload Files
# Q14  -> Logs
# Q15  -> System Regular Updates
# Q16  -> Third-part Software
# Q17  -> System Cloud Environment
# Q18  -> Hardware Specifications
# Q19  -> Hardware Auth
# Q20  -> Hardware Communications
# Q21  -> Data Center Phisical Access


# TO -DO -> in case of answer "others" (user input),
# at the time of execution add to respective dict

question1 = {
    "1": "Android App",
    "2": "iOS App",
    "3": "Web Application",
    "4": "Hybrid Application",
    "5": "Harmony OS App",
    "6": "Tizen Application",
    "7": "IoT System",
    "8": "Chrome OS Application",
    "9": "Ubuntu Touch Application",
    "10": ""
}

question2 = {
    "1": "Entertainment",
    "2": "Mobile Game",
    "3": "m-Commerce ",
    "4": "m-Health",
    "5": "m-Learning",
    "6": "m-Payment",
    "7": "m-Social Networking",
    "8": "Multi User Collaboration",
    "9": "m-Tourism",
    "10": "Smart Agriculture",
    "11": "Smart Air Quality",
    "12": "Smart Healthcare",
    "13": "Smart Home",
    "14": "Smart Manufacturing",
    "15": "Smart Transportation",
    "16": "Smart Waste Monitoring",
    "17": "Smart Wearables"
}

question3 = {
    "1": "Yes",
    "2": "No"
}

question4 = {
    "1": "Biometric-based authentication",
    "2": "Channel-based authentication",
    "3": "Factors-based authentication",
    "4": "ID-based authentication",
    "5": ""
}

question5 = {
    "1": "Yes",
    "2": "No"
}

question6 = {
    "1": "SQL",
    "2": "NoSQL",
    "3": "Local Storage",
    "4": "Distributed Storage"
}

question7 = {
    "1": "SQL Server",
    "2": "MySQL",
    "3": "PostgreSQL",
    "4": "SQLite",
    "5": "OracleDB",
    "6": "MariaDB",
    "7": "Cassandra",
    "8": "CosmosDB",
    "9": "MongoDB",
    "10": "JADE",
    "11": "HBase",
    "12": "Neo4J",
    "13": "Redis",
    "14": ""
}

question8 = {
    "1": "Personal Information",
    "2": "Confidential Data",
    "3": "Critical Data",
    "4": ""
}

question9 = {
    "1": "Yes",
    "2": "No"
}

question10 = {
    "1": "The users will register themselves",
    "2": "Will be a administrator that will register the users"
}

question11 = {
    "1": "C#",
    "2": "C/C++",
    "3": "HTML5",
    "4": "Java",
    "5": "Javascript",
    "6": "PHP",
    "7": "Python",
    "8": "Ruby",
    "9": ""
}

question12 = {
    "1": "Yes",
    "2": "No"
}

question13 = {
    "1": "Yes",
    "2": "No"
}

question14 = {
    "1": "Yes",
    "2": "No"
}

question15 = {
    "1": "Yes",
    "2": "No"
}

question16 = {
    "1": "Yes",
    "2": "No"
}

question17 = {
    "1": "Community Cloud",
    "2": "Hybrid Cloud",
    "3": "Private Cloud",
    "4": "Public Cloud",
    "5": "Virtual Private Cloud"
}

question18 = {
    "1": "Yes",
    "2": "No"
}

question19 = {
    "1": "No Authentication",
    "2": "Symmetric Key",
    "3": "Basic Authentication (user/pass)",
    "4": "Certificates (X.509) ",
    "5": "TPM (Trusted Platform Module)"
}

question20 = {
    "1": "3G",
    "2": "4G/LTE",
    "3": "5G",
    "4": "GSM (2G)",
    "5": "Bluetooth ",
    "6": "Wi-Fi ",
    "7": "GPS ",
    "8": "RFID ",
    "9": "NFC",
    "10": ""
}

question21 = {
    "1": "Yes",
    "2": "No"
}

'''
>question template
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

    with open(filepath, 'r') as file:
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
    if version == 1:
        print("  **Which will be the mobile plataform of the system ?**  ")
    else:
        print("  **What is the mobile plataform of the system ?**  ")
    print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
    print("")
    print("  1 - Android Application  ")
    print("  2 - iOS Application  ")
    print("  3 - Web Application  ")
    print("  4 - Hybrid Application  ")
    print("  5 - Harmony OS App  ")
    print("  6 - Tizen Application  ")
    print("  7 - IoT System  ")
    print("  8 - Chrome OS Application  ")
    print("  9 - Ubuntu Touch Application  ")
    print("  10 - Others  ")
    print("")

    # function input() interprets the input
    # get user input differs from python 2.x and 3.x --> input() = version 3 | raw_input() = version 2.x
    # TO-DO change this funtion input (to enter a string it needs quotes)
    # maybe getting the python version and adapt the funtions or just using input() and enter string with quotes (current version)

    while (1):
        # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
        value = validateInput(1, 11)
        if value == 0:
            return
        if value == 10:
            print("  Please specify the mobile plataform: (name between single quotes)  ")
            value2 = validateInput(2)
            qans["Q1"] = qans["Q1"] + str(value2) + ";"

        else:
            qans["Q1"] = qans["Q1"] + str(value) + ";"


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

    value = validateInput(1, 18)
    qans["Q2"] = str(value)


# ----------------------------------------------------------------------------

def authentication(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system use authentication?**  ")
    else:
        print("  **The implemented system uses authentication ?**  ")
    print("")
    print("  1 - Yes ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q3"] = str(value)

    if value == 1:
        typeOfAuthentication(version)
    else:
        qans["Q4"]="N/A"

# ----------------------------------------------------------------------------

def typeOfAuthentication(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **What will be the authentication scheme to be implemented in the system?**  ")
    else:
        print("  **What is the authentication scheme implemented in the system ?**  ")
    
    print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
    print("")

    print("  1 - Biometric-based authentication")
    print("  2 - Channel-based authentication ")
    print("  3 - Factors-based authentication")
    print("  4 - ID-based authentication ")
    print("  5 - Other")
    print("")
    
    while (1):
        value = validateInput(1, 6)
        if value == 0:
            return
        if value == 5:
            print("  Please specify the authentication scheme: (name between single quotes)  ")
            # TO-DO change this funtion input
            value2 = validateInput(2)
            qans["Q4"] = qans["Q4"] + str(value2) + ";"

        else:
            qans["Q4"] = qans["Q4"] + str(value) + ";"

# ----------------------------------------------------------------------------
def hasDB(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  ** Will the system use a Database?**  ")
    else:
        print("  **Does the system use a Database?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q5"] = str(value)

    if value == 1:
        typeOfDatabase(version)
        if qans["Q6"] == '1' or qans["Q6"] == '2':
            whichDatabase(version)
        sensitiveData(version)

    else:
        qans["Q6"] = "N/A"
        qans["Q7"] = "N/A"
        qans["Q8"] = "N/A"
        return


# ----------------------------------------------------------------------------
def typeOfDatabase(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **What will be the type of data storage?**  ")
    else:
        print("  **What is type of data storage ?**  ")
    print("")
    print("  1 - SQL  ")
    print("  2 - NoSQL  ")
    print("  3 - Local Storage  ")
    print("  4 - Distributed Storage  ")
    print("")

    value = validateInput(1, 5)
    qans["Q6"] = str(value)


# ----------------------------------------------------------------------------
def whichDatabase(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Which Database will be used ?**  ")
    else:
        print("  **What is the Database used?**  ")

    print("")

    if qans["Q6"] == '1':
        print("  1 - SQL Server  ")
        print("  2 - MySQL  ")
        print("  3 - PostgreSQL  ")
        print("  4 - SQLite  ")
        print("  5 - OracleDB  ")
        print("  6 - MariaDB  ")

    if qans["Q6"] == '2':
        print("  7 - Cassandra ")
        print("  8 - CosmosDB  ")
        print("  9 - MongoDB  ")
        print(" 10 - JADE      ")
        print(" 11 - HBase     ")
        print(" 12 - Neo4j     ")
        print(" 13 - Redis     ")
        print(" 14 - Other     ")
        print("")
    value = validateInput(1, 15)
    if value == 14:
        print("  Please specify the name of database: (name between single quotes)  ")
        value2 = validateInput(2)
        qans["Q7"] = str(value2)
    else:
        qans["Q7"] = str(value)


# ----------------------------------------------------------------------------
def sensitiveData(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Which type of data will be stored?**  ")
    else:
        print("  **What is the type of data stored?**  ")

    print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
    print("")
    print("  1 - Personal Information (Names, Address,...)  ")
    print("  2 - Confidential Data  ")
    print("  3 - Critical Data  ")
    print("  4 - Other  ")
    print("")

    while (1):
        value = validateInput(1, 5)
        if value == 0:
            return
        if value == 4:
            print("  Please specify the type of data stored: (name between single quotes)  ")
            # TO-DO change this funtion input
            value2 = validateInput(2)
            # question_5["4"] = str(value2)
            qans["Q8"] = qans["Q8"] + str(value2) + ";"

        else:
            qans["Q8"] = qans["Q8"] + str(value) + ";"


def userRegist(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will there be a user registration?**  ")
    else:
        print("  **Is there a user registration?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q9"] = str(value)

    if value == 1:
        typeOfUserRegist(version)
    else:
        qans["Q10"] = "N/A"


# ----------------------------------------------------------------------------
def typeOfUserRegist(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print(" **Which way of user registration will be used ?**  ")
    else:
        print(" **Which way of user registration it's used ?**  ")
    print("")
    print("  1 - The users will register themselves  ")
    print("  2 - Will be a administrator that will register the users  ")
    print("")

    value = validateInput(1, 3)
    qans["Q10"] = str(value)


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
    print("  1 - C#  ")
    print("  2 - C/C++  ")
    print("  3 - HTML5  ")
    print("  4 - Java  ")
    print("  5 - Javascript  ")
    print("  6 - PHP  ")
    print("  7 - Python  ")
    print("  8 - Ruby  ")
    print("  9 - Other/Property Language  ")
    print("")

    while (1):
        value = validateInput(1, 10)
        if value == 0:
            return
        if value == 9:
            print("  Please specify the programming language: (name between single quotes)  ")
            # TO-DO change this funtion input
            value2 = validateInput(2)
            # question_9["8"]  = str(value2)
            qans["Q11"] = qans["Q11"] + str(value2) + ";"

        else:
            qans["Q11"] = qans["Q11"] + str(value) + ";"


# ----------------------------------------------------------------------------
def inputForms(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system allow user input forms?**  ")
    else:
        print("  **Has the system user input forms?**  ")
    print("")
    print("  1 -Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q12"] = str(value)


# ----------------------------------------------------------------------------
def allowUploadFiles(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system allow upload files?**  ")
    else:
        print("  **Does the system allow upload files?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q13"] = str(value)


# ----------------------------------------------------------------------------
def systemLogs(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system record event logs?**  ")
    else:
        print("  **Has The system a logging regist?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q14"] = str(value)


# ----------------------------------------------------------------------------
def allowUpdateSystem(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system allow regular updates?**  ")
    else:
        print("  **Has the system a regular updates?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q15"] = str(value)


# ----------------------------------------------------------------------------
def allowThirdParty(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system use third-party apps?**  ")
    else:
        print("  **Does the system use third-party apps?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q16"] = str(value)


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

    value = validateInput(1, 6)
    qans["Q17"] = str(value)


# ----------------------------------------------------------------------------
def hardwareSpecs(version):
    print("")
    print("---")
    print("")
    print("  **Do you want to further specify hardware details concerning the system ?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q18"] = str(value)

    if value == 1:
        hardwareAuth(version)
        hardwareComunication(version)
    else:
        qans["Q19"] = "N/A"
        qans["Q20"] = "N/A"


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
    print("  1 - No Authentication   ")
    print("  2 - Symmetric Key   ")
    print("  3 - Basic Authentication (user/pass)  ")
    print("  4 - Certificates (X.509)   ")
    print("  5 - TPM (Trusted Platform Module)  ")
    print("")

    value = validateInput(1, 6)
    qans["Q19"] = str(value)


# ----------------------------------------------------------------------------
def hardwareComunication(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **What wireless technologies will be on the hardware?**  ")
    else:
        print("  **What are the wireless tecnologies presents in hardware. Enter several options and end with 0.**  ")
    print("")
    print("  1 - 3G ")
    print("  2 - 4G / LTE ")
    print("  3 - 5G  ")
    print("  4 - GSM (2G)  ")
    print("  5 - Bluetooth  ")
    print("  6 - Wi-Fi  ")
    print("  7 - GPS  ")
    print("  8 - RFID  ")
    print("  9 - NFC  ")
    print("  10 - Others")
    print("")
    while(1):
        value = validateInput(1, 11)
        if value == 0:
            break
        if value == 10:
            print("Please specify the wireless technologies: (name between single quotes)")
            value2 = validateInput(2)
            qans["Q20"] = qans["Q20"] + str(value2) + ";"
        else:
            qans["Q20"] = qans["Q20"] + str(value) + ";"


# value = validateInput(1,10)
# qans["Q19"]= qans["Q19"] + str(value) + ";"

# ----------------------------------------------------------------------------
def dataCenterAcess(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Can someone gain physical access to the machine where the system will operates?** ")
    else:
        print("  **Can someone gain physical access to the machine where the system operates?**  ")
    print("")
    print("  1 -Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    qans["Q21"] = str(value)


# ----------------------------------------------------------------------------
def printData():
    generate_file = open("ans.txt", "w")

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is user input text) OR fix this buy make it simple, verify if it the answer has only letters xD
    # find if the first caracter is a letter and if the answer has no more options
    if qans["Q1"][0].isdigit() == False and qans["Q1"].find(";") == -1:
        list_aux.append(qans["Q1"])

    else:

        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = qans["Q1"].split(";")

        # delete last item (= None)
        aux = aux[:-1]
        # print(aux)

        # iterate the answers chosen by the user
        for item in aux:

            # iterate the options of the question and check what the chosen answers match
            for option in question1:
                if item == option:
                    list_aux.append(question1[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    # print(list_aux)
    print("{:22} {:3} {:40} ".format("Mobile Plataform", ":", ' ; '.join(list_aux)))
    table_for_report.append(["Mobile Plataform", ' ; '.join(list_aux)])

    answers_list.append(qans["Q1"])
    comments_list.append(' ; '.join(list_aux))

    # --------------------------------------------
    for n in question2:
        item = qans["Q2"]
        if item == n:
            print("{:22} {:3} {:40}".format("Application domain type", ":", question2[n]))

            table_for_report.append(["Application domain type", question2[n]])

            answers_list.append(qans["Q2"])
            comments_list.append(question2[n])

    # --------------------------------------------
    for n in question3:
        item = qans["Q3"]
        if item == n:
            print("{:22} {:3} {:40}".format("Authentication", ":", question3[n]))

            table_for_report.append(["Authentication", question3[n]])

            answers_list.append(qans["Q3"])
            comments_list.append(question3[n])

    # --------------------------------------------
    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is user input text) or not answered
    if qans["Q4"][0].isdigit() == False and qans["Q4"].find(";") == -1:
        list_aux.append(qans["Q4"])

    else:

        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = qans["Q4"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question4:
                if item == option:
                    list_aux.append(question4[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Authentication schemes", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Authentication schemes", ' ; '.join(list_aux)])

    answers_list.append(qans["Q4"])
    comments_list.append(' ; '.join(list_aux))
    
    # --------------------------------------------
    for n in question5:
        item = qans["Q5"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Has DB", ":", question5[n]))

            table_for_report.append(["Has DB", question5[n]])

            answers_list.append(qans["Q5"])
            comments_list.append(question5[n])

    # --------------------------------------------
    item = qans["Q6"]
    # case this question is not answered, and the answer it will be "N/A"
    if qans["Q6"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of data storage", ":", item))

        table_for_report.append(["Type of data storage", item])

        answers_list.append(qans["Q6"])
        comments_list.append(item)

    else:

        for n in question6:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of data storage", ":", question6[n]))

                table_for_report.append(["Type of data storage", question6[n]])

                answers_list.append(qans["Q6"])
                comments_list.append(question6[n])

    # --------------------------------------------

    item = qans["Q7"]
    for n in question7:
        if item == n:
            print("{:22} {:3} {:40} ".format("Which DB", ":", question7[n]))

            table_for_report.append(["Which DB", question7[n]])

            answers_list.append(qans["Q7"])
            comments_list.append(question7[n])

    # case of user input text
    if item.isdigit() == False:
        print("{:22} {:3} {:40} ".format("Which DB", ":", item))

        table_for_report.append(["Which DB", item])

        answers_list.append(qans["Q7"])
        comments_list.append(item)

    # --------------------------------------------
    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is user input text) or not answered
    if qans["Q8"][0].isdigit() == False and qans["Q8"].find(";") == -1:
        list_aux.append(qans["Q8"])

    else:

        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = qans["Q8"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question8:
                if item == option:
                    list_aux.append(question8[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Type of data stored", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Type of data stored", ' ; '.join(list_aux)])

    answers_list.append(qans["Q8"])
    comments_list.append(' ; '.join(list_aux))

    # --------------------------------------------
    for n in question9:
        item = qans["Q9"]
        if item == n:
            print("{:22} {:3} {:40}".format("User Registration", ":", question9[n]))

            table_for_report.append(["User Registration", question9[n]])

            answers_list.append(qans["Q9"])
            comments_list.append(question9[n])

    # --------------------------------------------
    item = qans["Q10"]
    if qans["Q10"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of Registration", ": ", item))

        table_for_report.append(["Type of Registration", item])

        answers_list.append(qans["Q10"])
        comments_list.append(item)

    else:
        for n in question10:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of Registration", ": ", question10[n]))

                table_for_report.append(["Type of Registration", question10[n]])

                answers_list.append(qans["Q10"])
                comments_list.append(question10[n])

    # --------------------------------------------
    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if qans["Q11"][0].isdigit() == False and qans["Q11"].find(";") == -1:
        list_aux.append(qans["Q11"])

    else:

        # cut the string in the delimitator ";"
        aux = qans["Q11"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question11:
                if item == option:
                    list_aux.append(question11[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Programming Languages", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Programming Languages", ' ; '.join(list_aux)])

    answers_list.append(qans["Q11"])
    comments_list.append(' ; '.join(list_aux))

    # --------------------------------------------
    for n in question12:
        item = qans["Q12"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Input Forms", ":", question12[n]))

            table_for_report.append(["Input Forms", question12[n]])

            answers_list.append(qans["Q12"])
            comments_list.append(question12[n])

    # --------------------------------------------
    for n in question13:
        item = qans["Q13"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Upload Files", ":", question13[n]))

            table_for_report.append(["Upload Files", question13[n]])

            answers_list.append(qans["Q13"])
            comments_list.append(question13[n])

    # --------------------------------------------
    for n in question14:
        item = qans["Q14"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has logs", ":", question14[n]))

            table_for_report.append(["The system has logs", question14[n]])

            answers_list.append(qans["Q14"])
            comments_list.append(question14[n])

    # --------------------------------------------
    for n in question15:
        item = qans["Q15"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has regular updates", ":", question15[n]))

            table_for_report.append(["The system has regular updates", question15[n]])

            answers_list.append(qans["Q15"])
            comments_list.append(question15[n])

    # --------------------------------------------
    for n in question16:
        item = qans["Q16"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has third-party", ":", question16[n]))

            table_for_report.append(["The system has third-party", question16[n]])

            answers_list.append(qans["Q16"])
            comments_list.append(question16[n])

    # --------------------------------------------
    for n in question17:
        item = qans["Q17"]
        if item == n:
            print("{:22} {:3} {:40}".format("System Cloud Environments", ":", question17[n]))

            table_for_report.append(["System Cloud Environments", question17[n]])

            answers_list.append(qans["Q17"])
            comments_list.append(question17[n])

    # --------------------------------------------
    for n in question18:
        item = qans["Q18"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Hardware Specification", ":", question18[n]))

            table_for_report.append(["Hardware Specification", question18[n]])

            answers_list.append(qans["Q18"])
            comments_list.append(question18[n])

    # --------------------------------------------
    for n in question19:
        item = qans["Q19"]
        if item == n:
            print("{:22} {:3} {:40} ".format("HW Authentication", ":", question19[n]))

            table_for_report.append(["HW Authentication", question19[n]])

            answers_list.append(qans["Q19"])
            comments_list.append(question19[n])

    # --------------------------------------------
    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if qans["Q20"][0].isdigit() == False and qans["Q20"].find(";") == -1:
        list_aux.append(qans["Q20"])

    else:

        # cut the string in the delimitator ";"
        aux = qans["Q20"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question20:
                if item == option:
                    list_aux.append(question20[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("HW Wireless Tech", ":", ' ; '.join(list_aux)))

    table_for_report.append(["HW Wireless Tech", ' ; '.join(list_aux)])

    answers_list.append(qans["Q20"])
    comments_list.append(' ; '.join(list_aux))

    # --------------------------------------------
    for n in question21:
        item = qans["Q21"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Data Center Phisical Access", ":", question21[n]))

            table_for_report.append(["Data Center Phisical Access", question21[n]])

            answers_list.append(qans["Q21"])
            comments_list.append(question21[n])

    # -------------------------------------------
    # write / generate a file with all answers
    for i in range(0, len(answers_list)):
        generate_file.write("{:20}{:3}{:20}\n".format(answers_list[i], " # ", comments_list[i]))

    generate_file.close()


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def securRequirconvertReport():
    # input_filename = ("guides/example_report.md")
    # input_filename = "some_markdown.md")
    input_filename = ("SECURITY_REQUIREMENTS.md")

    output_filename = ("SECURITY_REQUIREMENTS.html")

    with open(input_filename, "r") as f:
        html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

    out = open(output_filename, "w")
    out.write(html_text)

    # writing in pdf file, the html content

    resultFile = open("SECURITY_REQUIREMENTS.pdf", "w+b")
    pisa.CreatePDF(html_text, dest=resultFile)


# print( pisastatus)


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def goodPracticeConvertReport():
    # input_filename = ("guides/example_report.md")
    # input_filename = "some_markdown.md")
    input_filename = ("GOOD_PRACTICES.md")

    output_filename = ("GOOD_PRACTICES.html")

    with open(input_filename, "r") as f:
        html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

    out = open(output_filename, "w")
    out.write(html_text)

    # writing in pdf file, the html content

    resultFile = open("GOOD_PRACTICES.pdf", "w+b")
    pisa.CreatePDF(html_text, dest=resultFile)

# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def securityMechanismsConvertReport():
    # input_filename = ("guides/example_report.md")
    # input_filename = "some_markdown.md")
    input_filename = ("SECURITY_MECHANISMS.md")

    output_filename = ("SECURITY_MECHANISMS.html")

    with open(input_filename, "r") as f:
        html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

    out = open(output_filename, "w")
    out.write(html_text)

    # writing in pdf file, the html content

    resultFile = open("SECURITY_MECHANISMS.pdf", "w+b")
    pisa.CreatePDF(html_text, dest=resultFile)


# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def attackModelConvertReport():
    # input_filename = ("guides/example_report.md")
    # input_filename = "some_markdown.md")
    input_filename = ("ATTACKS_MAPPING.md")

    output_filename = ("ATTACKS_MAPPING.html")

    with open(input_filename, "r") as f:
        html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

    out = open(output_filename, "w")
    out.write(html_text)

    # writing in pdf file, the html content

    resultFile = open("ATTACKS_MAPPING.pdf", "w+b")
    pisa.CreatePDF(html_text, dest=resultFile)

# ----------------------------------------------------------------------------
# function to convert the markdown report to html and pdf format
def testSpecConvertReport():
    # input_filename = ("guides/example_report.md")
    # input_filename = "some_markdown.md")
    input_filename = ("TEST_SPECIFICATION.md")

    output_filename = ("TEST_SPECIFICATION.html")

    with open(input_filename, "r") as f:
        html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

    out = open(output_filename, "w")
    out.write(html_text)

    # writing in pdf file, the html content

    resultFile = open("TEST_SPECIFICATION.pdf", "w+b")
    pisa.CreatePDF(html_text, dest=resultFile)


#############################################################################################################

@with_goto
def switch1():
    label.begin
    
    val = 0
    while True:
        try:
            val = int(input("\nWhats is your option?\n"))       
        except ValueError:
            print("Erro! Introduza um número inteiro entre 1 e 8, de acordo o menu acima!")
            goto.begin
        else:
            break

    
    with Switch(val) as case:
        if case(1):
            print("---")
            print("")
            print("  **Which way do you want to run this tool?**  ")
            print("")
            print("  1 - Answer the questions one by one.  ")
            print("  2 - Use a text file with the answers already written.  ")
            print("")

            input_choice = validateInput(1, 3)
            print("")

            # answer the questions by hand
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
                dataCenterAcess(version)
                print("**The questionnaire is over!**")

            # answers already written in the input file
            else:
                print("---")
                print("")
                print("  **What is the name of the input file (ans.txt)?**  ")
                print("")
                readInputFromFile()

                qans["Q1"] = input_list[0]
                qans["Q2"] = input_list[1]
                qans["Q3"] = input_list[2]
                qans["Q4"] = input_list[3]
                qans["Q5"] = input_list[4]
                qans["Q6"] = input_list[5]
                qans["Q7"] = input_list[6]
                qans["Q8"] = input_list[7]
                qans["Q9"] = input_list[8]
                qans["Q10"] = input_list[9]
                qans["Q11"] = input_list[10]
                qans["Q12"] = input_list[11]
                qans["Q13"] = input_list[12]
                qans["Q14"] = input_list[13]
                qans["Q15"] = input_list[14]
                qans["Q16"] = input_list[15]
                qans["Q17"] = input_list[16]
                qans["Q18"] = input_list[17]
                qans["Q19"] = input_list[18]
                qans["Q20"] = input_list[19]
                qans["Q21"] = input_list[20]

            informationCapture()

            print("# Processing Done! Choose another option to process the requests!")

        if case(2):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST REQUIREMENTS ELICITATION PROCESSING\n\n")
            securityRequirements()
            informationCapture()

        if case(3):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST BEST PRACTICES ELICITATION PROCESSING\n\n")
            goodPractices()
            informationCapture()
        
        if case(4):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST SECURITY MECHANISMS ELICITATION PROCESSING\n\n")
            securityMechanisms()
            informationCapture()

        if case(5):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST ATTACK MODELS ELICITATION PROCESSING\n\n")
            attackModels()
            informationCapture()

        if case(6):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST TEST SPECIFICATION ELICITATION PROCESSING\n\n")
            testSpecification()
            informationCapture()

        if case(7):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST FULL REPORT PROCESSING\n\n")
            fullReport()
            informationCapture()


        if case(8):
            print("\n\n*** Application finished successfully! ***\n\n")
            exit(0)

        if case.default:
            print("\nError! Insert a valid value between 1 and 8!\n")
            goto.begin


#############################################################################################################
# Information Capture main function
def informationCapture():
    print("************************************************************************************************")
    print("\nWelcome to SECloudMobDESIGNS Framework!\n")
    print("\nWhat would you like to do?\n")
    print("\n1. First, Answer the Questions Necessary for Possible Processing")
    print("\n2. Process Security Requirement Elicitation Request")
    print("\n3. Process Secure Development Best Practice Guide Request ")
    print("\n4. Process Secure Development Security Mechanisms Guide Request")
    print("\n5. Mapping Attack Models Request")
    print("\n6. Process Secure Development Test Specification Guide Request")
    print("\n7. Process Full Report")
    print("\n8. Exit")
    print("\n\nSelect your option (1-8):")
    switch1()


#############################################################################################################
# Processing Information main function about Security Requirements
def securityRequirements():
    print("")
    print("  Processing information.....")
    print("")

    printData()

    report = open("SECURITY_REQUIREMENTS.md", "w")
    report.write("# Final Security Requirements Report " + '\n')
    report.write("\n")

    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")

    ###################################################################################################

    # check if database and personal information, confidential or critical data are choosen
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/confidentiality.md", "r").read())

    ###################################################################################################
    # integrity requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/integrity.md", "r").read())

    ###################################################################################################
    # avaliability requirements

    report.write(open("requirements/avaliability.md", "r").read())

    ###################################################################################################
    # authentication requirements
    if qans["Q3"].find("1") != -1:
        report.write(open("requirements/authentication.md", "r").read())

    ###################################################################################################
    # authorization requirements
    if qans["Q5"].find("1") != -1:
        if qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write(open("requirements/authorization.md", "r").read())

    ###################################################################################################
    # nonRepudiaton requirements
    if qans["Q5"].find("1") != -1:
        if qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/nonRepudiation.md", "r").read())
            report.write(open("requirements/accountability.md", "r").read())

    ###################################################################################################
    # reliability requirements
    report.write(open("requirements/reliability.md", "r").read())

    ###################################################################################################
    # privacy requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/privacy.md", "r").read())

    ###################################################################################################
    # physical security requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1) and qans["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/physicalSecurity.md", "r").read())

    ###################################################################################################
    # forgery resistance requirement
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1) and qans["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/forgeryResistance.md", "r").read())

    ###################################################################################################
    # tampering detection requirement
    if qans["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/tamperDetection.md", "r").read())

    ###################################################################################################
    # data freshness requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/dataFreshness.md", "r").read())

    ###################################################################################################
    # confinement requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q13"].find("1") != -1 or qans["Q15"].find("1") != -1 or qans["Q16"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/confinement.md", "r").read())

    ###################################################################################################
    # Interoperability requirement
    if qans["Q13"].find("1") != -1 and qans["Q15"].find("1") != -1 and qans["Q16"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/interoperability.md", "r").read())

    ###################################################################################################
    # data origin authentication
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q5"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/dataOriginAuthentication.md", "r").read())
            
    report.close()
    securRequirconvertReport()
    print("# Processing done! Check your requirements in the SECURITY_REQUIREMENTS.pdf file")


#############################################################################################################
# Processing Information main function about Good Practices
def goodPractices():
    print("")
    print("  Processing information.....")
    print("")

    report = open("GOOD_PRACTICES.md", "w")
    report.write("# Final Security Good Practices " + '\n')
    report.write("\n")

    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")

    # check if embebbed systems are chosen
    if (qans["Q1"].find("1") != -1 or qans["Q1"].find("2") != -1 or qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1 or qans["Q1"].find("5") != -1 or qans["Q1"].find("6") != -1):
        if qans["Q1"].find("7") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("goodPractices/IOT_Security_guide.md", "r").read())
    
    # check if SQL database is choosed
    if qans["Q1"].find("3") != -1 and qans["Q1"].find("4"):
        if qans["Q5"].find("1") != -1 and qans["Q6"].find("1"):
            report.write("\n")
            report.write("\n")
            
            # write SQL injection guide
            report.write(open("goodPractices/SQL_Injection_guide.md", "r").read())

    # check if Java and C# programming languages are chosen
    if (qans["Q1"].find("1") != -1 and (qans["Q11"].find("1") != -1 or qans["Q11"].find("4") != -1)):
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/Java_C#_guide.md", "r").read())

    # checks whether input forms are used
    if qans["Q12"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        # write input validation guide
        report.write(open("goodPractices/Input_Validation_guide.md", "r").read())

    # checks whether the mobile app uses authentication and stores personal, confidential or critical data
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            # Session Management guide
            report.write(open("goodPractices/Session_Management_guide.md", "r").read())

    # checks whether the mobile web or hybrid app uses authentication and stores personal, confidential or critical data
    if qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1:
        if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1): 
            report.write("\n")
            report.write("\n")
            # write XSS guide
            report.write(open("goodPractices/Cross_Site_Scripting_guide.md", "r").read())
            
    # checks whether the mobile app use database and stores confidential or critical data
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        # write XSS guide
        report.write(open("goodPractices/Cryptography_guide.md", "r").read())

    # checks whether the mobile app store confidential or crital data and uses hybrid or public Cloud
    if qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
        if qans["Q17"].find("2") != -1 or qans["Q17"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            # write SSL/TLS guide
            report.write(open("goodPractices/TLS_guide.md", "r").read())

    # checks whether the mobile app use authentication, database and store confidential or critical data
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            # write Access Control guide
            report.write(open("goodPractices/Access_Control_guide.md", "r").read())

    # checks whether mobile app uploads files
    if qans["Q12"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write file upload guide
        report.write(open("goodPractices/File_Upload_guide.md", "r").read())

    # Checks whether mobile app generate logging info
    if qans["Q13"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write logging guide
        report.write(open("goodPractices/Logging_guide.md", "r").read())

    # checks whether mobile applications make regular updates
    if qans["Q14"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write update guide
        report.write(open("goodPractices/App_Update_guide.md", "r").read())

    # checks whether mobile applications interact with third-party applications 
    if qans["Q15"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write third-party guide
        report.write(open("goodPractices/App_Third_Party_guide.md", "r").read())

    report.close()
    goodPracticeConvertReport()
    print("# Processing done! Check your requirements in the GOOD_PRACTICES.pdf file")


#############################################################################################################
# Processing Information main function about Attack Models
def attackModels():
    print("")
    print("  Processing information.....")
    print("")

    report = open("ATTACKS_MAPPING.md", "w")
    report.write("# Final Attack Models Report  " + '\n')
    report.write("\n")

    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")
    report.write("\n")
    report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # Database use and public cloud environment MitM attacks
    if qans["Q5"].find("1") != -1 and (qans["Q17"].find("4") != -1 or qans["Q17"].find("2") != -1):
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/mitmAttack.md", "r").read())

            # MitM attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](mitmAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, we have XSS
    if qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1 and (qans["Q17"].find("4") != -1 or qans["Q17"].find("2") != -1):
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/XSS.md", "r").read())

            # XSS attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](xssAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the aplication is web or hybrid, we have Cookie Poisoning
    if (qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1) and (qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/dnsPoisoningAttack.md", "r").read())

        # CookiePoisoning attack tree diagram

        # Write de scheme in the report
        report.write("![alt text](dnsPoisoningAttack.png)")
        report.write("\n")
        report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, and storage personal, confidential or critical data, we have a Malicious QR Code Attacks
    if (qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1) and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/maliciousQRCode.md", "r").read())
            # Malicious QR Code attack diagram

            # Write de scheme in the report
            report.write("![alt text](malicIousQRCodeAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # f the application is web or hybrid, we have CAPTCHA Breaking Attacks
    if (qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1) and (qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/captchaBreaking.md", "r").read())

    # CAPTCHA Breaking attack tree diagram

    # Write de scheme in the report
    # report.write("![alt text](design_schemes6.png)")
    # report.write("\n")
    # report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # Database use and public cloud environment SQLi attacks
    if (qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1) and qans["Q3"].find("1") != -1 :
        if qans["Q5"].find("1") != -1 and qans["Q6"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q7"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/SQLi.md", "r").read())

            # SQLi attack tree diagram

            # Write the scheme in the report
            report.write("![alt text](SQLi.png)")
            report.write("\n")
            report.write("\n")
    
    ###########################################################################################################
    ###########################################################################################################
    # DoS Attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write(open("attackModels/DoS.md", "r").read())
            # DoS attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](DoS.png)")
            report.write("\n")
            report.write("\n")
            
            # DDoS attack tree
            report.write(open("attackModels/DDoS.md", "r").read())
            
            # DDoS attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](DDoS.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # Sniffer Attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q17"].find("4") != -1 or qans["Q17"].find("2") != -1):
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write(open("attackModels/Sniffer.md", "r").read())

            # Sniffer attack tree diagram

            # Write the scheme in the report
            report.write("![alt text](eavesdropingAttack.png)")
            report.write("\n")
            report.write("\n")

    # If the application is web or hybrid, we have DNS Poisoning Attack

    ###########################################################################################################
    ###########################################################################################################
    # DNS Attacks
    if qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1:
        report.write(open("attackModels/DNS.md", "r").read())

        # DNS Poisoning attack tree diagram

        # Write the scheme in the report

        # report.write("![alt text](dnsPoisoningAttack.png)")
        # report.write("\n")
        # report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, we have Reused IP Address Attacks
    if qans["Q1"].find("3") != -1 or qans["Q1"].find("4") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/reusedIPAddress.md", "r").read())

        # Reused IP Address attack tree diagram

        # Write the scheme in the report
        report.write("![alt text](ipSpoofingAttack.png)")
        report.write("\n")
        report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, we have Phishing Attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1):
        if (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/phishingAttack.md", "r").read())
            
            # Phishing Attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](phishingAttack.png)")
            report.write("\n")
            report.write("\n")
            ###########################################################################################################
            ###########################################################################################################
            # Botnet Attacks
            report.write(open("attackModels/Botnet.md", "r").read())

            # Botnet attack tree diagram

            # Write the scheme in the report
            report.write("![alt text](botnetAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, we have XML
    if qans["Q1"].find("4") != -1 or qans["Q1"].find("3") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/XMLi.md", "r").read())

        # XML Attack tree diagram

        # Write the scheme in the report
        report.write("![alt text](xmliAttack.png)")
        report.write("\n")
        report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the application is web or hybrid, we have Session Hijacking and Session Fixation
    if qans["Q1"].find("4") != -1 or qans["Q1"].find("3") != -1:
        if qans["Q7"].find("2") != -1 or qans["Q7"].find("3") != -1:
            if qans["Q4"].find("1") != -1 and qans["Q10"].find("6") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/sessionHijacking.md", "r").read())

                # Session Hijacking attack tree diagram

                # Write the scheme in the report
                report.write("![alt text](sidHijacking.png)")
                report.write("\n")
                report.write("\n")

                ###########################################################################
                ###########################################################################
                # Session Fixation
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/sessionFixation.md", "r").read())

                # Session Fixation Attack tree diagram

                # Write the scheme in the report
                report.write("![alt text](sidFixation.png)")
                report.write("\n")
                report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for iOS, Tizen and embedded platforms (Buffer Overflow)
    if qans["Q1"].find("2") != -1 or qans["Q1"].find("6") != -1 or qans["Q1"].find("7") != -1:
        if qans["Q11"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/bufferOverflows.md", "r").read())

        # Buffer Overflows attack diagram

        # Write the scheme in the report
        report.write("![alt text](bufferOverflowAttackTree.png)")
        report.write("\n")
        report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android, iOS, Tizen and embedded platforms (Mobile Apllication Spoofing )
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 :
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/Spoofing.md", "r").read())

            # Spoofing attack tree diagram

            # Write the scheme in the report
            report.write("![alt text](spoofingAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 :
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/VMMigration.md", "r").read())

            # Attack on VM at migration tree diagram

            # Write the scheme in the report
            report.write("![alt text](vmMigrationAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################

    # If the system was development for Android, iOS, Tizen and embedded platforms (Insiders Malicious Attacks)
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 :
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            if qans["Q21"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/maliciousInsider.md", "r").read())

                # Malicious Insiders attack tree diagram

                # Write the scheme in the report
                report.write("![alt text](maliciousInsidersAttack.png)")
                report.write("\n")
                report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android, iOS, Tizen and embedded platforms (VM Escape Attack)
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/VMEscape.md", "r").read())
            
            # VM Escape attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](vmEscapeAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android, iOS, Tizen and embedded platforms (Cross VM Attack)
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/crossVM.md", "r").read())

            # Cross Side Channel attack tree diagram

            # Write the scheme in the report
            report.write("![alt text](sideChannelAttack.png)")
            report.write("\n")
            report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android and iOS (Malware Injection Attacks)
        if (qans["Q1"].find("1") != -1 or qans["Q1"].find("2") != -1) and qans["Q5"].find("1") != -1:    
            if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/malwareInjection.md", "r").read())

                # Cross VM attack tree diagram

                # Write the scheme in the report
                report.write("![alt text](malwareInjectionAttack.png)")
                report.write("\n")
                report.write("\n")

    ###########################################################################################################
    ###########################################################################################################
    # If the system was development for Android, iOS, Tizen and embedded platforms (Tampering Attacks)
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            if qans["Q21"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/tamperingAttack.md", "r").read())

                # Tampering Detection attack tree diagram

                # Write the scheme in the report
                report.write("![alt text](tamperingAttack.png)")
                report.write("\n")
                report.write("\n")

    ###########################################################################################################

    report.close()
    attackModelConvertReport()
    print("# Processing done! Check your requirements in the ATTACKS_MAPPING.pdf file")

#############################################################################################################
# Processing Information main function about Test Specification
def testSpecification():
    print("")
    print("  Processing information.....")
    print("")

    report = open("TEST_SPECIFICATION.md", "w")
    report.write("# Final Security Test Specification and Tools Report  " + '\n')
    report.write("\n")

    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")
    report.write("\n")
    report.write("\n")

    ###################################################################################################
    ###################################################################################################
    # Security Testing against DoS, DDoS and Botnet Attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q17"].find("1") != -1 or qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1 :
            report.write(open("securityTesting/BOTNETDOSDDOSTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    ###################################################################################################
    ###################################################################################################
    # Security Testing against MitM, DoS, DDoS, Botnet, Phishing and Spoofing attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if (qans["Q17"].find("4") != -1 or qans["Q17"].find("2") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/BotnetDoSDDoSPHISINGSPOOFINGPHISHINGMITMTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    ###################################################################################################
    ###################################################################################################
    # Security Testing against SQLi, XMLi, CRSF, XSS, googleHacking and phishing attacks 
    if qans["Q1"].find("4") != -1 or  qans["Q1"].find("3") != -1:
        if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and qans["Q6"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
            if qans["Q17"].find("1") != -1 or (qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1):
                report.write("\n")
                report.write("\n")
                report.write(open("securityTesting/SQLiXSSCSRFSPOOFINGTEST.md", "r").read())

    ###################################################################################################
    ###################################################################################################
    # Security Testing against Sniffing, Botnet, Phishing and Spoofing Attacks
    if qans["Q1"].find("1") != -1 or qans["Q1"].find("2") != -1  or qans["Q1"].find("4") != -1 or qans["Q1"].find("3") != -1:
        if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
            if qans["Q17"].find("2") != -1 or qans["Q17"].find("4") != -1:
                report.write(open("securityTesting/BOTNETSNIFFINGSPOOFINGPHISHINGTEST.md", "r").read())
                report.write("\n")
                report.write("\n")

    ###################################################################################################
    ###################################################################################################
    # Security Testing against Botnet, Spoofing and Sniffing attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1) :
        if qans["Q20"].find("1") != -1 or  qans["Q20"].find("2") != -1 or qans["Q20"].find("4") != -1 or qans["Q20"].find("5") != -1 or qans["Q20"].find("6") != -1 or qans["Q20"].find("8") != -1 :
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/BOTSPOOFINGSNIFFINGTEST.md", "r").read())

    ###################################################################################################
    ###################################################################################################
    # Security Testing against Buffer Overflow attacks
    if qans["Q1"].find("2") != -1 or qans["Q1"].find("6") != -1 or qans["Q1"].find("7") != -1:
        if qans["Q10"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/BUFFEROVERFLOWTEST.md", "r").read())

    ###################################################################################################
    ###################################################################################################
    # Security Testing against Malicious Insider and VM-Migration attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/MINSIDERVMMIGRATIONTEST.md", "r").read())
            report.write("\n")
            report.write("\n")
    ###################################################################################################
    ###################################################################################################

    # Security Testing against Malware Injection and Side-channel attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q21"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/MALWAREINJECTIONSIDECHANNELTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    ###################################################################################################
    ###################################################################################################
    # Security Testing against physical Attacks
    if qans["Q3"].find("1") != -1 and qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q21"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/physicalAttacksTest.md", "r").read())
            report.write("\n")
            report.write("\n")

    report.close()
    testSpecConvertReport()
    print("# Processing done! Check your requirements in the TEST_SPECIFICATION.pdf file")

#############################################################################################################
# Processing Information main function about Security Mechanisms
def securityMechanisms():
    print("")
    print("  Processing information.....")
    print("")

    printData()

    report = open("SECURITY_MECHANISMS.md", "w")
    report.write("# Final Security Mechanisms Report " + '\n')
    report.write("\n")

    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")

    ###################################################################################################

    # Backup mechanisms
    if qans["Q5"].find("1") != -1 and (
            qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/backupMechanism.md", "r").read())

    ###################################################################################################
    # Audit and cryptographic algorithms mechanisms
    if qans["Q5"].find("1") != -1 and (
            qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/auditMechanisms.md", "r").read())

        report.write(open("mechanisms/cryptographicAlgorithmsMechanisms.md", "r").read())

    ###################################################################################################
    # Authentication mechanisms
    if qans["Q3"].find("1") != -1 and qans["Q4"].find("1") != -1:
        report.write(open("mechanisms/biometricAuthenticationMechanism.md", "r").read())
    if qans["Q3"].find("1") != -1 and qans["Q4"].find("2") != -1:
        report.write(open("mechanisms/channelBasedAuthenticationMechanism.md", "r").read())
    if qans["Q3"].find("1") != -1 and qans["Q4"].find("3") != -1:
        report.write(open("mechanisms/factorsBasedAuthenticationMechanism.md", "r").read())
    if qans["Q3"].find("1") != -1 and qans["Q4"].find("4") != -1:
        report.write(open("mechanisms/IDBasedAuthenticationMechanism.md", "r").read())

    ###################################################################################################    
    # Cryptographic protocolos mechanisms    
    if qans["Q5"].find("1") != -1 and (
            qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/cryptographicProtocolsMechanism.md", "r").read())

    ###################################################################################################
    # Access control mechanisms
    if qans["Q5"].find("1") != -1:
        if qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write(open("mechanisms/accessControlMechanisms.md", "r").read())

    ###################################################################################################
    # Inspection and registration mechanisms
    if qans["Q5"].find("1") != -1:
        if qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/inspectionMechanism.md", "r").read())
            report.write(open("mechanisms/registrationMechanism.md", "r").read())

    ###################################################################################################
    # physical security requirements
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("1") != -1 or qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1) and qans["Q21"].find(
            "1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/deviceDetectionMechanism.md", "r").read())
        report.write(open("mechanisms/physicalLocationMechanism.md", "r").read())


    ###################################################################################################
    # Confinement mechanisms
    if qans["Q5"].find("1") != -1 and (qans["Q8"].find("2") != -1 or qans["Q8"].find("3") != -1):
        if qans["Q13"].find("1") != -1 or qans["Q15"].find("1") != -1 or qans["Q16"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/confinementMechanism.md", "r").read())

    ###################################################################################################
    # Filtering mechanisms
    if qans["Q13"].find("1") != -1 and qans["Q15"].find("1") != -1 and qans["Q16"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/filteringMecanism.md", "r").read())

    report.close()
    securityMechanismsConvertReport()
    print("# Processing done! Check your requirements in the SECURITY_MECHANISMS.pdf file")

def fullReport():
    
    securityRequirements()
    goodPractices()
    securityMechanisms()
    attackModels()
    testSpecification()

    pdfs = ['SECURITY_REQUIREMENTS.pdf', 'GOOD_PRACTICES.pdf', 'SECURITY_MECHANISMS.pdf', 'ATTACKS_MAPPING.pdf', 'TEST_SPECIFICATION.pdf']

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("FULL_REPORT.pdf")
    merger.close()
    print("\n\n *** Processing  done! See the full report requested in the FINAL_REPORT.pdf file. \n\n ***")

if __name__ == "__main__":
    print("---")
    print("")
    print("#  Welcome to ")
    print("")
    print("#  SECloudMobDESIGNS ")
    print("")
    print("  The **SECloudMobDESIGNS** is a custom made program.")
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

    print("")
    print("#############################################################")  # after this is for debugging xD

    print("")
    print("")
    print("")

    exit(0)

# license Apache-2.0
