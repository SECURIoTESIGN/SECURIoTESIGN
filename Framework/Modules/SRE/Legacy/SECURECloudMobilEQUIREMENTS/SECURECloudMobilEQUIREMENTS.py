#coding=utf-8
import os

confidentiality = 0
integrity = 0
availability = 0
authentication = 0
identiAuthentication = 0
authorization = 0
nonRepudiation = 0
accountability = 0
reliability = 0
privacy = 0
physicalSecurity = 0
forgeryResistance = 0
tamperDetection = 0
dataFreshness = 0
confinement = 0
interoperability = 0
dataOrigin = 0

print ("#   SECURECloudMobilEQUIREMENTS\n"
        "    The  **SECURECloudMobilEQUIREMENTS** is a custom made program. It helps in the creation of cloud and mobile tools apps security\n"
        "    by providing the security requirements before the creation of the tool It is part of the outputs of\n"
        "    project ystematization of the Safety Engineering Process in the Cloud and Mobile Ecosystem. \n"
        "##  License\n "
        "    Developed by Francisco Chimuco and Pedro R. M. Inácio Department of Computer Science Universidade da Beira\n"
        "    Interior Copyright 2019 Francisco and Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0\n")

while True :

        print("#  Do you wish to run a older test? \n")
        print("   1 - Yes \n")
        print("   2 - No\n")
        print("   Answer\n")
        q0 = input()
        print ("\n")
        if (q0 < '3'and q0!='') :
                break


if (q0 =='1') :

    answerlist=[]

    while True:
        print ("#  Insert the name of the file\n")
        filename = input()

        if(os.path.exists(filename)):
            break
    with open(filename) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            x = line.split("\n")
            answerlist.append(x[0])
    fp.close()

    q1 = answerlist[0]
    q2 = answerlist[1]
    q3 = answerlist[2]
    q4 = answerlist[3]
    q4_1 = answerlist[4]
    q4_2 = answerlist[5]
    q4_3 = answerlist[6]
    q5 = answerlist[7]
    q5_1 = answerlist[8]
    q6 = answerlist[9]
    q7 = answerlist[10]
    q8 = answerlist[11]
    q9 = answerlist[12]
    q10 = answerlist[13]
    q11 = answerlist[14]
    q12 = answerlist[15]
    q13 =answerlist[16]
    q14 =answerlist[17]
    q15 =answerlist[18]

    # Questions
# Q1   -> Architeture
# Q2   -> Application Domain Type
# Q3   -> Authentication
# Q4   -> Has a DB
# Q5   -> Location Data Storage
# Q6   -> Type of data storage
# Q7   -> Which db
# Q8   -> Type of data
# Q9   -> User Registration
# Q10  -> Way of user registration
# Q11  -> Client Programming Languages
# Q12  -> Server Programming Languages
# Q13  -> Input Forms
# Q14  -> Upload Files
# Q15  -> Logs
# Q16  -> System Regular Updates
# Q17  -> Third-part Software
# Q18  -> System Cloud Environment
# Q19  -> Device Phisical Access
# Q20  -> Data Center Phisical Access



else:

        while True:
            print("Question 1 \n")
            print("## Which will be the archicteture of the system? \n")
            print("  1 - Android Application \n")
            print("  2 - iOS Application \n")
            print("  3 - Hybrid Application \n")
            print("  4 - Sailfish OS Application \n")
            print("  5 - Tizen Application\n")
            print("  6 - Ubuntu Touch Application \n")
            print("  7 - Web Application \n")
            print(" Answer: \n")
            
            aux = input()
            q1 = int(aux)
            print ("\n")
            if (q1<8 and q1>0):
                    break
             
        while True:
            print("#  Question 2 \n")
            print("## State the domain type for your Cloud and Mobile system: \n")
            print("   1 - Game \n")
            print("   2 - m-Commerce \n")
            print("   3 - m-Health \n")
            print("   4 - m-Learning \n")
            print("   5 - m-Payment \n")
            print("   6 - m-Social Networking \n")
            print("   7 - m-Tourism \n")
            print("   8 - Multi-user Collaboration \n")
            print("   9 - Entertainment \n")
            print("  10 - Smart Agriculture \n")
            print("  11 - Smart Air Quality \n")
            print("  12 - Smart Healthcare \n")
            print("  13 - Smart Home \n")
            print("  14 - Smart Manufacturing \n")
            print("  15 - Smart Transportation \n")
            print("  16 - Smart Waste Monitoring \n")
            print("  17 - Smart Wearables \n")
            print("  Answer: \n")
            aux = input()
            q2 = int(aux)
            print ("\n")
            if (q2 < 18 and q2 >0):
                    break

        while True:
            print("#   Question 3 \n")
            print("##  Which type of authentication will be implemented? \n")
            print(" 1 - No Authentication \n")
            print(" 2 - Username and Password \n")
            print(" 3 - Social Networks/Google \n")
            print(" 4 - Biometrics \n")
            print(" 5 - Two Factor Authentication \n")
            print(" 6 - Mult Factor Authentication \n")
            print("Answer: \n")
            
            aux = input()
            q3 = int(aux)
            print ("\n")
            if (q3 < 7 and q3 > 0):
                break   

        while True:
            print ("#  Question 4 \n")
            print ("## Will the system use a database? \n")
            print ("   1 - Yes \n")
            print ("   2 - No \n")
            print ("   Answer: \n")

            aux = input()
            q4 = int(aux)
            print("\n")
            if (q4 < 3 and q4 > 0):
                break

        q4_3 =-1
        q4_2 = -1
        q4_1 = -1
        if (q4 == 1):
            while True:
                print ("##  Question 4.1 \n")
                print ("### Where the system will store the data? \n")
                print ("    1 - Local Database (Device) \n")
                print ("    2 - Remote Database  \n")
                print ("    3 - Both \n")
                print ("   Answer:  \n")

                aux = input()
                q4_1 = int(aux)
                print ("\n")
                if (q4_1 < 4 and q4_1 > 0):
                    break

            while True:
                print ("##  Question 4.2 \n")
                print ("### What is the type of database? \n")
                print(" 1 - SQL \n")
                print(" 2 - NoSQL \n")
                print(" Answer: \n")

                aux = input()
                q4_2 = int(aux)
                print ("\n")

                if (q4_2 < 3 and q4_2 > 0):
                    break
            while True:
                print ("##  Question 4.3 \n")
                print ("### Which type of data will be stored? \n")
                print(" 1 - Personal Information (Names, Address,...) \n")
                print(" 2 - Confidential Data \n")
                print(" 3 - Critical Data \n")
                print(" 4 - Personal Information & Confidential Data \n")
                print(" 5 - Personal Information & Critical Data \n")
                print(" 6 - All \n")
                print(" Answer: \n")
                
                aux = input()
                q4_3 = int(aux)
                print("\n")
                    
                if (q4_3 < 7 and q4_3 > 0):
                    break

        while True:
            print ("#  Question 5 \n")
            print ("## There will be a user registration? \n")
            print ("   1 - Yes \n")
            print ("   2 - No \n")
            print ("   Answer: \n")

            aux = input()
            q5 = int(aux)
            print ("\n")

            if (q5 < 3 and q5 > 0):
                break

        q5_1=-1
        if (q5 == 1):
            while True:
                print (" Question 5.1 \n")
                print ("  Which way of user registration will be used? \n")
                print ("  1 - The users will register themselves \n")
                print ("  2 - Will be an administrator that will register the users \n")
                print ("  Answer: \n")
                        
                aux = input()
                q5_1=int(aux)
                print ("\n")
                if (q5_1 < 3 and q5_1 > 0):
                    break

        while True:
            print(" Question 6 \n")
            print("## What programming language will be used in the implementation of the system?")
            print("  1 - C# ")
            print("  2 - C/C++ ")
            print("  3 - HTML5 + CSS + JavaScript ")
            print("  4 - Java (Android) ")
            print("  5 - Objective C ")
            print("  6 - Perl ")
            print("  7 - Ruby ")
            print("  8 - Swift ")
            print("  9 - Kotlin ")
            print(" 10 - Python ")
            print(" 11 - None ")
            print("  Answer: \n")
                    
            aux = input()
            q6=int(aux)
            if (q6 <= 11 and q6 > 0):
                break
            
        
        while True:
            print(" Question 7 \n")
            print("## What programming language will be used in the implementation of the server-side system?")
            print(" 1 - C# ")
            print(" 2 - PHP ")
            print(" 3 - Python ")
            print(" 4 - HTML ")
            print(" 5 - None ")
            print(" Answer: \n")
                    
            aux = input()
            q7=int(aux)
            if (q7 <= 5 and q7 > 0):
                break

        while True:
            print(" Question 8 \n")
            print("## The system will allow user input forms? \n")
            print(" 1 - Yes ")
            print(" 2 - No ")
            print(" Answer: \n")
                
            aux = input()
            q8=int(aux)
            if (q8 < 3 and q8 > 0):
                break
            
        while True:
            print(" Question 9 \n")
            print("## The system will allow upload files? \n")
            print(" 1 - Yes ")
            print(" 2 - No ")
            print(" Answer: \n")
                
            aux = input()
            q9=int(aux)
            if (q9 < 3 and q9 >0):
                break
            
        while True:
            print(" Question 10 \n")
            print("## The system will have a regist of logs? \n")
            print(" 1 - Yes ")
            print(" 2 - No ")
            print(" Answer: \n ")
                
            aux = input()
            q10=int(aux)
            if (q10 < 3 and q10 > 0):
                break

        while True:
            print ("# Question 11 \n")
            print ("## Will the system receive regular updates? \n")
            print (" 1 - Yes \n")
            print (" 2 - No \n")
            print (" Answer: \n")

            aux = input()
            q11 = int(aux)
            print ("\n")

            if (q11 < 3 and q11 > 0):
                break

        while True:
            print ("#  Question 12 \n")
            print ("## Will the system work with third-party software? \n")
            print ("   1 - Yes \n")
            print ("   2 - No \n")
            print ("   Answer: \n")

            aux = input()
            q12 = int(aux)
            print ("\n")

            if (q12 < 3 and q12 > 0):
                break
        
        while True:
            print("# Question 13 \n ")
            print("## In what environment will the system be used? \n")
            print(" 1 - Community Cloud (Remote connection) \n")
            print(" 2 - Public Cloud (Remote connection) \n")
            print(" 3 - Private Cloud (Local connection) \n")
            print(" 4 - Hybrid Cloud (Mix Connection) \n")
            print(" 5 - Virtual Private Cloud \n")
            print(" Answer: \n")
            
            aux = input()
            q13 = int(aux)
            print("\n")
            
            if (q13 < 6 and q13 > 0):
                break
        
        while True:
            print("#  Question 14 \n")
            print("## Can someone with bad intentions gain physical access to the location where       \n"
                    "  this software will be running and obtain private information?                   \n")
            print("   1 - Yes \n")
            print("   2 - No \n")
            print("   Answer: \n")

            aux = input()
            q14 = int(aux)

            if (q14 < 3 and q14 > 0):
                break

        while True:
            print("#  Question 15 \n")
            print("## Can someone gain physical access to the machine where the system operates        \n"
                "   or some of the system components and preform some type of modification to        \n"
                "   it's hardware?                                                                   \n")
            print("   1 - Yes \n")
            print("   2 - No \n")
            print("   Answer: \n")

            aux = input()
            q15 = int(aux)

            if (q15 < 3 and q15 > 0):
                    break
    
        while True:
            print ("#  Do you wish a detailed report? \n")
            print ("   1 - Yes\n")
            print ("   2 - No\n")
            print ("   Answer: \n")

            aux = input()
            verbose = int(aux)
            if (verbose < 3 and verbose > 0):
                break

        while True:
            print ("#  Do you wish to save this test? \n")
            print ("   1 - Yes \n")
            print ("   2 - No \n")
            print ("   Answer: \n")

            aux = input()
            qsave= int(aux)

            if(qsave < 3 and qsave > 0):
                break

        if (qsave == 1):
            while True:
                print ("#  Insert the name of the test:\n")
                testname = input()
                if (testname != ''):
                    break

            fsave= open(testname,"w")
            if (q1 == 8):
                fsave.write("\n"+str(q1)+"\n"+str(q2)+"\n"+str(3)+str(q4)+"\n"+str(q4_1)+"\n"+str(q4_2)+"\n"+str(q4_3)+"\n"+"\n"+str(q5)+"\n"+str(q5_1)+"\n"+"\n"+str(q7)+"\n"+str(q8)+"\n"+str(q9)+"\n"+str(q10)+"\n"+str(11)+"\n"+str(q12)+"\n"+str(q13)+"\n"+str(q14)+"\n"+str(q15))
            else:
                fsave.write("\n"+str(q1)+"\n"+str(q2)+"\n"+str(3)+str(q4)+"\n"+str(q4_1)+"\n"+str(q4_2)+"\n"+str(q4_3)+"\n"+"\n"+str(q5)+"\n"+str(q5_1)+"\n"+str(q6)+"\n"+str(q7)+"\n"+str(q8)+"\n"+str(q9)+"\n"+str(q10)+"\n"+str(11)+"\n"+str(q12)+"\n"+str(q13)+"\n"+str(q14)+"\n"+str(q15))
            fsave.close()

if q1 == 1:
    confidentiality = 1
    privacy = 1
    integrity = 1
    accountability = 1
    authentication = 1
    authorization = 1

if q1 == 2:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    integrity = 1
    accountability = 1

if q1 == 3:
    authentication = 1
    authorization = 1
    confidentiality = 1
    integrity = 1
    availability = 1
    reliability = 1
    accountability = 1
    
if q1 == 4:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1

if q1 == 5:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1

if q1 == 6:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1

if q1 == 7:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1

if q2 == 1:
    confidentiality = 1
    availability = 1
    integrity = 1
    
if q2 == 2:
    confidentiality = 1
    integrity = 1
    availability = 1
    privacy = 1
    reliability = 1
    authentication = 1
    nonRepudiation = 1
    accountability = 1
    nonRepudiation = 1
    authorization = 1
    interoperability = 1
    forgeryResistance = 1

if q2 == 3:
    confidentiality = 1
    integrity = 1
    availability = 1
    privacy = 1
    reliability = 1
    authentication = 1
    nonRepudiation = 1
    accountability = 1
    nonRepudiation = 1
    authorization = 1
    interoperability = 1
    forgeryResistance = 1

if q2 == 4:
    confidentiality =1
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1
    reliability = 1
    accountability = 1
    authorization = 1
    interoperability = 1
    privacy = 1

if q2 == 5:
    confidentiality = 1
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1
    reliability = 1
    accountability = 1
    authorization = 1
    interoperability = 1
    privacy=1

if q2 == 6:
    confidentiality = 1
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1
    reliability = 1
    accountability = 1
    authorization = 1
    interoperability = 1
    privacy=1

if q2 == 7:
    confidentiality = 1
    integrity = 1
    availability = 1

if q2 == 8:
    onfidentiality = 1
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    authentication = 1
    reliability = 1
    accountability = 1
    authorization = 1
    privacy=1

if q2 == 9:
    confidentiality = 1
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1
    reliability = 1
    accountability = 1
    authorization = 1
    interoperability = 1
    privacy=1

if q2 == 10:
    confidentiality = 1
    privacy = 1
    integrity = 1
    accountability = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    physicalSecurity = 1

if q2 == 11:
    authentication = 1
    authorization = 1
    confidentiality = 1
    integrity = 1
    availability = 1
    reliability = 1
    nonRepudiation = 1
    accountability = 1
    physicalSecurity = 1

if q2 == 12:
    confidentiality = 1
    integrity = 1
    availability = 1
    authentication = 1
    authorization = 1
    nonRepudiation = 1
    accountability = 1
    reliability = 1
    privacy = 1
    physicalSecurity = 1

if q2 == 13:
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1
    physicalSecurity = 1

if q3 == 1:
    privacy = 0
    confidentiality = 0

if q3 == 2:
    confidentiality = 0
    integrity = 0
    authentication = 1
    authorization = 0
    privacy = 0

if q3 == 3:
    confidentiality = 0
    integrity = 0
    authentication = 1
    privacy = 0

if q3 == 4:
    confidentiality = 1
    integrity = 1
    authentication = 1
    privacy = 1

if q3 == 5:
    confidentiality = 1
    integrity = 1
    authentication = 1
    privacy = 1

if q3 == 6:
    confidentiality = 1
    integrity = 1
    authentication = 1
    privacy = 1

if q3 == 7:
    confidentiality = 1
    integrity = 1
    authentication = 1
    privacy = 1
    nonRepudiation = 1
    reliability = 1
    authorization = 1
    forgeryResistance = 1
    dataOrigin = 1

if q4 == 1:
    physicalSecurity = 1
    integrity = 1
    availability = 1
    forgeryResistance = 1
    authentication = 1
    nonRepudiation = 1

if q4_1 == 1:
    confidentiality = 1
    integrity = 1
    availability = 1
    authentication = 1
    authorization = 1
    dataOrigin = 1
    dataFreshness = 1
    privacy = 1
    forgeryResistance = 1
    physicalSecurity = 1

if q4_1 == 2:
    confidentiality = 1
    integrity = 1
    availability = 1
    authentication = 1
    dataOrigin = 1
    dataFreshness = 1
    physicalSecurity = 1
    authorization = 1

if q4_1 == 3:
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    physicalSecurity = 1
    integrity = 1
    authentication = 1
    nonRepudiation = 1
    authorization = 1

if q4_2 == 1:
    authentication = 1
    forgeryResistance = 1
    tamperDetection = 1
    authorization = 1

if q4_2 == 2:
    authentication = 1
    forgeryResistance = 1
    tamperDetection = 1
    authorization = 1

if q4_3 == 1:
    confidentiality = 1
    privacy = 1
    physicalSecurity = 1
    authentication = 1

if q4_3 == 2:
    privacy = 1
    confidentiality = 1
    physicalSecurity = 1
    authorization = 1
    forgeryResistance = 1
    authentication = 1

if q4_3 == 3:
    privacy = 1
    confidentiality = 1
    physicalSecurity = 1
    authorization = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1
if (q4_3 == 6):
    confidentiality = 1
    integrity = 1
    availability = 1
    authentication = 1
    authorization = 1
    nonRepudiation = 1
    accountability = 1
    reliability = 1
    privacy = 1
    physicalSecurity = 1
    forgeryResistance = 1
    tamperDetection = 1
    dataFreshness = 1
    confinement = 1
    interoperability = 1
    dataOrigin = 1

if q5 == 1:
    authentication = 1
    nonRepudiation = 1
if q5_1 == 1:
    authentication = 1
    nonRepudiation = 1
if q5_1 == 2:
    authentication = 1
    nonRepudiation = 0
    privacy = 0

if q6 == 1:
    confidentiality = 1
    integrity = 1
    privacy = 1
    authentication = 1
    authorization = 1

if q6 == 2 or q6 == 5:
    confidentiality = 0
    integrity = 0
    privacy = 0
    authentication = 0
    authorization = 0

if q6 == 3:
    confidentiality = 1
    integrity = 1
    privacy = 1
    authorization = 1
    authorization = 1

if q6 == 4:
    confidentiality = 1
    integrity = 1
    privacy = 1
    authentication = 1
    authorization = 1

if q6 == 9 or q6 == 10:
    confidentiality = 1
    integrity = 1
    privacy = 1
    authentication = 1
    authorization = 1

if q9 == 1:
    authorization = 1
    confinement = 1
    dataOrigin = 1

if q10 == 1:
    privacy = 1
    confidentiality = 1
    reliability = 1
    integrity = 1
    authentication = 1
    authorization = 1
    nonRepudiation = 1

if q11 == 1:
    authentication = 1
    interoperability = 1
    confinement = 1
    tamperDetection = 1

if q12 == 1:
    confinement = 1
    interoperability = 1

if q13 == 1:
    privacy = 1
    integrity = 1
    identiAuthentication = 1
    authorization = 1
    availability = 1
    confidentiality = 1
    nonRepudiation = 1

if q13 == 2:
    privacy = 1
    integrity = 1
    identiAuthentication = 1
    authorization = 1
    availability = 1
    confidentiality = 1
    nonRepudiation = 1

if (q13 == 3):
    privacy = 1
    integrity = 1
    identiAuthentication = 1
    authorization = 1
    availability = 0
    confidentiality = 1
    nonRepudiation = 1

if (q13 == 4):
    privacy = 0
    integrity = 1
    identiAuthentication = 1
    authorization = 1
    availability = 0
    confidentiality = 1
    nonRepudiation = 0

if (q13 == 5):
    privacy = 0
    integrity = 0
    identiAuthentication = 1
    authorization = 1
    availability = 1
    confidentiality = 0
    nonRepudiation = 0

if (q14 == 1):
    physicalSecurity = 1

if (q15 == 1):
    tamperDetection = 1


print ("# Analysis done! Check your requirements \n")


f = open("requirements.txt", "w")

f.write("#   SECURECloudMobilEQUIREMENTS                                                                              \n"
        "    The  **SECURECloudMobilEQUIREMENTS** is a custom made program. It helps in the                           \n"
        "    creation of Cloud and Mobile tools with security by providing the security requirements              \n"
        "    before the creation of the tool It is part of the outputs of PHD Thesis  entitled                    \n"
        "    ystematization of the Safety Engineering Process in the Cloud and Mobile Ecosystem.               \n" 
        "##  License                                                                                              \n"
        "    Developed by Francisco T. Chimuco and Pedro R. M. Inácio Department of Computer                      \n"
        "    Science Universidade da Beira Interior Copyright 2019 Francisco T. Chimuco and                       \n"
        "    Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0                                            \n\n")


f.write("# The Requirements to develop your tool are: \n")
f.write("\n")
f.write("---\n")
f.write("\n")


if (confidentiality == 1):

    f.write("## Confidentiality                           \n")
    f.write("\n")
    f.write("The property that ensures that information is not disclosed or made available \n"
            "to any unauthorized entity. In other words,personal information cannot be     \n"
            "accessed by an unauthorized third party                                       \n")
    if(q4 == 1):
        if (q4_1 == 1 or q4_1 == 2 or q4_1 == 3):
            f.write("This requirement is applied were the information is stored             \n")

if (integrity == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Integrity                                 \n")
    f.write("\n")
    f.write("Is the property of safeguarding the correctness and completeness of assets in\n"
            "a Cloud & Mobile system. In other words it involves maintaining the data consistent,   \n"
            "trustworthy and accurate during it life-cycle                                \n")

    if (q4_1 == 1):
        f.write("This requirement is applied in the Mobile                                 \n")

    if (q4_1 == 2):
        f.write("This requirement is applied in the Cloud                              \n")
    
    if (q4_1 == 3):
        f.write("This requirements is applied in the Cloud and Mobile Ecossystem")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by       \n"
                "attacks such as:                                                                \n")
        f.write("\n")
        f.write("\t* SQL Injection Attacks:                                                      \n"
                "\t  In this type of attack, the attacker inserts malicious code with the        \n"
                "\t  e thintention of accessing the unauthorized database for the purpose of     \n"
                "\t  obtaining confidential or critical data from the legitimate user.           \n")
        f.write("\n")
        f.write("\t* Wrapping Attacks:                                                           \n"
                "\t  In a wrapping attack scenario, the attacker duplicates the SOAP message     \n"
                "\t  in the course of the translation and sends it to the server as a legitimate \n"
                "\t  user. Therefore, the attacker may interfere with the malicious code.        \n")
        f.write("\n")
        f.write("\t* MITM Attacks:                                                               \n"
            "\t  In this type of attack, an attacker attempts to intrude on a mail exchange      \n"
            "\t  or continuous message between two users or clients of a cloud-based mobile      \n"
            "\t application (client-server).                                                     \n")
        f.write("\n")
        f.write("\t* Cookie Poisoning:                                                           \n"
            "\t  This type of attack consists of replacing or modifying cookie content in ways   \n"
            "\t  to gain unauthorized access to applications or Web pages.                       \n")
    
if (availability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Availability                                                                   \n")
    f.write("\n")
    f.write("Refers to the property which ensures that a mobile device or system is             \n"
            "accessible and usable upon demand by authorized entities. In other words the mobile\n"
            "cloud-based application need to be always available to access by authorized people \n")
    if (q4 == 1 and q4_1 == 1):
        f.write("This requirement is applied in the device                                      \n")
    if (q4 == 1 and q4_1 == 2):
        f.write("This requirement is applied in the cloud                                       \n")

    if(q4 == 1 and q4_1 == 3):
        f.write("This requirement is applied in the system and in the cloud                     \n")
    if(q11 == 1):
        f.write("This requirement is applied in the system                                      \n")
    if (verbose ==1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by      \n"
                "attacks such as:                                                               \n")
        f.write("\t* DoS Attacks:                                                              \n"
            "\t In this type of attacks, the attacker attempts to prevent the provision of a    \n"
            "\t service or resource that are signed by authorized users by launching various    \n"
            "\t types of flood                                                                  \n")
        f.write("\t* DDoS Attacks:                                                              \n"
            "\t It is an improved case of DoS attacks in terms of flooding the target server    \n"
            "\t with server with a huge amount of packets.                                      \n")
    
if (authentication == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Authentication                                                                  \n")
    f.write("\n")
    f.write("Is the assurance that information transaction is from the source it claims to      \n"
            "be from. The device authenticates itself prior to receiving or transmitting        \n"
            "any information. It assures that the information received is authentic.            \n"
            "It is assumed that communications may be intercepted by an unauthorized entity and \n"
            "data at rest may be subject to unauthorized access during transport and rest,      \n" 
            "taking into account the nature of the cloud and mobile ecosystem.                  \n") 
    if(q4==1 and q4_1 == 1):
        f.write("This requirement is applied in the device                                      \n")

    if(q4 == 1 and q4_1 == 2):
        f.write("This requirement is applied in the cloud and Internet                          \n")

    if (q4== 1 and q4_1 == 3):
        f.write("This requirement is applied in the System                                      \n")

    if (q4 == 1 and q4_3 < 7):
        f.write("This requirement is applied in the database                                    \n")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by      \n"
                "attacks such as:                                                               \n")
        f.write("\n")
        f.write("\t* Botnet Attack:                                                              \n"
                "\t A botnet is a collection of compromised devices that can be remotely        \n"
                "\t controlled by an attacker, i.e. the bot master. Its main purpose is to       \n"
                "\t steal business information, remote access, online fraud, phishing,           \n"
                "\t malware distribution, spam emails, etc.                                      \n") 
        f.write("\n")
        f.write("\t* Phishing Attack:                                                            \n"
                "\t  In a scenario of this type of attack, when using cloud services, an         \n"
                "\t  attacker can conduct phishing attacks by manipulating the web link to       \n"
                "\t  redirect it to a false link and hijack the user account for the purpose of  \n"
                "\t  stealing the your sensitive data.                                         \n")
        f.write("\n")
        f.write("\t* DNS Attack:                                                                 \n"
                "\t  DNS attacks always occur in the case where the attacker makes use of the    \n"
                "\t  translation of the domain name in an Internet Protocol (IP) address,        \n"                                             
                 "\t in order to access the confidential data of the user in an unauthorized way \n")
        f.write("\n")
        f.write("\t* MITM Attack:                                                                \n"
                "\t  In this type of attack, an attacker attempts to intrude on a mail exchange  \n"
                "\t  or continuous message between two users or clients of a cloud-based mobile      \n"
                "\t  application (client-server).                                                     \n")
        f.write("\n")
        f.write("\t* Reused IP Address Attack:                                                   \n"
                "\t  This type of attack occurs whenever a IP address is reused on a network.    \n"
                "\t  This occurs because in a network the number of IP addresses is usually      \n"
                "\t  limited, which causes an address assigned to one user to be assigned to     \n"
                "\t  another, so that it leaves the network.                                     \n")
        f.write("\n")
        f.write("\t* Wrapping Attacks:                                                           \n"
                "\t  In a wrapping attack scenario, the attacker duplicates the SOAP message     \n"
                "\t  in the course of the translation and sends it to the server as a legitimate \n"
                "\t  user. Therefore, the attacker may interfere with the malicious code.        \n")
        f.write("\n")
        f.write("\t* Cookie Poisoning Attack:                                                    \n"
                "\t  This type of attack consists of replacing or modifying cookie content in    \n"
                "\t  ways to gain unauthorized access to applications or Web pages.              \n")
        f.write("\n")
        f.write("\t* Google Hacking Attacks:                                                     \n"
                "\t  This type of attack involves the use of the Google search engine for the    \n"
                "\t  purpose of discovering confidential information that a hacker or wrongdoer  \n"
                "\t   can use for their benefit by hacking the account of a used.                \n")     
        f.write("\t* Hypervisor Attacks:                                                         \n"
                "\t  In this type of attack, the attacker aims to compromise the authenticity   \n"
                "\t  of sensitive user data and the availability of services from the cloud at   \n"
                "\t  the VM level.                                           \n")
          
               
if (authorization == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Authorization                                                                   \n")
    f.write("\n")
    f.write("The property that determines whether the user or device has rights/privileges      \n"
            "to access a resource, or issue commands                                            \n")
    
    f.write("These requirements or assumptions apply to the secure coding of PHP, C/C++, Java,   \n" 
               "C#, PHP, HTML, JavaScript, Swift programming languages in building mobile Android \n" 
               "applications.                                                                   \n")
    
    if(q4_3 >= 2 ):
        f.write("This requirement is applied were the information might be accessed from        \n"
                "and between the communications in the cloud and mobile ecosystem.              \n")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by      \n"
                "attacks such as:                                                               \n")
        f.write("\n")
        f.write("\n")
        f.write("\t* SQL Injection Attack:                                                      \n"
                "\t  in  this  attack  the  perpetrator injects  malicious code in the system   \n"
                "\t  to gain access to information or even to gain control of the entire system \n")
        f.write("\n")
        f.write("\t* XSS Attack:                                                                 \n"
                "\t  in  this  attack  the  perpetrator injects  malicious code in the system    \n"
                "\t  to gain access to information or even to gain control of the entire system  \n")
        f.write("\n")
        f.write("\t* Reused IP Address:                                                          \n"
                "\t  This type of attack occurs whenever a IP address is reused on a network.    \n"
                "\t  This occurs because in a network the number of IP addresses is usually      \n"
                "\t  limited, which causes an address assigned to one user to be assigned to     \n"
                "\t  another, so that it leaves the network.                                     \n")
        f.write("\n")
        f.write("\t* Botnet Attacks:                                                             \n"
                "\t  A botnet is a collection of compromised devices that can be remotely         \n"
                "\t  controlled by an attacker, i.e. the bot master. Its main purpose is to       \n"
                "\t  steal business information, remote access, online fraud, phishing,           \n"
                "\t  malware distribution, spam emails, etc.                                      \n") 
        f.write("\n")
        f.write("\t* Sniffer Attacks:                                                            \n"
                "\t  This type of attack is carried out by attackers using applications that     \n"
                "\t  can capture data packets in transit on a network, and if they are not.      \n"
                "\t  heavily encrypted, can be read or interpreted.                              \n")
        f.write("\n")
        f.write("\t* Wrapping Attacks:                                                           \n"
                "\t  In this attack scenario, the attacker duplicates the SOAP message           \n"
                "\t  in the course of the translation and sends it to the server as a legitimate \n"
                "\n  user. Therefore, the attacker may interfere with the malicious code.        \n")
        f.write("\n")
        f.write("\t* Google Hacking Attacks:                                                     \n"
                "\t  This type of attack involves the use of the Google search engine for the    \n"
                "\t  purpose of discovering confidential information that a hacker or wrongdoer  \n"
                "\t   can use for their benefit by hacking the account of a used.                \n")
        f.write("\n")
        f.write("\t* Hypervisor Attacks:                                                         \n"
                "\t  In this type of attack, the attacker aims to compromise the authenticity   \n"
                "\t  of sensitive user data and the availability of services from the cloud at   \n"
                "\t  the VM level.                                                               \n")
        f.write("\n")
        f.write("\t* OS Command Injection:                                                        \n"
                "\t Applications are considered vulnerable to the OS command injection attack if  \n"
                "\t they utilize non validated user input in a system level command what can lead \n"
                "\t to the invocation of scripts injected by the attacker.                        \n")
        if ((q1 == 2 or q1 == 1) and (q6 == 2 or q6 == 6)):
            f.write("\n")
            f.write("\t* Buffer Overflows:                                                          \n"
                    "\t Buffer overflows is an anomaly where a program, while writing data to a buffer, \n"
                    "\t overruns the buffer's boundary and overwrites adjacent memory. It can be     \n" 
                    "\t triggered by non-validated inputs that are designed to execute code.         \n")
        if ( q1 == 8 and q4_3>=2 and q7 == 2):
            f.write("\t* Session Hijacking:                                                          \n"
                    "\t an attacker impersonates a legitimate user through stealing or predicting a  \n"
                    "\t valid session ID.                                                            \n")
            f.write("\t* Session Fixation:                                                           \n"
                    "\t an attacker has a valid session ID and forces the victim to use this ID.    \n")
if (nonRepudiation == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Non-Repudiation                                                                  \n")
    f.write("\n")
    f.write("The security property that ensures that the transfer of messages or                 \n"
            "credentials between 2 mobile users entities is undeniable                           \n")
    if (q3 >=2):
        if (q4_3 >= 2):
            f.write("This requirement is applied between information transactions                \n")
            f.write("This requirement is applied between information transactions over the Internet  \n")
            f.write("This requirement is applied in the Cloud                                        \n")
            f.write("This requirement is applied in the database                                     \n")

if (accountability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Accountability                                                                   \n")
    f.write("\n")
    f.write("The property that ensures that every action can be traced back to a single          \n"
            "user or device                                                                      \n")
    if (q3 >= 2):
        if(q4_3 >= 2):
            f.write("This requirement is applied over Internet transactions                          \n")
    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by        \n"
                "attacks such as:                                                                \n")
        f.write("\n")
        f.write("\t* DNS Attacks:                                                                 \n"
                "\t  DNS attacks always occur in the case where the attacker makes use of the    \n"
                "\t  translation of the domain name in an Internet Protocol (IP) address,        \n"                                             
                "\t in order to access the confidential data of the user in an unauthorized way \n")
        f.write("\n")
        f.write("\t* MITM Attacks:                                                                \n"
                "\t  In this type of attack, an attacker attempts to intrude on a mail exchange   \n"
                "\t  or continuous message between two users or clients of a cloud-based mobile   \n"
                "\t  application (client-server).                                                 \n")

if (reliability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Reliability                                                                       \n")
    f.write("\n")
    f.write("Refers to the property that guarantees consistent intended behavior of an a          \n"
            "general system, in this case applied to cloud and mobile ecosystem.                   \n")
    
    f.write("This requirement is applied over Internet transactions in the cloud and mobile ecosystem. \n")

if(privacy == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Privacy                                                                    \n")
    f.write("\n")
    f.write("In the context of cloud and mobile, privacy refers to the control of the user over the     \n"
            "disclosure of his data. In other words only the user has control of the       \n"
            "sharing of is personal information, is data is only made public if the user   \n"
            "allowed it                                                                    \n")
    if (q4 == 1):
        if (q4_1 == 1 or q4_1 == 2 or q4_1 == 3):
            f.write("This requirement is applied where the information is stored             \n")

if (physicalSecurity ==1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Physical Security                                                          \n")
    f.write("\n")
    f.write("Refers to the security measures designed to deny unauthorized physical access \n"
            "to mobile devices and equipment, and to protect them from damage or in other     \n"
            "words gaining physical access to the device won't give access to it's         \n"
            "information                                                                   \n")

    if (q4_1 <=3 or q3 == 1 or q4_3 <=6):
        f.write("This requirement is applied were the information is stored                    \n")

    if(q15 == 1):
        f.write("Apply this requirement to the device                                          \n")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("\t* Physical Attack:                                                          \n"
                "\t  is when the perpetrator gains physical access to the location where the   \n"
                "\t  system is operating and tries to gain information stored in the system    \n"
                "\t  using his physical access                                                 \n")

if(forgeryResistance == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Forgery Resistance                                                         \n")
    f.write("\n")
    f.write("Is the propriety that ensures that the contents shared between entities cannot\n"
            "be forged by a third party trying to damage or harm the system or its users.  \n"
            "In other words no one can try to forge content and send it in the name of     \n"
            "another entities                                                              \n")
    if (q3 >= 2):
        if (q4_1 == 2 or q4_1 == 3):
            f.write("This requirement is applied in the device                                     \n")
            f.write("This requirement is applied in the Cloud                                      \n")
            f.write("This requirement is applied in the database                                   \n")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("\t* Impersonation Attack:                                                     \n"
                "\t  in this attack the attacker pretends to be one of the users of the system \n"
                "\t  to fulfill is bad intentions.                                             \n")

if (tamperDetection == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Tamper Detection                                                           \n")
    f.write("\n")
    f.write("Ensures all devices are physically secured, such that any tampering attempt is\n"
            "detected                                                                      \n")
    if (q15 == 1):
        f.write("This requirement is applied in the device and in the cloud data center    \n")


    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("\t* Tampering:                                                                \n"
                "\t  is when a attacker preforms physical modifications on the hardware where  \n"
                "\t  the software is implemented                                               \n")
        f.write("\n")
        f.write("\t* Reused IP Address Attack:                                                   \n"
                "\t  This type of attack occurs whenever a IP address is reused on a network.    \n"
                "\t  This occurs because in a network the number of IP addresses is usually      \n"
                "\t  limited, which causes an address assigned to one user to be assigned to     \n"
                "\t  another, so that it leaves the network.                                     \n")

if (dataFreshness == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Data Freshness                                                                 \n")
    f.write("\n")
    f.write("Status that ensures that data is the most recent, and that old messages are       \n"
            "not mistakenly used as fresh or purposely replayed by perpetrators. In other      \n"
            "words this requirement provides the guarantee that the data displayed is the      \n"
            "most recent                                                                       \n")
    if (q3 >= 2):
        if (q4 == 1):
            f.write("This requirement is applied to the cloud, since it says that messages     \n"
                    "\t sent between components of the cloud and mobile ecosystem can be       \n" 
                    "\t captured and forwarded, by hypothesis.                                 \n")
            f.write("\t This requirement is applied between the communications                    \n")

if (confinement == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Confinement                                                                    \n")
    f.write("\n")
    f.write("Ensures that even if a party is corrupted, the spreading of the effects of the    \n"
            "attack is as confined as possible.                                            \n")
    if (q3 >= 2 or q12 == 1):
        if (q4 == 1):
            f.write("\t This requirement is applied in the entire system.                          \n")

if( interoperability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Interoperability                                                              \n")
    f.write("\n")
    f.write("Is the propriety that ensures that different software communicates and works      \n"
            "well with each-other. I.e a software in health-care that works with data that     \n"
            "comes from a third-party needs to be able to use and process the information      \n"
            "given to it by this software                                                      \n")

    if (q12 == 1):
        f.write("\t This requirement is applied in the entire system                              \n")

if( dataOrigin == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Data Origin Authentication                                                     \n")
    f.write("\n")
    f.write("Ensures that the data being received by the software comes from the source it     \n"
            "claims to be. In other words it ensures that the data being received is           \n"
            "authentic and from a trusted party                                                \n")
    if (q3 >= 2 or q3 == 3 or q3 == 4 or q3 == 5 or q3 == 6):
        if (q4 == 1):
            f.write("\t This requirement is applied between the communications                    \n")

    if (verbose == 1):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("\t* MITM attack:                                                              \n"
                "\t  is when an attacker gains access to a packet and re-sends it when it’s    \n"
                "\t  beneficial to him, resulting in him gaining the trust of the system.      \n")


# If the system uses local and remote or remote database, authentication by username and password, 
# and if it is used in a community or private cloud
if (q4 == 1 and q4_3 >=2):
    f.write("\n\n ### RISK ANALISYS: ### \n\n")
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("\t These security risks affect all cloud layers! \n\n")

    if (q13 == 1):
        f.write(" Low Security Risk in the cloud environments! \n")
    if (q13 == 2):
        f.write(" Low Security Risk in the cloud-based applications! \n")
    if (q13 == 3):
        f.write(" Absolute Security Risk in the cloud-based applications! \n")
    if (q13 == 4):
        f.write(" Medium Security Risk in the cloud-based applications! \n")
    if (q13 == 5):
        f.write(" Low Security Risk in the cloud-based applications! \n")

f.close()
