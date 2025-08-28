from switch import Switch
import os

class DataHandler:
    version = 1

    # list that contains to answers in the written file
    input_list = []

    # add the answers (output) to a list to write as the respective answers and comments in the generated file with answers
    answers_list = []
    comments_list = []
    table_for_report = []

    # class DataHandler:

    # create a dictionary to store the answers to the questions
    # questions_and_answers as questions_and_answers
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

    def readInputFromFile(self):
        # user inputs the file name and checks if the file exists
        while True:
            filepath = self.validateInput(2)
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
                self.input_list.append(line.split('#')[0].strip())
                line = file.readline()

    """
    [Summary]: Common method to validate input and implemts dynamic arguments
    [Arguments]: 
        - arg(1) what to validate -> if it is to validate a int or a string (1 or 2)
        - arg(2) n_options -> number of options in the question (==range)
    [Returns]: Returns user inputs
    """

    def validateInput(self, *arg):
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

    def arqui(self, version):
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

            if value > 10 or value < 0:
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
                    self.questions_and_answers["Q1"] = self.questions_and_answers["Q1"] + str(value) + ";"

    """
    [Summary]: Method that gets the domain of the mobile application developed or to be developed
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def domain(self, version):
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

            if value > 19 or value <= 0:
                print("Wrong! Enter a whole number between 1 and 19, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                # if value == 0:
                #     return
                # else:
                self.questions_and_answers["Q2"] = str(value)
                return

    """
    [Summary]: Method that allows identifying if the application to be developed or developed uses authentication or not
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def authentication(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                # if value == 0:
                #     return
                # else:
                self.questions_and_answers["Q3"] = str(value)

                if value == 1:
                    self.typeOfAuthentication(version)
                else:
                    self.questions_and_answers["Q4"] = "N/A"
                return

    """
    [Summary]: Method responsible for identifying the authentication scheme to be used or used by the application
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def typeOfAuthentication(self, version):
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

            if value > 4 or value < 0:
                print("Wrong! Enter a whole number between 1 and 4, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                if value == 0:
                    return
                # if value == 5:
                #     print("  Please specify authentication scheme: (name between single quotes)  ")
                #     value2 = validateInput(2)
                #     self.questions_and_answers["Q4"] = self.questions_and_answers["Q4"] + str(value2) + ";"
                else:
                    self.questions_and_answers["Q4"] = self.questions_and_answers["Q4"] + str(value) + ";"

    """
    [Summary]: Method that allows identifying if the application to be developed or developed uses a database or not
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def hasDB(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                # if value == 0:
                #     return
                # else:
                self.questions_and_answers["Q5"] = str(value)

                if value == 1:
                    self.typeOfDatabase(version)
                    if self.questions_and_answers["Q6"] == '1' or self.questions_and_answers["Q6"] == '2':
                        self.whichDatabase(version)
                    self.sensitiveData(version)
                    self.storageLocation(version)
                else:
                    self.questions_and_answers["Q6"] = "N/A"
                    self.questions_and_answers["Q7"] = "N/A"
                    self.questions_and_answers["Q8"] = "N/A"
                return

    """
    [Summary]: Method to identify the type of storage of the end-users of the application
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def typeOfDatabase(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                # if value == 0:
                #     return
                # else:
                self.questions_and_answers["Q6"] = str(value)
                return

    """
    [Summary]: Method allowing the identification of the DBMS to be used by the system
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def whichDatabase(self, version):
        print("")
        print("---")
        print("")
        if version == 1:
            print("  **Which Database (DBMS) will be used ?**  ")
        else:
            print("  **What is the Database (DBMS) used?**  ")

        print("")

        if self.questions_and_answers["Q6"] == '1':
            print("  1 - SQL Server  ")
            print("  2 - MySQL  ")
            print("  3 - PostgreSQL  ")
            print("  4 - SQLite  ")
            print("  5 - OracleDB  ")
            print("  6 - MariaDB  ")

        if self.questions_and_answers["Q6"] == '2':
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

            if value > 13 or value < 1:
                print("Wrong! Enter a whole number between 1 and 14, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                # if value == 14:
                #     print(" Please specify the DBMS name: (name between single quotes)  ")
                #     value2 = validateInput(2)
                #     self.questions_and_answers["Q7"] = str(value2)
                # else:
                #     self.questions_and_answers["Q7"] = str(value)

                # return
                self.questions_and_answers["Q7"] = str(value)

                return

    """
    [Summary]: Method allowing the identification of the type of data handled by the system (personal, confidential or critical)
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def sensitiveData(self, version):
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

            if value > 3 or value < 0:
                print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                if value == 0:
                    return
                # if value == 4:
                #     print("  Please specify the type of information handled: (name between single quotes)  ")
                #     value2 = validateInput(2)
                #     self.questions_and_answers["Q8"] = self.questions_and_answers["Q8"] + str(value2) + ";"
                else:
                    self.questions_and_answers["Q8"] = self.questions_and_answers["Q8"] + str(value) + ";"

    """
    [Summary]: Method allowing the identification of whether or not the application allows users to register
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def storageLocation(self, version):
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

            if value > 3 or value < 1:
                print("Wrong! Enter a whole number between 1 and 3, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                self.questions_and_answers["Q9"] = str(value)
                return

    """
    [Summary]: Method allowing the identification of whether or not the application allows users to register
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def userRegist(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                self.questions_and_answers["Q10"] = str(value)
                if value == 1:
                    self.typeOfUserRegist(version)
                else:
                    self.questions_and_answers["Q11"] = "N/A"

                return

    """
    [Summary]: Method to identify the type of registration of users to the system
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def typeOfUserRegist(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                self.questions_and_answers["Q11"] = str(value)
                return

    """
    [Summary]: Method to identify the programming language to be used or used for coding the application
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def languages(self, version):
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

            if value > 11 or value < 0:
                print("Wrong! Enter a whole number between 1 and 12, according to the menu above!")
                continue
            else:
                # validate a integer (arg[0]==1 and specify the number available options(arg[1]==10))
                if value == 0:
                    return
                # if value == 11:
                #     print("  Please specify the programming language: (name between single quotes)  ")
                #     value2 = validateInput(2)
                #     self.questions_and_answers["Q12"] = self.questions_and_answers["Q12"] + str(value2) + ";"
                else:
                    self.questions_and_answers["Q12"] = self.questions_and_answers["Q12"] + str(value) + ";"

    """
    [Summary]: Method to identify if the application uses or not user input forms
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def inputForms(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q13"] = str(value)
                return

    """
    [Summary]: Method to identify the application allows or not upload files
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def allowUploadFiles(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q14"] = str(value)
                return

    """
    [Summary]: Method to identify the application records or not logs
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def systemLogs(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q15"] = str(value)
                return

    """
    [Summary]: Method to identify the application allows or not regular updates
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def allowUpdateSystem(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q16"] = str(value)
                return

    """
    [Summary]: Method to identify the application uses or not third-party apps
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def allowThirdParty(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q17"] = str(value)
                return

    """
    [Summary]: Method to identify the Cloud development model (environment) used by the application
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def cloudPlatform(self, version):
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

            if value > 5 or value < 1:
                print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q18"] = str(value)
                return

    """
    [Summary]: Method that allows identifying if the user wants to specify some hardware details (network and authentication scheme) or not
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def hardwareSpecs(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q19"] = str(value)

                if value == 1:
                    self.hardwareAuth(version)
                    self.hardwareComunication(version)
                else:
                    self.questions_and_answers["Q20"] = "N/A"
                    self.questions_and_answers["Q21"] = "N/A"
                return

    """
    [Summary]: Method allowing the identification of the authentication paradigm implemented in relation to the hardware
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def hardwareAuth(self, version):
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

            if value > 5 or value < 1:
                print("Wrong! Enter a whole number between 1 and 5, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q20"] = str(value)
                return

    """
    [Summary]: Method allowing the identification of wireless network technologies implemented in relation to hardware
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def hardwareComunication(self, version):
        print("")
        print("---")
        print("")
        if version == 1:
            print("  **What wireless technologies will be on the hardware?**  ")
        else:
            print(
                "  **What are the wireless tecnologies presents in hardware. Enter several options and end with 0.**  ")
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

            if value > 12 or value < 0:
                print("Wrong! Enter a whole number between 1 and 12, according to the menu above!")
                continue
            else:
                if value == 0:
                    return
                # if value == 12:
                #     print("Please specify the wireless technologies: (name between single quotes)")
                #     value2 = validateInput(2)
                #     self.questions_and_answers["Q21"] = self.questions_and_answers["Q21"] + str(value2) + ";"
                else:
                    self.questions_and_answers["Q21"] = self.questions_and_answers["Q21"] + str(value) + ";"

    """
    [Summary]: Method to identify the existence or not of the possibility of physical access to the system (data centre and mobile device)
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def dataCenterAcess(self, version):
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

            if value > 2 or value < 1:
                print("Wrong! Enter a whole number between 1 and 2, according to the menu above!")
                continue
            else:
                self.questions_and_answers["Q22"] = str(value)
                return

    """
    [Summary]: Method to open/create and store in the file 'ans.txt' the answers to the user questionnaire
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def print_data(self):
        generate_file = open("ans.txt", "w")

        list_aux = []
        # it is a multiple question

        # find if the answer correspond to option "others" (means that is user input text) OR fix this buy make it simple, verify if it the answer has only letters xD
        # find if the first caracter is a letter and if the answer has no more options
        if self.questions_and_answers["Q1"][0].isdigit() == False and self.questions_and_answers["Q1"].find(";") == -1:
            list_aux.append(self.questions_and_answers["Q1"])

        else:

            # variable aux is a list that contains the answers chosen by the user to the question in cause
            # cut the string in the delimitator ";"
            aux = self.questions_and_answers["Q1"].split(";")

            # delete last item (= None)
            aux = aux[:-1]
            # print(aux)

            # iterate the answers chosen by the user
            for item in aux:

                # iterate the options of the question and check what the chosen answers match
                for option in self.question1:
                    if item == option:
                        list_aux.append(self.question1[option])

                # case of user input text
                if item.isdigit() == False:
                    list_aux.append(item)

        # print(list_aux)
        print("{:22} {:3} {:40} ".format("Mobile Platform", ":", ' ; '.join(list_aux)))
        self.table_for_report.append(["Mobile Platform", ' ; '.join(list_aux)])

        self.answers_list.append(self.questions_and_answers["Q1"])
        self.comments_list.append(' ; '.join(list_aux))

        for n in self.question2:
            item = self.questions_and_answers["Q2"]
            if item == n:
                print("{:22} {:3} {:40}".format("Application domain type", ":", self.question2[n]))

                self.table_for_report.append(["Application domain type", self.question2[n]])

                self.answers_list.append(self.questions_and_answers["Q2"])
                self.comments_list.append(self.question2[n])

        for n in self.question3:
            item = self.questions_and_answers["Q3"]
            if item == n:
                print("{:22} {:3} {:40}".format("Authentication", ":", self.question3[n]))

                self.table_for_report.append(["Authentication", self.question3[n]])

                self.answers_list.append(self.questions_and_answers["Q3"])
                self.comments_list.append(self.question3[n])

        list_aux = []
        # it is a multiple question
        # find if the answer correspond to option "others" (means that is user input text) or not answered
        if self.questions_and_answers["Q4"][0].isdigit() == False and self.questions_and_answers["Q4"].find(";") == -1:
            list_aux.append(self.questions_and_answers["Q4"])
        else:
            # variable aux is a list that contains the answers chosen by the user to the question in cause
            # cut the string in the delimitator ";"
            aux = self.questions_and_answers["Q4"].split(";")

            # delete last item (= None)
            aux = aux[:-1]

            for item in aux:
                for option in self.question4:
                    if item == option:
                        list_aux.append(self.question4[option])

                # case of user input text
                if item.isdigit() == False:
                    list_aux.append(item)

        print("{:22} {:3} {:40} ".format("Authentication schemes", ":", ' ; '.join(list_aux)))

        self.table_for_report.append(["Authentication schemes", ' ; '.join(list_aux)])

        self.answers_list.append(self.questions_and_answers["Q4"])
        self.comments_list.append(' ; '.join(list_aux))

        for n in self.question5:
            item = self.questions_and_answers["Q5"]
            if item == n:
                print("{:22} {:3} {:40} ".format("Has DB", ":", self.question5[n]))

                self.table_for_report.append(["Has DB", self.question5[n]])

                self.answers_list.append(self.questions_and_answers["Q5"])
                self.comments_list.append(self.question5[n])

        item = self.questions_and_answers["Q6"]
        # case this question is not answered, and the answer it will be "N/A"
        if self.questions_and_answers["Q6"].isdigit() == False:
            print("{:22} {:3} {:40} ".format("Type of database", ":", item))

            self.table_for_report.append(["Type of database", item])

            self.answers_list.append(self.questions_and_answers["Q6"])
            self.comments_list.append(item)

        else:
            for n in self.question6:
                if item == n:
                    print("{:22} {:3} {:40} ".format("Type of database", ":", self.question6[n]))

                    self.table_for_report.append(["Type of database", self.question6[n]])

                    self.answers_list.append(self.questions_and_answers["Q6"])
                    self.comments_list.append(self.question6[n])

        item = self.questions_and_answers["Q7"]
        for n in self.question7:
            if item == n:
                print("{:22} {:3} {:40} ".format("Which DB", ":", self.question7[n]))

                self.table_for_report.append(["Which DB", self.question7[n]])

                self.answers_list.append(self.questions_and_answers["Q7"])
                self.comments_list.append(self.question7[n])

        # case of user input text
        if item.isdigit() == False:
            print("{:22} {:3} {:40} ".format("Which DB", ":", item))

            self.table_for_report.append(["Which DB", item])

            self.answers_list.append(self.questions_and_answers["Q7"])
            self.comments_list.append(item)

        list_aux = []
        # it is a multiple question

        # find if the answer correspond to option "others" (means that is user input text) or not answered
        if self.questions_and_answers["Q8"][0].isdigit() == False and self.questions_and_answers["Q8"].find(";") == -1:
            list_aux.append(self.questions_and_answers["Q8"])
        else:

            # variable aux is a list that contains the answers chosen by the user to the question in cause
            # cut the string in the delimitator ";"
            aux = self.questions_and_answers["Q8"].split(";")

            # delete last item (= None)
            aux = aux[:-1]

            for item in aux:
                for option in self.question8:
                    if item == option:
                        list_aux.append(self.question8[option])
                # case of user input text
                if item.isdigit() == False:
                    list_aux.append(item)

        print("{:22} {:3} {:40} ".format("Type of information handled", ":", ' ; '.join(list_aux)))

        self.table_for_report.append(["Type of information handled", ' ; '.join(list_aux)])

        self.answers_list.append(self.questions_and_answers["Q8"])
        self.comments_list.append(' ; '.join(list_aux))

        item = self.questions_and_answers["Q9"]
        # case this question is not answered, and the answer it will be "N/A"
        if self.questions_and_answers["Q9"].isdigit() == False:
            print("{:22} {:3} {:40} ".format("Storage Location", ":", item))

            self.table_for_report.append(["Storage Location", item])

            self.answers_list.append(self.questions_and_answers["Q9"])
            self.comments_list.append(item)

        else:
            for n in self.question9:
                if item == n:
                    print("{:22} {:3} {:40} ".format("Storage Location", ":", self.question9[n]))

                    self.table_for_report.append(["Storage Location", self.question9[n]])

                    self.answers_list.append(self.questions_and_answers["Q9"])
                    self.comments_list.append(self.question9[n])

        for n in self.question10:
            item = self.questions_and_answers["Q10"]
            if item == n:
                print("{:22} {:3} {:40}".format("User Registration", ":", self.question10[n]))

                self.table_for_report.append(["User Registration", self.question10[n]])

                self.answers_list.append(self.questions_and_answers["Q10"])
                self.comments_list.append(self.question10[n])

        item = self.questions_and_answers["Q11"]
        if self.questions_and_answers["Q11"].isdigit() == False:
            print("{:22} {:3} {:40} ".format("Type of Registration", ": ", item))

            self.table_for_report.append(["Type of Registration", item])

            self.answers_list.append(self.questions_and_answers["Q11"])
            self.comments_list.append(item)
        else:
            for n in self.question11:
                if item == n:
                    print("{:22} {:3} {:40} ".format("Type of Registration", ": ", self.question11[n]))

                    self.table_for_report.append(["Type of Registration", self.question11[n]])

                    self.answers_list.append(self.questions_and_answers["Q11"])
                    self.comments_list.append(self.question11[n])

        list_aux = []
        # it is a multiple question

        # find if the answer correspond to option "others" (means that is only user input text)
        if self.questions_and_answers["Q12"][0].isdigit() == False and self.questions_and_answers["Q12"].find(";") == -1:
            list_aux.append(self.questions_and_answers["Q12"])
        else:

            # cut the string in the delimitator ";"
            aux = self.questions_and_answers["Q12"].split(";")

            # delete last item (= None)
            aux = aux[:-1]

            for item in aux:
                for option in self.question12:
                    if item == option:
                        list_aux.append(self.question12[option])

                # case of user input text
                if item.isdigit() == False:
                    list_aux.append(item)

        print("{:22} {:3} {:40} ".format("Programming Languages", ":", ' ; '.join(list_aux)))

        self.table_for_report.append(["Programming Languages", ' ; '.join(list_aux)])

        self.answers_list.append(self.questions_and_answers["Q12"])
        self.comments_list.append(' ; '.join(list_aux))

        for n in self.question13:
            item = self.questions_and_answers["Q13"]
            if item == n:
                print("{:22} {:3} {:40} ".format("Input Forms", ":", self.question13[n]))

                self.table_for_report.append(["Input Forms", self.question13[n]])

                self.answers_list.append(self.questions_and_answers["Q13"])
                self.comments_list.append(self.question13[n])

        for n in self.question14:
            item = self.questions_and_answers["Q14"]
            if item == n:
                print("{:22} {:3} {:40} ".format("Upload Files", ":", self.question14[n]))

                self.table_for_report.append(["Upload Files", self.question14[n]])

                self.answers_list.append(self.questions_and_answers["Q14"])
                self.comments_list.append(self.question14[n])

        for n in self.question15:
            item = self.questions_and_answers["Q15"]
            if item == n:
                print("{:22} {:3} {:40} ".format("The system has logs", ":", self.question15[n]))

                self.table_for_report.append(["The system has logs", self.question15[n]])

                self.answers_list.append(self.questions_and_answers["Q15"])
                self.comments_list.append(self.question15[n])

        for n in self.question16:
            item = self.questions_and_answers["Q16"]
            if item == n:
                print("{:22} {:3} {:40} ".format("The system has regular updates", ":", self.question16[n]))

                self.table_for_report.append(["The system has regular updates", self.question16[n]])

                self.answers_list.append(self.questions_and_answers["Q16"])
                self.comments_list.append(self.question16[n])

        for n in self.question17:
            item = self.questions_and_answers["Q17"]
            if item == n:
                print("{:22} {:3} {:40} ".format("The system has third-party", ":", self.question17[n]))

                self.table_for_report.append(["The system has third-party", self.question17[n]])

                self.answers_list.append(self.questions_and_answers["Q17"])
                self.comments_list.append(self.question17[n])

        for n in self.question18:
            item = self.questions_and_answers["Q18"]
            if item == n:
                print("{:22} {:3} {:40}".format("System Cloud Environments", ":", self.question18[n]))

                self.table_for_report.append(["System Cloud Environments", self.question18[n]])

                self.answers_list.append(self.questions_and_answers["Q18"])
                self.comments_list.append(self.question18[n])

        for n in self.question19:
            item = self.questions_and_answers["Q19"]
            if item == n:
                print("{:22} {:3} {:40} ".format("Hardware Specification", ":", self.question19[n]))

                self.table_for_report.append(["Hardware Specification", self.question19[n]])

                self.answers_list.append(self.questions_and_answers["Q19"])
                self.comments_list.append(self.question19[n])

        for n in self.question20:
            item = self.questions_and_answers["Q20"]
            if item == n:
                print("{:22} {:3} {:40} ".format("HW Authentication", ":", self.question20[n]))

                self.table_for_report.append(["HW Authentication", self.question20[n]])

                self.answers_list.append(self.questions_and_answers["Q20"])
                self.comments_list.append(self.question20[n])

        list_aux = []
        # it is a multiple question

        # find if the answer correspond to option "others" (means that is only user input text)
        if self.questions_and_answers["Q21"][0].isdigit() == False and self.questions_and_answers["Q21"].find(";") == -1:
            list_aux.append(self.questions_and_answers["Q21"])
        else:
            # cut the string in the delimitator ";"
            aux = self.questions_and_answers["Q21"].split(";")

            # delete last item (= None)
            aux = aux[:-1]

            for item in aux:
                for option in self.question21:
                    if item == option:
                        list_aux.append(self.question21[option])
                # case of user input text
                if item.isdigit() == False:
                    list_aux.append(item)

        print("{:22} {:3} {:40} ".format("HW Wireless Tech", ":", ' ; '.join(list_aux)))

        self.table_for_report.append(["HW Wireless Tech", ' ; '.join(list_aux)])

        self.answers_list.append(self.questions_and_answers["Q21"])
        self.comments_list.append(' ; '.join(list_aux))

        for n in self.question22:
            item = self.questions_and_answers["Q22"]
            if item == n:
                print("{:22} {:3} {:40} ".format("Device or Data Center Physical Access", ":", self.question22[n]))

                self.table_for_report.append(["Device or Data Center Physical Access", self.question22[n]])

                self.answers_list.append(self.questions_and_answers["Q22"])
                self.comments_list.append(self.question22[n])

        # write / generate a file with all answers
        for i in range(0, len(self.answers_list)):
            generate_file.write("{:20}{:3}{:20}\n".format(self.answers_list[i], " # ", self.comments_list[i]))

        generate_file.close()

    """
    [Summary]: Method auxiliary to the input method responsible for processing user requests
    [Arguments]: No arguments
    [Returns]: No return
    """

    def answerQuestionnaire(self):
        # answer the questions by hand
        self.arqui(self.version)
        self.domain(self.version)
        self.authentication(self.version)
        self.hasDB(self.version)
        self.userRegist(self.version)
        self.languages(self.version)
        self.inputForms(self.version)
        self.allowUploadFiles(self.version)
        self.systemLogs(self.version)
        self.allowUpdateSystem(self.version)
        self.allowThirdParty(self.version)
        self.cloudPlatform(self.version)
        self.hardwareSpecs(self.version)
        self.dataCenterAcess(self.version)

        print("**The questionnaire is over!**\n\n")
        self.print_data()
        #information_capture()
    def openFile(self):
        # answers already written in the input file
        print("---")
        print("")
        print("  **What is the name of the input file (ans.txt)?**  ")
        print("")
        self.readInputFromFile()

        self.questions_and_answers["Q1"] = self.input_list[0]
        self.questions_and_answers["Q2"] = self.input_list[1]
        self.questions_and_answers["Q3"] = self.input_list[2]
        self.questions_and_answers["Q4"] = self.input_list[3]
        self.questions_and_answers["Q5"] = self.input_list[4]
        self.questions_and_answers["Q6"] = self.input_list[5]
        self.questions_and_answers["Q7"] = self.input_list[6]
        self.questions_and_answers["Q8"] = self.input_list[7]
        self.questions_and_answers["Q9"] = self.input_list[8]
        self.questions_and_answers["Q10"] = self.input_list[9]
        self.questions_and_answers["Q11"] = self.input_list[10]
        self.questions_and_answers["Q12"] = self.input_list[11]
        self.questions_and_answers["Q13"] = self.input_list[12]
        self.questions_and_answers["Q14"] = self.input_list[13]
        self.questions_and_answers["Q15"] = self.input_list[14]
        self.questions_and_answers["Q16"] = self.input_list[15]
        self.questions_and_answers["Q17"] = self.input_list[16]
        self.questions_and_answers["Q18"] = self.input_list[17]
        self.questions_and_answers["Q19"] = self.input_list[18]
        self.questions_and_answers["Q20"] = self.input_list[19]
        self.questions_and_answers["Q21"] = self.input_list[20]
        self.questions_and_answers["Q22"] = self.input_list[21]

        # information_capture()

        print("# Processing Done! Choose another option to process the requests!")
            #                     else:
            #                       #  information_capture()
            #
            #         if case(2):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print("\t\t The request for security requirements is in progress ... \n\n")
            #             get_requirements()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/SECURITY_REQUIREMENTS.pdf')
            #             information_capture()
            #
            #         if case(3):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print("\t\t The request for best practice guidelines is in progress ... \n\n")
            #             get_security_best_practices()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/GOOD_PRACTICES.pdf')
            #             information_capture()
            #
            #         if case(4):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print("\t\t The request for security mechanisms is in progress ... \n\n")
            #             get_mechanisms()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/SECURITY_MECHANISMS.pdf')
            #             information_capture()
            #
            #         if case(5):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print("\t\t The request for attack models is in progress ... \n\n")
            #             get_attack_models()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/ATTACKS_MAPPING.pdf')
            #             information_capture()
            #
            #         if case(6):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print(
            #                 "\t\t The request for the security testing specification and tools is in progress ... \n\n")
            #             get_security_test_recommendation()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/TEST_SPECIFICATION.pdf')
            #             information_capture()
            #
            #         if case(7):
            #             print(
            #                 "\n********************************************************************************************\n")
            #             print("\t\t The full report request is in progress ... \n\n")
            #             fullReport()
            #             # webbrowser.open_new(r'file:///Users/FranciscoChimuco/SecD4CLOUDMOBILEv1.3/FULL_REPORT.pdf')
            #             information_capture()
            #
            #         if case(8):
            #             print("\n\n*** Application finished successfully! ***\n\n")
            #             exit(0)
            #
            #         if case.default:
            #             print("\nError! Insert a valid value between 1 and 8!\n")
            #
            #break