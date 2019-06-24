#ifndef REPORT_H
#define REPORT_H

#include <iostream>
#include <string>
#include <windows.h>
#include <mysql.h>
Report.h
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#include <vector>
#include <sstream>
#include <string.h>
#include <tuple>
#include <conio.h>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <stdlib.h>
#include<bits/stdc++.h>
#include <chrono>
#include <thread>
#include <fstream>

class Report
{
    public:
        Report();

    //Function that formats the report that will be displayed on the Console
    void formatReport_for_Consle(std::string request_id, int flag, std::string algo_name1, std::string algo_name2, std::string algo_name3, std::string algo_name4, std::string algo_name5, std::string algo_name6, std::string Re_6, std::string Re_7, std::string Re_8, std::string Re_9, std::string Re_10, std::string Re_11, std::string Re_12, std::string Re_13, std::string Re_14, std::string Re_15);

    //Function that formats the report that will be written to a text file
    void formatReport_for_TextFile(std::string request_id, int flag, std::string algo_name1, std::string algo_name2, std::string algo_name3, std::string algo_name4, std::string algo_name5, std::string algo_name6, std::string Re_6, std::string Re_7, std::string Re_8, std::string Re_9, std::string Re_10, std::string Re_11, std::string Re_12, std::string Re_13, std::string Re_14, std::string Re_15);

    //Function that prints the relevant report for lightweight encryption algorithms
    void cipher_Info1(std::string algo_name1);

    //Function that prints the relevant report for lightweight cryptographic hash functions
    void cipher_Info2(std::string algo_name2);

    //Function that prints the relevant report for lightweight authentication algorithms
    void cipher_Info3(std::string algo_name3);
};

#endif // REPORT_H

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Report.cpp

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include "Report.h"

Report::Report()
{
    //ctor
}

using namespace std;

void Report::formatReport_for_Consle(string request_id, int flag, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, string Re_6, string Re_7, string Re_8, string Re_9, string Re_10, string Re_11, string Re_12, string Re_13, string Re_14, string Re_15)
{

       //Function that formats the report that will be displayed on the Console
        if(flag == 1)
        {
          /*
           // system("cls");
           // std::cout << "\n" "***********************************************************************************************************" << endl;
            std::cout << "\n\t\t    A BRIEF OVERVIEW OF THE FUNCTIONALITY OF THE IoT-HarPSecA TOOL " <<endl <<endl;
            std::cout << "  The Requirement Elicitation component of this tool can generate diverse security requirements, hence\n";
            std::cout << "  its application is not limited to the IoT. It can be used to generate security requirements for stan- \n";
            std::cout << "  dard computer systems. However, the application of the tool's component that recommends security \n";
            std::cout << "  algorithms does not extend to the standard security algorithms. Its application is only limited to the\n";
            std::cout << "  IoT space because it can only recommend lightweight security algorithms suitable for resource-constra-\n";
            std::cout << "  ined environments, which can be implemented in software or hardware.\n";


            //The Requirement Elicitation component of this tool can generate diverse security requirements, hence its application is not
           // limited to the IoT. It can be used to generate security requirements for standard computer systems. However, the application
             //of the tool's component that recommends security algorithms does not extend to the standard security algorithms. Its application
             //is only limited to the IoT space because it can only recommend lightweight security algorithms suitable for resource-constrained
             // environments, which can be implemented in software or hardware.
*/
                std::cout << endl << endl;
                std::cout << "\n\t\t     A REPORT ON THE REQUEST OF THE USER WITH REQUEST ID No.: " << request_id <<endl <<endl;
                std::cout << "   This report consists of brief information about the recommended Lightweight Cryptographic Algorithms\n";
                std::cout << "   (LWCAs), as well as short best practice guidelines for the implementation of the LWCAs. The report \n";
                std::cout << "   also includes some security measures needed to be taken in order to meet the remaining security \n";
                std::cout << "   requirements that were generated by the Requirement Elicitation tool to which no algorithms have been \n";
                std::cout << "   recommended.\n";


                std::cout << endl;

                std::cout << "\n\  THE RECOMMENDED ALGORITHMS " << endl <<endl;

                int counter = 0;
                 if(!algo_name1.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name1 << ":- ";
                     cipher_Info1( algo_name1);
                 }
                 if(!algo_name2.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name2 << ":- ";
                     cipher_Info2( algo_name2);
                 }
                 if(!algo_name3.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name3 << ":- ";
                     cipher_Info3( algo_name3);
                 }
                 if(!algo_name4.empty() && algo_name1.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name4 << ":- ";
                     cipher_Info1( algo_name1);
                 }
                 if(!algo_name5.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name5 << ":- ";
                 }
                 if(!algo_name6.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name6 << ":- ";
                 }
                 if(algo_name6.empty() && !algo_name2.empty() && (!algo_name1.empty() || !algo_name4.empty()))
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << "*Authenticated Encryption" << ":- Since your security requirements include confidentiality and/or privacy\n";
                     std::cout << "      as well as integrity, you may want to consider returning to the main menu to select option 10 in   \n";
                     std::cout << "      order to modify your request, and then include 'Confidentiality & Authenticity' in your security \n";
                     std::cout << "      requirements. This is because the mechanism that satisfies the 'Confidentiality & Authenticity'   \n";
                     std::cout << "      security requirement is the authenticated encryption, which can provide message integrity and \n";
                     std::cout << "      message origin authentication in addition to protecting data confidentiality and/or user privacy. \n";
                 }
                   counter = 0;


                std::cout << "\n\n  THE OTHER SECURITY REQUIREMENTS "  << endl << endl;
                 int counter2 = 0;
                 if(!Re_6.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Availability:- " << "This is\n"<< endl;
                 }
                 if(!Re_7.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Physical Security:- " << " \n"<< endl;
                 }
                 if(!Re_8.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Authorization:- " << " \n"<< endl;
                 }
                 if(!Re_9.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Forgery Resistance:-" << " \n"<< endl;
                 }
                 if(!Re_10.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Confinement:-" << " \n"<< endl;
                 }
                 if(!Re_11.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Accountability:-" << " \n"<< endl;
                 }
                 if(!Re_12.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Reliability:-" << " \n"<< endl;
                 }
                 if(!Re_13.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Data Freshness:-" << " \n"<< endl;
                 }
                 if(!Re_14.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Data Origin Authentication:-" << " \n"<< endl;
                 }
                 if(!Re_15.empty())
                 {
                     counter2+=1;
                     cout << "  " << counter2 << ". " << "Tamper Detection:-" << " \n"<< endl;
                 }
                   counter = 0;


                std::cout << "  As stated by the principle of least privilege [1], the idea is that every user, process or computer has \n";
                std::cout << "  access only the information that is necessary in order to carry on its activity. For this reason, for it\n";


        }
        else if(flag == 2)
        {
          /*
            std::cout << endl << endl;
                std::cout << "\n\t\t    A REPORT ON THE REQUEST OF THE USER WITH REQUEST ID No.: " << request_id <<endl <<endl;
                std::cout << "  The Requirement Elicitation component of this tool can generate diverse security requirements, hence\n";
                std::cout << "  its application is not limited to IoT. It can be used to generate security requirements for standard\n";
                std::cout << "  computer systems. However, the application of the tool's component that recommends security algorithms\n";
                std::cout << "  is only limited to the IoT Space because it can only recommend lightweight security algorithms that can\n";
                std::cout << "  be implemented in software or hardware, and not standard security algorithms.\n";
           */
                std::cout << endl << endl;
                std::cout << "\n\t\t     A REPORT ON THE REQUEST OF THE USER WITH REQUEST ID No.: " << request_id <<endl <<endl;
                std::cout << "   This report consists of brief information about the recommended Lightweight Cryptographic Algorithms\n";
                std::cout << "   (LWCAs), as well as short best practice guidelines for the implementation of the LWCAs.\n";

                std::cout << endl;

                std::cout << "\n\  THE RECOMMENDED ALGORITHMS " << endl <<endl;

                int counter = 0;
                 if(!algo_name1.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name1 << ":- ";
                     cipher_Info1( algo_name1);
                 }
                 if(!algo_name2.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name2 << ":- ";
                     cipher_Info2( algo_name2);
                 }
                 if(!algo_name3.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name3 << ":- ";
                     cipher_Info3( algo_name3);
                 }
                 if(!algo_name4.empty() && algo_name1.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name4 << ":- ";
                     cipher_Info1( algo_name1);
                 }
                 if(!algo_name5.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name5 << ":- ";
                 }
                 if(!algo_name6.empty())
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << algo_name6 << ":- ";
                 }
                 if(algo_name6.empty() && !algo_name2.empty() && (!algo_name1.empty() || !algo_name4.empty()))
                 {
                     counter+=1;
                     cout << "  " << counter << ". " << "*Authenticated Encryption" << ":- Since your security requirements include confidentiality and/or privacy\n";
                     std::cout << "      as well as integrity, you may want to consider returning to the main menu to select option 10 in   \n";
                     std::cout << "      order to modify your request, and then include 'Confidentiality & Authenticity' in your security \n";
                     std::cout << "      requirements. This is because the mechanism that satisfies the 'Confidentiality & Authenticity'   \n";
                     std::cout << "      security requirement is the authenticated encryption, which can provide message integrity and \n";
                     std::cout << "      message origin authentication in addition to protecting data confidentiality and/or user privacy. \n";
                 }
                   counter = 0;
            }

}



void Report::formatReport_for_TextFile(string request_id, int flag, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, string Re_6, string Re_7, string Re_8, string Re_9, string Re_10, string Re_11, string Re_12, string Re_13, string Re_14, string Re_15)
{

}

void Report::cipher_Info1(std::string algo_name1)
{
	std::string option1 = "SPECK", option2 = "SIMON", option3 = "Clefi", option4 = "Midor", option5 = "TWINE", option6 = "Picco", option7 = "ChaCh", option8 = "Enoco", option9 = "Grain", option10 = "Trivi", option11 = "MICKE";
	std::string algoName = algo_name1.substr(0, 5);
	if(algoName == option1)
	{
        std::cout << "SPECK is a family of lightweight block ciphers designed by the United States National\n";
        std::cout << "     Security Agency (NSA) to provide security in constrained environments where memory, storage space,\n";
        std::cout << "     and computational capabilities are limited. SPECK has been optimized for performance in software \n";
        std::cout << "     implementation. SPECK supports a variety of block and key sizes (i.e., block/key - 32/64, 48/72, 48\n";
        std::cout << "     /96, 64/96, 64/128, 96/96, 96/144, 128/128, 128/192, 128/256). Complete details about SPECK can be  \n";
        std::cout << "     found at at https://eprint.iacr.org/2013/404.pdf. Additionally, the C and Python implementations can \n";
        std::cout << "     be found at https://github.com/inmcm/Simon_Speck_Ciphers.\n"<< endl;
	}
	else if(algoName == option2)
	{
        std::cout << "SIMON is a family of lightweight block ciphers designed by the United States National\n";
        std::cout << "     Security Agency (NSA) to provide security in constrained environments where memory, storage space,\n";
        std::cout << "     and computational capabilities are limited. SIMON has been optimized for performance in hardware \n";
        std::cout << "     implementation. SIMON supports a variety of block and key sizes (i.e., block/key - 32/64, 48/72, 48\n";
        std::cout << "     /96, 64/96, 64/128, 96/96, 96/144, 128/128, 128/192, 128/256). Complete details about SIMON can be  \n";
        std::cout << "     found at at https://eprint.iacr.org/2013/404.pdf. Additionally, the C and Python implementations can \n";
        std::cout << "     be found at https://github.com/inmcm/Simon_Speck_Ciphers.\n"<< endl;
	}
	else if(algoName == option3)
	{
        std::cout << "CLEFIA is a lightweight proprietary block cipher algorithm developed by Sony. The \n";
        std::cout << "     block cipher is intended to serve as a safe alternative to AES with the flexibility for efficient\n";
        std::cout << "     implementation in both hardware and software. CLEFIA supports 128-bit (16 bytes) block size and \n";
        std::cout << "     three different key sizes of 128, 192, and 256 bits. More information about CLEFIA can be found at\n";
        std::cout << "     https://www.sony.net/Products/cryptography/clefia/about/appendix_01.html, and a C implementation  \n";
        std::cout << "     can be found at https://github.com/fedescarpa/clefia. \n" << endl;
	}
	else if(algoName == option4)
	{
        std::cout << "Midori, a Japanese word for green, is a 128-bit secret key block cipher that comes \n";
        std::cout << "     in two variants, Midori 64 and Midori 128. The 64 and 128 correspond to the different block sizes\n";
        std::cout << "     (i.e., Midori 64/128 and Midori 128/128). The two variants of Midori provide acceptable security \n";
        std::cout << "     level with optimal energy consumption when implemented in hardware. More information about Midori \n";
        std::cout << "     can be found at https://eprint.iacr.org/2015/1142.pdf, and a hardware design of Midori 128 written \n";
        std::cout << "     in VHDL can be found at https://github.com/tomirio619/Midori. \n" << endl;
	}
	else if(algoName == option5)
	{
        std::cout << "TWINE is a lightweight 64-bit block cipher that supports 80 and 128 bit key sizes. The\n";
        std::cout << "     cipher is designed to be efficient on both software and hardware. For software implementation, TWINE\n";
        std::cout << "     consumes less CPU time and occupies a small ROM space. The cipher is also designed to perform well\n";
        std::cout << "     on various types of CPUs, from low-end microcontrollers to high-end CPUs, such as the Intel Core-i\n";
        std::cout << "     series. For more information on TWINE, refer to https://wwwljk.imag.fr/membres/Pierre.Karpman/cry_\n";
        std::cout << "     intro_tp_twine.pdf. In addition, some information on the C implementation of TWINE can be found at \n";
        std::cout << "     https://github.com/dgryski/go-twine.\n" << endl;
	}
	else if(algoName == option6)
	{
        std::cout << "Piccolo is a lightweight 64-bit block cipher that supports 80 and 128 bit key sizes.\n";
        std::cout << "     The cipher achieves both high security and notably compact implementation in hardware. For example, \n";
        std::cout << "     for encryption, the gate equivalent (GE) requirements for the 80 and the 128-bit key modes are only\n";
        std::cout << "     683 and 758, respectively; and only 60 additional GEs are required to support the decryption function.\n";
        std::cout << "     More information about the structure of Piccolo can be found at https://www.iacr.org/archive/ches2011\n";
        std::cout << "     /69170343/69170343.pdf, and a C implementation can be found at https://github.com/Daeinar/piccolo.\n"<< endl;

	}
	else if(algoName == option7)
	{
        std::cout << "ChaCha20 is a stream cipher with a 256-bit key and a 96-bit initialization vector(IV).\n";
        std::cout << "     Aside from a secret key and an IV, it receives a 128-bit constant anda 32-bit block counter, and \n";
        std::cout << "     outputs a 512-bit pseudo-random number. The algorithm utilizes 32-bit word arithmetic additions, \n";
        std::cout << "     exclusive ORs (XORs), and cyclic shifts, and is suitable for software implementation. Because it  \n";
        std::cout << "     requires little cost for initialization, it can process short messages quickly. Additionally, \n";
        std::cout << "     ChaCha20 uses no table lookups, straightforward implementation is secure against cache-timing \n";
        std::cout << "     attacks. More information about the stream cipher can be found at https://asecuritysite.com/\n";
        std::cout << "     encryption/chacha, and https://www.cryptrec.go.jp/report/cryptrec-gl-2003-2016en.pdf; and a C \n";
        std::cout << "     implementation can be found at https://github.com/Ginurx/chacha20-c\n"<< endl;
	}
	else if(algoName == option8)
	{
        std::cout << "Enocoro is a stream cipher that consists of two algorithms, Enocoro-80 with 80-bit key \n";
        std::cout << "     and Enocoro-128v2 with 128-bit key. The two algorithms claim a level of security corresponding to the \n";
        std::cout << "     key length. But the output data is limited to 2^32 bytes and 2^64 bytes, respectively, by fixing the \n";
        std::cout << "     key and IV. Unlike other lightweight stream ciphers, this cipher processes in 8-bit units and can \n";
        std::cout << "     achieve  processing speeds similar to AES even in software implementation. More information and code\n";
        std::cout << "     can be found at https://www.hitachi.com/rd/yrl/crypto/enocoro/index.html. Additional information can \n";
        std::cout << "     also be found at https://www.cryptrec.go.jp/report/cryptrec-gl-2003-2016en.pdf. \n"<< endl;

	}
	else if(algoName == option9)
	{
        std::cout << "Grain is a hardware-oritented stream cipher. Two algorithms of Grain were selected for\n";
        std::cout << "     the eSTREAM portfolio: one with an 80-bit key and a 64-bit IV and the other with a 128-bit key and\n";
        std::cout << "     an 80-bit IV. The cipher comprises one bitwise linear feedback shift register and one non-linear\n";
        std::cout << "     feedback shift register. Among other lightweight stream ciphers, this stream cipher is superior for \n";
        std::cout << "     lightweight hardware implementation. It can achieve certain degrees of parallelism, software \n";
        std::cout << "     implementation performs sufficiently for practical uses. For more information on the cipher, we \n";
        std::cout << "     refer the user to https://cr.yp.to/streamciphers/grain/desc.pdf, and  https://www.cryptrec.go.jp/\n";
        std::cout << "     report/cryptrec-gl-2003-2016en.pdf. \n"<< endl;
	}
	else if(algoName == option10)
	{
        std::cout << "Trivium is a stream cipher that is optimized for hardware implementation, which was  \n";
        std::cout << "     selected in the eSTREAM portfolio. The cipher accepts an 80-bit key and an 80-bit IV. A keystream \n";
        std::cout << "     generated for each pair of key and IV is limited to 264 bits. Trivium has a unique design consisting  \n";
        std::cout << "     of three serial non-linear feedback shift registers of different lengths. Based on bitwise operations,\n";
        std::cout << "     but having high levels of parallelism, it features lightweight hardware implementation and high \n";
        std::cout << "     speeds in software implementation. Nonetheless, Trivium is not suitable for processing short data \n";
        std::cout << "     because of its long initialization time. More information can be found at https://eprint.iacr.org/\n";
        std::cout << "     2009/431.pdf and  https://www.cryptrec.go.jp/report/cryptrec-gl-2003-2016en.pdf. A VHDL \n";
        std::cout << "     implementation of Trivium can be found at https://github.com/akshjums/Trivium-Cipher.\n" << endl;
	}
	else if(algoName == option11)
	{
        std::cout << "MICKEY 2.0 is a hardware-oriented stream cipher selected in the eSTREAM portfolio. The \n";
        std::cout << "     cipher accepts an 80-bit key and an 80-bit IV. The number of available IVs for a fixed key is limited \n";
        std::cout << "     up to 240. In addition, the maximum length of a keystream for a pair of key and IV is 240 bits. This  \n";
        std::cout << "     stream cipher consists of one linear feedback shift register and one non-linear feedback shift \n";
        std::cout << "     register, featuring irregular clock control. Parallel processing is difficult due to the clock \n";
        std::cout << "     control mechanism. More information can be found at http://www.ecrypt.eu.org/stream/mickeypf.html.\n";
        std::cout << "     \n";
        std::cout << "      \n";
        std::cout << "     \n" << endl;
	}
}


//Function that prints the relevant report for lightweight cryptographic hash functions
    void Report::cipher_Info2(std::string algo_name2)
    {
        std::string option1 = "PHOTON", option2 = "SPONGE", option3 = "Keccak", option4 = "U-QUAR", option5 = "S-QUAR";
        std::string algoName = algo_name2.substr(0, 6);
        if(algoName == option1)
        {
            std::cout << "PHOTON is a family of lightweight hash functions that come in five different \n";
            std::cout << "     flavors with the following digest sizes: 80, 128, 160, 224 and 256 bits. PHOTON can be represented \n";
            std::cout << "     in this format: PHOTON-n/r/r', where n is the output length in bits, r represents the input block  \n";
            std::cout << "     length, and r' is the output block length. Thus, the five variants are PHOTON-80/20/16, PHOTON-128  \n";
            std::cout << "     /16/16, PHOTON-160/36/36, PHOTON-224/32/32, and PHOTON-256/32/32. The lightweight hash function is \n";
            std::cout << "     suitable for extremely constrained devices such as passive RFID tags. Although it is optimized for \n";
            std::cout << "     hardware implementation, PHOTON can equally be implemented in software. More details about PHOTON \n";
            std::cout << "     can be found at https://eprint.iacr.org/2011/609.pdf and https://pdfs.semanticscholar.org/63d1/ \n";
            std::cout << "     7f64d7a7d5b1bcd199c2569334e7194e40e1.pdf\n"<< endl;
        }
        else if(algoName == option2)
        {
            std::cout << "SPONGENT a family of lightweight hash functions based on a sponge construction   \n";
            std::cout << "     instantiated with a PRESENT-type permutation. SPONGENT can produce hash sizes of 88, 128, 160, 224,\n";
            std::cout << "     and 256 bit. It offers a lot of flexibility in terms of serialization degree and speed. For more\n";
            std::cout << "     information about SPONGENT, refer to https://www.iacr.org/archive/ches2011/69170311/69170311.pdf\n"<< endl;
        }
        else if(algoName == option3)
        {
            std::cout << "Keccak is a set of seven permutation functions called Keccak-f[b], which can be \n";
            std::cout << "     used to construct a stream cipher, a cryptographic hash function, a Pseudo Random Number Generator \n";
            std::cout << "     (PRNG), Message Authentication Code (MAC) or an Authenticated Encryption Associated Data (AEAD)  \n";
            std::cout << "     algorithm. The 'b' represents the width which is between 25 and 1600 by multiplicative steps of 2\n";
            std::cout << "     (b 25, 50, 100, 200, 400, 800, 1,600). The functions relevant to the lightweight cryptography are  \n";
            std::cout << "     Keccak-f[100], Keccak-f[200], and Keccak-f[400]. More information about Keccak can be found at \n";
            std::cout << "     https://keccak.team/ and https://www.iacr.org/archive/eurocrypt2013/78810311/78810311.pdf.  \n" << endl;
        }
        else if(algoName == option4)
        {
            std::cout << "QUARK is a hash function family consisting of three instances, namely U-QUARK,  \n";
            std::cout << "     D-QUARK, and S-QUARK. It can be used for message authentication, stream encryption, or  \n";
            std::cout << "     authenticated encryption. QUARK is based on a sponge construction, and it is only optimized \n";
            std::cout << "     for hardware implementation. More details about the lightweight hash function can be found\n";
            std::cout << "     at https://131002.net/quark/quark_full.pdf, and https://www.iacr.org/archive/ches2010/62250001 \n";
            std::cout << "     /62250001.pdf; and a C implementation can be found at https://github.com/veorq/Quark. \n" << endl;
        }
        else if(algoName == option5)
        {
            std::cout << "QUARK is a hash function family consisting of three instances, namely U-QUARK,  \n";
            std::cout << "     D-QUARK, and S-QUARK. It can be used for message authentication, stream encryption, or  \n";
            std::cout << "     authenticated encryption. QUARK is based on a sponge construction, and it is only optimized \n";
            std::cout << "     for hardware implementation. More details about the lightweight hash function can be found\n";
            std::cout << "     at https://131002.net/quark/quark_full.pdf, and https://www.iacr.org/archive/ches2010/62250001 \n";
            std::cout << "     /62250001.pdf; and a C implementation can be found at https://github.com/veorq/Quark. \n" << endl;
        }
    }


    //Function that prints the relevant report for lightweight authentication algorithms
    void Report::cipher_Info3(std::string algo_name3)
    {
        std::string option1 = "SipHas", option2 = "", option3 = "";
        std::string algoName = algo_name3.substr(0, 6);
        if(algoName == option1)
        {
            std::cout << "SipHash is a keyed hash function with a key length of 128 bits and an output length\n";
            std::cout << "     of 64 bits. It is optimized for software implementation and runs fast on a CPU that supports \n";
            std::cout << "     64-bit operations only. The target applications of SipHash include network traffic authentication \n";
            std::cout << "     and hash-table lookups protected against hash-flooding denial-of-service attacks. More information \n";
            std::cout << "     about the SipHash can be found at https://cr.yp.to/siphash/siphash-20120620.pdf, and a Javascript  \n";
            std::cout << "     implementation can be found at https://github.com/jedisct1/siphash-js.  \n" << endl;
        }
        else if(algoName == option2)
        {

        }
        else if(algoName == option3)
        {

        }
    }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
