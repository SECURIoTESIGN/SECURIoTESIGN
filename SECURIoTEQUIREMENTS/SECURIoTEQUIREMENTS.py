#coding=utf-8


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

print ( "#   SECURIoTEQUIREMENTS\n"
        "    The  **SECURIoTEQUIREMENTS** is a custom made program. It helps in the creation of IoT tools with security\n"
        "    by providing the security requirements before the creation of the tool It is part of the outputs of\n"
        "    project Project SECURIoTESIGN, with funding  by FCT-Fundação para a Ciência e Tecnologia (Portugal) through\n"
        "    the  research grant SFRH/BD/133838/2017.\n "
        "## License\n "
        "   Developed by Carolina Lopes and Pedro R. M. Inácio Department of Computer Science Universidade da Beira\n"
        "    Interior Copyright 2019 Carolina Lopes and Pedro R. M. Inácio  SPDX-License-Identifier: Apache-2.0\n" )

while True :
        print "#  Question 1 \n"
        print "## State the domain type for your IoT system: \n"
        print "   1 - Smart Home \n"
        print "   2 - Smart Healthcare \n"
        print "   3 - Smart Manufacturing \n"
        print "   4 - Smart Wearables\n"
        print "   5 - Smart Toy \n"
        print "   Answer: \n"
        q1 = raw_input()
        print "\n"
        if (q1 < '6' ) :
                break


if q1 == '1' :
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


while True:
        print "#  Question 2 \n"
        print "## Type of users: \n"
        print "   1 - Individual user \n"
        print "   2 -  Corporate user \n"
        print "   3 - Admin user \n"
        print "   4 - No user \n"
        print "   Answer: \n"

        q2 = raw_input()
        print("\n")
        if (q2 <'5'):
                break;

q2_2=-1
q2_1=-1
if (q2 < '4'):
        while True:
                print "##  Question 2.1 \n"
                print "### Does the system has user LogIn? \n"
                print "    1 - Yes \n"
                print "    2 - No  \n"
                print "   Answer:  \n"

                q2_1 = raw_input()
                print "\n"
                if(q2_1 < '3'):
                        break

        if (q2_1 == '1'):
                authentication = 1
                nonRepudiation = 1

        if(q2_1 == '2'):
                authentication = 0
                nonRepudiation = 0

        while True :
                print "##  Question 2.2 \n"
                print "### Does the system hold any user information? \n"
                print "    1 - Yes \n"
                print "    2 - No \n"
                print "   Answer: \n"

                q2_2 = raw_input()
                print "\n"

                if(q2_2 < '3'):
                        break

        if(q2_2 == '1'):
                privacy = 1
                confidentiality = 1

        if (q2_2 == '2'):
                privacy = 0
                confidentiality = 0

q2_3=-1
if q2 == '4':
        while True:
                print "##  Question 2.3 \n"
                print "### Does the system store any kind of information? \n"
                print "    1 - Yes \n"
                print "    2 - No \n"
                print "   Answer: \n"

                q2_3 = raw_input()
                print "\n"

                if(q2_3 < '3'):
                        break

        if q2_3 == '1' :
                privacy = 1
                confidentiality = 1

        if q2_3 == '2':
                privacy = 0
                confidentiality = 0
q2_4=-1
q2_5=-1
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

        if (q2_4 == '1'):
                privacy = 1
                confidentiality = 1
                physicalSecurity = 1

        if(q2_4 == '2'):
                privacy = 1
                confidentiality = 1
                physicalSecurity = 1
                authorization = 1
                forgeryResistance=1
                authentication = 1

        if (q2_4 == '3'):
                privacy = 1
                confidentiality = 1
                physicalSecurity = 1
                authorization = 1
                forgeryResistance = 1
                dataFreshness = 1
                tamperDetection = 1
                nonRepudiation = 1
                authentication = 1

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

        if(q2_5 == '1'):
                tamperDetection = 1
                nonRepudiation = 1
                authentication = 1
                confinement = 1

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

q3_1=-1
if(q3 == '1'):
        nonRepudiation = 1
        accountability = 1
        reliability = 1

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
        if(q3_1 == '1'):
                integrity = 1
                availability = 1
                dataFreshness = 1
                forgeryResistance = 1
                nonRepudiation = 1


while True:
        print "#  Question 4 \n"
        print "## Will it store data in a db? \n"
        print "   1 - Yes \n"
        print "   2 - No \n"
        print "   Answer: \n"

        q4 = raw_input()
        print "\n"

        if(q4 < '3'):
                break

if (q4 =='1' ):
        physicalSecurity = 1
        integrity = 1
        availability = 1
        forgeryResistance = 1
        authentication = 1
        nonRepudiation = 1

while True:
        print "#  Question 5 \n"
        print "## Will the system receive regular updates? \n"
        print "   1 - Yes \n"
        print "   2 - No \n"
        print "   Answer: \n"

        q5 = raw_input()
        print "\n"

        if(q5 < '3'):
                break

if(q5 == '1'):
        availability = 1

while True:
        print "#  Question 6 \n"
        print "## Will the system work with third parties software? \n"
        print "   1 - Yes \n"
        print "   2 - No \n"
        print "   Answer: \n"

        q6 = raw_input()
        print "\n"

        if(q6 < '3'):
                break

if(q6 == '1'):
        confinement = 1

print "# Analysis done check your requirements \n"

f = open("requierments.txt", "w")


f.write("# The Requierments to develop your tool are: \n")
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

if (integrity == 1):
    f.write("---\n")
    f.write("## Integrity                                 \n")
    f.write("\n")
    f.write("Is the property of safeguarding the          \n"
            "correctness and completeness of assets in an \n"
            "IoT system. In other words it involves       \n"
            "maintaining the data consistent, trustworthy \n"
            "and accurate during its life-cycle           \n")

if (availability == 1):
    f.write("---\n")
    f.write("## Availability                              \n")
    f.write("\n")
    f.write("Refers to the property which ensures that an \n"
            "IoT device or system is accessible and usable\n"
            "upon demand by authorized entities. In other \n"
            "words the device needs to be always available\n"
            "to access by authorized people               \n")

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

if (authorization == 1):
    f.write("---\n")
    f.write("## Authorization                             \n")
    f.write("\n")
    f.write("The property that determines whether the user\n"
            "or device has rights/privileges to access a  \n"
            "resource, or issue commands                  \n")

if (nonRepudiation == 1):
    f.write("---\n")
    f.write("## Non-Repudiation                           \n")
    f.write("\n")
    f.write("The security property that ensures that the  \n"
            "transfer of messages or credentials between 2\n"
            "IoT entities is undeniable                   \n")

if (accountability == 1):
    f.write("---\n")
    f.write("## Accountability                            \n")
    f.write("\n")
    f.write("The property that ensures that every action   \n"
            "can be traced back to a single user or device \n")

if (reliability == 1):
    f.write("---\n")
    f.write("## Reliability                               \n")
    f.write("\n")
    f.write("Refers to the property that guarantees       \n"
            "consistent intended behavior of an a general \n"
            "system, in this case applied to IoT          \n")

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

if (tamperDetection == 1):
    f.write("---\n")
    f.write("## Tamper Detection                          \n")
    f.write("\n")
    f.write("Ensures all devices are physically secured,  \n"
            "such that any tampering attempt is detected  \n")

if (dataFreshness == 1):
    f.write("---\n")
    f.write("## Data Freshness                            \n")
    f.write("\n")
    f.write("status that ensures that data is the most    \n"
            "recent, and that old messages are not        \n"
            "mistakenly used as fresh or purposely        \n"
            "replayed by perpetrators. In other words this\n"
            "requirement provides the guarantee that the  \n"
            "data displayed is the most recent            \n")

if (confinement == 1):
    f.write("---\n")
    f.write("## Confinement                               \n")
    f.write("\n")
    f.write("Ensures that even if a party is corrupted,   \n"
            "the spreading of the effects of the attack is\n"
            "as confined as possible.                     \n")