#!/usr/bin/python coding=utf-8
# !/bin/bash

"""
// ---------------------------------------------------------------------------
//
//	Security by Design for Cloud, Mobile and IoT Ecosystem (SecD4CLOUDMOBILE)
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
from sys import exit
import webbrowser
from markdown import markdown
from xhtml2pdf import pisa
from switch import Switch
from PyPDF2 import PdfMerger

################################# GLOBAL VARIABLES #################################

version = 1

# list that contains to answers in the written file
input_list = []

# add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
answers_list = []
comments_list = []
table_for_report = []

# create a dictionary to store the answers to the questions
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
    "Q21": "",
    "Q22": ""
}

# Questions
# Q1   -> Mobile Platform
# Q2   -> Application Domain Type
# Q3   -> Authentication 
# Q4   -> Authentication Schemes
# Q5   -> Has a DB
# Q6   -> Type of data storage
# Q7   -> DBMS name
# Q8   -> Type of data
# Q9   -> Local of data storage
# Q10  -> User Registration
# Q11  -> Way of user registration
# Q12  -> Programming Languages
# Q13  -> Input Forms
# Q14  -> Upload Files
# Q15  -> Logs
# Q16  -> System Regular Updates
# Q17  -> Third-party Software
# Q18  -> System Cloud Environment
# Q19  -> Hardware Specifications
# Q20  -> Hardware Auth
# Q21  -> Hardware Communications
# Q22  -> Data Center Physical Access


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
    "9": "Ubuntu Touch Application"
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
    "17": "Smart Wearables",
    "18": "Smart City",
    "19": "Smart Cars"
}

question3 = {
    "1": "Yes",
    "2": "No"
}

question4 = {
    "1": "Biometric-based authentication",
    "2": "Channel-based authentication",
    "3": "Factors-based authentication",
    "4": "ID-based authentication"
}

question5 = {
    "1": "Yes",
    "2": "No"
}

question6 = {
    "1": "SQL (Relational Database)",
    "2": "NoSQL"
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
    "13": "Redis"
}

question8 = {
    "1": "Personal Information",
    "2": "Confidential Data",
    "3": "Critical Data"
}

question9 = {
    "1": "Local Storage (Centralized Database)",
    "2": "Remote Storage (Cloud Database)",
    "3": "Both"
}

question10 = {
    "1": "Yes",
    "2": "No"
}

question11 = {
    "1": "The users will register themselves",
    "2": "Will be an administrator that will register the users"
}

question12 = {
    "1": "C#",
    "2": "C/C++/Objective-C",
    "3": "HTML5 + CSS + JavaScript",
    "4": "Java",
    "5": "Javascript",
    "6": "PHP",
    "7": "Python",
    "8": "Ruby",
    "9": "Kotlin",
    "10": "Swift",
    "11": "Dart"
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
    "1": "Yes",
    "2": "No"
}

question18 = {
    "1": "Community Cloud",
    "2": "Hybrid Cloud",
    "3": "Private Cloud",
    "4": "Public Cloud",
    "5": "Virtual Private Cloud"
}

question19 = {
    "1": "Yes",
    "2": "No"
}

question20 = {
    "1": "No Authentication",
    "2": "Symmetric Key",
    "3": "Basic Authentication (user/pass)",
    "4": "Certificates (X.509) ",
    "5": "TPM (Trusted Platform Module)"
}

question21 = {
    "1": "3G",
    "2": "4G/LTE",
    "3": "5G",
    "4": "GSM (2G)",
    "5": "Bluetooth ",
    "6": "Wi-Fi ",
    "7": "GPS ",
    "8": "RFID ",
    "9": "NFC",
    "10": "ZigBee",
    "11": "LoRa",
    "12": "NB-IoT"
}

question22 = {
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
    print("--->")
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
    print("")

    # function input() interprets the input
    # get user input differs from python 2.x and 3.x --> input() = version 3 | raw_input() = version 2.x
    
    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 9, according to the menu above!")
            continue
        
        if value>10 or value<0:
            print("Wrong! Enter a whole number between 1 and 9, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            if value == 0:
                return
            # if value == 10:
            #     print("  Please specify the mobile platform: (name between single quotes)  ")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q1"] = questions_and_answers["Q1"] + str(value2) + ";"
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
    print(" 18 - Smart City ")
    print(" 19 - Smart Cars")
    print("")
    
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 19, according to the menu above!")
            continue
        
        if value>19 or value<=0:
            print("Wrong! Enter a whole number between 1 and 19, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            # if value == 0:
            #     return
            # else:
            questions_and_answers["Q2"] = str(value)
            return

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
    
    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            # if value == 0:
            #     return
            # else:
            questions_and_answers["Q3"] = str(value)
            
            if value == 1:
                typeOfAuthentication(version)
            else:
                questions_and_answers["Q4"]="N/A"
            return

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
    print("")
    
    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 4, according to the menu above!")
            continue
        
        if value>4 or value<0:
            print("Wrong! Enter a whole number between 1 and 4, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            if value == 0:
                return
            # if value == 5:
            #     print("  Please specify authentication scheme: (name between single quotes)  ")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q4"] = questions_and_answers["Q4"] + str(value2) + ";"
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

    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            # if value == 0:
            #     return
            # else:
            questions_and_answers["Q5"] = str(value)
            
            if value == 1:
                typeOfDatabase(version)
                if questions_and_answers["Q6"] == '1' or questions_and_answers["Q6"] == '2':
                    whichDatabase(version)
                sensitiveData(version)
                storageLocation(version)
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
        print("  **What will be the type of data storage ?**  ")
    else:
        print("  **What is type of data storage?**  ")
    print("")
    print("  1 - SQL DBMS (Relational Database) ")
    print("  2 - NoSQL DBMS ")
    print("")
    
    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            # if value == 0:
            #     return
            # else:
            questions_and_answers["Q6"] = str(value)
            return    

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
        print("")
        
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 14, according to the menu above!")
            continue
        
        if value>13 or value<1:
            print("Wrong! Enter a whole number between 1 and 14, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            # if value == 14:
            #     print(" Please specify the DBMS name: (name between single quotes)  ")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q7"] = str(value2)
            # else:
            #     questions_and_answers["Q7"] = str(value)
                
            # return
            questions_and_answers["Q7"] = str(value)
                
            return

"""
[Summary]: Method allowing the identification of the type of data handled by the system (personal, confidential or critical)
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def sensitiveData(version):
    print("")
    print("---")
    print("")
    if version == 1:
        print("  **What type of information will the application handle?**  ")
    else:
        print("  **What is the type of information handled by the application?**  ")

    print("  (This is a multiple choice question. Enter several options and end with 0.)  ")
    print("")
    print("  1 - Personal Information (Names, Address,...)  ")
    print("  2 - Confidential Data  ")
    print("  3 - Critical Data  ")
    print("")
    
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        
        if value>3 or value<0:
            print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            if value == 0:
                return
            # if value == 4:
            #     print("  Please specify the type of information handled: (name between single quotes)  ")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q8"] = questions_and_answers["Q8"] + str(value2) + ";"
            else:
                questions_and_answers["Q8"] = questions_and_answers["Q8"] + str(value) + ";"

"""
[Summary]: Method allowing the identification of whether or not the application allows users to register
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
def storageLocation(version):
    print("")
    print("---")
    print("")
    
    if version == 1:
        print("  **Where will the system store the data?**  ")
    else:
        print("  **What is the storage location of the system?**  ")
        
    print("")
    print("  1 - Local Storage (Centralized database) ")
    print("  2 - Remote Storage (Cloud Database) ")
    print("  3 - Both (Hybrid Database) ")
    print("")

    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 3, according to the menu above!")
            continue
        
        if value>3 or value<1:
            print("Wrong! Enter a whole number between 1 and 3, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            questions_and_answers["Q9"] = str(value)  
            return    

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

    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            questions_and_answers["Q10"] = str(value)
            if value == 1:
                typeOfUserRegist(version)
            else:
                questions_and_answers["Q11"] = "N/A"
 
            return    

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
    
    value = 0
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            questions_and_answers["Q11"] = str(value)
            return

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
    print("  2 - Obective-C/C/C++ ")
    print("  3 - HTML5 + CSS + JavaScript ")
    print("  4 - Java  ")
    print("  5 - Javascript ")
    print("  6 - PHP  ")
    print("  7 - Python  ")
    print("  8 - Ruby  ")
    print("  9 - Kotlin ")
    print(" 10 - Swift ")
    print(" 11 - Dart ")
    print("")

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 12, according to the menu above!")
            continue
        
        if value>11 or value<0:
            print("Wrong! Enter a whole number between 1 and 12, according to the menu above!")
            continue
        else:
            # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
            if value == 0:
                return
            # if value == 11:
            #     print("  Please specify the programming language: (name between single quotes)  ")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q12"] = questions_and_answers["Q12"] + str(value2) + ";"
            else:
                questions_and_answers["Q12"] = questions_and_answers["Q12"] + str(value) + ";"
                

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
    
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q13"] = str(value)
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q14"] = str(value)
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q15"] = str(value)
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q16"] = str(value)
            return

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
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q17"] = str(value)
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        
        if value>5 or value<1:
            print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        else:
            questions_and_answers["Q18"] = str(value)
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q19"] = str(value)

            if value == 1:
                hardwareAuth(version)
                hardwareComunication(version)
            else:
                questions_and_answers["Q20"] = "N/A"
                questions_and_answers["Q21"] = "N/A"
            return

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        
        if value>5 or value<1:
            print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
            continue
        else:
            questions_and_answers["Q20"] = str(value)
            return

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
    print("  10 - ZigBee ")
    print(" 11 - LoRa")
    print(" 12 - NB-IoT")
    print("")
    
    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 12, according to the menu above!")
            continue
        
        if value>12 or value<0:
            print("Wrong! Enter a whole number between 1 and 12, according to the menu above!")
            continue
        else:
            if value == 0:
                return
            # if value == 12:
            #     print("Please specify the wireless technologies: (name between single quotes)")
            #     value2 = validateInput(2)
            #     questions_and_answers["Q21"] = questions_and_answers["Q21"] + str(value2) + ";"
            else:
                questions_and_answers["Q21"] = questions_and_answers["Q21"] + str(value) + ";"

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

    value = -1
    while True:
        try:
            print("")
            value = int(input("-->"))
        except ValueError:
            print("Error! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        
        if value>2 or value<1:
            print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
            continue
        else:
            questions_and_answers["Q22"] = str(value)
            return

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
        print("{:22} {:3} {:40} ".format("Type of database", ":", item))

        table_for_report.append(["Type of database", item])

        answers_list.append(questions_and_answers["Q6"])
        comments_list.append(item)

    else:
        for n in question6:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of database", ":", question6[n]))

                table_for_report.append(["Type of database", question6[n]])

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

    print("{:22} {:3} {:40} ".format("Type of information handled", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Type of information handled", ' ; '.join(list_aux)])

    answers_list.append(questions_and_answers["Q8"])
    comments_list.append(' ; '.join(list_aux))

    item = questions_and_answers["Q9"]
    # case this question is not answered, and the answer it will be "N/A"
    if questions_and_answers["Q9"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Storage Location", ":", item))

        table_for_report.append(["Storage Location", item])

        answers_list.append(questions_and_answers["Q9"])
        comments_list.append(item)

    else:
        for n in question9:
            if item == n:
                print("{:22} {:3} {:40} ".format("Storage Location", ":", question9[n]))

                table_for_report.append(["Storage Location", question9[n]])

                answers_list.append(questions_and_answers["Q9"])
                comments_list.append(question9[n])

    for n in question10:
        item = questions_and_answers["Q10"]
        if item == n:
            print("{:22} {:3} {:40}".format("User Registration", ":", question10[n]))

            table_for_report.append(["User Registration", question10[n]])

            answers_list.append(questions_and_answers["Q10"])
            comments_list.append(question10[n])

    item = questions_and_answers["Q11"]
    if questions_and_answers["Q11"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of Registration", ": ", item))

        table_for_report.append(["Type of Registration", item])

        answers_list.append(questions_and_answers["Q11"])
        comments_list.append(item)
    else:
        for n in question11:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of Registration", ": ", question11[n]))

                table_for_report.append(["Type of Registration", question11[n]])

                answers_list.append(questions_and_answers["Q11"])
                comments_list.append(question11[n])

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q12"][0].isdigit() == False and questions_and_answers["Q12"].find(";") == -1:
        list_aux.append(questions_and_answers["Q12"])
    else:

        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q12"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question12:
                if item == option:
                    list_aux.append(question12[option])

            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Programming Languages", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Programming Languages", ' ; '.join(list_aux)])

    answers_list.append(questions_and_answers["Q12"])
    comments_list.append(' ; '.join(list_aux))

    for n in question13:
        item = questions_and_answers["Q13"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Input Forms", ":", question13[n]))

            table_for_report.append(["Input Forms", question13[n]])

            answers_list.append(questions_and_answers["Q13"])
            comments_list.append(question13[n])

    for n in question14:
        item = questions_and_answers["Q14"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Upload Files", ":", question14[n]))

            table_for_report.append(["Upload Files", question14[n]])

            answers_list.append(questions_and_answers["Q14"])
            comments_list.append(question14[n])

    for n in question15:
        item = questions_and_answers["Q15"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has logs", ":", question15[n]))

            table_for_report.append(["The system has logs", question15[n]])

            answers_list.append(questions_and_answers["Q15"])
            comments_list.append(question15[n])

    for n in question16:
        item = questions_and_answers["Q16"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has regular updates", ":", question16[n]))

            table_for_report.append(["The system has regular updates", question16[n]])

            answers_list.append(questions_and_answers["Q16"])
            comments_list.append(question16[n])

    for n in question17:
        item = questions_and_answers["Q17"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has third-party", ":", question17[n]))

            table_for_report.append(["The system has third-party", question17[n]])

            answers_list.append(questions_and_answers["Q17"])
            comments_list.append(question17[n])

    for n in question18:
        item = questions_and_answers["Q18"]
        if item == n:
            print("{:22} {:3} {:40}".format("System Cloud Environments", ":", question18[n]))

            table_for_report.append(["System Cloud Environments", question18[n]])

            answers_list.append(questions_and_answers["Q18"])
            comments_list.append(question18[n])

    for n in question19:
        item = questions_and_answers["Q19"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Hardware Specification", ":", question19[n]))

            table_for_report.append(["Hardware Specification", question19[n]])

            answers_list.append(questions_and_answers["Q19"])
            comments_list.append(question19[n])

    for n in question20:
        item = questions_and_answers["Q20"]
        if item == n:
            print("{:22} {:3} {:40} ".format("HW Authentication", ":", question20[n]))

            table_for_report.append(["HW Authentication", question20[n]])

            answers_list.append(questions_and_answers["Q20"])
            comments_list.append(question20[n])

    list_aux = []
    # it is a multiple question

    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q21"][0].isdigit() == False and questions_and_answers["Q21"].find(";") == -1:
        list_aux.append(questions_and_answers["Q21"])
    else:
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q21"].split(";")

        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question21:
                if item == option:
                    list_aux.append(question21[option])
            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("HW Wireless Tech", ":", ' ; '.join(list_aux)))

    table_for_report.append(["HW Wireless Tech", ' ; '.join(list_aux)])

    answers_list.append(questions_and_answers["Q21"])
    comments_list.append(' ; '.join(list_aux))

    for n in question22:
        item = questions_and_answers["Q22"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Device or Data Center Physical Access", ":", question22[n]))

            table_for_report.append(["Device or Data Center Physical Access", question22[n]])

            answers_list.append(questions_and_answers["Q22"])
            comments_list.append(question22[n])

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
def switch1():
    val = 0
    while True:
        try:
            val = int(input("\nWhat is your option?\n --> "))
            #print("-->")
        except ValueError:
            print("Error! Enter a whole number between 1 and 8, according to the menu above!")
            continue
        
        if val>8 or val<1:
            print("Wrong! Enter a whole number between 1 and 8, according to the menu above!")
            continue
        else:
            with Switch(val) as case:
                if case(1):
                    print("---")
                    print("")
                    print("  Answer the questions one by one!  ")
                    print("")
                    print("  1 - Answer the questions one by one.  ")
                    print("  2 - Use a text file with the answers already written.  ")
                    print("  3 - Return to the main menu")
                    print("")

                    value = 0
                    while True:
                        try:
                            print("")
                            value = int(input("-->"))
                        except ValueError:
                            print("Error! Enter a whole number between 1 and 3, according to the menu above!")
                            continue

                        if value > 3 or value < 0:
                            print("Wrong! Enter a whole number between 1 and 3, according to the menu above!")
                            continue
                        else:
                    
                            # answer the questions by hand
                            if value == 1:
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

                                print("**The questionnaire is over!**\n\n")
                                print_data()
                                information_capture()

                            # answers already written in the input file
                            elif value == 2:
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
                                questions_and_answers["Q22"] = input_list[21]

                                information_capture()

                                print("# Processing Done! Choose another option to process the requests!")
                            else:
                                information_capture()

                if case(2):
                    print("\n********************************************************************************************\n")
                    print("\t\t The request for security requirements is in progress ... \n\n")
                    get_requirements()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/SECURITY_REQUIREMENTS.pdf')
                    information_capture()
                    
                if case(3):
                    print("\n********************************************************************************************\n")
                    print("\t\t The request for best practice guidelines is in progress ... \n\n")
                    get_security_best_practices()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/GOOD_PRACTICES.pdf')
                    information_capture()
                    
                if case(4):
                    print("\n********************************************************************************************\n")
                    print("\t\t The request for security mechanisms is in progress ... \n\n")
                    get_mechanisms()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/SECURITY_MECHANISMS.pdf')
                    information_capture()
                    
                if case(5):
                    print("\n********************************************************************************************\n")
                    print("\t\t The request for attack models is in progress ... \n\n")
                    get_attack_models()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/ATTACKS_MAPPING.pdf')
                    information_capture()
                    
                if case(6):
                    print("\n********************************************************************************************\n")
                    print("\t\t The request for the security testing specification and tools is in progress ... \n\n")
                    get_security_test_recommendation()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/TEST_SPECIFICATION.pdf')
                    information_capture()
                    
                if case(7):
                    print("\n********************************************************************************************\n")
                    print("\t\t The full report request is in progress ... \n\n")
                    fullReport()
                    #webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/FULL_REPORT.pdf')
                    information_capture()
                    
                if case(8):
                    print("\n\n*** Application finished successfully! ***\n\n")
                    exit(0)
                    
                if case.default:
                    print("\nError! Insert a valid value between 1 and 8!\n")

        break

"""
[Summary]: Method responsible for creating the main menu and capturing the user data
[Arguments]: No argument
[Return]: No return
"""
def information_capture():
    print("************************************************************************************************")
    print("\nWelcome to SecD4CLOUDMOBILE Framework!\n")
    print("\nWhat would you like to do? (1-8)\n")
    print("\n1. Answer the Questions Required for Processing")
    print("\n2. Security Requirement Elicitation Request")
    print("\n3. Secure Development Best Practices Request")
    print("\n4. Secure Development Mechanisms Request")
    print("\n5. Attack Model Mapping Request")
    print("\n6. Security Test Specification and Tool Request")
    print("\n7. Full Report Request")
    print("\n8. Exit")
    switch1()

"""
[Summary]: Method responsible for processing information about CSRE
[Arguments]: No arguments
[Return]: No return
"""
def get_requirements():
    print("")
    print("  Processing information.....")
    print("")

   # print_data()

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

    # confidentiality requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/confidentiality.md", "r").read())

    # integrity requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/integrity.md", "r").read())

    # availability requirement
    report.write("\n")
    report.write("\n")

    report.write(open("security_requirements/availability.md", "r").read())

    # authentication requirement
    if questions_and_answers["Q3"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/authentication.md", "r").read())

    # authorization requirement
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_requirements/authorization.md", "r").read())

    # nonRepudiaton and accountability requirements
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_requirements/nonRepudiation.md", "r").read())
            report.write("\n")
            report.write(open("security_requirements/accountability.md", "r").read())

    # reliability requirement
    report.write("\n")
    report.write("\n")
    report.write(open("security_requirements/reliability.md", "r").read())

    # # privacy security_requirements
    # if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
    #     report.write("\n")
    #     report.write("\n")
    #     report.write(open("security_requirements/privacy.md", "r").read())

    # physical security requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q22"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/physicalSecurity.md", "r").read())

    # forgery resistance requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q22"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/forgeryResistance.md", "r").read())

    # tampering detection requirement
    if questions_and_answers["Q22"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/tamperDetection.md", "r").read())

    # data freshness requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/dataFreshness.md", "r").read())

    # confinement requirement
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q14"].find("1") != -1 or questions_and_answers["Q16"].find("1") != -1 or questions_and_answers["Q17"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_requirements/confinement.md", "r").read())

    # Interoperability requirement
    if questions_and_answers["Q14"].find("1") != -1 and questions_and_answers["Q16"].find("1") != -1 and questions_and_answers["Q17"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_requirements/interoperability.md", "r").read())

    # data origin authentication
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q5"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_requirements/dataOriginAuthentication.md", "r").read())

    report.close()
    requirements_convert_report()
    print("\n\n # Processing done! Check your requirements in the SECURITY_REQUIREMENTS.pdf file")

"""
[Summary]: Method responsible for processing information about CSBPG module
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

    # Injection security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if (questions_and_answers["Q13"].find("1") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Injection_Prevention_Cheat_Sheet.md", "r").read())

    # SQL Injection Prevention security best practices guidelines
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4"):
        if questions_and_answers["Q5"].find("1") != -1 and questions_and_answers["Q6"].find("1"):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/SQL_Injection_Prevention_Cheat_Sheet.md", "r").read())
    
    # Authentication security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Authentication_Cheat_Sheet.md", "r").read())
        
        # Multifactor authentication security best practices guidelines 
        if (questions_and_answers["Q4"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Multifactor_Authentication_Cheat_Sheet.md", "r").read())

    
    # Authorization security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Authorization_Cheat_Sheet.md", "r").read())
        
        # Transaction Authorization security best practices guidelines
        if (questions_and_answers["Q2"].find("3") != -1 or questions_and_answers["Q2"].find("6") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Transaction_Authorization_Cheat_Sheet.md", "r").read())
    
    # Cross-Site-Scripting security best practices guidelines
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1):
        if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
            if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Cross_Site_Scripting_Prevention_Cheat_Sheet.md", "r").read())
    
    # Cross Site Request Forgery security best practices guidelines
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1):
        if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
            if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md", "r").read())
    
    # Cryptographic Storage security best practices guidelines
    if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Cryptographic_Storage_Cheat_Sheet.md", "r").read())
    
    # Database security best practices guidelines    
    if (questions_and_answers["Q5"].find("1") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Database_Security_Cheat_Sheet.md", "r").read())
          
    # Denial of Service security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Denial_of_Service_Cheat_Sheet.md", "r").read())
        
    # File uploading security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if (questions_and_answers["Q14"].find("1") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/File_Upload_Cheat_Sheet.md", "r").read())

    # HTML5 security best practices guidelines
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1):
        if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
            if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
                if (questions_and_answers["Q12"].find("3") != -1):
                    report.write("\n\n")

                    report.write(open("security_best_practices_guidelines/HTML5_Security_Cheat_Sheet.md", "r").read())
    
    # Securing CSS security best practices guidelines
    if (questions_and_answers["Q12"].find("3") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Securing_Cascading_Style_Sheets_Cheat_Sheet.md", "r").read())
    
    # Injection prevention in Java security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if (questions_and_answers["Q12"].find("4") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Injection_Prevention_in_Java_Cheat_Sheet.md", "r").read())
    
    # Secure Logging security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if (questions_and_answers["Q15"].find("1") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Logging_Cheat_Sheet.md", "r").read())
    
    # Logging Vocabulary security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if (questions_and_answers["Q15"].find("1") != -1):
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Logging_Vocabulary_Cheat_Sheet.md", "r").read())
    
    # Nodejs security best practices guidelines 
    if (questions_and_answers["Q12"].find("5") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Nodejs_Security_Cheat_Sheet.md", "r").read())
    
    # NPM security best practices guidelines 
    if (questions_and_answers["Q12"].find("5") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/NPM_Security_Cheat_Sheet.md", "r").read())
    
    # Third Party Javascript security best practices guidelines 
    if (questions_and_answers["Q12"].find("5") != -1):
        if (questions_and_answers["Q17"].find("1") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Third_Party_Javascript_Management_Cheat_Sheet.md", "r").read())
            
    # Password Storage security best practices guidelines
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Password_Storage_Cheat_Sheet.md", "r").read())
    
    # PHP Configuration security best practices guidelines 
    if (questions_and_answers["Q12"].find("6") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/PHP_Configuration_Cheat_Sheet.md", "r").read())  
    
    # Ruby on Rails security best practices guidelines 
    if (questions_and_answers["Q12"].find("6") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Ruby_on_Rails_Cheat_Sheet.md", "r").read()) 
    
    # Server Side Request Forgery Prevention security best practices guidelines 
    if (questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1):
        if (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md", "r").read())
    
    # Session Management security best practices guidelines
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/Session_Management_Cheat_Sheet.md", "r").read())
    
    # Transport Layer Protection security best practices guidelines
    if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Transport_Layer_Protection_Cheat_Sheet.md", "r").read())
     
    # Input Validation security best practices guidelines
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            if questions_and_answers["Q13"].find("1") != -1:
                report.write("\n\n")

                report.write(open("security_best_practices_guidelines/Input_Validation_Cheat_Sheet.md", "r").read())
    
    # User Privacy Protection security best practices guidelines
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("security_best_practices_guidelines/User_Privacy_Protection_Cheat_Sheet.md", "r").read())
         
    # Cryptography security best practices guidelines
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/Cryptography_guide.md", "r").read())

    # Secure Sofware Update security best practices guidelines
    if questions_and_answers["Q16"].find("1") != -1:
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/App_Update_guide.md", "r").read())

    # Third-Party Application security best practices guidelines 
    if questions_and_answers["Q17"].find("1") != -1:
        report.write("\n\n")

        report.write(open("security_best_practices_guidelines/App_Third_Party_guide.md", "r").read())

    report.close()
    security_best_practices_convert_report()
    print("\n\n # Processing done! Check your security best practices guidelines in the GOOD_PRACTICES.pdf file")

"""
[Summary]: Method responsible for processing information about CMAME module
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

    # report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
    # report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

    '''
    for i in range( 0,len(table_for_report) ):
        report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
    '''
    for i in range(0, len(table_for_report)):
        report.write(
            "{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")

    # MitM attack model
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/mitm_attack_model.md", "r").read())

            # Write de scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/MiTM_Attack_Tree.JPG)")
            report.write("\n\n")

    # Brute Force attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q13"].find("1") != -1:
                report.write(open("attack_models/brute_force_Attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Brute_Force_Attack_Tree.JPG)")
                report.write("\n\n")

    # Eavesdropping attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attack_models/eavesdropping_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Eavesdropping_Attack_Tree.JPG)")
            report.write("\n\n")

    # XSS attack model
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 and (
            questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/xss_attack_model.md", "r").read())

            # Write de scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/XSS_Attack_Tree.JPG)")
            report.write("\n\n")

    # CSRF attack model
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 and (
            questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/csrf_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/CSRF_Attack_Tree.JPG)")
            report.write("\n\n")

    # Cookie Poisoning attack model
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (
            questions_and_answers["Q18"].find("2") != -1 or questions_and_answers["Q18"].find("4") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("attack_models/cookie_poisoning_attack_model.md", "r").read())

        # Write de scheme in the report
        report.write("\n\n")
        report.write("![alt text](attack_models/Cookie_Poisoning_Attack_Tree.JPG)")
        report.write("\n\n")

    # Cache Poisoning attack model
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (
            questions_and_answers["Q18"].find("2") != -1 or questions_and_answers["Q18"].find("4") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("attack_models/cache_poisoning_attack_model.md", "r").read())

        # Write de scheme in the report
        report.write("\n\n")
        report.write("![alt text](attack_models/Cache_Poisoning_Attack_Tree.JPG)")
        report.write("\n\n")

    # Malicious QR Code attack model
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and \
            questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/malicious_qr_code_attack_model.md", "r").read())

            # Write de scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Malicious_QR_Code_Attack_Tree.JPG)")
            report.write("\n\n")

    # SQLi attack model
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and \
            questions_and_answers["Q3"].find("1") != -1:
        if questions_and_answers["Q5"].find("1") != -1 and questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q7"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/sqli_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/SQL_Injection_Attack_Tree.JPG)")
            report.write("\n\n")

    # Flooding attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attack_models/flooding_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Flooding_Attack_Tree.JPG)")
            report.write("\n\n")

    # Sniffing attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write(open("attack_models/sniffing_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Sniffing_Attack_Tree.JPG)")
            report.write("\n\n")

    # Phishing attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/phishing_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Phishing_Attack_Tree.JPG)")
            report.write("\n\n")

    # Pharming attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/pharming_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Pharming_Attack_Tree.JPG)")
            report.write("\n\n")

    # Botnet attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q18"].find("2") != -1 or questions_and_answers["Q18"].find("4") != -1):
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/botnet_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Botnet_Attack_Tree.JPG)")
            report.write("\n\n")

    # Session Hijacking attack model
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("2") != -1 and questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/session_hijacking_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Session_Hijacking_Attack_Tree.JPG)")
                report.write("\n\n")

    # Buffer Overflow attack model
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or \
            questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q12"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/buffer_overflow_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Buffer_Overflow_Attack_Tree.JPG)")
            report.write("\n\n")

    # Spoofing attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/spoofing_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Spoofing_Attack_Tree.JPG)")
            report.write("\n\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/vm_migration_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/VM_Migration_Attack_Tree.JPG)")
            report.write("\n\n")

    # Malicious Insider attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/malicious_insider_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Malicious_Insider_Attack_Tree.JPG)")
                report.write("\n\n")

    # Bypassing Physical Security attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/bypassing_physical_security_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Bypassing_Physical_Security_Attack_Tree.JPG)")
                report.write("\n\n")

        # Physical Theft attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/physical_theft_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write(
                    "![alt text](attack_models/physical_theft_attack_tree.JPG)")
                report.write("\n\n")

    # VM Escape attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/VM-Escape-Attacks-Model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/VM_Escape_Attack_Tree.JPG)")
            report.write("\n\n")

    # Side-Channel attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/side_channel_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Side_Channel_Attack_Tree.JPG)")
            report.write("\n\n")

        # Malware-as-a-Service attack model
        if (questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1) or \
                questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("5") != -1 or \
                questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/malware_injection_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/MaaS_Attack_Tree.JPG)")
                report.write("\n\n")

    # Tampering attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/tampering_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Tampering_Attack_Tree.JPG)")
                report.write("\n\n")

    # Bluejacking and Bluesnarfing attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("5") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/bluejacking_attack_model.md", "r").read())

                report.write("\n\n")
                report.write(open("attack_models/bluesnarfing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Bluetooth_Attack_Tree.JPG)")
                report.write("\n\n")

    # GPS Jamming attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("7") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/gps_jamming_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/GPS_Jamming_Attack_Tree.JPG)")
                report.write("\n\n")

    # GPS Spoofing attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("7") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/gps_spoofing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/gps_spoofing_attack_tree.JPG)")
                report.write("\n\n")

    # Code injection attack model
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/code_injection_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Code_Injection_Attack_Tree.JPG)")
                report.write("\n\n")

    # SSRF attack model
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/ssrf_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/SSRF_Attack_Tree.JPG)")
                report.write("\n\n")

    # Command Injection attack model
    if questions_and_answers["Q1"].find("3") != -1 and questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/command_injection_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Command_Injection_Attack_Tree.JPG)")
                report.write("\n\n")

    # Cellular Jamming attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                    questions_and_answers["Q21"].find("3") != -1 or questions_and_answers["Q21"].find("4") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/cellular_jamming_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Cellular_Jamming_Attack_Tree.JPG)")
                report.write("\n\n")

    # Cellular Rogue Base Station Attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                    questions_and_answers["Q21"].find("3") != -1 or questions_and_answers["Q21"].find(
                "4") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/cellular_rogue_base_station_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Cellular_Rogue_Base_Station_Attack_Tree.JPG)")
                report.write("\n\n")

    # Cryptanalysis attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/cryptanalysis_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Cryptanalysis_Attack_Tree.JPG)")
            report.write("\n\n")

    # Reverse Engineering attack model
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attack_models/reverse_engineering_attack_model.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Reverse_Engineering_Attack_Tree.JPG)")
                report.write("\n\n")

    # Audit Log Manipulation attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q14"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/audit_log_attack_model.md", "r").read())

            # Tampering Detection attack tree diagram
            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Audit_Log_Manipulation_Attack_Tree.JPG)")
            report.write("\n")
            report.write("\n")

    # Wi-Fi Jamming Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/wi_fi_jamming_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Wi_Fi_Jamming_Attack_Tree.JPG)")
                report.write("\n\n")

    # Wi-Fi SSID Tracking attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/wi_fi_ssid_tracking_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("![alt text](attack_models/Wi_Fi_SSID_Tracking_Attack_Tree.JPG)")

    # Access Point Hijacking attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/access_point_hijacking_model.md", "r").read())

                # Write the scheme in the report
                report.write("![alt text](attack_models/Wi_Fi_SSID_Tracking_Attack_Tree.JPG)")

    # Byzantine Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/byzantine_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Byzantine_Attack_Tree.JPG)")

        # On-Off Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/on_off_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/On_Off_Attack_Tree.JPG)")

    # Spectre Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/spectre_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Spectre_Attack_Tree.JPG)")

    # Meltdown Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/meltdown_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Meltdown_Attack_Tree.JPG)")

    # Hardware Integrity Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/hardware_integrity_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Hardware_Integrity_Attack_Tree.JPG)")

    # Rowhammer Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("attack_models/rowhammer_attack_model.md", "r").read())

        # Write the scheme in the report
        report.write("\n\n")
        report.write("![alt text](attack_models/Rowhammer_Attack_Tree.JPG)")

    # RF Interference on RFIDs attack Model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/interference_on_rfid_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Interference_On_RFID_Attack_Tree.JPG)")

    # Node Tampering attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("attack_models/node_tampering_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](attack_models/Node_Tampering_Attack_Tree.JPG)")

    # Node Jamming in WSNs attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/node_jamming_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Node_Jamming_Attack_Tree.JPG)")

    # Sybil attack Model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/sybil_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Sybil_Attack_Tree.JPG)")

    # Malicious Node Injection attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/malicious_node_injection_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Malicious_Node_Injection_Attack_Tree.JPG)")

    # RFID Spoofing attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/rfid_Spoofing_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/RFID_Spoofing_Attack_Tree.JPG)")

    # RFID Cloning attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/rfid_cloning_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/RFID_Cloning_Attack_Tree.JPG)")

    # RFID Unauthorized Access attack model
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/rfid_unauthorized_access_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/RFID_Unauthorized_Access_Attack_Tree.JPG)")

        # Orbital Jamming attack model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                questions_and_answers["Q21"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/orbital_jamming_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/Orbital_Jamming_Attack_Tree.JPG)")

        # NFC Payment Replay Attack Model
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("9") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("attack_models/nfc_payment_replay_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](attack_models/NFC_Payment_Replay_Attack_Tree.JPG)")

    report.close()
    attack_models_convert_report()
    print("\n\n # Processing done! Check your attack models in the ATTACKS_MAPPING.pdf file")


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
        report.write(
            "{:3}{:25}{:3}{:60}{:3}\n".format("|", table_for_report[i][0], "|", table_for_report[i][1], "|"))

    report.write("\n")

    # Testing DoS Jamming attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                questions_and_answers["Q21"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/cellular_jamming_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Wi-Fi Jamming attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("6") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/wi_fi_jamming_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing NFC Payment Replay attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("9") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/nfc_payment_replay_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Orbital Jamming attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                questions_and_answers["Q21"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/orbital_jamming_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing GPS Jamming attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("7") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/gps_jamming_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Bluesnarfing attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("5") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/bluesnarfing_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Bluejacking attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("5") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/bluejacking_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Wi-Fi SSID Tracking attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("6") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/wi_fi_ssid_tracking_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Byzantine attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("6") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/byzantine_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing On-Off attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/on_off_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Malicious Insider attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/malicious_insider_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Sniffing attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/sniffing_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing MitM attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/mitm_testing_guide.md", "r", errors="ignore").read())

    # Testing Eavesdropping attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q18"].find("4") != -1 or questions_and_answers["Q18"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/eavesdropping_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing CSRF attack
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/csrf_testing_guide.md", "r", errors="ignore").read())

    # Testing SQLi attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/sqli_testing_guide.md", "r", errors="ignore").read())

    # Testing XSS attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/xss_testing_guide.md", "r", errors="ignore").read())

    # Testing SSRF attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/ssrf_testing_guide.md", "r", errors="ignore").read())

    # Testing Command Injection attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/command_injection_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Command Injection attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/code_injection_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Audit Log Manipulation attacks
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
                questions_and_answers["Q6"].find("1") != -1 and (
                questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/audit_log_manipulation_testing_guide.md", "r",
                     errors="ignore").read())

    # Testing Brute Force Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q13"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("security_test_recommendation/brute_force_testing_guide.md", "r",
                                  errors="ignore").read())

    # Testing Cryptanalysis Attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/cryptanalysis_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Phishing attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/phishing_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Pharming attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/pharming_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Spoofing attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and \
            questions_and_answers["Q6"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/spoofing_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Session Fixation attack
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 and questions_and_answers["Q8"].find("2") != -1 and \
                    questions_and_answers["Q8"].find("3") != -1:
                if questions_and_answers["Q18"].find("2") != -1 or questions_and_answers["Q18"].find("4") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(
                        open("security_test_recommendation/session_fixation_testing_guide.md", "r",
                             errors="ignore").read())

    # Testing Session Hijacking attacks
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 and questions_and_answers["Q8"].find("2") != -1 and \
                    questions_and_answers["Q8"].find("3") != -1:
                if questions_and_answers["Q18"].find("2") != -1 or questions_and_answers["Q18"].find("4") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(
                        open("security_test_recommendation/session_hijacking_testing_guide.md", "r",
                             errors="ignore").read())

    # Testing Access Point Hijacking attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("6") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/access_point_hijacking_testing_guide.md", "r",
                     errors="ignore").read())

    # Testing Cellular Rogue Base Station attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q21"].find("1") != -1 or questions_and_answers["Q21"].find("2") != -1 or \
                questions_and_answers["Q21"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/cellular_rogue_base_station_testing_guide.md", "r",
                     errors="ignore").read())

    # Testing GPS Spoofing attack
    if questions_and_answers["Q21"].find("7") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_test_recommendation/gps_spoofing_testing_guide.md", "r",
                          errors="ignore").read())

    # Testing RF Interference on RFIDs attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/interference_on_rfid_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Tampering Attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("security_test_recommendation/tampering_testing_guide.md", "r",
                                  errors="ignore").read())

    # Testing Node Tampering attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            if questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("security_test_recommendation/node_tampering_testing_guide.md", "r",
                                  errors="ignore").read())

    # Testing Node Jamming in WSNs attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/node_jamming_testing_guide.md", "r",
                              errors="ignore").read())

        # Testing Sybil attack
        if questions_and_answers["Q1"].find("7") != -1:
            if questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("security_test_recommendation/sybil_testing_guide.md", "r",
                                  errors="ignore").read())

    # Testing Malicious Node Injection attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("10") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/malicious_node_injection_testing_guide.md", "r",
                     errors="ignore").read())

    # Testing RFID Spoofing attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/rfid_Spoofing_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing RFID Cloning attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/rfid_cloning_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing RFID Unauthorized Access attack
    if questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q21"].find("8") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/rfid_unauthorized_access_testing_guide.md", "r",
                     errors="ignore").read())

    # Testing Botnet attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/botnet_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Malware-as-a-Service attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/maas_testing_guide.md", "r", errors="ignore").read())

    # Testing Flooding Attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/flooding_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Buffer Overflow attacks
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or \
            questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q12"].find("2") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/buffer_overflow_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Bypassing Physical Security attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(
                open("security_test_recommendation/bps_testing_guide.md", "r", errors="ignore").read())

    # Testing Physical theft attack
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/physical_theft_testing_guide.md", "r",
                              errors="ignore").read())

        # Testing VM Migration attacks
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("security_test_recommendation/vm_migration_testing_guide.md", "r",
                                  errors="ignore").read())

    # Testing Side-Channel attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/side_channel_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Spectre attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/spectre_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Meltdown attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/meltdown_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Hardware Integrity attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_test_recommendation/hardware_integrity_testing_guide.md", "r",
                              errors="ignore").read())

    # Testing Rowhammer attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(
            open("security_test_recommendation/rowhammer_testing_guide.md", "r", errors="ignore").read())

    # Testing Reverse Engineering attacks
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1:
            if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or \
                    questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(
                    open("security_test_recommendation/reverse_engineering_testing_guide.md", "r",
                         errors="ignore").read())

    # Testing VM Escape attacks
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
            questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(
            open("security_test_recommendation/vm_escape_testing_guide.md", "r", errors="ignore").read())

    report.close()
    security_test_recommendation_convert_report()
    print(
        "\n\n # Processing done! Check your security test specification and automation tools in the TEST_SPECIFICATION.pdf file")

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

    # backup mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/backup_mechanism_guide.md", "r").read())

    # audit mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/audit_mechanisms_guide.md", "r").read())

    #  cryptographic algorithms mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/cryptographic_algorithms_mechanisms.md", "r").read())

    # biometric authentication mechanisms
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("1") != -1:
        report.write(open("security_mechanisms/biometric_authentication_mechanism.md", "r").read())

    # channel-based authentication mechanisms
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("2") != -1:
        report.write(open("security_mechanisms/channel_based_authentication_mechanism.md", "r").read())

    # factors-based authentication mechanisms
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("3") != -1:
        report.write(open("security_mechanisms/factors_based_authentication_mechanism.md", "r").read())
        
    # id-based authentication mechanisms
    if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q4"].find("4") != -1:
        report.write(open("security_mechanisms/id_based_authentication_mechanism.md", "r").read())

    # cryptographic protocolos mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (
            questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("security_mechanisms/cryptographic_protocols_mechanisms.md", "r").read())

    # access control mechanisms
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_mechanisms/access_control_mechanisms.md", "r").read())

    # inspection and logging mechanisms
    if questions_and_answers["Q5"].find("1") != -1:
        if questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("security_mechanisms/inspection_mechanisms.md", "r").read())

            report.write(open("security_mechanisms/logging_mechanisms.md", "r").read())

    # device tamper detection mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q22"].find(
            "1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/device_detection_mechanisms.md", "r").read())

    # physical location mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("1") != -1 or questions_and_answers["Q8"].find("2") != -1 or
                questions_and_answers["Q8"].find("3") != -1) and questions_and_answers["Q22"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/physical_location_mechanism.md", "r").read())

    # confinement mechanisms
    if questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q8"].find("2") != -1 or questions_and_answers["Q8"].find("3") != -1):
        if questions_and_answers["Q14"].find("1") != -1 or questions_and_answers["Q16"].find("1") != -1 or questions_and_answers["Q17"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("security_mechanisms/confinement_mechanisms.md", "r").read())

    # filtering mechanisms
    if questions_and_answers["Q14"].find("1") != -1 and questions_and_answers["Q16"].find("1") != -1 and questions_and_answers["Q17"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/filtering_mechanism.md", "r").read())

    # iot and lora mechanisms
    if (questions_and_answers["Q1"].find("1") != -1  or questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("4") != -1) and questions_and_answers["Q1"].find("7") != -1 and (questions_and_answers["Q21"].find("11") != -1 or questions_and_answers["Q21"].find("12")):
        report.write("\n")
        report.write("\n")

        report.write(open("security_mechanisms/iot_lora_security_mechanisms.md", "r").read())

    report.close()
    mechanisms_convert_report()
    print("\n\n # Processing done! Check your security mechanisms in the SECURITY_MECHANISMS.pdf file")

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

    merger = PdfMerger()

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
