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

# add the answers (output) to a list to write as the respective answers and comments 
# in the generated file with answers
answers_list = []
comments_list = []
table_for_report = []

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
    "Q19": "",
    "Q20": "",
}

"""
// [Questions]
// Q1   -> Architecture
// Q2   -> Application Domain Type
// Q3   -> Authentication
// Q4   -> Has a DB
// Q5   -> Type of data storage
// Q6   -> Which db
// Q7   -> Type of data
// Q8   -> User Registration
// Q9   -> Way of user registration
// Q10  -> Programming Languages
// Q11  -> Input Forms
// Q12  -> Upload Files
// Q13  -> Logs
// Q14  -> System Regular Updates
// Q15  -> Third-part Software
// Q16  -> System Cloud Environment
// Q17  -> Hardware Specifications
// Q18  -> Hardware Auth
// Q19  -> Hardware Communications
// Q20  -> Data Center Phisical Access
"""

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
    "1": "No Authentication",
    "2": "Username and Password",
    "3": "Social Networks / Google",
    "4": "SmartCard",
    "5": "Biometrics",
    "6": "Two Factor Authentication",
    "7": "Multi Factor Authentication"
}

question4 = {
    "1": "Yes",
    "2": "No"
}

question5 = {
    "1": "SQL",
    "2": "NoSQL",
    "3": "Local Storage",
    "4": "Distributed Storage"
}

question6 = {
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

question7 = {
    "1": "Personal Information",
    "2": "Confidential Data",
    "3": "Critical Data",
    "4": ""
}

question8 = {
    "1": "Yes",
    "2": "No"
}

question9 = {
    "1": "The users will register themselves",
    "2": "Will be a administrator that will register the users"
}

question10 = {
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

question11 = {
    "1": "Yes",
    "2": "No"
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
    "1": "Community Cloud",
    "2": "Hybrid Cloud",
    "3": "Private Cloud",
    "4": "Public Cloud",
    "5": "Virtual Private Cloud"
}

question17 = {
    "1": "Yes",
    "2": "No"
}

question18 = {
    "1": "No Authentication",
    "2": "Symmetric Key",
    "3": "Basic Authentication (user/pass)",
    "4": "Certificates (X.509) ",
    "5": "TPM (Trusted Platform Module)"
}

question19 = {
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

question20 = {
    "1": "Yes",
    "2": "No"
}

'''
>Question templates
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
    while True:
        filepath = validateInput(2)
        if not os.path.isfile(filepath):
            print("File path {} does not exist...".format(filepath))
        else:
            break

    with open(filepath, 'r') as file:
        line = file.readline()
        while line:

            # read line until character '#' which means after that is a comment
            input_list.append(line.split('#')[0].strip())
            line = file.readline()


"""
[Summary]: Common method to validate input and implemts dynamic arguments
[Arguments]: 
    - arg(1) what to validate -> if it is to validate a int or a string (1 or 2)
    - arg(2) n_options -> number of options in the question (==range)
[Returns]: Returns inputs user
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
        print("  **Which will be the architecture of the system?**  ")
    else:
        print("  **What is the architecture of the system?**  ")
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
            print("  Please specify the architecture: (name between single quotes)  ")
            value2 = validateInput(2)
            # question_1["9"] = str(value2)
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
        print("  **Which will be the domain of the system?**  ")
    else:
        print("  **What is the domain of the system ?**")

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
        print("  **Which type of authentication will be implemented ?**  ")
    else:
        print("  **What is the type of authentication implemented in the system ?**  ")
    print("")
    print("  1 - No Authentication  ")
    print("  2 - Username and Password  ")
    print("  3 - Social Networks/Google  ")
    print("  4 - SmartCard  ")
    print("  5 - Biometrics  ")
    print("  6 - Two Factor Authentication  ")
    print("  7 - Multi Factor Authentication  ")
    print("")

    value = validateInput(1, 8)
    questions_and_answers["Q3"] = str(value)


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
        print("  ** Will the system use a Database?**  ")
    else:
        print("  **Does the system use a Database?**  ")
    print("")
    print("  1 - Yes  ")
    print("  2 - No  ")
    print("")

    value = validateInput(1, 3)
    questions_and_answers["Q4"] = str(value)

    if value == 1:
        typeOfDatabase(version)
        if questions_and_answers["Q5"] == '1' or questions_and_answers["Q5"] == '2':
            whichDatabase(version)
        sensitiveData(version)

    else:
        questions_and_answers["Q5"] = "N/A"
        questions_and_answers["Q6"] = "N/A"
        questions_and_answers["Q7"] = "N/A"
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
        print("  **What is type of data storage ?**  ")
    print("")
    print("  1 - SQL  ")
    print("  2 - NoSQL  ")
    print("  3 - Local Storage  ")
    print("  4 - Distributed Storage  ")
    print("")

    value = validateInput(1, 5)
    questions_and_answers["Q5"] = str(value)

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
        print("  **Which Database will be used ?**  ")
    else:
        print("  **What is the Database used?**  ")

    print("")

    if questions_and_answers["Q5"] == '1':
        print("  1 - SQL Server  ")
        print("  2 - MySQL  ")
        print("  3 - PostgreSQL  ")
        print("  4 - SQLite  ")
        print("  5 - OracleDB  ")
        print("  6 - MariaDB  ")

    if questions_and_answers["Q5"] == '2':
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
        questions_and_answers["Q6"] = str(value2)
    else:
        questions_and_answers["Q6"] = str(value)

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
    print("  4 - Other  ")
    print("")

    while (1):
        value = validateInput(1, 5)
        if value == 0:
            return
        if value == 4:
            print("  Please specify the architecture: (name between single quotes)  ")
            # TO-DO change this funtion input
            value2 = validateInput(2)
            # question_5["4"] = str(value2)
            questions_and_answers["Q7"] = questions_and_answers["Q7"] + str(value2) + ";"

        else:
            questions_and_answers["Q7"] = questions_and_answers["Q7"] + str(value) + ";"

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
    questions_and_answers["Q8"] = str(value)

    if value == 1:
        typeOfUserRegist(version)
    else:
        questions_and_answers["Q9"] = "N/A"

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
        print(" **Which way of user registration will be used?**  ")
    else:
        print(" **Which way of user registration it's used?**  ")
    print("")
    print("  1 - The users will register themselves  ")
    print("  2 - Will be a administrator that will register the users  ")
    print("")

    value = validateInput(1, 3)
    questions_and_answers["Q9"] = str(value)

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
            questions_and_answers["Q10"] = questions_and_answers["Q10"] + str(value2) + ";"

        else:
            questions_and_answers["Q10"] = questions_and_answers["Q10"] + str(value) + ";"

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
    questions_and_answers["Q11"] = str(value)

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
    questions_and_answers["Q12"] = str(value)

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
    questions_and_answers["Q13"] = str(value)

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
    questions_and_answers["Q14"] = str(value)

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
    questions_and_answers["Q15"] = str(value)


"""
[Summary]: Method to identify the Cloud development model (environment) used by the application
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""
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
    questions_and_answers["Q16"] = str(value)

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
    questions_and_answers["Q17"] = str(value)

    if value == 1:
        hardwareAuth(version)
        hardwareComunication(version)
    else:
        questions_and_answers["Q18"] = "N/A"
        questions_and_answers["Q19"] = "N/A"

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
    questions_and_answers["Q18"] = str(value)

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
    print("  2 - 4G/LTE ")
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
            print("Please specify the architecture: (name between single quotes)")
            value2 = validateInput(2)
            questions_and_answers["Q19"] = questions_and_answers["Q19"] + str(value2) + ";"
        else:
            questions_and_answers["Q19"] = questions_and_answers["Q19"] + str(value) + ";"


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
    questions_and_answers["Q20"] = str(value)


"""
[Summary]: Método que permite abrir/criar e armazenar no ficheiro 'ans.txt' as respostas ao questionário do utilizador
[Arguments]: 
    - $version$: An integer constant equal to unity
[Returns]: No return
"""   
def printData():
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
    print("{:22} {:3} {:40} ".format("Architecture", ":", ' ; '.join(list_aux)))
    table_for_report.append(["Architecture", ' ; '.join(list_aux)])

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

    for n in question4:
        item = questions_and_answers["Q4"]
        if item == n:
            # print( "Has DB {:>18} ".format(":     ") + question_2[n])
            print("{:22} {:3} {:40} ".format("Has DB", ":", question4[n]))
            table_for_report.append(["Has DB", question4[n]])
            answers_list.append(questions_and_answers["Q4"])
            comments_list.append(question4[n])

    item = questions_and_answers["Q5"]
    # case this question is not answered, and the answer it will be "N/A"
    if questions_and_answers["Q5"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of data storage", ":", item))
        table_for_report.append(["Type of data storage", item])
        answers_list.append(questions_and_answers["Q5"])
        comments_list.append(item)
    else:
        for n in question5:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of data storage", ":", question5[n]))
                table_for_report.append(["Type of data storage", question5[n]])
                answers_list.append(questions_and_answers["Q5"])
                comments_list.append(question5[n])

    item = questions_and_answers["Q6"]
    for n in question6:
        if item == n:
            print("{:22} {:3} {:40} ".format("Which DB", ":", question6[n]))
            table_for_report.append(["Which DB", question6[n]])
            answers_list.append(questions_and_answers["Q6"])
            comments_list.append(question6[n])

    # case of user input text
    if item.isdigit() == False:
        print("{:22} {:3} {:40} ".format("Which DB", ":", item))
        table_for_report.append(["Which DB", item])
        answers_list.append(questions_and_answers["Q6"])
        comments_list.append(item)

    list_aux = []
    
    # it is a multiple question
    # find if the answer correspond to option "others" (means that is user input text) or not answered
    if questions_and_answers["Q7"][0].isdigit() == False and questions_and_answers["Q7"].find(";") == -1:
        list_aux.append(questions_and_answers["Q7"])
    else:
        # variable aux is a list that contains the answers chosen by the user to the question in cause
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q7"].split(";")
        # delete last item (= None)
        aux = aux[:-1]

        for item in aux:
            for option in question7:
                if item == option:
                    list_aux.append(question7[option])
            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Type of data stored", ":", ' ; '.join(list_aux)))
    table_for_report.append(["Type of data stored", ' ; '.join(list_aux)])
    answers_list.append(questions_and_answers["Q7"])
    comments_list.append(' ; '.join(list_aux))

    for n in question8:
        item = questions_and_answers["Q8"]
        if item == n:
            print("{:22} {:3} {:40}".format("User Registration", ":", question8[n]))
            table_for_report.append(["User Registration", question8[n]])
            answers_list.append(questions_and_answers["Q8"])
            comments_list.append(question8[n])

    item = questions_and_answers["Q9"]
    if questions_and_answers["Q9"].isdigit() == False:
        print("{:22} {:3} {:40} ".format("Type of Registration", ": ", item))
        table_for_report.append(["Type of Registration", item])
        answers_list.append(questions_and_answers["Q9"])
        comments_list.append(item)
    else:
        for n in question9:
            if item == n:
                print("{:22} {:3} {:40} ".format("Type of Registration", ": ", question9[n]))
                table_for_report.append(["Type of Registration", question9[n]])
                answers_list.append(questions_and_answers["Q9"])
                comments_list.append(question9[n])

    list_aux = []
    # it is a multiple question
    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q10"][0].isdigit() == False and questions_and_answers["Q10"].find(";") == -1:
        list_aux.append(questions_and_answers["Q10"])
    else:
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q10"].split(";")
        # delete last item (= None)
        aux = aux[:-1]
        for item in aux:
            for option in question10:
                if item == option:
                    list_aux.append(question10[option])
            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("Programming Languages", ":", ' ; '.join(list_aux)))

    table_for_report.append(["Programming Languages", ' ; '.join(list_aux)])
    answers_list.append(questions_and_answers["Q10"])
    comments_list.append(' ; '.join(list_aux))

    for n in question11:
        item = questions_and_answers["Q11"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Input Forms", ":", question11[n]))
            table_for_report.append(["Input Forms", question11[n]])
            answers_list.append(questions_and_answers["Q11"])
            comments_list.append(question11[n])

    for n in question12:
        item = questions_and_answers["Q12"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Upload Files", ":", question12[n]))
            table_for_report.append(["Upload Files", question12[n]])
            answers_list.append(questions_and_answers["Q12"])
            comments_list.append(question12[n])

    for n in question13:
        item = questions_and_answers["Q13"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has logs", ":", question13[n]))
            table_for_report.append(["The system has logs", question13[n]])
            answers_list.append(questions_and_answers["Q13"])
            comments_list.append(question13[n])

    for n in question14:
        item = questions_and_answers["Q14"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has regular updates", ":", question14[n]))
            table_for_report.append(["The system has regular updates", question14[n]])
            answers_list.append(questions_and_answers["Q14"])
            comments_list.append(question14[n])

    for n in question15:
        item = questions_and_answers["Q15"]
        if item == n:
            print("{:22} {:3} {:40} ".format("The system has third-party", ":", question15[n]))
            table_for_report.append(["The system has third-party", question15[n]])
            answers_list.append(questions_and_answers["Q15"])
            comments_list.append(question15[n])

    for n in question16:
        item = questions_and_answers["Q16"]
        if item == n:
            print("{:22} {:3} {:40}".format("System Cloud Environments", ":", question16[n]))
            table_for_report.append(["System Cloud Environments", question16[n]])
            answers_list.append(questions_and_answers["Q16"])
            comments_list.append(question16[n])

    for n in question17:
        item = questions_and_answers["Q17"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Hardware Specification", ":", question17[n]))
            table_for_report.append(["Hardware Specification", question17[n]])
            answers_list.append(questions_and_answers["Q17"])
            comments_list.append(question17[n])

    for n in question18:
        item = questions_and_answers["Q18"]
        if item == n:
            print("{:22} {:3} {:40} ".format("HW Authentication", ":", question18[n]))
            table_for_report.append(["HW Authentication", question18[n]])
            answers_list.append(questions_and_answers["Q18"])
            comments_list.append(question18[n])

    list_aux = []
    # it is a multiple question
    # find if the answer correspond to option "others" (means that is only user input text)
    if questions_and_answers["Q19"][0].isdigit() == False and questions_and_answers["Q19"].find(";") == -1:
        list_aux.append(questions_and_answers["Q19"])
    else:
        # cut the string in the delimitator ";"
        aux = questions_and_answers["Q19"].split(";")
        # delete last item (= None)
        aux = aux[:-1]
        for item in aux:
            for option in question19:
                if item == option:
                    list_aux.append(question19[option])
            # case of user input text
            if item.isdigit() == False:
                list_aux.append(item)

    print("{:22} {:3} {:40} ".format("HW Wireless Tech", ":", ' ; '.join(list_aux)))

    table_for_report.append(["HW Wireless Tech", ' ; '.join(list_aux)])

    answers_list.append(questions_and_answers["Q19"])
    comments_list.append(' ; '.join(list_aux))

    for n in question20:
        item = questions_and_answers["Q20"]
        if item == n:
            print("{:22} {:3} {:40} ".format("Data Center Phisical Access", ":", question20[n]))
            table_for_report.append(["Data Center Phisical Access", question20[n]])
            answers_list.append(questions_and_answers["Q20"])
            comments_list.append(question20[n])

    # write / generate a file with all answers
    for i in range(0, len(answers_list)):
        generate_file.write("{:20}{:3}{:20}\n".format(answers_list[i], " # ", comments_list[i]))
    generate_file.close()

"""
[Summary]: Method to convert the markdown Security Requirements report to html and pdf format
[Arguments]: 
    - $version$: An integer constant equal to unity
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
[Arguments]: 
    - $version$: An integer constant equal to unity
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

@with_goto
def switch1():
    label.begin
    val = 0
    
    while True:
        try:
            val = int(input("\n\nWhat is your option?\n\n"))       
        except ValueError:
            print("\n\nError! Enter a whole number between 1 and 7, according to the menu above!\n\n")
            goto.begin
        else:
            break
    with Switch(val) as case:
        if case(1):
            print("---")
            print("")
            print("  **\n\nWhich way do you want to run this tool?**\n\n  ")
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
                print("\n\n**The questionnaire is over!**\n\n")

            # answers already written in the input file
            else:
                print("---")
                print("")
                print("  \n\n**What is the name of the input file (ans.txt)?**\n\n  ")
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

            informationCapture()

            print("\n\n# Processing Done! Choose another option to process the requests!\n\n")

        if case(2):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST REQUIREMENTS ELICITATION PROCESSING\n\n")
            get_requirements()
            # You must specify the current path of the source code
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SECloudMobDESIGNS/SECloudMobDESIGNS.py/SECURITY_REQUIREMENTS.pdf')
            informationCapture()

        if case(3):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST BEST PRACTICES ELICITATION PROCESSING\n\n")
            get_good_practices()
            # You must specify the current path of the source code
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SECloudMobDESIGNS/SECloudMobDESIGNS.py/GOOD_PRACTICES.pdf')
            informationCapture()

        if case(4):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST ATTACK MODELS ELICITATION PROCESSING\n\n")
            get_attack_models()
            # You must specify the current path of the source code
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SECloudMobDESIGNS/SECloudMobDESIGNS.py/ATTACKS_MAPPING.pdf')
            informationCapture()

        if case(5):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST TEST SPECIFICATION ELICITATION PROCESSING\n\n")
            get_security_test_recommendation()
            # You must specify the current path of the source code
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SECloudMobDESIGNS/SECloudMobDESIGNS.py/TEST_SPECIFICATION.pdf')
            informationCapture()

        if case(6):
            print("\n********************************************************************************************\n")
            print("\t\tREQUEST FULL REPORT PROCESSING\n\n")
            fullReport()
            # You must specify the current path of the source code
            webbrowser.open_new(r'file:///Users/FranciscoChimuco/SECURIoTESIGN/SECloudMobDESIGNS/SECloudMobDESIGNS.py/FULL_REPORT.pdf')
            informationCapture()

        if case(7):
            print("\n\n*** Application finished successfully! ***\n\n")
            exit(0)

        if case.default:
            print("\n\n*** Error! Insert a valid value between 1 and 7! ***\n\n")
            goto.begin

"""
[Summary]: Method responsible for creating the main menu
[Arguments]: No argument
[Return]: No return
"""
def informationCapture():
    print("************************************************************************************************")
    print("\nWelcome to SECloudMobDESIGNS Framework!\n")
    print("\nWhat would you like to do?\n")
    print("\n1. First, Answer the Questions Necessary for Possible Processing")
    print("\n2. Process Security Requirement Elicitation Request")
    print("\n3. Process Secure Development Best Practice Guide Request ")
    print("\n4. Mapping Security Attack Models Request")
    print("\n5. Process Secure Development Test Specification Guide Request")
    print("\n6. Process Full Report")
    print("\n7. Exit")
    print("\n\nSelect your option (1-7):")
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

    # check if authentication, database and personal information, confidential or critical data are choosen
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/confidentiality.md", "r").read())

    # integrity requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/integrity.md", "r").read())

    report.write(open("requirements/avaliability.md", "r").read())

    # authentication requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write(open("requirements/authentication.md", "r").read())

    # authorization requirements
    # if (questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write(open("requirements/authorization.md", "r").read())

    # nonRepudiaton requirements
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/nonRepudiation.md", "r").read())
            report.write(open("requirements/accountability.md", "r").read())

    # realiability requirements
    report.write(open("requirements/reliability.md", "r").read())
    
    # privacy requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/privacy.md", "r").read())

    # physical security requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1) and questions_and_answers["Q20"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/physicalSecurity.md", "r").read())

    # forgery resistance requirement
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1) and questions_and_answers["Q20"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/forgeryResistance.md", "r").read())

    # tampering detection requirement
    if questions_and_answers["Q20"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/tamperDetection.md", "r").read())

    # data freshness requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/dataFreshness.md", "r").read())

    # confinement requirements
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        if questions_and_answers["Q12"].find("1") != -1 or questions_and_answers["Q14"].find("1") != -1 or questions_and_answers["Q15"].find("1") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("requirements/confinement.md", "r").read())

    # Interoperability requirement
    if questions_and_answers["Q12"].find("1") != -1 and questions_and_answers["Q14"].find("1") != -1 and questions_and_answers["Q15"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/interoperability.md", "r").read())

    # data origin authentication
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("requirements/dataOriginAuthentication.md", "r").read())

    report.close()
    requirements_convert_report()
    print("# Processing done! Check your requirements in the SECURITY_REQUIREMENTS.pdf file")

"""
[Summary]: Method responsible for processing information about SBPG
[Arguments]: No arguments
[Return]: No return
"""
def get_good_practices():
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
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q1"].find("7") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("goodPractices/IOT_Security_guide.md", "r").read())
    
    # check if SQL database is choosed
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4"):
        if questions_and_answers["Q3"].find("1") != -1 and questions_and_answers["Q5"].find("1"):
            report.write("\n")
            report.write("\n")
            
            # write SQL injection guide
            report.write(open("goodPractices/SQL_Injection_guide.md", "r").read())

    # check if language program are chosen
    if (questions_and_answers["Q1"].find("1") != -1 and (questions_and_answers["Q10"].find("1") != -1 or questions_and_answers["Q10"].find("4") != -1)):
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/Java_C#_guide.md", "r").read())

    # check if input forms is used
    if questions_and_answers["Q11"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        # write input validation guide
        report.write(open("goodPractices/Input_Validation_guide.md", "r").read())

    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q3"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            
            # Session Management guide
            report.write(open("goodPractices/Session_Management_guide.md", "r").read())
            report.write("\n")
            report.write("\n")
            # write XSS guide
            report.write(open("goodPractices/Cross_Site_Scripting_guide.md", "r").read())

            report.write("\n")
            report.write("\n")

    # write Cryptography guide
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n\n")
        report.write(open("goodPractices/Cryptography_guide.md", "r").read())

    # write SSL/TLS guide
    if ((questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (
            questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1)):
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/TLS_guide.md", "r").read())

    if questions_and_answers["Q9"].find("1") != -1:
        report.write("\n")
        report.write("\n")

        # write Access Control guide
        report.write(open("goodPractices/Access_Control_guide.md", "r").read())

    if questions_and_answers["Q11"].find("1") != -1:
        # check if file upload are chosen

        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/File_Upload_guide.md", "r").read())

    # logging info
    if questions_and_answers["Q12"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/Logging_guide.md", "r").read())

    # Update info
    if questions_and_answers["Q13"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/App_Update_guide.md", "r").read())

    # Third-party info
    if questions_and_answers["Q14"].find("1") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("goodPractices/App_Third_Party_guide.md", "r").read())

    report.close()
    goodPracticeConvertReport()
    print("# Processing done! Check your requirements in the GOOD_PRACTICES.pdf file")



"""
[Summary]: Method responsible for processing information about AME
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
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("4") != -1 or questions_and_answers["Q16"].find("2") != -1):
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/mitmAttack.md", "r").read())

            # MitM attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](mitmAttack.png)")
            report.write("\n")
            report.write("\n")
    
    # If the application is web or hybrid, we have XSS
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1 and (questions_and_answers["Q16"].find("4") != -1 or questions_and_answers["Q16"].find("2") != -1):
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/XSS.md", "r").read())

            # XSS attack tree diagram
            # Write de scheme in the report
            report.write("![alt text](xssAttack.png)")
            report.write("\n")
            report.write("\n")
            
    # If the aplication is web or hybrid, we have Cookie Poisoning
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (questions_and_answers["Q16"].find("2") != -1 or questions_and_answers["Q16"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/dnsPoisoningAttack.md", "r").read())

        # CookiePoisoning attack tree diagram
        # Write de scheme in the report
        report.write("![alt text](dnsPoisoningAttack.png)")
        report.write("\n")
        report.write("\n")

    # If the application is web or hybrid, we have Malicious QR Code Injection Attacks
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/maliciousQRCode.md", "r").read())
            
            # Malicious QR Code attack diagram
            # Write de scheme in the report
            report.write("![alt text](malicIousQRCodeAttack.png)")
            report.write("\n")
            report.write("\n")
            
    # If the application is web or hybrid, we have CAPTCHA Breaking Attacks
    if (questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1) and (questions_and_answers["Q16"].find("2") != -1 or questions_and_answers["Q16"].find("4") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/captchaBreaking.md", "r").read())

    # CAPTCHA Breaking attack tree diagram
    # Write de scheme in the report
    # report.write("![alt text](design_schemes6.png)")
    # report.write("\n")
    # report.write("\n")

    # Database use and public cloud environment SQLi attacks
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        if questions_and_answers["Q4"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/SQLi.md", "r").read())

            # SQLi attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](SQLi.png)")
            report.write("\n")
            report.write("\n")
    
    # DoS Attacks
    if questions_and_answers["Q4"].find("1") != -1 and (
            questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write(open("attackModels/DoS.md", "r").read())

        # DoS attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](DoS.png)")
        report.write("\n")
        report.write("\n")
        
        report.write(open("attackModels/DDoS.md", "r").read())

        # DDoS attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](DDoS.png)")
        report.write("\n")
        report.write("\n")

    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q16"].find("4") != -1 or questions_and_answers["Q16"].find("2") != -1):
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write(open("attackModels/Sniffer.md", "r").read())

            # Sniffer attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](eavesdropingAttack.png)")
            report.write("\n")
            report.write("\n")

    # If the application is web or hybrid, we have DNS Poisoning Attack
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        report.write(open("attackModels/DNS.md", "r").read())

        # DNS Poisoning attack tree diagram
        # Write the scheme in the report
        # report.write("![alt text](dnsPoisoningAttack.png)")
        # report.write("\n")
        # report.write("\n")

    # If the application is web or hybrid, we have Reused IP Address Attacks
    if questions_and_answers["Q1"].find("3") != -1 or questions_and_answers["Q1"].find("4") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/reusedIPAddress.md", "r").read())

        # Reused IP Address attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](ipSpoofingAttack.png)")
        report.write("\n")
        report.write("\n")

    # If the application is web or hybrid, we have Phishing Attacks
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/phishingAttack.md", "r").read())

        # Phishing Attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](phishingAttack.png)")
        report.write("\n")
        report.write("\n")
        
        # Botnet Attacks
        report.write(open("attackModels/Botnet.md", "r").read())

        # Botnet attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](botnetAttack.png)")
        report.write("\n")
        report.write("\n")

    # If the application is web or hybrid, we have XML
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/XMLi.md", "r").read())

        # XML Attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](xmliAttack.png)")
        report.write("\n")
        report.write("\n")
        
    # If the application is web or hybrid, we have Session Hijacking and Session Fixation
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            if questions_and_answers["Q4"].find("1") != -1 and questions_and_answers["Q10"].find("6") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/sessionHijacking.md", "r").read())

                # Session Hijacking attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](sidHijacking.png)")
                report.write("\n")
                report.write("\n")

                # Session Fixation
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/sessionFixation.md", "r").read())

                # Session Fixation Attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](sidFixation.png)")
                report.write("\n")
                report.write("\n")
                
    # If the system was development for iOS, Tizen and embedded platforms (Buffer Overflow)
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q10"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/bufferOverflows.md", "r").read())

        # Buffer Overflows attack diagram
        # Write the scheme in the report
        report.write("![alt text](bufferOverflowAttackTree.png)")
        report.write("\n")
        report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Mobile Apllication Spoofing )
    if questions_and_answers["Q4"].find("1") != -1 :
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/Spoofing.md", "r").read())

            # Spoofing attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](spoofingAttack.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
    if questions_and_answers["Q4"].find("1") != -1 :
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/VMMigration.md", "r").read())

            # Attack on VM at migration tree diagram
            # Write the scheme in the report
            report.write("![alt text](vmMigrationAttack.png)")
            report.write("\n")
            report.write("\n")
            
    # If the system was development for Android, iOS, Tizen and embedded platforms (Insiders Malicious Attacks)
    if questions_and_answers["Q4"].find("1") != -1 :
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            if questions_and_answers["Q20"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/maliciousInsider.md", "r").read())

                # Malicious Insiders attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](maliciousInsidersAttack.png)")
                report.write("\n")
                report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (VM Escape Attack)
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        report.write("\n")
        report.write("\n")
        report.write(open("attackModels/VMEscape.md", "r").read())

        # VM Escape attack tree diagram
        # Write the scheme in the report
        report.write("![alt text](vmEscapeAttack.png)")
        report.write("\n")
        report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Side-Channel)
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("attackModels/crossVM.md", "r").read())

            # Side-Channel attack tree diagram
            # Write the scheme in the report
            report.write("![alt text](sideChannelAttack.png)")
            report.write("\n")
            report.write("\n")

    # If the system was development for Android, iOS, Tizen and embedded platforms (Malware Injection Attacks)
        if (questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1) and questions_and_answers["Q4"].find("1") != -1:    
            if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/malwareInjection.md", "r").read())

                # Cross VM attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](malwareInjectionAttack.png)")
                report.write("\n")
                report.write("\n")
                
    # If the system was development for Android, iOS, Tizen and embedded platforms (Tampering Attacks)
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            if questions_and_answers["Q20"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("attackModels/tamperingAttack.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("![alt text](tamperingAttack.png)")
                report.write("\n")
                report.write("\n")

    report.close()
    attack_models_convert_report()
    print("# Processing done! Check your requirements in the ATTACKS_MAPPING.pdf file")

"""
[Summary]: Method resposable pelo precessamento da informação relativa ao módulo STSTAT
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
    
    # Security Testing against DoS, DDoS and Botnet Attacks
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        if questions_and_answers["Q16"].find("1") != -1 or questions_and_answers["Q16"].find("2") != -1 or questions_and_answers["Q16"].find("3") != -1 or questions_and_answers["Q16"].find("4") != -1 :
            report.write(open("securityTesting/BOTNETDOSDDOSTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    # Security Testing against MitM attacks
    if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
        if (questions_and_answers["Q16"].find("4") != -1 or questions_and_answers["Q16"].find("2") != -1):
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/BotnetDoSDDoSPHISINGSPOOFINGPHISHINGMITMTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    # Security Testing against SQLi, XMLi, CRSF, XSS, googleHacking, etc. and phishing attacks 
    if questions_and_answers["Q1"].find("4") != -1 or  questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q4"].find("1") != -1 and questions_and_answers["Q5"].find("1") != -1 and (questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1):
            if questions_and_answers["Q16"].find("1") != -1 or (questions_and_answers["Q16"].find("2") != -1 or questions_and_answers["Q16"].find("4") != -1):
                report.write("\n")
                report.write("\n")
                report.write(open("securityTesting/SQLiXSSCSRFSPOOFINGTEST.md", "r").read())
                
    # Security Testing against Sniffing, Pharming, Phishing, Spoofing Attacks
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("2") != -1  or questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q16"].find("2") != -1 or questions_and_answers["Q16"].find("4") != -1:
            report.write(open("securityTesting/BOTNETSNIFFINGSPOOFINGPHISHINGTEST.md", "r").read())
            report.write("\n")
            report.write("\n")

    # Malware Spoofing, Watering Hole Attack, Sniffing, etc.
    if questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("3") != -1:
        if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1) :
            if questions_and_answers["Q19"].find("1") != -1 or  questions_and_answers["Q19"].find("2") != -1 or questions_and_answers["Q19"].find("4") != -1 or questions_and_answers["Q19"].find("5") != -1 or questions_and_answers["Q19"].find("6") != -1 or questions_and_answers["Q19"].find("8") != -1 :
                report.write("\n")
                report.write("\n")
                report.write(open("securityTesting/BOTSPOOFINGSNIFFINGTEST.md", "r").read())

    # If the system was development for iOS, Tizen and embedded platforms (Buffer Overflows)
    if questions_and_answers["Q1"].find("2") != -1 or questions_and_answers["Q1"].find("6") != -1 or questions_and_answers["Q1"].find("7") != -1:
        if questions_and_answers["Q10"].find("2") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/BUFFEROVERFLOWTEST.md", "r").read())

    # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
    if questions_and_answers["Q4"].find("1") != -1:
        if questions_and_answers["Q7"].find("1") != -1 or questions_and_answers["Q7"].find("2") != -1 or questions_and_answers["Q7"].find("3") != -1:
            report.write("\n")
            report.write("\n")
            report.write(open("securityTesting/MINSIDERVMMIGRATIONTEST.md", "r").read())
            report.write("\n")
            report.write("\n")
  
    # If the system was development for Android, iOS, Tizen and embedded platforms (Insiders Malicious Attacks)
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("5") != -1 or questions_and_answers["Q1"].find("6") != -1:
        if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q6"].find("1") != -1 or questions_and_answers["Q6"].find("2") != -1 or questions_and_answers["Q6"].find("3") != -1):
            if questions_and_answers["Q20"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("securityTesting/MALWAREINJECTIONSIDECHANNELTEST.md", "r").read())
                report.write("\n")
                report.write("\n")

    # Security Testing against physical Attacks
    if questions_and_answers["Q1"].find("1") != -1 or questions_and_answers["Q1"].find("4") != -1 or questions_and_answers["Q1"].find("5") != -1 or questions_and_answers["Q1"].find("6") != -1:
        if questions_and_answers["Q4"].find("1") != -1 and (questions_and_answers["Q6"].find("1") != -1 or questions_and_answers["Q6"].find("2") != -1 or questions_and_answers["Q6"].find("3") != -1):
            if questions_and_answers["Q20"].find("1") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("securityTesting/physicalAttacksTest.md", "r").read())
                report.write("\n")
                report.write("\n")

    report.close()
    security_test_recommendation_convert_report()
    print("# Processing done! Check your requirements in the TEST_SPECIFICATION.pdf file")

"""
[Summary]: Method responsible for creating, printing and outputting the complete processing report
[Arguments]: No arguments
[Return]: No return
"""    
def fullReport():
    
    get_requirements()
    get_good_practices()
    get_attack_models()
    get_security_test_recommendation()

    pdfs = ['SECURITY_REQUIREMENTS.pdf', 'GOOD_PRACTICES.pdf', 'ATTACKS_MAPPING.pdf', 'TEST_SPECIFICATION.pdf']

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
    print("# Security by Design for Cloud and Mobile Ecosystem (SecD4CLOUDMOBILE) ")
    print("")
    print("  The **SecD4CLOUDMOBILE** is a custom made program.")
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
