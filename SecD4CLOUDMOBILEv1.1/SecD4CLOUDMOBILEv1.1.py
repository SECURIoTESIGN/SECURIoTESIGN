#!/usr/bin/python coding=utf-8
# !/bin/bash

"""
// ---------------------------------------------------------------------------
//
//	Security by Design for Cloud and Mobile Ecosystem (SecD4CLOUDMOBILE)  
//
//  Copyright (C) 2020 Instituto de Telecomunicações (www.it.pt)
//  Copyright (C) 2020 Universidade da Beira Interior (www.ubi.pt)
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// This Work was developed under Doctoral Grant, supported by project 
// CENTRO-01-0145-FEDER-000019 - C4 - Competence Center in Cloud Computing, 
// Research Line 1: Cloud Systems, Work package WP 1.2 - Systems design and development 
// processes and software for Cloud and Internet of Things ecosystems, cofinanced by the 
// European Regional Development Fund (ERDF) through the Programa Operacional Regional do 
// Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científica e 
// Tecnológica - Programas Integrados de IC&DT.
// ---------------------------------------------------------------------------
"""

import os
import webbrowser
from markdown import markdown
from xhtml2pdf import pisa
from switch import Switch
from goto import with_goto
from PyPDF2 import PdfFileMerger

################################# GLOBAL VARIABLES #################################

version = 1

# list that contains to answers in the written file
input_list = []

# add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
answers_list = []
comments_list = []
table_for_report = []

# create a dictionairy to store the answers to the questions
# question_and_answers as questions_and_answers
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
    "Q19": "",
    "Q20": "",
    "Q21":""
}

# Questions
# Q1   -> Mobile Platform
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
    "1": "SQL (Relational Database)",
    "2": "NoSQL",
    "3": "Local Storage (Centralized Database)",
    "4": "Distributed Storage",
    "5": "Cloud Database"
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
    "2": "Will be an administrator that will register the users"
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
    "9": "Kotlin",
    "10": ""
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

################################# FUNCTIONS #################################

"""
 [Summary]: Common method that validates the filename entered by the user and checks if the file exists or not
 [Returns]: No return
"""
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


"""
[Summary]: Common method to validate input and implemts dynamic arguments
[Arguments]: 
    - arg(1) what to validate -> if it is to validate a int or a string (1 or 2)
    - arg(2) n_options -> number of options in the question (==range)
[Returns]: Returns user inputs
"""
def validateInput(*arg):

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


"""
[Summary]: Method that gets the platform of the mobile application developed or to be developed
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def arqui(version):
    print("---")
    print("")
    if version == 1:
        print("  **Which will be the mobile platform of the system?**  ")
    else:
        print("  **What is the mobile platform of the system?**  ")
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

    while (1):
        # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
        value = validateInput(1, 11)
        if value == 0:
            return
        if value == 10:
            print("  Please specify the mobile platform: (name between single quotes)  ")
            value2 = validateInput(2)
            questions_and_answers["Q1"] = questions_and_answers["Q1"] + str(value2) + ";"

        else:
            questions_and_answers["Q1"] = questions_and_answers["Q1"] + str(value) + ";"

"""
[Summary]: Method that gets the domain of the mobile application developed or to be developed
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q2"] = str(value)

"""
[Summary]: Method that allows identifying if the application to be developed or developed uses authentication or not
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q3"] = str(value)

    if value == 1:
        typeOfAuthentication(version)
    else:
        questions_and_answers["Q4"]="N/A"

"""
[Summary]: Method responsible for identifying the authentication scheme to be used or used by the application
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
            questions_and_answers["Q4"] = questions_and_answers["Q4"] + str(value2) + ";"

        else:
            questions_and_answers["Q4"] = questions_and_answers["Q4"] + str(value) + ";"

"""
[Summary]: Method that allows identifying if the application to be developed or developed uses a database or not
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def hasDB(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Will the system use a Database?**  ")
    else:
        print("  **Does the system use a Database?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    questions_and_answers["Q5"] = str(value)

    if value == 1:
        typeOfDatabase(version)
        if questions_and_answers["Q6"] == '1' or questions_and_answers["Q6"] == '2':
            whichDatabase(version)
        sensitiveData(version)
    else:
        questions_and_answers["Q6"] = "N/A"
        questions_and_answers["Q7"] = "N/A"
        questions_and_answers["Q8"] = "N/A"
        return

"""
[Summary]: Method to identify the type of storage of the end-users of the application
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def typeOfDatabase(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **What will be the type of data storage?**  ")
    else:
        print("  **What is type of data storage?**  ")
    print("")
    print("  1 - SQL (Relational Database) ")
    print("  2 - NoSQL  ")
    print("  3 - Local Storage  (Centralized Database) ")
    print("  4 - Distributed Storage ")
    print("  5 - Cloud Database ")
    print("")

    value = validateInput(1, 6)
    questions_and_answers["Q6"] = str(value)

"""
[Summary]: Method allowing the identification of the DBMS to be used by the system
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def whichDatabase(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **Which Database (DBMS) will be used ?**  ")
    else:
        print("  **What is the Database (DBMS) used?**  ")

    print("")

    if questions_and_answers["Q6"] == '1':
        print("  1 - SQL Server  ")
        print("  2 - MySQL  ")
        print("  3 - PostgreSQL  ")
        print("  4 - SQLite  ")
        print("  5 - OracleDB  ")
        print("  6 - MariaDB  ")

    if questions_and_answers["Q6"] == '2':
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
        questions_and_answers["Q7"] = str(value2)
    else:
        questions_and_answers["Q7"] = str(value)

"""
[Summary]: Method allowing the identification of the type of data stored by the system (personal, confidential or critical)
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    print("  4 - Other ")
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
            questions_and_answers["Q8"] = questions_and_answers["Q8"] + str(value2) + ";"
        else:
            questions_and_answers["Q8"] = questions_and_answers["Q8"] + str(value) + ";"

"""
[Summary]: Method allowing the identification of whether or not the application allows users to register
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q9"] = str(value)

    if value == 1:
        typeOfUserRegist(version)
    else:
        questions_and_answers["Q10"] = "N/A"

"""
[Summary]: Method to identify the type of registration of users to the system
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    print("  2 - Will be an administrator that will register the users  ")
    print("")

    value = validateInput(1, 3)
    questions_and_answers["Q10"] = str(value)

"""
[Summary]: Method to identify the programming language to be used or used for coding the application
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    print("  9 - Kotlin ")
    print("  10 - Other/Property Language  ")
    print("")

    while (1):
        value = validateInput(1, 11)
        if value == 0:
            return
        if value == 9:
            print("  Please specify the programming language: (name between single quotes)  ")
            # TO-DO change this funtion input
            value2 = validateInput(2)
            # question_9["8"]  = str(value2)
            questions_and_answers["Q11"] = questions_and_answers["Q11"] + str(value2) + ";"

        else:
            questions_and_answers["Q11"] = questions_and_answers["Q11"] + str(value) + ";"

"""
[Summary]: Method to identify if the application uses or not user input forms
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q12"] = str(value)

"""
[Summary]: Method to identify the application allows or not upload files
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q13"] = str(value)

"""
[Summary]: Method to identify the application records or not logs
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q14"] = str(value)

"""
[Summary]: Method to identify the application allows or not regular updates
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q15"] = str(value)

"""
[Summary]: Method to identify the application uses or not third-party apps
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q16"] = str(value)

"""
[Summary]: Method to identify the Cloud development model (environment) used by the application
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def cloudPlatform(version):
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
    questions_and_answers["Q17"] = str(value)

"""
[Summary]: Method that allows identifying if the user wants to specify some hardware details (network and authentication scheme) or not
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q18"] = str(value)

    if value == 1:
        hardwareAuth(version)
        hardwareComunication(version)
    else:
        questions_and_answers["Q19"] = "N/A"
        questions_and_answers["Q20"] = "N/A"

"""
[Summary]: Method allowing the identification of the authentication paradigm implemented in relation to the hardware
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q19"] = str(value)

"""
[Summary]: Method allowing the identification of wireless network technologies implemented in relation to hardware
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
            questions_and_answers["Q20"] = questions_and_answers["Q20"] + str(value2) + ";"
        else:
            questions_and_answers["Q20"] = questions_and_answers["Q20"] + str(value) + ";"

"""
[Summary]: Method to identify the existence or not of the possibility of physical access to the system (data centre and mobile device)
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q21"] = str(value)

"""
[Summary]: Method to open/create and store in the file 'ans.txt' the answers to the user questionnaire
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def print_data():
    generate_file = open("ans.txt", "w")

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is user input text) OR fix this buy make it simple, verify if it the answer has only letters xD
    # find if the first caracter is a letter and if the answer has no more options
    if questions_and_answers["Q1"][0].isdigit() == False and questions_and_answers["Q1"].find(";") == -1:
        list_aux.append(questions_and_answers["Q1"])

    else:

        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q1"].split(";")

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
    print("{:22} {:3} {:40} ".format("Mobile Platform", ":", ' ; '.join(list_aux)))
    table_for_report.append(["Mobile Platform", ' ; '.join(list_aux)])

    answers_list.append(questions_and_answers["Q1"])
    comments_list.append(' ; '.join(list_aux))

    for n in question2:
        item = questions_and_answers["Q2"]
        if item == n:
            print("{:22} {:3} {:40}".format("Application domain type", ":", question2[n]))

            table_for_report.append(["Application domain type", question2[n]])

            answers_list.append(questions_and_answers["Q2"])
            comments_list.append(question2[n])

    for n in question3:
        item = questions_and_answers["Q3"]
        if item == n:
            print("{:22} {:3} {:40}".format("Authentication", ":", question3[n]))

            table_for_report.append(["Authentication", question3[n]])

            answers_list.append(questions_and_answers["Q3"])
            comments_list.append(question3[n])

    list_aux = []
    # it is a multiple question
    # find if the answer correspond to option "others" (means that is user input text) or not answered
    if questions_and_answers["Q4"][0].isdigit() == False and questions_and_answers["Q4"].find(";") == -1:
        list_aux.append(questions_and_answers["Q4"])
    else:
        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q4"].split(";")

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

    answers_list.append(questions_and_answers["Q4"])
    comments_list.append(' ; '.join(list_aux))

    for n in question5:
        item = questions_and_answers["Q5"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Has DB", ":", question5[n]))

            table_for_report.append(["Has DB", question5[n]])

            answers_list.append(questions_and_answers["Q5"])
            comments_list.append(question5[n])

    item = questions_and_answers["Q6"]
    # case this question is not answered, and the answer it will be "N/A"
    if questions_and_answers["Q6"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of data storage", ":", item))

        table_for_report.append(["Type of data storage", item])

        answers_list.append(questions_and_answers["Q6"])
        comments_list.append(item)

    else:
        for n in question6:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of data storage", ":", question6[n]))

                table_for_report.append(["Type of data storage", question6[n]])

                answers_list.append(questions_and_answers["Q6"])
                comments_list.append(question6[n])

    item = questions_and_answers["Q7"]
    for n in question7:
        if item == n:
            print("{:22} {:3} {:40} ".format("Which DB", ":", question7[n]))

            table_for_report.append(["Which DB", question7[n]])

            answers_list.append(questions_and_answers["Q7"])
            comments_list.append(question7[n])

    # case of user input text
    if item.isdigit() == False:
        print("{:22} {:3} {:40} ".format("Which DB", ":", item))

        table_for_report.append(["Which DB", item])

        answers_list.append(questions_and_answers["Q7"])
        comments_list.append(item)

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is user input text) or not answered
    if questions_and_answers["Q8"][0].isdigit() == False and questions_and_answers["Q8"].find(";") == -1:
        list_aux.append(questions_and_answers["Q8"])
    else:

        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q8"].split(";")

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

    answers_list.append(questions_and_answers["Q8"])
    comments_list.append(' ; '.join(list_aux))

    for n in question9:
        item = questions_and_answers["Q9"]
        if item == n:
            print("{:22} {:3} {:40}".format("User Registration", ":", question9[n]))

            table_for_report.append(["User Registration", question9[n]])

            answers_list.append(questions_and_answers["Q9"])
            comments_list.append(question9[n])

    item = questions_and_answers["Q10"]
    if questions_and_answers["Q10"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of Registration", ": ", item))

        table_for_report.append(["Type of Registration", item])

        answers_list.append(questions_and_answers["Q10"])
        comments_list.append(item)
    else:
        for n in question10:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of Registration", ": ", question10[n]))

                table_for_report.append(["Type of Registration", question10[n]])

                answers_list.append(questions_and_answers["Q10"])
                comments_list.append(question10[n])

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q11"][0].isdigit() == False and questions_and_answers["Q11"].find(";") == -1:
        list_aux.append(questions_and_answers["Q11"])
    else:

        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q11"].split(";")

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

    answers_list.append(questions_and_answers["Q11"])
    comments_list.append(' ; '.join(list_aux))

    for n in question12:
        item = questions_and_answers["Q12"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Input Forms", ":", question12[n]))

            table_for_report.append(["Input Forms", question12[n]])

            answers_list.append(questions_and_answers["Q12"])
            comments_list.append(question12[n])

    for n in question13:
        item = questions_and_answers["Q13"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Upload Files", ":", question13[n]))

            table_for_report.append(["Upload Files", question13[n]])

            answers_list.append(questions_and_answers["Q13"])
            comments_list.append(question13[n])

    for n in question14:
        item = questions_and_answers["Q14"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has logs", ":", question14[n]))

            table_for_report.append(["The system has logs", question14[n]])

            answers_list.append(questions_and_answers["Q14"])
            comments_list.append(question14[n])

    for n in question15:
        item = questions_and_answers["Q15"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has regular updates", ":", question15[n]))

            table_for_report.append(["The system has regular updates", question15[n]])

            answers_list.append(questions_and_answers["Q15"])
            comments_list.append(question15[n])

    for n in question16:
        item = questions_and_answers["Q16"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has third-party", ":", question16[n]))

            table_for_report.append(["The system has third-party", question16[n]])

            answers_list.append(questions_and_answers["Q16"])
            comments_list.append(question16[n])

    for n in question17:
        item = questions_and_answers["Q17"]
        if item == n:
            print("{:22} {:3} {:40}".format("System Cloud Environments", ":", question17[n]))

            table_for_report.append(["System Cloud Environments", question17[n]])

            answers_list.append(questions_and_answers["Q17"])
            comments_list.append(question17[n])

    for n in question18:
        item = questions_and_answers["Q18"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Hardware Specification", ":", question18[n]))

            table_for_report.append(["Hardware Specification", question18[n]])

            answers_list.append(questions_and_answers["Q18"])
            comments_list.append(question18[n])

    for n in question19:
        item = questions_and_answers["Q19"]
        if item == n:
            print("{:22} {:3} {:40} ".format("HW Authentication", ":", question19[n]))

            table_for_report.append(["HW Authentication", question19[n]])

            answers_list.append(questions_and_answers["Q19"])
            comments_list.append(question19[n])

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q20"][0].isdigit() == False and questions_and_answers["Q20"].find(";") == -1:
        list_aux.append(questions_and_answers["Q20"])
    else:
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q20"].split(";")

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

    answers_list.append(questions_and_answers["Q20"])
    comments_list.append(' ; '.join(list_aux))

    for n in question21:
        item = questions_and_answers["Q21"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Data Center Phisical Access", ":", question21[n]))

            table_for_report.append(["Data Center Phisical Access", question21[n]])

            answers_list.append(questions_and_answers["Q21"])
            comments_list.append(question21[n])

    # write / generate a file with all answers
    for i in range(0, len(answers_list)):
        generate_file.write("{:20}{:3}{:20}\n".format(answers_list[i], " # ", comments_list[i]))

    generate_file.close()

"""
[Summary]: Method to convert the markdown Security Requirements report to html and pdf format
[Arguments]: No arguments
[Returns]: No return
"""
def requirements_convert_report():
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

"""
[Summary]: Method to convert the markdown Security Best Practices Guidelines (SBPG) report to html and pdf format
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def security_best_practices_convert_report():
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


"""
[Summary]: Method to convert the markdown Security Mechanism Elicitation (SME) report to html and pdf format
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def mechanisms_convert_report():
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

"""
[Summary]: Method to convert the markdown Attack Models Elicitation (AME) report to html and pdf format
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def attack_models_convert_report():
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

"""
[Summary]: Method to convert the markdown Security Test Specification and Automation Tools (STSAT) report to html and pdf format
[Arguments]: No arguments
[Returns]: No return
"""
def security_test_recommendation_convert_report():
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

"""
[Summary]: Method auxiliary to the input method responsible for processing user requests
[Arguments]: No arguments
[Returns]: No return
"""
@with_goto
def switch1():

    label.begin

    val = 0
    while True:
        try:
            val = int(input("\nWhat is your option?\n"))
            print("-->")
        except ValueError:
            print("Error! Enter a whole number between 1 and 8, according to the menu above!")
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
                cloudPlatform(version)
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
                questions_and_answers["Q20"] = input_list[19]
                questions_and_answers["Q21"] = input_list[20]

            information_capture()

            print("# Processing Done! Choose another option to process the requests!")

        if case(2):
            print("\n********************************************************************************************\n")
            print("\t\t The request for security requirements is in progress ... \n\n")
            get_requirements()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/SECURITY_REQUIREMENTS.pdf')
            information_capture()

        if case(3):
            print("\n********************************************************************************************\n")
            print("\t\t The request for best practice guidelines is in progress ... \n\n")
            get_security_best_practices()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/GOOD_PRACTICES.pdf')
            information_capture()

        if case(4):
            print("\n********************************************************************************************\n")
            print("\t\t The request for security mechanisms is in progress ... \n\n")
            get_mechanisms()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/SECURITY_MECHANISMS.pdf')
            information_capture()

        if case(5):
            print("\n********************************************************************************************\n")
            print("\t\t The request for attack models is in profess ... \n\n")
            get_attack_models()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/ATTACKS_MAPPING.pdf')
            information_capture()

        if case(6):
            print("\n********************************************************************************************\n")
            print("\t\t The request for the security testing specification and tools is in progress ... \n\n")
            get_security_test_recommendation()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/TEST_SPECIFICATION.pdf')
            information_capture()

        if case(7):
            print("\n********************************************************************************************\n")
            print("\t\t The full report request is in progress ... \n\n")
            fullReport()
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SecD4CLOUDMOBILEv1.1/FULL_REPORT.pdf')
            information_capture()

        if case(8):
            print("\n\n*** Application finished successfully! ***\n\n")
            exit(0)

        if case.default:
            print("\nError! Insert a valid value between 1 and 8!\n")
            goto.begin

"""
[Summary]: Method responsible for creating the main menu and capturing the user data
[Arguments]: No argument
[Return]: No return
"""
def information_capture():
    print("************************************************************************************************")
    print("\nWelcome to SecD4CLOUDMOBILE Framework!\n")
    print("\nWhat would you like to do?\n")
    print("\n1. First, Answer the Questions Necessary for Possible Processing")
    print("\n2. Security Requirement Elicitation Request")
    print("\n3. Secure Development Best Practice Guidelines Request")
    print("\n4. Secure Development Security Mechanisms Request")
    print("\n5. Attack Model Mapping Request")
    print("\n6. Security Test Specification and Tool Request")
    print("\n7. Full Report Request")
    print("\n8. Exit")
    print("\n\nSelect your option (1-8):")
    switch1()


"""
[Summary]: Method responsible for processing information about SRE
[Arguments]: No arguments
[Return]: No return
"""
def get_requirements():
    print("")
    print("  Processing information.....")
    print("")

    print_data()

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

    # check if database and personal information, confidential or critical data are choosen
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/confidentiality.md", "r").read())

    # integrity requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/integrity.md", "r").read())

    # avaliability requirement
    report.write("\n")
    report.write("\n")
    report.write(open("requirements/avaliability.md", "r").read())

    # authentication requirement
    if questions_and_answers["Q3"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/authentication.md", "r").read())

    # authorization requirement
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/authorization.md", "r").read())

    # nonRepudiaton and accountability requirements
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/nonRepudiation.md", "r").read())
            report.write(open("requirements/accountability.md", "r").read())

    # reliability requirement
    report.write("\n")
    report.write("\n")
    report.write(open("requirements/reliability.md", "r").read())

    # privacy requirements
    # if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
    #     report.write("\n")
    #     report.write("\n")
    #     report.write(open("requirements/privacy.md", "r").read())

    # physical security requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/physicalSecurity.md", "r").read())

    # forgery resistance requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/forgeryResistance.md", "r").read())

    # tampering detection requirement
    if questions_and_answers["Q21"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/tamperDetection.md", "r").read())

    # data freshness requirements
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/dataFreshness.md", "r").read())

    # confinement requirements
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q13"].find("1") != -1 or questions_and_answers["Q15"].find("1") != -1 or questions_and_answers["Q16"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/confinement.md", "r").read())

    # Interoperability requirement
    if questions_and_answers["Q13"].find("1") != -1 and questions_and_answers["Q15"].find("1") != -1 and questions_and_answers["Q16"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/interoperability.md", "r").read())

    # data origin authentication
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q5"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/dataOriginAuthentication.md", "r").read())

    report.close()
    requirements_convert_report()
    print("# Processing done! Check your requirements in the SECURITY_REQUIREMENTS.pdf file")

"""
[Summary]: Method responsible for processing information about SBPG module
[Arguments]: No arguments
[Return]: No return
"""
def get_security_best_practices():
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
    if (questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("5") != -1 or questions_and_answers["Q1"].find("6") != -1):
        if questions_and_answers["Q1"].find("7") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("goodPractices/IOT_Security_guide.md", "r").read())

    # check if SQL database is choosed
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4"):
        if questions_and_answers["Q5"].find("1") != -1 and questions_and_answers["Q6"].find("1"):
            report.write("\n")
            report.write("\n")

            # write SQL injection guide
            report.write(open("goodPractices/SQL_Injection_guide.md", "r").read())

    # check if Java and C# programming languages are chosen
    if (questions_and_answers["Q1"].find("1") != -1 and (questions_and_answers["Q11"].find("1") != -1 or questions_and_answers["Q11"].find("4") != -1)):
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/Java_C#_guide.md", "r").read())

    # checks whether input forms are used
    if questions_and_answers["Q12"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        # write input validation guide
        report.write(open("goodPractices/Input_Validation_guide.md", "r").read())

    # checks whether the mobile app uses authentication and stores personal, confidential or critical data
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            # Session Management guide
            report.write(open("goodPractices/Session_Management_guide.md", "r").read())

    # checks whether the mobile web or hybrid app uses authentication and stores personal, confidential or critical data
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            # write XSS guide
            report.write(open("goodPractices/Cross_Site_Scripting_guide.md", "r").read())

    # checks whether the mobile app use database and stores confidential or critical data
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        # write XSS guide
        report.write(open("goodPractices/Cryptography_guide.md", "r").read())

    # checks whether the mobile app store confidential or crital data and uses hybrid or public Cloud
    if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
        if questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            # write SSL/TLS guide
            report.write(open("goodPractices/TLS_guide.md", "r").read())

    # checks whether the mobile app use authentication, database and store confidential or critical data
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            # write Access Control guide
            report.write(open("goodPractices/Access_Control_guide.md", "r").read())

    # checks whether mobile app uploads files
    if questions_and_answers["Q12"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write file upload guide
        report.write(open("goodPractices/File_Upload_guide.md", "r").read())

    # Checks whether mobile app generate logging info
    if questions_and_answers["Q13"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write logging guide
        report.write(open("goodPractices/Logging_guide.md", "r").read())

    # checks whether mobile applications make regular updates
    if questions_and_answers["Q14"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write update guide
        report.write(open("goodPractices/App_Update_guide.md", "r").read())

    # checks whether mobile applications interact with third-party applications 
    if questions_and_answers["Q15"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        # write third-party guide
        report.write(open("goodPractices/App_Third_Party_guide.md", "r").read())

    report.close()
    security_best_practices_convert_report()
    print("# Processing done! Check your security best practices guidelines in the GOOD_PRACTICES.pdf file")


"""
[Summary]: Method responsible for processing information about AME module
[Arguments]: No arguments
[Return]: No return
"""
def get_attack_models():
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

    # Database use and public cloud environment MitM attacks
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/mitmAttack.md", "r").read())

            # MitM attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](attackModels/mitmAttackTree.png")
            report.write("\n")
            report.write("\n")

    # Brute Force and Eavesdropping Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attackModels/bruteForceAttack.md", "r").read())

            # Brute Force attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/bruteForceAttackTree.png)")
            report.write("\n")
            report.write("\n")

            report.write(open("attackModels/eavesdroppingAttack.md", "r").read())

            # Eavesdropping attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/eavesdroppingAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the application is web or hybrid, we have XSS
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 and (questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/XSS.md", "r").read())

            # XSS attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](attackModels/xssAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the application is web or hybrid, we have CSRF
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 and (questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/csrfAttack.md", "r").read())

            # CSRF attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/csrfAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the aplication is web or hybrid, we have Cookie Poisoning
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/cachePoisoning.md", "r").read())

        # CookiePoisoning attack tree diagram
        # Write de scheme in the report
        report.write("![alt text](attackModels/cachePoisoningAttackTree.png)")
        report.write("\n")
        report.write("\n")

    # If the application is web or hybrid, and storage personal, confidential or critical data, we have a Malicious QR Code Attacks
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/maliciousQRCode.md", "r").read())

            # Malicious QR Code attack diagram
            # Write de scheme in the report
            report.write("![alt text](attackModels/QRCodeAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # f the application is web or hybrid, we have CAPTCHA Breaking Attacks
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/captchaBreaking.md", "r").read())

    # CAPTCHA Breaking attack tree diagram
    # Write de scheme in the report
    # report.write("![alt text](design_schemes6.png)")
    # report.write("\n")
    # report.write("\n")

    # Database use and public cloud environment SQLi attacks
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and questions_and_answers["Q3"].find("1") != -1 :
        if questions_and_answers["Q5"].find("1") != -1 and questions_and_answers["Q6"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/SQLi.md", "r").read())

            # SQLi attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/sqliAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # DoS Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attackModels/flooding.md", "r").read())
            # DoS attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/floodingAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # Sniffing Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attackModels/sniffing.md", "r").read())

            # Sniffing attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/sniffingAttackTree.png)")
            report.write("\n")
            report.write("\n")

    
    # If the application is web or hybrid, we have Phishing Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("4") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/phishingAttack.md", "r").read())

            # Phishing Attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/phishingAttackTree.png)")
            report.write("\n")
            report.write("\n")

            # Botnet Attacks
            report.write(open("attackModels/Botnet.md", "r").read())

            # Botnet attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/botnetAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the application is web or hybrid, we have XML
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/XMLi.md", "r").read())

        # XML Attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](attackModels/xmliAttackTree.png)")
        report.write("\n")
        report.write("\n")

    # If the application is web or hybrid, we have Session Hijacking
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("2") != -1 and questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/sessionHijacking.md", "r").read())

                # Session Hijacking attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/sessionHijackingAttackTree.png)")
                report.write("\n")
                report.write("\n")


    # If the system was development for iOS, Tizen and embedded platforms (Buffer Overflow)
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q11"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/bufferOverflows.md", "r").read())

        # Buffer Overflows attack diagram
        # Write the scheme in the report
        report.write("![alt text](attackModels/bufferOverflowAttackTree.png)")
        report.write("\n")
        report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Mobile Apllication Spoofing )
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 :
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/spoofing.md", "r").read())

            # Spoofing attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/spoofingAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/vmMigration.md", "r").read())

            # Attack on VM at migration tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/VMMigrationAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Insiders Malicious Attacks)
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 :
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/maliciousInsider.md", "r").read())

                # Malicious Insiders attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/maliciousInsiderAttackTree.png)")
                report.write("\n")
                report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (VM Escape Attack)
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/VMEscape.md", "r").read())

            # VM Escape attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/vmEscapeAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Side-Channel Attack)
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/Side-Channel.md", "r").read())

            # Side-Channel attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/sideChannelAttackTree.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android and iOS (Malware-as-a-Service Attacks)
        if (questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1) or questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("5") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/malwareInjection.md", "r").read())

                # Malware-as-a-Service Attacks tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/malwareInjectionAttackTree.png)")
                report.write("\n")
                report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Tampering Attacks)
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/tamperingAttack.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/tamperingAttackTree.png)")
                report.write("\n")
                report.write("\n")
    
    # If the application or system uses authentication, database and stores sensitive data, it is subject to Bluejacking, Bluesnarfing and Bluesmack/DOS attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q20"].find("5") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/bluejacking_bluesnarfing.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/bluetoothAttackTree.png)")
                report.write("\n")
                report.write("\n")

    # If the application or system uses authentication, database, stores sensitive data and use GPS, it is subject to GPS Jamming attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q20"].find("7") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/gps_jamming.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/gps_jammingAttackTree.png)")
                report.write("\n")
                report.write("\n")
    # If the web or hybrid application or system uses authentication, database and stores sensitive data, it is subject to Code Injection attacks
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/code_injection.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/codeInjectionAttackTree.png)")
                report.write("\n")
                report.write("\n")

    # If the web or hybrid application or system uses authentication, database and stores sensitive data, it is subject to SSRF attacks
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/SSRF.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/SSRFAttackTree.png)")
                report.write("\n")
                report.write("\n")

    # If the web or hybrid application or system uses authentication, database and stores sensitive data, it is subject to Command Injection attacks
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/command_injection.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/commandInjectionAttackTree.png)")
                report.write("\n")
                report.write("\n")
    
    # If the application or system uses authentication, database, stores sensitive data and use GPS, it is subject to GPS Jamming attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q20"].find("1") != -1 or questions_and_answers["Q20"].find("2") != -1 or questions_and_answers["Q20"].find("3") != -1 or questions_and_answers["Q20"].find("4") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/cellular_jamming.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/cellularJammingAttackTree.png)")
                report.write("\n")
                report.write("\n")

    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/cryptanalysis.md", "r").read())

            # Tampering Detection attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/cryptanalysisAttackTree.png)")
            report.write("\n")
            report.write("\n")

    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/reverse_enginnering.md", "r").read())

            # Tampering Detection attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/reverseEngineeringAttackTree.png)")
            report.write("\n")
            report.write("\n")


    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q14"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/audit_log_manipulation.md", "r").read())

            # Tampering Detection attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](attackModels/auditLogManipulationAttackTree.png)")
            report.write("\n")
            report.write("\n")

    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q20"].find("6") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/Wi-Fi_jamming.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/Wi-Fi_JammingAttackTree.png)")
                report.write("\n")
                report.write("\n")

                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/Wi-Fi_SSID_Tracking.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/Wi-Fi_TrackingAttackTree.png)")
                report.write("\n")
                report.write("\n")

                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/byzantine.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](attackModels/byzantineAttackTree.png)")
                report.write("\n")
                report.write("\n")


                

    report.close()
    attack_models_convert_report()
    print("# Processing done! Check your attack models in the ATTACKS_MAPPING.pdf file")

"""
[Summary]: Method responsible for processing information about STSAT module
[Arguments]: No arguments
[Return]: No return
"""
def get_security_test_recommendation():
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


    # Security Testing against DoS Jamming, Wi-Fi Jamming, Orbital Jamming, GPS Jamming, Flooding Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q17"].find("1") != -1 or questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("4") != -1:
            report.write(open("securityTesting/AttackGroupDoSToFlooding.md", "r").read())

            report.write("\n")
            report.write("\n")

    # Security Testing against Malicious Insider, Sniffing, MiTM, Eavesdropping attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupMIToEavesdropping.md", "r").read())
    # Security Testing against Malicious Insider, Sniffing, MiTM, Eavesdropping attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q17"].find("4") != -1 or questions_and_answers["Q17"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupMiTMToBruteForce.md", "r").read())


    # Security Testing against SQLi, XSS, CSRF, SSRF, Command Injection and Code Injection attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupSQLiToCodeInjection.md", "r").read())

    # Security Testing against XSS, SQLi, CSRF, Session Fixation, Session Hijacking, Access Point Hijacking, Command Injection,
    # Code Injection, Botnet, Malware as a Service, Spoofing, Pharming, Phishing, GPS Spoofing, Rogue Access Point,
    # Cellular Rogue Base Station and SSRF Attacks Attacks
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 and questions_and_answers["Q8"].find("2") != -1 and questions_and_answers["Q8"].find("3") != -1:
                if questions_and_answers["Q17"].find("2") != -1 or questions_and_answers["Q17"].find("4") != -1:
                    report.write("\n")
                    report.write("\n")
                    report.write(open("securityTesting/AttackGroupXSSToSSRF.md", "r").read())

    # Security Testing against Botnet, Spoofing and Sniffing attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q20"].find("1") != -1 or questions_and_answers["Q20"].find("2") != -1 or questions_and_answers["Q20"].find("4") != -1 or questions_and_answers[
            "Q20"].find("5") != -1 or questions_and_answers["Q20"].find("6") != -1 or questions_and_answers["Q20"].find("8") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupMaaSToNFC.md", "r").read())

    # Security Testing against Buffer Overflow attacks
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q10"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupBufferOverflow.md", "r").read())

    # Security Testing against Bypassing Physical Security, Physical Theft and VM Migration attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupBPSToVM.md", "r").read())

    # Security Testing against Malware Injection and Side-channel attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupMaaSToBluejacking.md", "r").read())

    # Security Testing against Spoofing, Eavesdropping, Sniffing, Botnets, MiTM, Flooding and Reverse Enginnering attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/AttackGroupSpoofingToREA.md", "r").read())

    # Security Testing against Malware.as-a-Service, Eavesdropping and Botnets attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("securityTesting/AttackGroupMaaSToBotnet.md", "r").read())
    
    # Security Testing against Phishing, Botnet and Malware-as-a-Service attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("securityTesting/AttackGroupPhishingToMaaS.md", "r").read())
    
    # Security Testing against Spoofing, Eavesdropping, Botnet and Flooding attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("securityTesting/AttackGroupSpoofingToFlooding.md", "r").read())
            
    # Security Testing against SQLi, Command Injection, Session Hijacking, Botnet, 
    # Access Point Hijacking, Brute Force, Phishing, Spoofing, 
    # MiTM, Buffer Overflow, Sniffing, CSRF, VM Migration attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("securityTesting/AttackGrupSQLiToVM.md", "r").read())
    
    
    
    report.close()
    security_test_recommendation_convert_report()
    print("# Processing done! Check your security test specification and automation tools in the TEST_SPECIFICATION.pdf file")

"""
[Summary]: Method responsible for processing information about SME module
[Arguments]: No arguments
[Return]: No return
"""
def get_mechanisms():
    print("")
    print("  Processing information.....")
    print("")

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

    # Backup mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/backupMechanism.md", "r").read())

    # Audit and cryptographic algorithms mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/auditMechanisms.md", "r").read())

        report.write(open("mechanisms/cryptographicAlgorithmsMechanisms.md", "r").read())

    # Authentication mechanisms
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("1") != -1:
        report.write(open("mechanisms/biometricAuthenticationMechanism.md", "r").read())
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("2") != -1:
        report.write(open("mechanisms/channelBasedAuthenticationMechanism.md", "r").read())
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("3") != -1:
        report.write(open("mechanisms/factorsBasedAuthenticationMechanism.md", "r").read())
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("4") != -1:
        report.write(open("mechanisms/IDBasedAuthenticationMechanism.md", "r").read())

    # Cryptographic protocolos mechanisms    
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/cryptographicProtocolsMechanism.md", "r").read())

    # Access control mechanisms
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/accessControlMechanisms.md", "r").read())

    # Inspection and registration mechanisms
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/inspectionMechanism.md", "r").read())
            report.write(open("mechanisms/registrationMechanism.md", "r").read())

    # physical security requirements
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q21"].find(
            "1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/deviceDetectionMechanism.md", "r").read())
        report.write(open("mechanisms/physicalLocationMechanism.md", "r").read())

    # Confinement mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q13"].find("1") != -1 or questions_and_answers["Q15"].find("1") != -1 or questions_and_answers["Q16"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("mechanisms/confinementMechanism.md", "r").read())

    # Filtering mechanisms
    if questions_and_answers["Q13"].find("1") != -1 and questions_and_answers["Q15"].find("1") != -1 and questions_and_answers["Q16"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("mechanisms/filteringMecanism.md", "r").read())

    report.close()
    mechanisms_convert_report()
    print("# Processing done! Check your security mechanisms in the SECURITY_MECHANISMS.pdf file")

"""
[Summary]: Method responsible for creating, printing and outputting the complete processing report
[Arguments]: No arguments
[Return]: No return
"""
def fullReport():

    get_requirements()
    get_security_best_practices()
    get_mechanisms()
    get_attack_models()
    get_security_test_recommendation()

    pdfs = ['SECURITY_REQUIREMENTS.pdf', 'GOOD_PRACTICES.pdf', 'SECURITY_MECHANISMS.pdf', 'ATTACKS_MAPPING.pdf', 'TEST_SPECIFICATION.pdf']

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("FULL_REPORT.pdf")
    merger.close()
    print("\n\n *** Processing  done! See the full report requested in the FULL_REPORT.pdf file! ***\n\n")


if __name__ == "__main__":
    print("---")
    print("")
    print("#  Welcome to ")
    print("")
    print("#  SecD4CLOUDMOBILE ")
    print("")
    print("  The **SecD4CLOUDMOBILE** is a custom made program")
    print("  This program implements a questionnaire about the development")
    print("  of mobile cloud-based application and generate a report with secure development guides.")
    print("  It is part of the outputs of the doctoral thesis project entitled Systematization of the ")
    print("  Security Engineering Process in the Cloud and Mobile Ecosystem ")
    print("")
    print("## License")
    print("")
    print("  Developed by Francisco T. Chimuco and Pedro R. M. Inácio")
    print("  Department of Computer Science")
    print("  Universidade da Beira Interior")
    print("")
    print("  Copyright 2021 Francisco T. Chimuco and Pedro R. M. Inácio")
    print("")
    print("  SPDX-License-Identifier: Apache-2.0")
    print("")
    information_capture()

    print("")
    print("#############################################################")

    print("")
    print("")
    print("")

    exit(0)

# license Apache-2.0
