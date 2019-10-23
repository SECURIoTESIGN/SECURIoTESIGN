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
        if (q0 == '1'or q0=='2') :
                break

        else :
            print "Insert a valid answer \n"


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
    verbose = answerlist[17]


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
            if (q1 == '1' or q1 == '2' or q1 == '3' or q1 == '4' or q1 == '5' or q1 == '6'):
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 2 \n"
            print "## Will the system have a user? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q2 = raw_input()
            print("\n")
            if (q2 == '1' or q2 == '2'):
                break

            else:
                print "Insert a valid answer \n"

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
                if (q2_1 == '1' or q2_1 == '2'):
                    break
                else:
                    print "Insert a valid answer \n"



            while True:
                print "##  Question 2.2 \n"
                print "### Will the system hold any user information? \n"
                print "    1 - Yes \n"
                print "    2 - No \n"
                print "   Answer: \n"

                q2_2 = raw_input()
                print "\n"

                if (q2_2 == '1' or q2_2 =='2'):
                    break

                else:
                    print "Insert a valid answer \n"



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

                if (q2_3 == '1' or q2_3 == '2'):
                    break

                else:
                    print "Insert a valid answer \n"


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

                if (q2_4 == '1' or q2_4 == '2' or q2_4 == '3'):
                    break

                else:
                    print "Insert a valid answer \n"



            while True:
                print "##  Question 2.5 \n"
                print "### Will this information be sent to an entity? \n"
                print "    1 - Yes \n"
                print "    2 - No  \n"
                print "    Answer: \n"

                q2_5 = raw_input()
                print "\n"

                if (q2_5 == '1' or q2_5 == '2'):
                    break

                else:
                    print "Insert a valid answer \n"



        while True:
            print "#   Question 3 \n"
            print "##  Will the system be connected to the internet? \n"
            print "    1 - Yes \n"
            print "    2 - No \n"
            print "    Answer: \n"

            q3 = raw_input()
            print "\n"
            if (q3 == '1' or q3 == '2'):
                break

            else:
                print "Insert a valid answer \n"

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

                if (q3_1 == '1' or q3_1 == '2'):
                    break

                else:
                    print "Insert a valid answer \n"


        while True:
            print "#  Question 4 \n"
            print "## Will it store data in a db? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q4 = raw_input()
            print "\n"

            if (q4 == '1' or q4 == '2'):
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 5 \n"
            print "## Will the system receive regular updates? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q5 = raw_input()
            print "\n"

            if (q5 == '1' or q5 == '2'):
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 6 \n"
            print "## Will the system work with third-party software? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q6 = raw_input()
            print "\n"

            if (q6 == '1' or q6 == '2'):
                break

            else:
                print "Insert a valid answer \n"


        while True:
            print "#  Question 7 \n"
            print "## Is there a possibility of the communications being eavesdropped? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q7 = raw_input()
            print " \n"

            if q7 == '1' or q7 == '2':
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 8 \n"
            print "## Could the messages sent between the system components be captured and resend? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q8 = raw_input()
            print "\n"

            if (q8 == '1' or q8 == '2'):
                break

            else:
                print "Insert a valid answer \n"


        while True:
            print "#  Question 9 \n"
            print "## Can someone try to impersonate a user to gain access to private information? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q9 = raw_input()

            if (q9 == '1' or q9 == '2'):
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 10 \n"
            print "## Can someone with bad intentions gain physical access to the location where \n" \
                  "   this software will be running and obtain private information?              \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q10 = raw_input()

            if (q10 == '1' or q10 == '2'):
                break

            else:
                print "Insert a valid answer \n"



        while True:
            print "#  Question 11 \n"
            print "## Can someone gain physical access to the machine where the system operates  \n" \
                  "   or some of the system components and preform some type of modification to  \n" \
                  "   it's hardware?                                                             \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            q11 = raw_input()

            if (q11 == '1' or q11 =='2'):
                break

            else:
                print "Insert a valid answer \n"

        verbose = -1

        while True:
            print "#  Do you wish a verbose report ? \n"
            print "   1 - Yes\n"
            print "   2 - No\n"
            print "   Answer: \n"

            verbose = raw_input()
            if (verbose == '1' or verbose == '2'):
                break

            else:
                print "Insert a valid answer \n"

        while True:
            print "#  Do you wish to save this test? \n"
            print "   1 - Yes \n"
            print "   2 - No \n"
            print "   Answer: \n"

            qsave= raw_input()

            if(qsave == '1' or qsave == '2'):
                break

            else:
                print "Insert a valid answer \n"

        if (qsave == '1'):
            while True:
                print "#  Insert the name of the test:\n"
                testname = raw_input();
                if(testname != ''):
                    break

            fsave= open(testname,"w")
            fsave.write("\n"+str(q1)+"\n"+str(q2)+"\n"+str(q2_1)+"\n"+str(q2_2)+"\n"+str(q2_3)+"\n"+str(q2_4)+"\n"+str(q2_5)+"\n"+str(q3)+"\n"+str(q3_1)+"\n"+str(q4)+"\n"+str(q5)+"\n"+str(q6)+"\n"+str(q7)+"\n"+str(q8)+"\n"+str(q9)+"\n"+str(q10)+"\n"+str(q11)+"\n"+str(verbose))
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

f.write("#  SECURIoTEQUIREMENTS\n"
        "   The  **SECURIoTEQUIREMENTS** is a custom made program. It helps in the    \n"
        "   creation of IoT tools with security by providing the security requirements\n"
        "   before the creation of the tool It is part of the outputs of project      \n"
        "   Project SECURIoTESIGN, with funding  by FCT-Fundação para a Ciência e     \n"
        "   Tecnologia (Portugal) through the  research grant SFRH/BD/133838/2017.    \n"
        "## License\n"
        "   Developed by Carolina Lopes and Pedro R. M. Inácio Department of Computer \n"
        "   Science Universidade da Beira Interior Copyright 2019 Carolina Lopes and  \n"
        "   Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0                 \n\n" )


f.write("# The Requirements to develop your tool are: \n")
f.write("\n")
f.write("---\n")
f.write("\n")


if (confidentiality == 1):

    f.write("## Confidentiality                           \n")
    f.write("\n")
    f.write("The property that ensures that information is not disclosed or made available \n"
            "to any unauthorized entity. In other words,personal information cannot be     \n"
            "accessed by an unauthorized third party.                                      \n")
    if(q2_2 == '1' or q2_3 == '1' or q2_4 == '1' or q2_4 == '2' or q2_4 == '3'):
        f.write("This requirement is applied were the information is stored.                   \n")

if (integrity == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Integrity                                 \n")
    f.write("\n")
    f.write("Is the property of safeguarding the correctness and completeness of assets in\n"
            "an IoT system. In other words it involves maintaining the data consistent,   \n"
            "trustworthy and accurate during it life-cycle.                               \n")

    if(q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                \n")

    if (q4 == '1'):
        f.write("This requirement is applied in the database.                             \n")

    if (verbose =='1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Sinkhole Attack:                                                          \n"
                "   In this attack some nods are made more attractive than others by tampering\n"
                "   with the routing information, when arriving to the sinkhole node the      \n"
                "   messages may be dropped or altered.                                       \n")
        f.write("\n")
        f.write("  *Malicious  code  injection:                                               \n"
                "   In  this  attack  the  perpetrator injects  malicious code in the system  \n"
                "   to gain access to information or even to gain control of the entire       \n"
                "   system.                                                                   \n")

if (availability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Availability                                                               \n")
    f.write("\n")
    f.write("Refers to the property which ensures that an IoT device or system is          \n"
            "accessible and usable upon demand by authorized entities. In other words the  \n"
            "device needs to be always available to access by authorized people.           \n")
    if (q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                 \n")

    if (q4 == '1'):
        f.write("This requirement is applied in the database.                              \n")

    if(q5 == '1'):
        f.write("This requirement is applied in the system.                                \n")

if (authentication == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Authentication                                                             \n")
    f.write("\n")
    f.write("Is the assurance that information transaction is from the source it claims to \n"
            "be from. The device authenticates itself prior to receiving or transmitting   \n"
            "any information. It assures that the information received is authentic.       \n")
    if(q2_1=='1' or q2_4 == '2' or q2_4 == '3' or q9 == '1'):
        f.write("This requirement is applied in the device.                                    \n")

    if(q2_5 == '1'):
        f.write("This requirement is applied in the communications via Internet.               \n")

    if (q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                     \n")

    if (q4 == '1'):
        f.write("This requirement is applied in the database.                                  \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Node Replication:                                                         \n"
                "   When an attacker copies the identity of an user and send false data in his\n"
                "   name.                                                                     \n")
        f.write("\n")
        f.write("  *Sinkhole Attack:                                                          \n"
                "   In this attack some nods are made more attractive than others by tampering\n"
                "   with the routing information, when arriving to the sinkhole node the      \n"
                "   messages may be dropped or altered.                                       \n")
        f.write("\n")
        f.write("  *Impersonation Attack:                                                     \n"
                "   In this attack the attacker pretends to be one of the users of the system \n"
                "   to fulfill is bad intentions.                                             \n")

if (authorization == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Authorization                                                              \n")
    f.write("\n")
    f.write("The property that determines whether the user or device has rights/privileges \n"
            "to access a resource, or issue commands.                                      \n")
    if(q2_4 == '2' or q2_4 == '3'):
        f.write("This requirement is applied were the information might be accessed from.      \n")

    if(q7 == '1'):
        f.write("This requirement is applied between the communications.                       \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Eavesdropping:                                                            \n"
                "   Is when an attacker has access to the data being sent between  two        \n"
                "   trusted  entities.                                                        \n")
        f.write("\n")
        f.write("  *Malicious  code  injection:                                               \n"
                "   In  this  attack  the  perpetrator injects  malicious code in the system  \n"
                "   to gain access to information or even to gain control of the entire       \n"
                "   system.                                                                   \n")

if (nonRepudiation == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Non-Repudiation                                                            \n")
    f.write("\n")
    f.write("The security property that ensures that the transfer of messages or           \n"
            "credentials between 2 IoT entities is undeniable.                             \n")
    if (q2_1 == '1' or q2_4 == '3' or q2_5 == '1' ):
        f.write("This requirement is applied between information transactions.                 \n")
    if(q3 == '1'):
        f.write("This requirement is applied between information transactions over the         \n"
                "Internet.                                                                     \n")

    if (q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                      \n")

    if (q4 == '1'):
        f.write("This requirement is applied in the database.                                   \n")

if (accountability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Accountability                                                             \n")
    f.write("\n")
    f.write("The property that ensures that every action can be traced back to a single    \n"
            "user or device.                                                               \n")
    if(q3 == '1'):
        f.write("This requirement is applied over Internet transactions.                       \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Node Replication:                                                         \n"
                "   When an attacker copies the identity of an user and send false data in his\n"
                "   name.                                                                     \n")

if (reliability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Reliability                                                                \n")
    f.write("\n")
    f.write("Refers to the property that guarantees consistent intended behavior of an a   \n"
            "general system, in this case applied to IoT.                                  \n")
    if (q3 == '1'):
        f.write("This requirement is applied over Internet transactions.                       \n")

if(privacy == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Privacy                                                                    \n")
    f.write("\n")
    f.write("In the context of IoT, privacy refers to the control of the user over the     \n"
            "disclosure of his data. In other words only the user has control of the       \n"
            "sharing of is personal information, is data is only made public if the user   \n"
            "allowed it.                                                                   \n")
    if (q2_2 == '1' or q2_3 == '1' or q2_4 == '1' or q2_4 == '2' or q2_4 == '3'):
        f.write("This requirement is applied were the information is stored.                   \n")


if (physicalSecurity ==1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Physical Security                                                          \n")
    f.write("\n")
    f.write("Refers to the security measures designed to deny unauthorized physical access \n"
            "to IoT devices and equipment, and to protect them from damage or in other     \n"
            "words gaining physical access to the device won't give access to it's         \n"
            "information.                                                                  \n")

    if (q2_4 == '1' or q2_4 == '2' or q2_4 == '3' or q4 == '1'):
        f.write("This requirement is applied were the information is stored.                   \n")

    if(q10 == '1'):
        f.write("Apply this requirement to the device.                                         \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Physical Attack:                                                          \n"
                "   Is when the perpetrator gains physical access to the location where the   \n"
                "   system is operating and tries to gain information stored in the system    \n"
                "   using his physical access.                                                \n")


if(forgeryResistance == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Forgery Resistance                                                         \n")
    f.write("\n")
    f.write("Is the propriety that ensures that the contents shared between entities cannot\n"
            "be forged by a third party trying to damage or harm the system or its users.  \n"
            "In other words no one can try to forge content and send it in the name of     \n"
            "another entities.                                                             \n")
    if (q2_4 == '2' or q2_4 == '3'):
        f.write("This requirement is applied in the device.                                    \n")
    if (q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                     \n")

    if (q4 == '1'):
        f.write("This requirement is applied in the database.                                  \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Impersonation Attack:                                                     \n"
                "   In this attack the attacker pretends to be one of the users of the system \n"
                "   to fulfill is bad intentions.                                             \n")

if (tamperDetection == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Tamper Detection                                                           \n")
    f.write("\n")
    f.write("Ensures all devices are physically secured, such that any tampering attempt is\n"
            "detected.                                                                     \n")
    if (q11 == '1'):
        f.write("This requirement is applied in the device.                                    \n")


    if (verbose =='1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Tampering:                                                                \n"
                "   Is when a attacker preforms physical modifications on the hardware where  \n"
                "   the software is implemented.                                              \n" )
        f.write("\n")
        f.write("  *Sinkhole Attack:                                                          \n"
                "   In this attack some nods are made more attractive than others by tampering\n "
                "   with the routing information, when arriving to the sinkhole node the      \n"
                "   messages may be dropped or altered.                                       \n")

if (dataFreshness == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Data Freshness                                                             \n")
    f.write("\n")
    f.write("Status that ensures that data is the most recent, and that old messages are   \n"
            "not mistakenly used as fresh or purposely replayed by perpetrators. In other  \n"
            "words this requirement provides the guarantee that the data displayed is the  \n"
            "most recent.                                                                  \n")
    if (q3_1 == '1'):
        f.write("This requirement is applied in the Cloud.                                     \n")

    if (q8 == '1'):
        f.write("This requirement is applied between the communications.                       \n")

if (confinement == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Confinement                                                                \n")
    f.write("\n")
    f.write("Ensures that even if a party is corrupted, the spreading of the effects of the\n"
            "attack is as confined as possible.                                            \n")
    if(q2_5 == '1' or q6 == '1'):
        f.write("This requirement is applied in the entire system.                             \n")


if( interoperability == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Interoperability                                                           \n")
    f.write("\n")
    f.write("Is the propriety that ensures that different software communicates and works  \n"
            "well with each-other. I.e a software in health-care that works with data that \n"
            "comes from a third-party needs to be able to use and process the information  \n"
            "given to it by this software.                                                 \n")

    if (q6 == '1'):
        f.write("This requirement is applied in the entire system.                             \n")


if( dataOrigin == 1):
    f.write("\n")
    f.write("---\n")
    f.write("\n")
    f.write("## Data Origin Authentication                                                 \n")
    f.write("\n")
    f.write("Ensures that the data being received by the software comes from the source it \n"
            "claims to be. In other words it ensures that the data being received is       \n"
            "authentic and from a trusted party.                                           \n")
    if (q8 == '1'):
        f.write("This requirement is applied between the communications.                       \n")

    if (verbose == '1'):
        f.write("\nNot addressing this requirement may lead to vulnerabilities explored by     \n"
                "attacks such as:                                                              \n")
        f.write("\n")
        f.write("  *Replay attack:                                                            \n"
                "   Is when an attacker gains access to a packet and re-sends it when it’s    \n"
                "   beneficial to him, resulting in him gaining the trust of the system.      \n")



f.close()