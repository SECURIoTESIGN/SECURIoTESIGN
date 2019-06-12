#coding=utf-8
import os

confidentiality = 0
integrity = 0
availability = 0
authentication = 0
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

print ( "#   SECURIoTEQUIREMENTS\n"
        "    The  **SECURIoTEQUIREMENTS** is a custom made program. It helps in the creation of IoT tools with security\n"
        "    by providing the security requirements before the creation of the tool It is part of the outputs of\n"
        "    project Project SECURIoTESIGN, with funding  by FCT-Fundação para a Ciência e Tecnologia (Portugal) through\n"
        "    the  research grant SFRH/BD/133838/2017.\n "
        "## License\n "
        "   Developed by Carolina Lopes and Pedro R. M. Inácio Department of Computer Science Universidade da Beira\n"
        "    Interior Copyright 2019 Carolina Lopes and Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0\n" )

while True :

        print "#  Do you wish to run a older test? \n"
        print "   1 - Yes \n"
        print "   2 - No\n"
        print "   Answer\n"
        q0 = raw_input()
        print "\n"
        if (q0 < '3') :
                break


if (q0 =='1') :

    answerlist=[]

    while True:
        print ("#  Insert the name of the file\n")
        filename = raw_input()

        if(os.path.exists(filename)):
            break;
    with open(filename) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            x = line.split("\n");
            answerlist.append(x[0])
    fp.close()



    q1 = answerlist[0]
    q2 = answerlist[1]
    q2_1 = answerlist[2]
    q2_2 = answerlist[3]
    q2_3 = answerlist[4]
    q2_4 = answerlist[5]
    q2_5 = answerlist[6]
    q3 = answerlist[7]
    q3_1 = answerlist[8]
    q4 = answerlist[9]
    q5 = answerlist[10]
    q6 = answerlist[11]
    q7 = answerlist[12]
    q8 = answerlist[13]
    q9 = answerlist[14]
    q10 = answerlist[15]
    q11 = answerlist[16]


else:

        while True:
            print "#  Question 1 \n"
            print "## State the domain type for your IoT system: \n"
            print "   1 - Smart Home \n"
            print "   2 - Smart Healthcare \n"
            print "   3 - Smart Manufacturing \n"
            print "   4 - Smart Wearables\n"
            print "   5 - Smart Toy \n"
            print "   6 - Smart Transportation\n"
            print "   Answer: \n"
            q1 = raw_input()
            print "\n"
            if (q1 < '7'):
                break



        while True:
            print "#  Question 2 \n"
            print "## Will the system have a user? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q2 = raw_input()
            print("\n")
            if (q2 < '3'):
                break;

        q2_2 = -1
        q2_1 = -1
        if (q2 == '1'):
            while True:
                print "##  Question 2.1 \n"
                print "### Will the system have user LogIn? \n"
                print "    1 - Yes \n"
                print "    2 - No  \n"
                print "   Answer:  \n"

                q2_1 = raw_input()
                print "\n"
                if (q2_1 < '3'):
                    break



            while True:
                print "##  Question 2.2 \n"
                print "### Will the system hold any user information? \n"
                print "    1 - Yes \n"
                print "    2 - No \n"
                print "   Answer: \n"

                q2_2 = raw_input()
                print "\n"

                if (q2_2 < '3'):
                    break



        q2_3 = -1
        if q2 == '2' or q2_2 == '2':
            while True:
                print "##  Question 2.3 \n"
                print "### Will the system store any kind of information? \n"
                print "    1 - Yes \n"
                print "    2 - No \n"
                print "   Answer: \n"

                q2_3 = raw_input()
                print "\n"

                if (q2_3 < '3'):
                    break


        q2_4 = -1
        q2_5 = -1
        if (q2_2 == '1') or (q2_3 == '1'):
            while True:
                print "##  Question 2.4 \n"
                print "### What will be the level of information stored? \n"
                print  "   1 - Normal Information \n"
                print  "   2 - Sensitive Information \n"
                print  "   3 - Critical Information \n"
                print  "   Answer: \n"

                q2_4 = raw_input()
                print "\n"

                if (q2_4 < '4'):
                    break



            while True:
                print "##  Question 2.5 \n"
                print "### Will this information be sent to an entity? \n"
                print "    1 - Yes \n"
                print "    2 - No  \n"
                print "    Answer: \n"

                q2_5 = raw_input()
                print "\n"

                if (q2_5 < '3'):
                    break



        while True:
            print "#   Question 3 \n"
            print "##  Will the system be connected to the internet? \n"
            print "    1 - Yes \n"
            print "    2 - No \n"
            print "    Answer: \n"

            q3 = raw_input()
            print "\n"
            if (q3 < '3'):
                break

        q3_1 = -1
        if (q3 == '1'):


            while True:
                print "##  Question 3.1 \n"
                print "### Will it send its data to a cloud? \n"
                print "    1 - Yes\n"
                print "    2 - No \n"
                print "    Answer: \n"

                q3_1 = raw_input()
                print "\n"

                if (q3_1 < '3'):
                    break


        while True:
            print "#  Question 4 \n"
            print "## Will it store data in a db? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q4 = raw_input()
            print "\n"

            if (q4 < '3'):
                break



        while True:
            print "#  Question 5 \n"
            print "## Will the system receive regular updates? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q5 = raw_input()
            print "\n"

            if (q5 < '3'):
                break



        while True:
            print "#  Question 6 \n"
            print "## Will the system work with third-party software? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q6 = raw_input()
            print "\n"

            if (q6 < '3'):
                break


        while True:
            print "#  Question 7 \n"
            print "## Is there a possibility of the communications being eavesdropped? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q7 = raw_input()
            print " \n"

            if q7 < '3':
                break



        while True:
            print "#  Question 8 \n"
            print "## Could the messages sent between the system components be captured and resend? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q8 = raw_input()
            print "\n"

            if (q8 < '3'):
                break


        while True:
            print "#  Question 9 \n"
            print "## Can someone try to impersonate a user to gain access to private information? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q9 = raw_input()

            if (q9 < '3'):
                break



        while True:
            print "#  Question 10 \n"
            print "## Can someone with bad intentions gain physical access to the location where this \n software will be running and obtain private information? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q10 = raw_input()

            if (q10 < '3'):
                break



        while True:
            print "#  Question 11 \n"
            print "## Can someone gain physical access to the machine where the system operates or \n some of the system components and preform some type of modification\n to its hardware? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q11 = raw_input()

            if (q11 < '3'):
                break


        while True:
            print "#  Do you wish a verbose report ? \n"
            print "   1 - Yes\n"
            print "   2 - No\n"
            print "   Answer: \n"

            verbose = raw_input()
            if (verbose <'3'):
                break

        while True:
            print "#  Do you wish to save this test? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            qsave= raw_input()

            if(qsave < '3'):
                break

        if (qsave == '1'):
            while True:
                print "#  Insert the name of the test:\n"
                testname = raw_input();
                if(testname != ''):
                    break

            fsave= open(testname,"w")
            fsave.write("\n"+str(q1)+"\n"+str(q2)+"\n"+str(q2_1)+"\n"+str(q2_2)+"\n"+str(q2_3)+"\n"+str(q2_4)+"\n"+str(q2_5)+"\n"+str(q3)+"\n"+str(q3_1)+"\n"+str(q4)+"\n"+str(q5)+"\n"+str(q6)+"\n"+str(q7)+"\n"+str(q8)+"\n"+str(q9)+"\n"+str(q10)+"\n"+str(q11))
            fsave.close()


if q1 == '1':
    confidentiality = 1
    privacy = 1
    integrity = 1
    accountability = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    physicalSecurity = 1

if q1 == '2':
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    integrity = 1
    availability = 1
    reliability = 1
    physicalSecurity = 1
    accountability = 1
    nonRepudiation = 1

if q1 == '3':
    authentication = 1
    authorization = 1
    confidentiality = 1
    integrity = 1
    availability = 1
    reliability = 1
    nonRepudiation = 1
    accountability = 1
    physicalSecurity = 1

if q1 == '4':
    confidentiality = 1
    privacy = 1
    authentication = 1
    authorization = 1
    availability = 1
    reliability = 1
    integrity = 1
    physicalSecurity = 1

if q1 == '5':
    availability = 1
    authentication = 1
    confidentiality = 1
    privacy = 1
    integrity = 1
    tamperDetection = 1

if q1 == '6':
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

if (q2_1 == '1'):
    authentication = 1
    nonRepudiation = 1

if (q2_1 == '2'):
    authentication = 0
    nonRepudiation = 0

if (q2_2 == '1'):
    privacy = 1
    confidentiality = 1

if (q2_2 == '2'):
    privacy = 0
    confidentiality = 0


if q2_3 == '1':
    privacy = 1
    confidentiality = 1

if q2_3 == '2':
    privacy = 0
    confidentiality = 0

if (q2_4 == '1'):
    privacy = 1
    confidentiality = 1
    physicalSecurity = 1

if (q2_4 == '2'):
    privacy = 1
    confidentiality = 1
    physicalSecurity = 1
    authorization = 1
    forgeryResistance = 1
    authentication = 1

if (q2_4 == '3'):
    privacy = 1
    confidentiality = 1
    physicalSecurity = 1
    authorization = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1

if (q2_5 == '1'):
    nonRepudiation = 1
    authentication = 1
    confinement = 1


if(q3 == '1'):
    nonRepudiation = 1
    accountability = 1
    reliability = 1

if (q3_1 == '1'):
    integrity = 1
    availability = 1
    dataFreshness = 1
    forgeryResistance = 1
    nonRepudiation = 1
    authentication = 1

if (q4 == '1'):
    physicalSecurity = 1
    integrity = 1
    availability = 1
    forgeryResistance = 1
    authentication = 1
    nonRepudiation = 1

if (q5 == '1'):
    availability = 1

if (q6 == '1'):
    confinement = 1
    interoperability = 1

if (q7 == '1'):
    authorization = 1

if (q8 == '1'):
    dataOrigin = 1
    dataFreshness = 1


if (q9 == '1'):
    authentication = 1

if (q10 == '1'):
    physicalSecurity = 1


if (q11 == '1'):
    tamperDetection = 1


print "# Analysis done check your requirements \n"


f = open("requirements.txt", "w")

f.write("#   SECURIoTEQUIREMENTS\n"
        "    The  **SECURIoTEQUIREMENTS** is a custom made program. It helps in the creation of IoT tools with security\n"
        "    by providing the security requirements before the creation of the tool It is part of the outputs of\n"
        "    project Project SECURIoTESIGN, with funding  by FCT-Fundação para a Ciência e Tecnologia (Portugal) through\n"
        "    the  research grant SFRH/BD/133838/2017.\n"
        "##  License\n "
        "   Developed by Carolina Lopes and Pedro R. M. Inácio Department of Computer Science Universidade da Beira\n"
        "    Interior Copyright 2019 Carolina Lopes and Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0\n\n" )


f.write("# The Requirements to develop your tool are: \n")
f.write("---\n")
f.write("---\n")


if (confidentiality == 1):

    f.write("## Confidentiality                           \n")
    f.write("\n")
    f.write("The property that ensures that information is\n"
            "not disclosed or made available to any       \n"
            "unauthorized entity. In other words,personal \n"
            "information cannot be accessed by an         \n"
            "unauthorized third party                     \n")
    if(q2_2 == '1' or q2_3 == '1' or q2_4 == '1' or q2_4 == '2' or q2_4 == '3'):
        f.write("Apply this requirement were the information \n"
                "is stored                                   \n")

if (integrity == 1):
    f.write("---\n")
    f.write("## Integrity                                 \n")
    f.write("\n")
    f.write("Is the property of safeguarding the          \n"
            "correctness and completeness of assets in an \n"
            "IoT system. In other words it involves       \n"
            "maintaining the data consistent, trustworthy \n"
            "and accurate during it life-cycle            \n")

    if(q3_1 == '1'):
        f.write("Apply this requirement in the Cloud        \n")

    if (q4 == '1'):
        f.write("Apply this requirement in the database     \n")

    if (verbose =='1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                               \n")
        f.write("Sinkhole Attack:                           \n"
                "in this attack some nods are made more     \n"
                "attractive than others by tampering with   \n"
                "the routing information, when arriving to  \n"
                "the sinkhole node the messages may be      \n"
                "dropped or altered                         \n")
        f.write("Malicious  code  injection:                \n"
                "in  this  attack  the  perpetrator         \n"
                "injects  malicious code in the system to    \n"
                "gain access to information or even to gain \n"
                "control of the entire system                \n")

if (availability == 1):
    f.write("---\n")
    f.write("## Availability                              \n")
    f.write("\n")
    f.write("Refers to the property which ensures that an \n"
            "IoT device or system is accessible and usable\n"
            "upon demand by authorized entities. In other \n"
            "words the device needs to be always available\n"
            "to access by authorized people               \n")
    if (q3_1 == '1'):
        f.write("Apply this requirement in the Cloud         \n")

    if (q4 == '1'):
        f.write("Apply this requirement in the database      \n")

    if(q5 == '1'):
        f.write("Apply this requirement in the system        \n")

if (authentication == 1):
    f.write("---\n")
    f.write("## Authentication                            \n")
    f.write("\n")
    f.write("Is the assurance that information transaction\n"
            "is from the source it claims to be from. The \n"
            "device authenticates itself prior to         \n"
            "receiving or transmitting any information.   \n"
            "It assures that the information received     \n"
            "is authentic                                 \n")
    if(q2_1=='1' or q2_4 == '2' or q2_4 == '3' or q9 == '1'):
        f.write("Apply this requirement in the device        \n")

    if(q2_5 == '1'):
        f.write("Apply this requirement in communications    \n"
                "via Internet                                \n")

    if (q3_1 == '1'):
        f.write("Apply this requirement in the Cloud         \n")

    if (q4 == '1'):
        f.write("Apply this requirement in the database      \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                                \n")
        f.write("Node Replication:                           \n"
                "when an attacker copies the identity of an  \n"
                "user and send false data in his name.       \n")
        f.write("Sinkhole Attack:                            \n"
                "in this attack some nods are made more      \n"
                "attractive than others by tampering with the\n"
                "routing information, when arriving to the   \n"
                "sinkhole node the messages may be dropped or \n"
                "altered.                                    \n")
        f.write("Impersonation Attack:                       \n"
                "in this attack the attacker pretends to be  \n"
                "one of the users of the system to fulfill is\n"
                "bad intentions.                             \n")

if (authorization == 1):
    f.write("---\n")
    f.write("## Authorization                             \n")
    f.write("\n")
    f.write("The property that determines whether the user\n"
            "or device has rights/privileges to access a  \n"
            "resource, or issue commands                  \n")
    if(q2_4 == '2' or q2_4 == '3'):
        f.write("Apply this requirement were the information \n"
                "might be accessed from                      \n")

    if(q7 == '1'):
        f.write("Apply this requirement between the          \n"
                "communications                              \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                                \n")
        f.write("Eavesdropping:                              \n"
                "is when an attacker has access to the data  \n"
                "being sent between  two  trusted  entities. \n")
        f.write("Malicious  code  injection:                \n"
                "in  this  attack  the  perpetrator         \n"
                "injects  malicious code in the system to    \n"
                "gain access to information or even to gain \n"
                "control of the entire system                \n")

if (nonRepudiation == 1):
    f.write("---\n")
    f.write("## Non-Repudiation                           \n")
    f.write("\n")
    f.write("The security property that ensures that the  \n"
            "transfer of messages or credentials between 2\n"
            "IoT entities is undeniable                   \n")
    if (q2_1 == '1' or q2_4 == '3' or q2_5 == '1' ):
        f.write("Apply this requirement between              \n"
                "information transactions                    \n")
    if(q3 == '1'):
        f.write("Apply this requirement between              \n"
                "information transactions over the Internet  \n")

    if (q3_1 == '1'):
        f.write("Apply this requirement in the Cloud         \n")

    if (q4 == '1'):
        f.write("Apply this requirement in the database      \n")

if (accountability == 1):
    f.write("---\n")
    f.write("## Accountability                            \n")
    f.write("\n")
    f.write("The property that ensures that every action  \n"
            "can be traced back to a single user or device\n")
    if(q3 == '1'):
        f.write("Apply this requirement over Internet         \n"
                "transactions                                 \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                                \n")
        f.write("Node Replication:                           \n"
                "when an attacker copies the identity of an  \n"
                "user and send false data in his name.       \n")

if (reliability == 1):
    f.write("---\n")
    f.write("## Reliability                               \n")
    f.write("\n")
    f.write("Refers to the property that guarantees       \n"
            "consistent intended behavior of an a general \n"
            "system, in this case applied to IoT          \n")
    if (q3 == '1'):
        f.write("Apply this requirement over Internet         \n"
                "transactions\n")

if(privacy == 1):
    f.write("---\n")
    f.write("## Privacy                                   \n")
    f.write("\n")
    f.write("In the context of IoT, privacy refers to the \n"
            "control of the user over the disclosure of   \n"
            "his data. In other words only the user has   \n"
            "control of the sharing of is personal        \n"
            "information, is data is only made public if  \n"
            "the user allowed it                          \n")
    if (q2_2 == '1' or q2_3 == '1' or q2_4 == '1' or q2_4 == '2' or q2_4 == '3'):
        f.write("Apply this requirement were the information  \n"
                "is stored                                    \n")


if (physicalSecurity ==1):
    f.write("---\n")
    f.write("## Physical Security                         \n")
    f.write("\n")
    f.write("Refers to the security measures designed to  \n"
            "deny unauthorized physical access to IoT     \n"
            "devices and equipment, and to protect them   \n"
            "from damage or in other words gaining        \n"
            "physical access to the device won't give     \n"
            "access to it's information                   \n")

    if (q2_4 == '1' or q2_4 == '2' or q2_4 == '3' or q4 == '1'):
        f.write("Apply this requirement were the information \n"
                "is stored                                   \n")

    if(q10 == '1'):
        f.write("Apply this requirement to the device        \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                                \n")
        f.write("Physical Attack:                            \n"
                "is when the perpetrator gains physical      \n"
                "access to the location where the system is  \n"
                "operating and tries to gain information     \n"
                "stored in the system using his physical     \n"
                "access                                      \n")


if(forgeryResistance == 1):
    f.write("---\n")
    f.write("## Forgery Resistance                        \n")
    f.write("\n")
    f.write("Is the propriety that ensures that the       \n"
            "contents shared between entities cannot be   \n"
            "forged by a third party trying to damage or  \n"
            "harm the system or its users. In other words \n"
            "no one can try to forge content and send it  \n"
            "in the name of another entities              \n")
    if (q2_4 == '2' or q2_4 == '3'):
        f.write("Apply this requirement in the device        \n")
    if (q3_1 == '1'):
        f.write("Apply this requirement in the Cloud         \n")

    if (q4 == '1'):
        f.write("Apply this requirement in the database      \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                                \n")
        f.write("Impersonation Attack:                       \n"
                "in this attack the attacker pretends to be  \n"
                "one of the users of the system to fulfill is\n"
                "bad intentions.                             \n")

if (tamperDetection == 1):
    f.write("---\n")
    f.write("## Tamper Detection                            \n")
    f.write("\n")
    f.write("Ensures all devices are physically secured,    \n"
            "such that any tampering attempt is detected    \n")
    if (q11 == '1'):
        f.write("Apply this requirement to the device       \n")


    if (verbose =='1'):
        f.write("\nBy not applying this requirement you may \n"
                "suffer from:                               \n")
        f.write("Tampering:                                 \n"
                "is when a attacker preforms physical       \n"
                "modifications on the hardware where the    \n"
                "software is implemented                    \n" )
        f.write("Sinkhole Attack:                           \n"
                "in this attack some nods are made more     \n"
                "attractive than others by tampering with   \n"
                "the routing information, when arriving to  \n"
                "the sinkhole node the messages may be      \n"
                "dropped or altered                         \n")

if (dataFreshness == 1):
    f.write("---\n")
    f.write("## Data Freshness                            \n")
    f.write("\n")
    f.write("Status that ensures that data is the most    \n"
            "recent, and that old messages are not        \n"
            "mistakenly used as fresh or purposely        \n"
            "replayed by perpetrators. In other words this\n"
            "requirement provides the guarantee that the  \n"
            "data displayed is the most recent            \n")
    if (q3_1 == '1'):
        f.write("Apply this requirement in the Cloud         \n")

    if (q8 == '1'):
        f.write("Apply this requirement between the          \n"
                "communications                              \n")

if (confinement == 1):
    f.write("---\n")
    f.write("## Confinement                               \n")
    f.write("\n")
    f.write("Ensures that even if a party is corrupted,   \n"
            "the spreading of the effects of the attack is\n"
            "as confined as possible.                     \n")
    if(q2_5 == '1' or q6 == '1'):
        f.write("Apply this requirement to the entire system \n")


if( interoperability == 1):
    f.write("---\n")
    f.write("## Interoperability                          \n")
    f.write("\n")
    f.write("Is the propriety that ensures that different \n"
            "software communicates and works well with    \n"
            "each-other. I.e a software in health-care    \n"
            "that works with data that comes from a       \n"
            "third-party needs to be able to use and      \n"
            "process the information given to it by this  \n"
            "software                                     \n")

    if (q6 == '1'):
        f.write("Apply this requirement to the entire system \n")


if( dataOrigin == 1):
    f.write("---\n")
    f.write("## Data Origin Authentication                \n")
    f.write("\n")
    f.write("Ensures that the data being received by the  \n"
            "software comes from the source it claims to  \n"
            "be. In other words it ensures that the data  \n"
            "being received is authentic and from a       \n"
            "trusted party                                \n")
    if (q8 == '1'):
        f.write("Apply this requirement between the          \n"
                "communications                              \n")

    if (verbose == '1'):
        f.write("\nBy not applying this requirement you may  \n"
                "suffer from:                                \n")
        f.write("Replay attack:                              \n"
                "is when an attacker gains access to a packet\n"
                "and re-sends it when it’s beneficial to him,\n"
                "resulting in him gaining the trust of the   \n"
                "system.                                     \n")



f.close()