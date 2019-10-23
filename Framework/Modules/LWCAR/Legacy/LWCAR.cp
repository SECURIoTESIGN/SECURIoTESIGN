
/* The LWCAR component is inside the main code of the IoT-HarPSecA tool */

#include <iostream>
#include <string>
#include <windows.h>
#include <mysql.h>
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

#include <ctime>

#include "sha256.h"

using std::string;
using std::cout;
using std::endl;


#include "Preliminary.h"
#include "Report.h"

using namespace std;

MYSQL* conn;
MYSQL_ROW row;
MYSQL_RES *res;
int qstate;
int strength = 0;
bool authorized_to_be_Admin = false;
string status = "";


static const char alphanum[] =
"0123456789"
"!@$&%^*"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"abcdefghijklmnopqrstuvwxyz";

int stringLength = sizeof(alphanum) -1;


char genRandom()
{
	return alphanum[rand() % stringLength];
}

std::string generateSalt()
{
    srand(time(0));
	std::string salti;

	for(unsigned int i = 0; i < 20; ++i)
	{
		salti += genRandom();
	}

	return salti;
}



class Processing_and_Output
{
    public:
     Processing_and_Output();
     int searchString(string s1, string s2);
     bool isCapable(int cpu, double fms, double rs, double cs, int cpu_, double flash, double ram, double clock);
     string concatStrings(string r1, string r2, string r3, string r4, string r5, string r6);
     auto mapping1(string userR, string r_1, string r_2, string r_3, string r_4, string r_5, string r_6, string r1, string r2, string r3, string r4, string r5, string r6);
     auto mapping1b(string userR, string r_1, string r_2, string r_3, string r_4, string r_5, string r_6, string r1, string r2, string r3, string r4, string r5, string r6);
     int checkSensitivity_of_User_ApplcArea(string as);
     int Check_if_streamCipherNeeded(string ps);
     auto select_MarchingAlgo(int flagx, int ds, int n_SC, int cpu_int, double fms_doub, double rs_doub);
     auto select_MarchingAlgo2_ThreeSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type);
     auto select_MarchingAlgo2_FourSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type);
     auto select_MarchingAlgo2_SixSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type);
     auto select_MarchingAlgo2_SevenSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type);
     auto mapping2(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, int cpu_int, double fms_doub, double rs_doub, string as, string ps);
     auto mapping2Hardware(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, double ccta1_doub, double tp1_doub, double ccta2_doub, double tp2_doub, double ccta3_doub, double tp3_doub, double ccta4_doub, double tp4_doub, double ccta5_doub, double tp5_doub, double ccta6_doub, double tp6_doub, string as, string ps, string type);
     string fetch_Algo(string IDx);
     auto display_Mech_Algo_mapping(int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6);
     auto display_Mech_Algo_mapping2(int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6, string energy);
     void format_Print_output(string s1, string s2, string s3, string s4, string s5, string s6, int f1, int f2, int f3, int f4, int f5, int f6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6);
     void format_TextOutput(string s1, string s2, string s3, string s4, string s5, string s6, int f1, int f2, int f3, int f4, int f5, int f6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight, double fms, double rs, double fms_, double rs_, string request_id);
     double reqWeighting(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6);
     void displayReq_Mech_mapping(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight, int warn1, string request_id);
     void write_Req_Mech_mapping(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight, double fms, double rs, double fms_, double rs_, string request_id);
     auto select_MarchingAlgo3(int flagx, int ds, int n_SC, double FMx, double RAMx);
     auto display_Mech_Algo_mapping3(string type, int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6);
     auto mapping2_3(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, double FM1_doub, double RAM1_doub, double FM2_doub, double RAM2_doub, double FM3_doub, double RAM3_doub, double FM4_doub, double RAM4_doub, double FM5_doub, double RAM5_doub, double FM6_doub, double RAM6_doub, string ad, string ps);
     void displayReq_Mech_mapping3(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, string request_id);
     void write_security_requirements_in_textFile(string Reqst_ID);
     void write_bestPracticeGuide_in_textFile(string Reqst_ID);
};

Processing_and_Output::Processing_and_Output()
{

}

    void Processing_and_Output::write_security_requirements_in_textFile(string Reqst_ID)
    {
                        system("cls");
                        string findbyID_query = "select * from users_requests_re where Reqst_ID = " + ("'"+Reqst_ID+"'");
                        const char* qn = findbyID_query.c_str();
                        qstate = mysql_query(conn, qn);

                        string state, Domain, anyUsr, Login, stoUsrInfo, stoAnyInfo, InfoType, infoSent2E, connected, dataSent2Cloud, dataStoredInDb, update, use3rdPrtySfw, evesdrop, capt_Resent, impersontUsr, physiclAcces;

                        if(!qstate)
                        {
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                state = row[1];
                                Domain = row[2];
                                anyUsr = row[3];
                                Login = row[4];
                                stoUsrInfo = row[5];
                                stoAnyInfo = row[6];
                                InfoType = row[7];
                                infoSent2E = row[8];
                                connected = row[9];
                                dataSent2Cloud = row[10];
                                dataStoredInDb = row[11];
                                update = row[12];
                                use3rdPrtySfw = row[13];
                                evesdrop = row[14];
                                capt_Resent = row[15];
                                impersontUsr = row[16];
                                physiclAcces = row[17];
                            }
                        }
                        else
                        {
                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                        }

                int domainSensitivity = checkSensitivity_of_User_ApplcArea(Domain);

                string flag1 = "1", flag2 = "1", flag3 = "1", flag4 = "1", flag5 = "1", flag6 = "1", flag7 = "1", flag8 = "1", flag9 = "", flag10 = "1", flag11 = "1", flag12 = "1", flag13 = "1", flag14 = "1", flag15 = "1", flag16 = "1", flag17 = "1", flag18 = "1", flag19 = "1", flag20 = "1";
                string flag21 = "1", flag22 = "1", flag23 = "1", flag24 = "1", flag25 = "1", flag26 = "1", flag27 = "1", flag28 = "1", flag29 = "1", flag30 = "1", flag6_, flag_6;
                string flag31 = "1", flag32 = "1", flag33 = "1", flag34 = "1", flag35 = "1", flag36 = "1", flag37 = "1", flag38 = "1", flag39 = "1", flag40 = "1", flag41 = "1", flag42 = "1", flag43 = "1", flag44 = "1";
                string Reqmt_1, Reqmt_2, Reqmt_3, Reqmt_4, Reqmt_5, Reqmt_6, Reqmt_7, Reqmt_8, Reqmt_9, Reqmt_10, Reqmt_11, Reqmt_12, Reqmt_13, Reqmt_14, Reqmt_15;


            fstream file;
            file.open("Security_Requirements.txt", ios::out | ios::trunc);
            if(file.is_open())
            {
                    file << "\n" "***********************************************************************************************************" << endl;
                    file << "\t   THE SECURITY REQUIREMENTS FOR THE IoT SYSTMEM OF THE USER WITH REQUEST ID No.: " << Reqst_ID << endl << endl;

                        file << left << setw(21) << setfill('-') << left << '+'
                        << setw(84) << setfill('-') << '+' << '+' << endl;

                        file << setfill(' ') << '|' << left << setw(20) << "SECURITY REQUIREMENT"
                        << setfill(' ') << '|' << left << setw(83) << "DESCRIPTION" << '|' << endl;

                         file << left << setw(21) << setfill('-') << left<< '+'
                         << setw(84) << setfill('-') << '+' << '+' << endl;

                         if(anyUsr == "Yes" && Login == "Yes")//
                         {
                            flag1 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(stoUsrInfo == "Yes" && anyUsr == "Yes")
                         {
                            flag2 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Privacy"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, menani- " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_4 = "PRIV";
                         }
                         if(stoUsrInfo == "Yes" && stoAnyInfo == "Yes")
                         {
                            flag3 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_1 = "CONF";
                         }
                         if(stoAnyInfo == "Yes" && flag3 != "2")
                         {
                            flag4 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_1 = "CONF";
                         }
                         if(InfoType == "Normal" && flag2 != "2" && !stoUsrInfo.empty())
                         {
                            flag2 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Privacy"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, menani- " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_4 = "PRIV";
                         }
                         if(InfoType == "Normal" && flag3 != "2" && flag4 != "2")
                         {
                            flag6 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_1 = "CONF";
                         }
                         if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                         {
                             flag6_ = "2";
                             file << setfill(' ') << '|' << left << setw(20) << "Integrity"
                            << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_2 = "INTG";
                         }
                         if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                         {
                             flag_6 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Availability"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << " usable upon demand by authorized entities." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_6 = "AVAI";
                         }

                         if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                         {
                            flag7 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_7 = "PHYS";
                         }
                         if(InfoType == "Sensitive" && stoUsrInfo == "Yes")
                         {

                         }
                         if(InfoType == "Sensitive" && stoUsrInfo != "Yes")
                         {

                         }
                         if(InfoType == "Sensitive" && flag3 != "2" && flag4 != "2" && flag6 != "2")
                         {
                            flag8 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_1 = "CONF";
                         }
                         if(InfoType == "Sensitive")
                         {
                            flag9 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authorization"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_8 = "AUTR";
                         }
                         if(InfoType == "Sensitive")
                         {
                            flag10 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                            << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_9 = "FORE";
                         }
                         if(InfoType == "Sensitive" && flag1 != "2")
                         {
                            flag11 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            cout << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(InfoType == "Critical" && flag2 != "2" && flag5 != "2")
                         {
                            flag2 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Privacy"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, menani- " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_4 = "PRIV";
                         }
                         if(InfoType == "Critical" && flag3 != "2" && flag4 != "2" && flag6 != "2" && flag8 != "2")
                         {
                            flag13 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_1 = "CONF";
                         }
                         if(InfoType == "Critical" && flag7 != "2")
                         {
                            flag14 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_7 = "PHYS";
                         }
                         if(InfoType == "Critical" && flag9 != "2")
                         {
                            flag15 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authorization"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_8 = "AUTR";
                         }
                         if(InfoType == "Critical" && flag10 != "2")
                         {
                            flag16 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                            << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_9 = "FORE";
                         }
                         if(InfoType == "Critical" && domainSensitivity == 1)
                         {
                            flag17 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_5 = "NONR";
                         }
                         if(InfoType == "Critical" && flag1 != "2" && flag11 != "2")
                         {
                            flag18 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(infoSent2E == "Yes" && flag17 != "2" && domainSensitivity == 1)
                         {
                             flag19 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_5 = "NONR";
                         }
                         if(infoSent2E == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2")
                         {
                            flag20 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(infoSent2E == "Yes")
                         {
                            flag21 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confinement"
                            << setfill(' ') << '|' << left << setw(83) << "Ensures that even if a party is corrupted, the spreading of the effects of the" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "attack is as confined as possible." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_10 = "CFMT";
                         }
                         if(connected == "Yes" && flag17 != "2" && flag19 != "2" && domainSensitivity == 1)
                         {
                             flag22 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_5 = "NONR";
                         }
                         if(connected == "Yes" && domainSensitivity == 1)
                         {
                             flag23 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Accountability"
                            << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that every action can be traced back to a single " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "user or device." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_11 = "ACCT";
                         }
                         if(connected == "Yes")
                         {
                             flag24 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Reliability"
                            << setfill(' ') << '|' << left << setw(83) << "Is the property that guarantees consistent intended behavior of an IoT system." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_12 = "RELI";
                         }
                         if(dataSent2Cloud == "Yes" && flag6_ != "2")
                         {
                             flag25 = "2";
                             file << setfill(' ') << '|' << left << setw(20) << "Integrity"
                            << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_2 = "INTG";
                         }
                         if(dataSent2Cloud == "Yes" && flag_6 != "2")
                         {
                             flag26 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Availability"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << " usable upon demand by authorized entities." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_6 = "AVAI";
                         }
                         if(dataSent2Cloud == "Yes")
                         {
                            flag27 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Data Freshness"
                            << setfill(' ') << '|' << left << setw(83) << "Ensures that data is the most recent, and that old messages cannot be replayed." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_13 = "DAFR";
                          }
                         if(dataSent2Cloud == "Yes" && flag10 != "2" && flag16 != "2")
                         {
                            flag28 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                            << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_9 = "FORE";
                         }
                         if(dataSent2Cloud == "Yes" && flag17 != "2" && flag19 != "2" && flag22 != "2" && domainSensitivity == 1)
                         {
                             flag29 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_5 = "NONR";
                         }
                         if(dataStoredInDb == "Yes" && flag7 != "2" && flag14 != "2" && flag22 != "2" )
                         {
                            flag30 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                            file<< left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_7 = "PHYS";
                         }
                         if(dataStoredInDb == "Yes" && flag6_ != "2" && flag25 != "2")
                         {
                             flag31 = "2";
                             file << setfill(' ') << '|' << left << setw(20) << "Integrity"
                            << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_2 = "INTG";
                         }
                         if(dataStoredInDb == "Yes" && flag_6 != "2" && flag26 != "2")
                         {
                             flag32 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Availability"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << " usable upon demand by authorized entities." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_6 = "AVAI";
                         }
                         if(dataStoredInDb == "Yes" && flag10 != "2" && flag16 != "2" && flag28 != "2")
                         {
                            flag33 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                            << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_9 = "FORE";
                         }
                         if(dataStoredInDb == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2")
                         {
                            flag34 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(dataStoredInDb == "Yes" && flag17 != "2" && flag19 != "2" && flag22 != "2" && flag29 != "2" && domainSensitivity == 1)
                         {
                             flag35 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_5 = "NONR";
                         }
                         if(update == "Yes" && flag_6 != "2" && flag26 != "2" && flag32 != "2")
                         {
                             flag36 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Availability"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << " usable upon demand by authorized entities." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_6 = "AVAI";
                         }

                         if(use3rdPrtySfw == "Yes" && flag21 != "2")
                         {
                            flag37 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Confinement"
                            << setfill(' ') << '|' << left << setw(83) << "Ensures that even if a party is corrupted, the spreading of the effects of the" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "attack is as confined as possible." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_10 = "CFMT";
                         }

                         if(evesdrop == "Yes" && flag9 != "2" && flag15 != "2" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes"))
                         {
                            flag39 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authorization"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_8 = "AUTR";
                         }
                         if(capt_Resent == "Yes" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes") && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2" && flag34 != "2")
                         {
                            flag40 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                         if(capt_Resent == "Yes" && flag27 != "2" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes"))
                         {
                            flag41 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Data Freshness"
                            << setfill(' ') << '|' << left << setw(83) << "Ensures that data is the most recent, and that old messages cannot be replayed." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_13 = "DAFR";
                          }
                         // impersontUsr
                         if(impersontUsr == "Yes" && Login == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2" && flag34 != "2" && flag40 != "2")
                           {
                            flag42 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Authentication"
                            << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_3 = "AUTH";
                         }
                        if(physiclAcces == "Yes" && flag7 != "2" && flag14 != "2" && flag22 != "2" && flag30 != "2")
                         {
                            flag43 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                            << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_7 = "PHYS";
                         }
                         if(use3rdPrtySfw == "Yes")
                        {
                            file << setfill(' ') << '|' << left << setw(20) << "Counterfeit "
                            << setfill(' ') << '|' << left << setw(83) << "Is the property that ensures effective validation of software such that any fake " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << "Resistance "
                            << setfill(' ') << '|' << left << setw(83) << "or maliciously modified software is rejected." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_14 = "CNFR";
                        }
                         if(physiclAcces == "Yes")
                         {
                             flag44 = "2";
                            file << setfill(' ') << '|' << left << setw(20) << "Tamper Detection"
                            << setfill(' ') << '|' << left << setw(83) << "Ensures all devices are physically secured, such that any tampering attempt is " << '|' << endl;
                            file << setfill(' ') << '|' << left << setw(20) << " "
                            << setfill(' ') << '|' << left << setw(83) << "detected." << '|' << endl;

                            file << left << setw(21) << setfill('-') << left<< '+'
                            << setw(84) << setfill('-') << '+' << '+' << endl;
                            Reqmt_15 = "TAMD";
                         }
                         flag1.erase(); flag2.erase(); flag3.erase(); flag4.erase(); flag5.erase();
                         state.erase(); Domain.erase(); anyUsr.erase(); Login.erase(); stoUsrInfo.erase(); stoAnyInfo.erase(); InfoType.erase(); infoSent2E.erase(); connected.erase(); dataSent2Cloud.erase(); dataStoredInDb.erase(); update.erase(); use3rdPrtySfw.erase(); evesdrop.erase(); capt_Resent.erase(); impersontUsr.erase(); physiclAcces.erase();

                          string request_query = "insert into generated_requirements (Reqst_ID, Reqmt_1, Reqmt_2, Reqmt_3, Reqmt_4, Reqmt_5, Reqmt_6, Reqmt_7, Reqmt_8, Reqmt_9, Reqmt_10, Reqmt_11, Reqmt_12, Reqmt_13, Reqmt_14, Reqmt_15) values('"+Reqst_ID+"', '"+Reqmt_1+"', '"+Reqmt_2+"', '"+Reqmt_3+"', '"+Reqmt_4+"', '"+Reqmt_5+"', '"+Reqmt_6+"', '"+Reqmt_7+"', '"+Reqmt_8+"', '"+Reqmt_9+"', '"+Reqmt_10+"', '"+Reqmt_11+"', '"+Reqmt_12+"', '"+Reqmt_13+"', '"+Reqmt_14+"', '"+Reqmt_15+"')";

                          const char* qr = request_query.c_str();
                          qstate = mysql_query(conn, qr);

                            if(!qstate)
                            {
                                 Reqmt_1.erase(); Reqmt_2.erase(); Reqmt_3.erase(); Reqmt_4.erase(); Reqmt_5.erase(); Reqmt_6.erase(); Reqmt_7.erase(); Reqmt_8.erase(); Reqmt_9.erase(); Reqmt_10.erase(); Reqmt_11.erase(); Reqmt_12.erase(); Reqmt_13.erase(); Reqmt_14.erase(); Reqmt_15.erase();
                            }
                    file.close();
             }
             else
             {
                cout <<"\n\tFile failed to open!" << endl;
             }
    }

    void Processing_and_Output::write_bestPracticeGuide_in_textFile(string Request_ID)
    {
            system("cls");
            string findbyID_query = "select * from users_requests_bp where Request_ID = " + ("'"+Request_ID+"'");
            const char* qn = findbyID_query.c_str();
            qstate = mysql_query(conn, qn);

            string Status, Struct1, Struct2, Struct3, Struct4, Struct5, Struct6, Struct7, Struct8, Struct9, Struct10, Struct11, anyUsr, usrRegist, typeOfRegist, anyUsrLogin, usrInput, holdUsrInfo, storeAnyInfo, sensitivOfInfo, typeOfAUTH, useDb;
            string typeOfDataStorg, typeOfDb, progrm1, progrm2, progrm3, progrm4, progrm5, progrm6, progrm7, progrm8, fileUpload, sysLog;

            if(!qstate)
            {
                res = mysql_store_result(conn);
                while((row = mysql_fetch_row(res)))
                {
                    Status = row[1];
                    Struct1 = row[2];
                    Struct2 = row[3];
                    Struct3 = row[4];
                    Struct4 = row[5];
                    Struct5 = row[6];
                    Struct6 = row[7];
                    Struct7 = row[8];
                    Struct8 = row[9];
                    Struct9 = row[10];
                    Struct10 = row[11];
                    Struct11 = row[12];
                    anyUsr = row[13];
                    usrRegist = row[14];
                    typeOfRegist = row[15];
                    anyUsrLogin = row[16];
                    usrInput = row[17];
                    holdUsrInfo = row[18];
                    storeAnyInfo = row[19];
                    sensitivOfInfo = row[20];
                    typeOfAUTH = row[21];
                    useDb = row[22];
                    typeOfDataStorg = row[23];
                    typeOfDb = row[24];
                    progrm1 = row[25];
                    progrm2 = row[26];
                    progrm3 = row[27];
                    progrm4 = row[28];
                    progrm5 = row[29];
                    progrm6 = row[30];
                    progrm7 = row[31];
                    progrm8 = row[32];
                    fileUpload = row[33];
                    sysLog = row[34];
                }
            }
            else
            {
                cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
            }

            fstream file;
            file.open("file_1.txt", ios::out | ios::trunc);
            if(file.is_open())
            {
                file << "\t  # THE BEST PRACTICE GUIDE FOR SECURE DEVELOPMENT REQUEST OF THE USER WITH REQUEST ID No.: " << Request_ID << endl << endl;



                file.close();
            }
            else
            {
                cout <<"\n\tFile failed to open!" << endl;
            }

    }

int Processing_and_Output::searchString(string s1, string s2)
{
    string s11, s22;
	s11=s1;
	s22 = s2;
	if(strstr(s11.c_str(),s22.c_str()))
	{
		return 1;
	}
	else
	{
		return -1;
	}
}

bool Processing_and_Output::isCapable(int cpu, double fms, double rs, double cs, int cpu_, double flash, double ram, double clock)
{
    if((cpu >= cpu_) && (fms >= flash) && (rs >= ram) && (cs >= clock))
    {
        return true;
    }
    else
    {
       return false;
    }
}

string Processing_and_Output::concatStrings(string r1, string r2, string r3, string r4, string r5, string r6)
{
  string reqmts;
  reqmts += " ";
  if(!r1.empty())
  reqmts += r1;
  reqmts += " ";
  if(!r2.empty())
  reqmts += r2;
  reqmts += " ";
  if(!r3.empty())
  reqmts += r3;
  reqmts += " ";
  if(!r4.empty())
  reqmts += r4;
  reqmts += " ";
  if(!r5.empty())
  reqmts += r5;
  reqmts += " ";
  if(!r6.empty())
  reqmts += r6;

  return reqmts;
}

auto Processing_and_Output::mapping1(string userR, string r_1, string r_2, string r_3, string r_4, string r_5, string r_6, string r1, string r2, string r3, string r4, string r5, string r6)
{
            struct result
            {
                int int1;
                int int2;
                int int3;
                int int4;
                int int5;
                int int6;
            };

    userR = concatStrings(r_1, r_2, r_3, r_4, r_5, r_6);
     int flag1 = searchString(userR, r1);
     int flag2 = searchString(userR, r2);
     int flag3 = searchString(userR, r3);
     int flag4 = searchString(userR, r4);
     int flag5 = searchString(userR, r5);
     int flag6 = searchString(userR, r6);

    return result {flag1, flag2, flag3, flag4, flag5, flag6};
}

auto Processing_and_Output::mapping1b(string userR, string r_1, string r_2, string r_3, string r_4, string r_5, string r_6, string r1, string r2, string r3, string r4, string r5, string r6)
{
            struct result
            {
                int int1;
                int int2;
                int int3;
                int int4;
                int int5;
                int int6;
            };

    userR = concatStrings(r_1, r_2, r_3, r_4, r_5, r_6);

     int flag1 = searchString(userR, r1);
     int flag2 = searchString(userR, r2);
     int flag3 = searchString(userR, r3);
     int flag4 = searchString(userR, r4);
     int flag5 = searchString(userR, r5);
     int flag6 = searchString(userR, r6);
    return result {flag1, flag2, flag3, flag4, flag5, flag6};
}

int Processing_and_Output::checkSensitivity_of_User_ApplcArea(string as)
{
    string sensitive_areas = "Healthcare Health Connected_Car Military Security Transportation Agriculture Agric Retail Industrial Factory Supply_Chain Financial Finance Bank Banking Elderly Child Kid Grid City Wearable Home";
    int searchResult = searchString(sensitive_areas, as);

    if(searchResult == 1)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}

int Processing_and_Output::Check_if_streamCipherNeeded(string ps)
{
    string where_SC_needed = "continuous unknown";
    int SC_needed = searchString(where_SC_needed, ps);

    if(SC_needed == 1)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}

auto Processing_and_Output::select_MarchingAlgo(int flagx, int ds, int n_SC, int cpu_int, double fms_doub, double rs_doub)
{
         struct result
            {
                int n1;
                int n2;
            };

            int num1, num2;

            int cpu1 = 32, cpu2 = 16, cpu3 = 8, cpu4 = 8, cpu5 = 64;
            double fms1 = 1.00, rs1 = 1.00, fms11 = 1.00, rs11 = 1.00;
            double fms2 = 10.00, rs2 = 1.00, fms22 = 1.00, rs22 = 1.00;
            double fms3 = 1.00, rs3 = 1.00, fms33 = 1.00, rs33 = 1.00;
            double fms4 = 1.00, rs4 = 1.00, fms44 = 1.00, rs44 = 1.00;
            double fms5 = 1.00, rs5 = 1.00, fms55 = 1.00, rs55 = 1.00;


        if(flagx == -1)
        {
            num1 = 0; num2 = 0;
            return result {num1, num2};
        }
        else if((flagx == 1) && (ds == 1) && (cpu_int >= cpu5) && (fms_doub <= 524288000*fms5 && fms_doub >= 4000000*fms55) && (rs_doub <= 16777216*rs5 && rs_doub >= 1000000*rs55))
        {
            if(n_SC == 1)
              {
                num1 = 9; num2 = 1;
                return result {num1, num2};
              }
            else
            {
                num1 = 9; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cpu_int >= cpu5) && (fms_doub <= 524288000*fms5 && fms_doub >= 4000000*fms55) && (rs_doub <= 16777216*rs5 && rs_doub >= 1000000*rs55))
        {
            if(n_SC == 1)
             {
                num1 = 10; num2 = 1;
                return result {num1, num2};
             }
            else
            {
                num1 = 10; num2 = 0;
                return result {num1, num2};
            }
        }
       else if((flagx == 1) && (ds == 1) && (cpu_int >= cpu1) && (fms_doub <= 32212254*fms1 && fms_doub >= 2000000*fms11) && (rs_doub <= 10000000*rs1 && rs_doub >= 250000*rs11))
        {
            if(n_SC == 1)
            {
                num1 = 1; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 1; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cpu_int >= cpu1) && (fms_doub <= 32212254*fms1 && fms_doub >= 2000000*fms11) && (rs_doub <= 10000000*rs1 && rs_doub >= 250000*rs11))
        {
             if(n_SC == 1)
            {
                num1 = 2; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 2; num2 = 0;
                return result {num1, num2};
            }
        }
       else if((flagx == 1) && (ds == 1) && (cpu_int >= cpu2) && (fms_doub <= 3221225*fms2 && fms_doub >= 100000*fms22) && (rs_doub <= 1000000*rs2 && rs_doub >= 10000*rs22))
        {
             if(n_SC == 1)
            {
                num1 = 3; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 3; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cpu_int >= cpu2) && (fms_doub <= 3221225*fms2 && fms_doub >= 100000*fms22) && (rs_doub <= 1000000*rs2 && rs_doub >= 1000*rs22))
        {
              if(n_SC == 1)
            {
                num1 = 4; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 4; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (cpu_int >= cpu3) && (fms_doub <= 322122*fms3 && fms_doub >= 64*fms33) && (rs_doub <= 10000*rs3 && rs_doub >= 6*rs33))
        {
             if(n_SC == 1)
            {
                num1 = 5; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 5; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cpu_int >= cpu3) && (fms_doub <= 322122*fms3 && fms_doub >= 64*fms33) && (rs_doub <= 10000*rs3 && rs_doub >= 6*rs33))
        {
              if(n_SC == 1)
            {
                num1 = 6; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 6; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cpu_int >= cpu4) && (fms_doub <= 32212*fms4 && fms_doub >= 10*fms44) && (rs_doub <= 5000*rs4 && rs_doub >= 4*rs44))
        {
              if(n_SC == 1)
              {
                num1 = 7; num2 = 1;
                return result {num1, num2};
              }
            else
            {
                num1 = 7; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cpu_int >= cpu4) && (fms_doub <= 32212*fms4 && fms_doub >= 10*fms44) && (rs_doub <= 5000*rs4 && rs_doub >= 4*rs44))
        {
             if(n_SC == 1)
             {
                num1 = 8; num2 = 1;
                return result {num1, num2};
             }
            else
            {
                num1 = 8; num2 = 0;
                return result {num1, num2};
            }
        }
        else
        {
            num1 = -1, num2 = 0;
            return result {num1, num2};
        }
}

auto Processing_and_Output::select_MarchingAlgo2_ThreeSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type)
{
         struct result
        {
            int n1;
            int n2;
        };
            int num1, num2;

            double cctay1, cctaz1, tpy1, tpz1, cctay2, cctaz2, tpy2, tpz2, cctay3, cctaz3, tpy3, tpz3;

            if(type == "FPGA")
            {
                cctay1 = 1.0, cctaz1 = 1.0, tpy1 = 1.0, tpz1 = 1.0;
                cctay2 = 1.0, cctaz2 = 1.0, tpy2 = 1.0, tpz2 = 1.0;
                cctay3 = 1.0, cctaz3 = 1.0, tpy3 = 1.0, tpz3 = 1.0;
            }
            else if(type == "ASIC")
            {
                cctay1 = 1.0, cctaz1 = 1.0, tpy1 = 1.0, tpz1 = 1.0;
                cctay2 = 1.0, cctaz2 = 1.0, tpy2 = 1.0, tpz2 = 1.0;
                cctay3 = 1.0, cctaz3 = 1.0, tpy3 = 1.0, tpz3 = 1.0;
            }



        if(flagx == -1)
        {
            num1 = 0; num2 = 0;
            return result {num1, num2};
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1& tpx <= tpz1))
        {
            if(n_SC == 1)
            {
                num1 = 1; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 1; num2 = 0;
                return result {num1, num2};
            }

        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
        {
             if(n_SC == 1)
            {
                num1 = 2; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 2; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
             if(n_SC == 1)
            {
                num1 = 3; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 3; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
              if(n_SC == 1)
            {
                num1 = 4; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 4; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
             if(n_SC == 1)
            {
                num1 = 5; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 5; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
              if(n_SC == 1)
            {
                num1 = 6; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 6; num2 = 0;
                return result {num1, num2};
            }
        }
        else
        {
            num1 = -1, num2 = 0;
            return result {num1, num2};
        }
}

auto Processing_and_Output::select_MarchingAlgo2_FourSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type)
{
         struct result
        {
            int n1;
            int n2;
        };
            int num1, num2;

            double cctay1, cctaz1, tpy1, tpz1, cctay2, cctaz2, tpy2, tpz2, cctay3, cctaz3, tpy3, tpz3, cctay4, cctaz4, tpy4, tpz4; //cctay5, cctaz5, tpy5, tpz5;

            if(type == "FPGA")
            {
                cctay1 = 1348.0, cctaz1 = 4500.0, tpy1 = 1.0, tpz1 = 256.9;
                cctay2 = 891.0, cctaz2 = 1347.9, tpy2 = 1.0, tpz2 = 280.9;
                cctay3 = 413.0, cctaz3 = 890.9, tpy3 = 1.0, tpz3 = 347.0;
                cctay4 = 135.0, cctaz4 = 412.9, tpy4 = 1.0, tpz4 = 389.0;
            }
            else if(type == "ASIC")
            {
                cctay1 = 7950.0, cctaz1 = 9000.0, tpy1 = 1.0, tpz1 = 5.5;//
                cctay2 = 6000.0, cctaz2 = 7949.0, tpy2 = 1.0, tpz2 = 5.3;//
                cctay3 = 3100.0, cctaz3 = 5999.0, tpy3 = 1.0, tpz3 = 6.0;//
                cctay4 = 2860.0, cctaz4 = 3099.0, tpy4 = 1.0, tpz4 = 5.0;//
            }

        if(flagx == -1)
        {
            num1 = 0; num2 = 0;
            return result {num1, num2};
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1& tpx <= tpz1))
        {
            if(n_SC == 1)
            {
                num1 = 1; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 1; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
        {
             if(n_SC == 1)
            {
                num1 = 2; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 2; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
             if(n_SC == 1)
            {
                num1 = 3; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 3; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
              if(n_SC == 1)
            {
                num1 = 4; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 4; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
             if(n_SC == 1)
            {
                num1 = 5; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 5; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
              if(n_SC == 1)
            {
                num1 = 6; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 6; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
        {
             if(n_SC == 1)
            {
                num1 = 7; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 7; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
        {
              if(n_SC == 1)
            {
                num1 = 8; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 8; num2 = 0;
                return result {num1, num2};
            }
        }

        else
        {
            num1 = -1, num2 = 0;
            return result {num1, num2};
        }
}

auto Processing_and_Output::select_MarchingAlgo2_SixSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type)
{
         struct result
        {
            int n1;
            int n2;
        };
            int num1, num2;

            double cctay1, cctaz1, tpy1, tpz1, cctay2, cctaz2, tpy2, tpz2, cctay3, cctaz3, tpy3, tpz3, cctay4, cctaz4, tpy4, tpz4, cctay5, cctaz5, tpy5, tpz5, cctay6, cctaz6, tpy6, tpz6;

            if(type == "FPGA")
            {
                cctay1 = 1.0, cctaz1 = 1.0, tpy1 = 1.0, tpz1 = 1.0;
                cctay2 = 1.0, cctaz2 = 1.0, tpy2 = 1.0, tpz2 = 1.0;
                cctay3 = 1.0, cctaz3 = 1.0, tpy3 = 1.0, tpz3 = 1.0;
                cctay4 = 1.0, cctaz4 = 1.0, tpy4 = 1.0, tpz4 = 1.0;
                cctay5 = 1.0, cctaz5 = 1.0, tpy5 = 1.0, tpz5 = 1.0;
                cctay6 = 1.0, cctaz6 = 1.0, tpy6 = 1.0, tpz6 = 1.0;
            }
            else if(type == "ASIC")
            {
                cctay1 = 738.0, cctaz1 = 864.0, tpy1 = 0.8, tpz1 = 1.0;//
                cctay2 = 865.0, cctaz2 = 1060.0, tpy2 = 0.3, tpz2 = 2.8;//
                cctay3 = 1061.0, cctaz3 = 1127.0, tpy3 = 0.5, tpz3 = 17.8;//
                cctay4 = 1128.0, cctaz4 = 1396.0, tpy4 = 1.0, tpz4 = 2.7;//
                cctay5 = 1397.0, cctaz5 = 2190.0, tpy5 = 2.7, tpz5 = 17.8;//
                cctay6 = 2191.0, cctaz6 = 4362.0, tpy6 = 0.4, tpz6 = 50.0;
            }

        if(flagx == -1)
        {
            num1 = 0; num2 = 0;
            return result {num1, num2};
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
        {
            if(n_SC == 1)
            {
                num1 = 1; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 1; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
        {
             if(n_SC == 1)
            {
                num1 = 2; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 2; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
             if(n_SC == 1)
            {
                num1 = 3; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 3; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
        {
              if(n_SC == 1)
            {
                num1 = 4; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 4; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
             if(n_SC == 1)
            {
                num1 = 5; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 5; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
        {
              if(n_SC == 1)
            {
                num1 = 6; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 6; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
        {
             if(n_SC == 1)
            {
                num1 = 7; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 7; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
        {
              if(n_SC == 1)
            {
                num1 = 8; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 8; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (cctax >= cctay5 && cctax <= cctaz5) && (tpx >= tpy5 && tpx <= tpz5))
        {
             if(n_SC == 1)
            {
                num1 = 9; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 9; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay5 && cctax <= cctaz5) && (tpx >= tpy5 && tpx <= tpz5))
        {
              if(n_SC == 1)
            {
                num1 = 10; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 10; num2 = 0;
                return result {num1, num2};
            }
        }
          else if((flagx == 1) && (ds == 1) && (cctax >= cctay6 && cctax <= cctaz6) && (tpx >= tpy6 && tpx <= tpz6))
        {
             if(n_SC == 1)
            {
                num1 = 11; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 11; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (cctax >= cctay6 && cctax <= cctaz6) && (tpx >= tpy6 && tpx <= tpz6))
        {
              if(n_SC == 1)
            {
                num1 = 12; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 12; num2 = 0;
                return result {num1, num2};
            }
        }
        else
        {
            num1 = -1, num2 = 0;
            return result {num1, num2};
        }
}

auto Processing_and_Output::select_MarchingAlgo2_SevenSteps(int flagx, int ds, int n_SC, double cctax, double tpx, string type)
{
         struct result
        {
            int n1;
            int n2;
        };
            int num1, num2;

            double cctay1, cctaz1, tpy1, tpz1, cctay2, cctaz2, tpy2, tpz2, cctay3, cctaz3, tpy3, tpz3, cctay4, cctaz4, tpy4, tpz4, cctay5, cctaz5, tpy5, tpz5, cctay6, cctaz6, tpy6, tpz6, cctay7, cctaz7, tpy7, tpz7;

            if(type == "FPGA")
            {
                cctay1 = 1.0, cctaz1 = 1.0, tpy1 = 1.0, tpz1 = 1.0;
                cctay2 = 1.0, cctaz2 = 1.0, tpy2 = 1.0, tpz2 = 1.0;
                cctay3 = 1.0, cctaz3 = 1.0, tpy3 = 1.0, tpz3 = 1.0;
                cctay4 = 1.0, cctaz4 = 1.0, tpy4 = 1.0, tpz4 = 1.0;
                cctay5 = 1.0, cctaz5 = 1.0, tpy5 = 1.0, tpz5 = 1.0;
                cctay6 = 1.0, cctaz6 = 1.0, tpy6 = 1.0, tpz6 = 1.0;
                cctay7 = 1.0, cctaz6 = 1.0, tpy6 = 1.0, tpz6 = 1.0;

            }
            else if(type == "ASIC")
            {
                cctay1 = 810.0, cctaz1 = 970.0, tpy1 = 4.2, tpz1 = 5.1;
                cctay2 = 971.0, cctaz2 = 1110.0, tpy2 = 3.4, tpz2 = 16.3;
                cctay3 = 1111.0, cctaz3 = 1400.0, tpy3 = 3.0, tpz3 = 12.1;
                cctay4 = 1401.0, cctaz4 = 1570.0, tpy4 = 177.8, tpz4 = 237.0;
                cctay5 = 1571.0, cctaz5 = 1799, tpy5 = 2.6, tpz5 = 200.0;
                cctay6 = 1800.0, cctaz6 = 2500, tpy6 = 2.8, tpz6 = 193.9;
                cctay7 = 2501.0, cctaz7 = 8600, tpy7 = 133.3, tpz7 = 6400.1;
            }

    if(n_SC ==1)
    {
               if(flagx == -1)
               {
                    num1 = 0; num2 = 0;
                    return result {num1, num2};
              }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay5 && cctax <= cctaz5))
            {
                if(n_SC == 1)
                  {
                    num1 = 9; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 9; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay5 && cctax <= cctaz5))
            {
                if(n_SC == 1)
                 {
                    num1 = 10; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 10; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay6 && cctax <= cctaz6))
            {
                if(n_SC == 1)
                  {
                    num1 = 11; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 11; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay6 && cctax <= cctaz6))
            {
                if(n_SC == 1)
                 {
                    num1 = 12; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 12; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay7 && cctax <= cctaz7))
            {
                if(n_SC == 1)
                  {
                    num1 = 13; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 13; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay7 && cctax <= cctaz7))
            {
                if(n_SC == 1)
                 {
                    num1 = 14; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 14; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay1 && cctax <= cctaz1))
            {
                if(n_SC == 1)
                {
                    num1 = 1; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 1; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay1 && cctax <= cctaz1))
            {
                 if(n_SC == 1)
                {
                    num1 = 2; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 2; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay2 && cctax <= cctaz2))
            {
                 if(n_SC == 1)
                {
                    num1 = 3; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 3; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay2 && cctax <= cctaz2))
            {
                  if(n_SC == 1)
                {
                    num1 = 4; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 4; num2 = 0;
                    return result {num1, num2};
                }
            }
             else if((flagx == 1) && (ds == 1) && (cctax >= cctay3 && cctax <= cctaz3))
            {
                 if(n_SC == 1)
                {
                    num1 = 5; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 5; num2 = 0;
                    return result {num1, num2};
                }
            }
             else if((flagx == 1) && (ds != 1) && (cctax >= cctay3 && cctax <= cctaz3))
            {
                  if(n_SC == 1)
                {
                    num1 = 6; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 6; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay4 && cctax <= cctaz4))
            {
                  if(n_SC == 1)
                {
                    num1 = 7; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 7; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay4 && cctax <= cctaz4))
            {
                 if(n_SC == 1)
                {
                    num1 = 8; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 8; num2 = 0;
                    return result {num1, num2};
                }
            }
            else
            {
                num1 = -1, num2 = 0;
                return result {num1, num2};
            }
    }
    else
    {
          if(flagx == -1)
               {
                    num1 = 0; num2 = 0;
                    return result {num1, num2};
              }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay5 && cctax <= cctaz5) && (tpx >= tpy5 && tpx <= tpz5))
            {
                if(n_SC == 1)
                  {
                    num1 = 9; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 9; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay5 && cctax <= cctaz5) && (tpx >= tpy5 && tpx <= tpz5))
            {
                if(n_SC == 1)
                 {
                    num1 = 10; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 10; num2 = 0;
                    return result {num1, num2};
                }

            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay6 && cctax <= cctaz6) && (tpx >= tpy6 && tpx <= tpz6))
            {
                if(n_SC == 1)
                  {
                    num1 = 11; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 11; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay6 && cctax <= cctaz6) && (tpx >= tpy6 && tpx <= tpz6))
            {
                if(n_SC == 1)
                 {
                    num1 = 12; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 12; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay7 && cctax <= cctaz7) && (tpx >= tpy7 && tpx <= tpz7))
            {
                if(n_SC == 1)
                  {
                    num1 = 13; num2 = 1;
                    return result {num1, num2};
                  }
                else
                {
                    num1 = 13; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay7 && cctax <= cctaz7) && (tpx >= tpy7 && tpx <= tpz7))
            {
                if(n_SC == 1)
                 {
                    num1 = 14; num2 = 1;
                    return result {num1, num2};
                 }
                else
                {
                    num1 = 14; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
            {
                if(n_SC == 1)
                {
                    num1 = 1; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 1; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay1 && cctax <= cctaz1) && (tpx >= tpy1 && tpx <= tpz1))
            {
                 if(n_SC == 1)
                {
                    num1 = 2; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 2; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
            {
                 if(n_SC == 1)
                {
                    num1 = 3; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 3; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay2 && cctax <= cctaz2) && (tpx >= tpy2 && tpx <= tpz2))
            {
                  if(n_SC == 1)
                {
                    num1 = 4; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 4; num2 = 0;
                    return result {num1, num2};
                }
            }
             else if((flagx == 1) && (ds == 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
            {
                 if(n_SC == 1)
                {
                    num1 = 5; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 5; num2 = 0;
                    return result {num1, num2};
                }
            }
             else if((flagx == 1) && (ds != 1) && (cctax >= cctay3 && cctax <= cctaz3) && (tpx >= tpy3 && tpx <= tpz3))
            {
                  if(n_SC == 1)
                {
                    num1 = 6; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 6; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds == 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
            {
                  if(n_SC == 1)
                {
                    num1 = 7; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 7; num2 = 0;
                    return result {num1, num2};
                }
            }
            else if((flagx == 1) && (ds != 1) && (cctax >= cctay4 && cctax <= cctaz4) && (tpx >= tpy4 && tpx <= tpz4))
            {
                 if(n_SC == 1)
                {
                    num1 = 8; num2 = 1;
                    return result {num1, num2};
                }
                else
                {
                    num1 = 8; num2 = 0;
                    return result {num1, num2};
                }
            }
            else
            {
                num1 = -1, num2 = 0;
                return result {num1, num2};
            }
    }
}

auto Processing_and_Output::mapping2(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, int cpu_int, double fms_doub, double rs_doub, string as, string ps)
{
            struct result
            {
                int int_1;
                int p1;
                int int_2;
                int int_3;
                int int_4;
                int p4;
                int int_5;
                int int_6;
                int p6;
            };

        int algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6;

       int domain_sensitivity = checkSensitivity_of_User_ApplcArea(as);
       int ds = domain_sensitivity;
       int needFor_SC = Check_if_streamCipherNeeded(ps);
       int n_SC = needFor_SC;

        auto s_MA_result1 = select_MarchingAlgo(flag1, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo1 = s_MA_result1.n1; ps1 = s_MA_result1.n2;

       auto s_MA_result2 = select_MarchingAlgo(flag2, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo2 = s_MA_result2.n1;

       auto s_MA_result3 = select_MarchingAlgo(flag3, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo3 = s_MA_result3.n1;

       auto s_MA_result4 = select_MarchingAlgo(flag4, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo4 = s_MA_result4.n1; ps4 = s_MA_result4.n2;

       auto s_MA_result5 = select_MarchingAlgo(flag5, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo5 = s_MA_result5.n1;

       auto s_MA_result6 = select_MarchingAlgo(flag6, ds, n_SC, cpu_int, fms_doub, rs_doub);
       algo6 = s_MA_result6.n1; ps6 = s_MA_result6.n2;

    return result {algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6};
}

auto Processing_and_Output::mapping2Hardware(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, double ccta1_doub, double tp1_doub, double ccta2_doub, double tp2_doub, double ccta3_doub, double tp3_doub, double ccta4_doub, double tp4_doub, double ccta5_doub, double tp5_doub, double ccta6_doub, double tp6_doub, string as, string ps, string type)
{
            struct result
            {
                int int_1;
                int p1;
                int int_2;
                int int_3;
                int int_4;
                int p4;
                int int_5;
                int int_6;
                int p6;
            };

        int algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6;
       int domain_sensitivity = checkSensitivity_of_User_ApplcArea(as);
       int ds = domain_sensitivity;
       int needFor_StreamCipher = Check_if_streamCipherNeeded(ps);
       int n_SC = needFor_StreamCipher;
       auto s_MA_result1 = select_MarchingAlgo2_SevenSteps(flag1, ds, n_SC, ccta1_doub, tp1_doub, type);
       algo1 = s_MA_result1.n1; ps1 = s_MA_result1.n2;
       auto s_MA_result2 = select_MarchingAlgo2_SixSteps(flag2, ds, n_SC, ccta2_doub, tp2_doub, type);
       algo2 = s_MA_result2.n1;
       auto s_MA_result3 = select_MarchingAlgo2_ThreeSteps(flag3, ds, n_SC, ccta3_doub, tp3_doub, type);
       algo3 = s_MA_result3.n1;
       auto s_MA_result4 = select_MarchingAlgo2_SevenSteps(flag4, ds, n_SC, ccta4_doub, tp4_doub, type);
       algo4 = s_MA_result4.n1; ps4 = s_MA_result4.n2;
       auto s_MA_result5 = select_MarchingAlgo2_ThreeSteps(flag5, ds, n_SC, ccta5_doub, tp5_doub, type);
       algo5 = s_MA_result5.n1;
       auto s_MA_result6 = select_MarchingAlgo2_FourSteps(flag6, ds, n_SC, ccta6_doub, tp6_doub, type);
       algo6 = s_MA_result6.n1; ps6 = s_MA_result6.n2;

    return result {algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6};
}

string Processing_and_Output::fetch_Algo(string IDx)
{
     string ID, block_size, key_size, cipher_name;
     ID = IDx;

    if(ID == "0")
    {
        cipher_name = "";
        return cipher_name;
    }
    else
    {
        string findbyID_query = "select * from crypto_algor where ID = " + ("'" + ID + "'");
        const char* qn = findbyID_query.c_str();
        qstate = mysql_query(conn, qn);

        if(!qstate)
        {
            res = mysql_store_result(conn);
            while((row = mysql_fetch_row(res)))
            {
                cipher_name = row[1];
                block_size = row[2];
                key_size = row[3];
            }
            return cipher_name;
        }
        else
        {
            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
        }
    }
}

auto Processing_and_Output::display_Mech_Algo_mapping(int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6)
{
     struct result
            {
                string st_1;
                string st_2;
                string st_3;
                string st_4;
                string st_5;
                string st_6;
            };

    string algName1, algName2, algName3, algName4, algName5, algName6;
    string ID1, ID2, ID3, ID4, ID5, ID6;

    if(algo1 != 0)
    {
       if(ps1 != 1)
       {
            if(algo1 == 1)
            {
                ID1 = "B30";
            }
            else if(algo1 == 2)
            {
                ID1 = "B29";
            }
            else if(algo1 == 3)
            {
                ID1 = "B33";
            }
            else if(algo1 == 4)
            {
                ID1 = "B2";
            }
            else if(algo1 == 5)
            {
                ID1 = "B14";
            }
             else if(algo1 == 6)
            {
                ID1 = "B13";
            }
            else if(algo1 == 7)
            {
                ID1 = "B13";
            }
            else if(algo1 == 8)
            {
                ID1 = "B11";
            }
             else if(algo1 == 9)
            {
                ID1 = "B29";
            }
            else if(algo1 == 10)
            {
                ID1 = "B28";
            }
            else
            {
                ID1 = "0";
            }
         algName1 = fetch_Algo(ID1);
       }
       else if(ps1 ==1)
       {
           if(algo1 == 1)
            {
                ID1 = "S2";
            }
            else if(algo1 == 2)
            {
                ID1 = "S2";
            }
            else if(algo1 == 3)
            {
                ID1 = "S2";
            }
            else if(algo1 == 4)
            {
                ID1 = "S1";
            }
             else if(algo1 == 5)
            {
                ID1 = "S2";
            }
             else if(algo1 == 6)
            {
                ID1 = "S1";
            }
             else if(algo1 == 7)
            {
                ID1 = "S2";
            }
            else if(algo1 == 8)
            {
                ID1 = "S1";
            }
             else if(algo1 == 9)
            {
                ID1 = "S2";
            }
            else if(algo1 == 10)
            {
                ID1 = "S3";
            }
           algName1 = fetch_Algo(ID1);
      }
    }
 // /*
    if(algo2 != 0)
    {
        if(algo2 == 1)
        {
            ID2 = "H10";
        }
        else if(algo2 == 2)
        {
            ID2 = "H10";
        }
        else if(algo2 == 3)
        {
            ID2 = "H8";
        }
        else if(algo2 == 4)
        {
            ID2 = "H8";
        }
        else if(algo2 == 5)
        {
            ID2 = "H6";
        }
        else if(algo2 == 6)
        {
            ID2 = "H6";
        }
        else if(algo2 == 7)
        {
            ID2 = "H4";
        }
        else if(algo2 == 8)
        {
            ID2 = "H4";
        }
        else if(algo2 == 9)
        {
            ID2 = "H12";
        }
        else if(algo2 == 10)
        {
            ID2 = "H12";
        }
        else
        {
            ID2 = "0";
        }
      algName2 = fetch_Algo(ID2);
    }

    if(algo3 != 0)
    {
        if(algo3 == 1)
        {
            ID3 = "0";
        }
        else if(algo3 == 2)
        {
            ID3 = "0";
        }
        else if(algo3 == 3)
        {
            ID3 = "0";
        }
        else if(algo3 == 4)
        {
            ID3 = "0";
        }
        else if(algo3 == 5)
        {
            ID3 = "0";
        }
        else if(algo3 == 6)
        {
            ID3 = "0";
        }
        else if(algo3 == 7)
        {
            ID3 = "0";
        }
        else if(algo3 == 8)
        {
            ID3 = "0";
        }
        else if(algo3 == 9)
        {
            ID3 = "M1";
        }
        else if(algo3 == 10)
        {
            ID3 = "M1";
        }
        else
        {
            ID3 = "0";
        }
     algName3 = fetch_Algo(ID3);
    }

    if(algo4 != 0)
    {
        if(ps4 != 1)
        {
            if(algo4 == 1)
            {
                ID4 = "B30";
            }
            else if(algo4 == 2)
            {
                ID4 = "B28";
            }
            else if(algo4 == 3)
            {
                ID4 = "B33";
            }
            else if(algo4 == 4)
            {
                ID4 = "B2";
            }
            else if(algo4 == 5)
            {
                ID4 = "B14";
            }
            else if(algo4 == 6)
            {
                ID4 = "B13";
            }
            else if(algo4 == 7)
            {
                ID4 = "B12";
            }
            else if(algo4 == 8)
            {
                ID4 = "B11";
            }
            else if(algo4 == 9)
            {
                ID4 = "B29";
            }
            else if(algo4 == 10)
            {
                ID4 = "B28";
            }
            else
            {
                ID4 = "0";
            }
         algName4 = fetch_Algo(ID4);
        }
        else if(ps4 == 1)
        {
            if(algo4 == 1)
            {
                ID4 = "S2";
            }
            else if(algo4 == 2)
            {
                ID4 = "S2";
            }
            else if(algo4 == 3)
            {
                ID4 = "S2";
            }
            else if(algo4 == 4)
            {
                ID4 = "S1";
            }
            else if(algo4 == 5)
            {
                ID4 = "S2";
            }
            else if(algo4 == 6)
            {
                ID4 = "S1";
            }
             else if(algo4 == 7)
            {
                ID4 = "S2";
            }
            else if(algo4 == 8)
            {
                ID4 = "S1";
            }
            else if(algo4 == 9)
            {
                ID4 = "S2";
            }
            else if(algo4 == 10)
            {
                ID4 = "S2";
            }
          algName4 = fetch_Algo(ID4);
        }
    }

    if(algo5 != 0)
    {
        if(algo5 == 1)
        {
            ID5 = "0";
        }
        else if(algo5 == 2)
        {
            ID5 = "0";
        }
        else if(algo5 == 3)
        {
            ID5 = "0";
        }
        else if(algo5 == 4)
        {
            ID5 = "0";
        }
        else if(algo5 == 5)
        {
            ID5 = "0";
        }
        else if(algo5 == 6)
        {
            ID5 = "0";
        }
        else if(algo5 == 7)
        {
            ID5 = "0";
        }
        else if(algo5 == 8)
        {
            ID5 = "0";
        }
        else if(algo5 == 9)
        {
            ID5 = "0";
        }
        else if(algo5 == 10)
        {
            ID5 = "0";
        }
        else
        {
            ID5 = "0";
        }
      algName5 = fetch_Algo(ID5);
    }

    if(algo6 != 0)
    {
       if(ps6 != 1)
       {
            if(algo6 == 1)
            {
                ID6 = "A13";
            }
            else if(algo6 == 2)
            {
                ID6 = "A13";
            }
            else if(algo6 == 3)
            {
                ID6 = "A4";
            }
            else if(algo6 == 4)
            {
                ID6 = "A12";
            }
            else if(algo6 == 5)
            {
                ID6 = "A4";
            }
            else if(algo6 == 6)
            {
                ID6 = "A13";
            }
            else if(algo6 == 7)
            {
                ID6 = "A1";
            }
            else if(algo6 == 8)
            {
                ID6 = "A1";
            }
            else if(algo6 == 9)
            {
                ID6 = "A13";
            }
            else if(algo6 == 10)
            {
                ID6 = "A6";
            }
            else
            {
                ID6 = "0";
            }
         algName6 =  fetch_Algo(ID6);
       }
       else if(ps6 == 1)
       {
            if(algo6 == 1)
            {
                ID6 = "A10";
            }
            else if(algo6 == 2)
            {
                ID6 = "A10"; //ACORN
            }
            else if(algo6 == 3)
            {
                ID6 = "A10"; //ACORN
            }
            else if(algo6 == 4)
            {
                ID6 = "A10";
            }
            else if(algo6 == 5)
            {
                ID6 = "A10";//ACORN
            }
            else if(algo6 == 6)
            {
                ID6 = "A10";//ACORN
            }
            else if(algo6 == 7)
            {
                ID6 = "0";
            }
            else if(algo6 == 8)
            {
                ID6 = "0";
            }
            else if(algo6 == 9)
            {
                ID6 = "A9";
            }
            else if(algo6 == 10)
            {
                ID6 = "A9";//AES-GCM
            }
           algName6 = fetch_Algo(ID6);
       }
    }
  return result {algName1, algName2, algName3, algName4, algName5, algName6};
}

auto Processing_and_Output::display_Mech_Algo_mapping2(int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6, string energy)
{
    struct result
            {
                string st1;
                string st2;
                string st3;
                string st4;
                string st5;
                string st6;
            };
        string alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name;

    string ID1, ID2, ID3, ID4, ID5, ID6;

        if(energy == "Low")
        {
                    if(algo1 != 0)
                    {
                       if(ps1 != 1)
                       {
                            if(algo1 == 1)
                            {
                                ID1 = "B40";
                            }
                            else if(algo1 == 2)
                            {
                                ID1 = "B39";
                            }
                            else if(algo1 == 3)
                            {
                                ID1 = "B25";
                            }
                            else if(algo1 == 4)
                            {
                                ID1 = "B25";
                            }
                            else if(algo1 == 5)
                            {
                                ID1 = "B26";
                            }
                             else if(algo1 == 6)
                            {
                                ID1 = "B26";
                            }
                            else if(algo1 == 7)
                            {
                                ID1 = "B26";
                            }
                            else if(algo1 == 8)
                            {
                                ID1 = "B26";
                            }
                            else if(algo1 == 9)
                            {
                                ID1 = "B34";
                            }
                            else if(algo1 == 10)
                            {
                                ID1 = "B34";
                            }
                            else if(algo1 == 11)
                            {
                                ID1 = "B35";
                            }
                            else if(algo1 == 12)
                            {
                                ID1 = "B3";
                            }
                            else if(algo1 == 13)
                            {
                                ID1 = "B4";
                            }
                            else if(algo1 == 14)
                            {
                                ID1 = "B28";
                            }
                            else
                            {
                                ID1 = "0";
                            }
                       }
                       else if(ps1 ==1)
                       {
                           if(algo1 == 1)
                            {
                                ID1 = "0"; //
                            }
                            else if(algo1 == 2)
                            {
                                ID1 = "0"; //
                            }
                            else if(algo1 == 3)
                            {
                                ID1 = "0"; //
                            }
                            else if(algo1 == 4)
                            {
                                ID1 = "0"; //
                            }
                             else if(algo1 == 5)
                            {
                                ID1 = "S7";
                            }
                             else if(algo1 == 6)
                            {
                                ID1 = "S7";
                            }
                             else if(algo1 == 7)
                            {
                                ID1 = "S7";
                            }
                            else if(algo1 == 8)
                            {
                                ID1 = "S7";
                            }
                            else if(algo1 == 9)
                            {
                                ID1 = "S7";
                            }
                            else if(algo1 == 10)
                            {
                                ID1 = "S7";
                            }
                             else if(algo1 == 11)
                            {
                                ID1 = "S3";
                            }
                            else if(algo1 == 12)
                            {
                                ID1 = "S7";
                            }
                            else if(algo1 == 13)
                            {
                                ID1 = "S5";
                            }
                            else if(algo1 == 14)
                            {
                                ID1 = "S4";
                            }
                      }
                    }

                    if(algo4 != 0)
                    {
                        if(ps4 != 1)
                        {
                            if(algo4 == 1)
                            {
                                ID4 = "B40";
                            }
                            else if(algo4 == 2)
                            {
                                ID4 = "B39";
                            }
                            else if(algo4 == 3)
                            {
                                ID4 = "B25";
                            }
                            else if(algo4 == 4)
                            {
                                ID4 = "B25";
                            }
                            else if(algo4 == 5)
                            {
                                ID4 = "B26";
                            }
                            else if(algo4 == 6)
                            {
                                ID4 = "B26";
                            }
                            else if(algo4 == 7)
                            {
                                ID4 = "B26";
                            }
                            else if(algo4 == 8)
                            {
                                ID4 = "B26";
                            }
                            else if(algo4 == 9)
                            {
                                ID4 = "B34";
                            }
                            else if(algo4 == 10)
                            {
                                ID4 = "B34";
                            }
                             else if(algo4 == 11)
                            {
                                ID4 = "B35";
                            }
                            else if(algo4 == 12)
                            {
                                ID4 = "B3";
                            }
                            else if(algo4 == 13)
                            {
                                ID4 = "B4";
                            }
                            else if(algo4 == 14)
                            {
                                ID4 = "B28";
                            }
                            else
                            {
                                ID4 = "0";
                            }
                        }
                        else if(ps4 == 1)
                        {
                            if(algo4 == 1)
                            {
                                ID4 = "0"; //
                            }
                            else if(algo4 == 2)
                            {
                                ID4 = "0"; //
                            }
                            else if(algo4 == 3)
                            {
                                ID4 = "0"; //
                            }
                            else if(algo4 == 4)
                            {
                                ID4 = "0"; //
                            }
                            else if(algo4 == 5)
                            {
                                ID4 = "S6";
                            }
                            else if(algo4 == 6)
                            {
                                ID4 = "S6";
                            }
                             else if(algo4 == 7)
                            {
                                ID4 = "S6";
                            }
                            else if(algo4 == 8)
                            {
                                ID4 = "S6";
                            }
                            else if(algo4 == 9)
                            {
                                ID4 = "S6";
                            }
                            else if(algo4 == 10)
                            {
                                ID4 = "S6";
                            }
                             else if(algo4 == 11)
                            {
                                ID4 = "S3";
                            }
                            else if(algo4 == 12)
                            {
                                ID4 = "S7";
                            }
                            else if(algo4 == 13)
                            {
                                ID4 = "S5";
                            }
                            else if(algo4 == 14)
                            {
                                ID4 = "S4";
                            }
                        }
                    }

                    if(!ID1.empty() && !ID4.empty())
                    {
                        alg1_name = fetch_Algo(ID1);
                    }
                    else if(!ID1.empty() && ID4.empty())
                    {
                         alg1_name = fetch_Algo(ID1);
                    }
                    else if(ID1.empty() && !ID4.empty())
                    {
                        alg4_name = fetch_Algo(ID4);
                    }

                    if(algo2 != 0)
                    {
                        if(algo2 == 1)
                        {
                            ID2 = "H4";
                        }
                        else if(algo2 == 2)
                        {
                            ID2 = "H20";
                        }
                        else if(algo2 == 3)
                        {
                            ID2 = "H4";
                        }
                        else if(algo2 == 4)
                        {
                            ID2 = "H22";
                        }
                        else if(algo2 == 5)
                        {
                            ID2 = "H5";
                        }
                        else if(algo2 == 6)
                        {
                            ID2 = "H21";
                        }
                        else if(algo2 == 7)
                        {
                            ID2 = "H1";
                        }
                        else if(algo2 == 8)
                        {
                            ID2 = "H4";
                        }
                        else if(algo2 == 9)
                        {
                            ID2 = "H23";
                        }
                        else if(algo2 == 10)
                        {
                            ID2 = "H15";
                        }
                        else if(algo2 == 11)
                        {
                            ID2 = "H12";
                        }
                        else if(algo2 == 12)
                        {
                            ID2 = "H15";
                        }
                        else
                        {
                            ID2 = "0";
                        }
                        alg2_name = fetch_Algo(ID2);
                    }

                    if(algo3 != 0)
                    {
                        if(algo3 == 1)
                        {
                            ID3 = "0";
                        }
                        else if(algo3 == 2)
                        {
                            ID3 = "0";
                        }
                        else if(algo3 == 3)
                        {
                            ID3 = "0";
                        }
                        else if(algo3 == 4)
                        {
                            ID3 = "0";
                        }
                        else if(algo3 == 5)
                        {
                            ID3 = "0";
                        }
                        else if(algo3 == 6)
                        {
                            ID3 = "0";
                        }
                        else
                        {
                            ID3 = "0";
                        }
                        alg3_name = fetch_Algo(ID3);
                    }


                    if(algo5 != 0)
                    {
                        if(algo5 == 1)
                        {
                            ID5 = "0";
                        }
                        else if(algo5 == 2)
                        {
                            ID5 = "0";
                        }
                        else if(algo5 == 3)
                        {
                            ID5 = "0";
                        }
                        else if(algo5 == 4)
                        {
                            ID5 = "0";
                        }
                        else if(algo5 == 5)
                        {
                            ID5 = "0";
                        }
                        else if(algo5 == 6)
                        {
                            ID5 = "0";
                        }
                        else
                        {
                            ID5 = "0";
                        }
                        alg5_name = fetch_Algo(ID5);
                    }

                    if(algo6 != 0)
                    {
                       if(ps6 != 1)
                       {
                            if(algo6 == 1)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 2)
                            {
                                ID6 = "A6";
                            }
                            else if(algo6 == 3)
                            {
                                ID6 = "A2";
                            }
                            else if(algo6 == 4)
                            {
                                ID6 = "A2";
                            }
                            else if(algo6 == 5)
                            {
                                ID6 = "A5";
                            }
                            else if(algo6 == 6)
                            {
                                ID6 = "A13";
                            }
                            else if(algo6 == 7)
                            {
                                ID6 = "A14";
                            }
                            else if(algo6 == 8)
                            {
                                ID6 = "A10";
                            }
                            else
                            {
                                ID6 = "0";
                            }
                           alg6_name = fetch_Algo(ID6);
                       }
                       else if(ps6 == 1)
                       {
                            if(algo6 == 1)
                            {
                                ID6 = "A9";
                            }
                            else if(algo6 == 2)
                            {
                                ID6 = "A9";
                            }
                            else if(algo6 == 3)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 4)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 5)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 6)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 7)
                            {
                                ID6 = "A10";
                            }
                            else if(algo6 == 8)
                            {
                                ID6 = "A10";
                            }
                         alg6_name =  fetch_Algo(ID6);
                       }
                    }
        }
        else
        {
                        if(algo1 != 0)
                        {
                           if(ps1 != 1)
                           {
                                if(algo1 == 1)
                                {
                                    ID1 = "B40";
                                }
                                else if(algo1 == 2)
                                {
                                    ID1 = "B39";
                                }
                                else if(algo1 == 3)
                                {
                                    ID1 = "B40";
                                }
                                else if(algo1 == 4)
                                {
                                    ID1 = "B39";
                                }
                                else if(algo1 == 5)
                                {
                                    ID1 = "B25";
                                }
                                 else if(algo1 == 6)
                                {
                                    ID1 = "B40";
                                }
                                else if(algo1 == 7)
                                {
                                    ID1 = "B3";
                                }
                                else if(algo1 == 8)
                                {
                                    ID1 = "B40";
                                }
                                else if(algo1 == 9)
                                {
                                    ID1 = "B3";
                                }
                                else if(algo1 == 10)
                                {
                                    ID1 = "B34";
                                }
                                 else if(algo1 == 11)
                                {
                                    ID1 = "B34";
                                }
                                else if(algo1 == 12)
                                {
                                    ID1 = "B3";
                                }
                                else if(algo1 == 13)
                                {
                                    ID1 = "B35";
                                }
                                else if(algo1 == 14)
                                {
                                    ID1 = "B3";
                                }
                                else
                                {
                                    ID1 = "0";
                                }
                           }
                           else if(ps1 ==1)
                           {
                               if(algo1 == 1)
                                {
                                    ID1 = "0";
                                }
                                else if(algo1 == 2)
                                {
                                    ID1 = "0"; //
                                }
                                else if(algo1 == 3)
                                {
                                    ID1 = "0"; //
                                }
                                else if(algo1 == 4)
                                {
                                    ID1 = "0"; //
                                }
                                 else if(algo1 == 5)
                                {
                                    ID1 = "S6";
                                }
                                 else if(algo1 == 6)
                                {
                                    ID1 = "S6";
                                }
                                 else if(algo1 == 7)
                                {
                                    ID1 = "S6";
                                }
                                else if(algo1 == 8)
                                {
                                    ID1 = "S6";
                                }
                                else if(algo1 == 9)
                                {
                                    ID1 = "S6";
                                }
                                else if(algo1 == 10)
                                {
                                    ID1 = "S6";
                                }
                                 else if(algo1 == 11)
                                {
                                    ID1 = "S7";
                                }
                                else if(algo1 == 12)
                                {
                                    ID1 = "S7";
                                }
                                else if(algo1 == 13)
                                {
                                    ID1 = "S3";
                                }
                                else if(algo1 == 14)
                                {
                                    ID1 = "S5";
                                }
                          }
                        }

                        if(algo4 != 0)
                        {
                            if(ps4 != 1)
                            {
                                if(algo4 == 1)
                                {
                                    ID4 = "B40";
                                }
                                else if(algo4 == 2)
                                {
                                    ID4 = "B39";
                                }
                                else if(algo4 == 3)
                                {
                                    ID4 = "B40";
                                }
                                else if(algo4 == 4)
                                {
                                    ID4 = "B39";
                                }
                                else if(algo4 == 5)
                                {
                                    ID4 = "B3";
                                }
                                else if(algo4 == 6)
                                {
                                    ID4 = "B40";
                                }
                                else if(algo4 == 7)
                                {
                                    ID4 = "B3";
                                }
                                else if(algo4 == 8)
                                {
                                    ID4 = "B40";
                                }
                                else if(algo4 == 9)
                                {
                                    ID4 = "B29";
                                }
                                else if(algo4 == 10)
                                {
                                    ID4 = "B34";
                                }
                                 else if(algo4 == 11)
                                {
                                    ID4 = "B3";
                                }
                                else if(algo4 == 12)
                                {
                                    ID4 = "B34";
                                }
                                else if(algo4 == 13)
                                {
                                    ID4 = "B35";
                                }
                                else if(algo4 == 14)
                                {
                                    ID4 = "B3";
                                }
                                else
                                {
                                    ID4 = "0";
                                }
                            }
                            else if(ps4 == 1)
                            {
                                if(algo4 == 1)
                                {
                                    ID4 = "0"; //
                                }
                                else if(algo4 == 2)
                                {
                                    ID4 = "0"; //
                                }
                                else if(algo4 == 3)
                                {
                                    ID4 = "0"; //
                                }
                                else if(algo4 == 4)
                                {
                                    ID4 = "0"; //
                                }
                                else if(algo4 == 5)
                                {
                                    ID4 = "S6";
                                }
                                else if(algo4 == 6)
                                {
                                    ID4 = "S6";
                                }
                                 else if(algo4 == 7)
                                {
                                    ID4 = "S6";
                                }
                                else if(algo4 == 8)
                                {
                                    ID4 = "S6";
                                }
                                else if(algo4 == 9)
                                {
                                    ID4 = "S6";
                                }
                                else if(algo4 == 10)
                                {
                                    ID4 = "S6";
                                }
                                 else if(algo4 == 11)
                                {
                                    ID4 = "S7";
                                }
                                else if(algo4 == 12)
                                {
                                    ID4 = "S7";
                                }
                                else if(algo4 == 13)
                                {
                                    ID4 = "S3";
                                }
                                else if(algo4 == 14)
                                {
                                    ID4 = "S5";
                                }
                            }
                        }

                        if(!ID1.empty() && !ID4.empty())
                        {
                           alg1_name = fetch_Algo(ID1);
                        }
                        else if(!ID1.empty() && ID4.empty())
                        {
                            alg1_name = fetch_Algo(ID1);
                        }
                        else if(ID1.empty() && !ID4.empty())
                        {
                           alg4_name = fetch_Algo(ID4);
                        }


                         if(algo2 != 0)
                        {
                            if(algo2 == 1)
                            {
                                ID2 = "H20";
                            }
                            else if(algo2 == 2)
                            {
                                ID2 = "H20";
                            }
                            else if(algo2 == 3)
                            {
                                ID2 = "H22";
                            }
                            else if(algo2 == 4)
                            {
                                ID2 = "H22";
                            }
                            else if(algo2 == 5)
                            {
                                ID2 = "H6";
                            }
                            else if(algo2 == 6)
                            {
                                ID2 = "H22";
                            }
                            else if(algo2 == 7)
                            {
                                ID2 = "H23";
                            }
                            else if(algo2 == 8)
                            {
                                ID2 = "H8";
                            }
                            else if(algo2 == 9)
                            {
                                ID2 = "H23";
                            }
                            else if(algo2 == 10)
                            {
                                ID2 = "H12";
                            }
                            else if(algo2 == 11)
                            {
                                ID2 = "H24";
                            }
                            else if(algo2 == 12)
                            {
                                ID2 = "H18";
                            }
                            else
                            {
                                ID2 = "0";
                            }
                           alg2_name = fetch_Algo(ID2);
                        }

                        if(algo3 != 0)
                        {
                            if(algo3 == 1)
                            {
                                ID3 = "0";
                            }
                            else if(algo3 == 2)
                            {
                                ID3 = "0";
                            }
                            else if(algo3 == 3)
                            {
                                ID3 = "0";
                            }
                            else if(algo3 == 4)
                            {
                                ID3 = "0";
                            }
                            else if(algo3 == 5)
                            {
                                ID3 = "0";
                            }
                            else if(algo3 == 6)
                            {
                                ID3 = "0";
                            }
                            else
                            {
                                ID3 = "0";
                            }
                          alg3_name =  fetch_Algo(ID3);
                        }


                        if(algo5 != 0)
                        {
                            if(algo5 == 1)
                            {
                                ID5 = "0";
                            }
                            else if(algo5 == 2)
                            {
                                ID5 = "0";
                            }
                            else if(algo5 == 3)
                            {
                                ID5 = "0";
                            }
                            else if(algo5 == 4)
                            {
                                ID5 = "0";
                            }
                            else if(algo5 == 5)
                            {
                                ID5 = "0";
                            }
                            else if(algo5 == 6)
                            {
                                ID5 = "0";
                            }
                            else
                            {
                                ID5 = "0";
                            }
                          alg5_name =  fetch_Algo(ID5);
                        }

                        if(algo6 != 0)
                        {
                           if(ps6 != 1)
                           {
                                if(algo6 == 1)
                                {
                                    ID6 = "A5";
                                }
                                else if(algo6 == 2)
                                {
                                    ID6 = "A4";
                                }
                                else if(algo6 == 3)
                                {
                                    ID6 = "A6";
                                }
                                else if(algo6 == 4)
                                {
                                    ID6 = "A6";
                                }
                                else if(algo6 == 5)
                                {
                                    ID6 = "A13";
                                }
                                else if(algo6 == 6)
                                {
                                    ID6 = "A13";
                                }
                                else if(algo6 == 7)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 8)
                                {
                                    ID6 = "A7";
                                }
                                else
                                {
                                    ID6 = "0";
                                }
                              alg6_name =  fetch_Algo(ID6);
                           }
                           else if(ps6 == 1)
                           {
                                if(algo6 == 1)
                                {
                                    ID6 = "A9";
                                }
                                else if(algo6 == 2)
                                {
                                    ID6 = "A9";
                                }
                                else if(algo6 == 3)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 4)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 5)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 6)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 7)
                                {
                                    ID6 = "A10";
                                }
                                else if(algo6 == 8)
                                {
                                    ID6 = "A10";
                                }
                              alg6_name =  fetch_Algo(ID6);
                           }
                        }

    }

    return result {alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name};
}

auto Processing_and_Output::select_MarchingAlgo3(int flagx, int ds, int n_SC, double FMx, double RAMx)
{
         struct result
        {
            int n1;
            int n2;
        };
            int num1, num2;

            double FMy1, FMz1, RAMy1, RAMz1, FMy2, FMz2, RAMy2, RAMz2, FMy3, FMz3, RAMy3, RAMz3, FMy4, FMz4, RAMy4, RAMz4;

                FMy1 = 300.0, FMz1 = 980.0, RAMy1 = 200.0, RAMz1 = 400.0;
                FMy2 = 981.0, FMz2 = 2000.0, RAMy2 = 200.0, RAMz2 = 460.0;
                FMy3 = 2001.0, FMz3 = 4200.0, RAMy3 = 200.0, RAMz3 = 655.0;
                FMy4 = 4201.0, FMz4 = 7100.0, RAMy4 = 200.0, RAMz4 = 660.0;

        if(flagx == -1)
        {
            num1 = 0; num2 = 0;
            return result {num1, num2};
        }
        else if((flagx == 1) && (ds == 1) && (FMx >= FMy1 && FMx <= FMz1) && (RAMx >= RAMy1 && RAMx <= RAMz1))
        {
            if(n_SC == 1)
            {
                num1 = 1; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 1; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (FMx >= FMy1 && FMx <= FMz1) && (RAMx >= RAMy1 && RAMx <= RAMz1))
        {
             if(n_SC == 1)
            {
                num1 = 2; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 2; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds == 1) && (FMx >= FMy2 && FMx <= FMz2) && (RAMx >= RAMy2 && RAMx <= RAMz2))
        {
             if(n_SC == 1)
            {
                num1 = 3; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 3; num2 = 0;
                return result {num1, num2};
            }
        }
        else if((flagx == 1) && (ds != 1) && (FMx >= FMy2 && FMx <= FMz2) && (RAMx >= RAMy2 && RAMx <= RAMz2))
        {
              if(n_SC == 1)
            {
                num1 = 4; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 4; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (FMx >= FMy3 && FMx <= FMz3) && (RAMx >= RAMy3 && RAMx <= RAMz3))
        {
             if(n_SC == 1)
            {
                num1 = 5; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 5; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (FMx >= FMy3 && FMx <= FMz3) && (RAMx >= RAMy3 && RAMx <= RAMz3))
        {
              if(n_SC == 1)
            {
                num1 = 6; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 6; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds == 1) && (FMx >= FMy4 && FMx <= FMz4) && (RAMx >= RAMy4 && RAMx <= RAMz4))
        {
             if(n_SC == 1)
            {
                num1 = 7; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 7; num2 = 0;
                return result {num1, num2};
            }
        }
         else if((flagx == 1) && (ds != 1) && (FMx >= FMy4 && FMx <= FMz4) && (RAMx >= RAMy4 && RAMx <= RAMz4))
        {
              if(n_SC == 1)
            {
                num1 = 8; num2 = 1;
                return result {num1, num2};
            }
            else
            {
                num1 = 8; num2 = 0;
                return result {num1, num2};
            }
        }

        else
        {
            num1 = -1, num2 = 0;
            return result {num1, num2};
        }
}

auto Processing_and_Output::mapping2_3(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, double FM1_doub, double RAM1_doub, double FM2_doub, double RAM2_doub, double FM3_doub, double RAM3_doub, double FM4_doub, double RAM4_doub, double FM5_doub, double RAM5_doub, double FM6_doub, double RAM6_doub, string ad, string ps)
{
            struct result
            {
                int int_1;
                int p1;
                int int_2;
                int int_3;
                int int_4;
                int p4;
                int int_5;
                int int_6;
                int p6;
            };

        int algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6;

       int domain_sensitivity = checkSensitivity_of_User_ApplcArea(ad);
       int ds = domain_sensitivity;
       int needFor_StreamCipher = Check_if_streamCipherNeeded(ps);
       int n_SC = needFor_StreamCipher;
       auto s_MA_result1 = select_MarchingAlgo3(flag1, ds, n_SC, FM1_doub, RAM1_doub);
       algo1 = s_MA_result1.n1; ps1 = s_MA_result1.n2;
       auto s_MA_result2 = select_MarchingAlgo3(flag2, ds, n_SC, FM2_doub, RAM2_doub);
       algo2 = s_MA_result2.n1;
       auto s_MA_result3 = select_MarchingAlgo3(flag3, ds, n_SC, FM3_doub, RAM3_doub);
       algo3 = s_MA_result3.n1;
       auto s_MA_result4 = select_MarchingAlgo3(flag4, ds, n_SC, FM4_doub, RAM4_doub);
       algo4 = s_MA_result4.n1; ps4 = s_MA_result4.n2;
       auto s_MA_result5 = select_MarchingAlgo3(flag5, ds, n_SC, FM5_doub, RAM5_doub);
       algo5 = s_MA_result5.n1;
       auto s_MA_result6 = select_MarchingAlgo3(flag6, ds, n_SC, FM6_doub, RAM6_doub);
       algo6 = s_MA_result6.n1; ps6 = s_MA_result6.n2;

    return result {algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6};
}

void Processing_and_Output::displayReq_Mech_mapping3(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, string request_id)
{
        std::cout << "\n" "****************************************************************************************************" << endl;
        std::cout<<"\t\t FINAL RESULTS FOR USER WITH REQUEST ID No.: " << request_id << endl << endl;


    string s1, s2, s3, s4, s5, s6;
    s1.erase(); s2.erase(); s3.erase(); s4.erase(); s5.erase(); s6.erase();
    int flag_1, flag_2, flag_3, flag_4, flag_5, flag_6;

    if(flag1 == 1 && flag4 ==1)
    {
        s1 = "Data Confidentiality/User Privacy";
        flag_1 = 1;
    }
    else if(flag1 == 1 && flag4 !=1)
    {
         s1 ="Data Confidentiality";
         flag_1 = 1;
    }
    if(flag2 == 1)
    {
        s2 = "Message Integrity";
        flag_2 = 1;
    }
    if(flag3 ==1)
    {
      s3 = "Authentication";
      flag_3 = 1;
    }
    if(flag4 ==1 && flag1 != 1)
    {
         s4 = "User Privacy";
         flag_4 = 1;
    }
    if(flag5 == 1)
    {
       s5 = "Non-repudiation";
       flag_5 = 1;
    }
    if(flag6 ==1)
    {
        s6 = "Confidentiality & Authenticity";
        flag_6 = 1;
    }


        cout << "\n YOUR SECURITY REQUIREMENTS AND RECOMMENDED SECURITY MECHANISMS AND SECURITY ALGORITHMS ARE: \n" << endl;


    format_Print_output(s1, s2, s3, s4, s5, s6, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6);

    Report report;

					char ch;
                    level:
					int flac = 0;

                    if(!algo_name1.empty() || !algo_name2.empty() || !algo_name1.empty() || !algo_name4.empty() || !algo_name5.empty() || !algo_name6.empty())
                    {
						flac = 2;
                        std::cout << "\n\n   \tWould you like to see a detailed report on the recommended algorithms?: \n";
                    }
                    else
                    {
                        std::cout << "\n\n\n  You don't have any security requirement, or no algorithms matching your security requirements are found.\n";
                        cout << "\n\n\t\t\t\tPress Enter to return to MAIN MENU \n";
                        return;
                    }

                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No, thank you";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

						std::cin>>ch;

						switch(ch)
						{
						case '1':
                                 {
                                    system("cls");
                                    std::cout << "\n" "****************************************************************************************************" << endl;
									 std::cout<<"\t\t FINAL RESULTS FOR USER WITH REQUEST ID No.: " << request_id << endl << endl;


									string s1, s2, s3, s4, s5, s6;
									s1.erase(); s2.erase(); s3.erase(); s4.erase(); s5.erase(); s6.erase();
									int flag_1, flag_2, flag_3, flag_4, flag_5, flag_6;

									if(flag1 == 1 && flag4 ==1)
									{
										s1 = "Data Confidentiality/User Privacy";
										flag_1 = 1;
									}
									else if(flag1 == 1 && flag4 !=1)
									{
										 s1 ="Data Confidentiality";
										 flag_1 = 1;
									}
									if(flag2 == 1)
									{
										s2 = "Message Integrity";
										flag_2 = 1;
									}
									if(flag3 ==1)
									{
									  s3 = "Authentication";
									  flag_3 = 1;
									}
									if(flag4 ==1 && flag1 != 1)
									{
										 s4 = "User Privacy";
										 flag_4 = 1;
									}
									if(flag5 == 1)
									{
									   s5 = "Non-repudiation";
									   flag_5 = 1;
									}
									if(flag6 ==1)
									{
										s6 = "Confidentiality & Authenticity";
										flag_6 = 1;
									}


										cout << "\n YOUR SECURITY REQUIREMENTS AND RECOMMENDED SECURITY MECHANISMS AND SECURITY ALGORITHMS ARE: \n" << endl;


									format_Print_output(s1, s2, s3, s4, s5, s6, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6);

                                    string Re_6 = "", Re_7 = "", Re_8 = "", Re_9 = "", Re_10 = "", Re_11 = "", Re_12 = "", Re_13 = "", Re_14 = "", Re_15 = "";

                                    report.formatReport_for_Consle(request_id, flac, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15);
                            break;
                            }
                        case '2':

                            break;
						default:
							system("cls");
							std::cout << "\n\t\tSorry! Wrong option selected." << std:: endl;
                            goto level;
						}

                        flac = 0;


        cout << "\n\n\t\t\t\tPress Enter to return to MAIN MENU \n";

}

auto Processing_and_Output::display_Mech_Algo_mapping3(string type, int algo1, int algo2, int algo3, int algo4, int algo5, int algo6, int ps1, int ps4, int ps6)
{
     struct result
            {
                string st_1;
                string st_2;
                string st_3;
                string st_4;
                string st_5;
                string st_6;
            };

    string algName1, algName2, algName3, algName4, algName5, algName6;
    string ID1, ID2, ID3, ID4, ID5, ID6;

	if(type == "AVR")
	{
		if(algo1 != 0)
			{
			   if(ps1 != 1)
			   {
					if(algo1 == 1)
					{
						ID1 = "B14";
					}
					else if(algo1 == 2)
					{
						ID1 = "B13";
					}
					else if(algo1 == 3)
					{
						ID1 = "B14";
					}
					else if(algo1 == 4)
					{
						ID1 = "B13";
					}
					else if(algo1 == 5)
					{
						ID1 = "B25";
					}
					 else if(algo1 == 6)
					{
						ID1 = "B32";
					}
					else if(algo1 == 7)
					{
						ID1 = "B18";
					}
					else if(algo1 == 8)
					{
						ID1 = "B17";
					}
					else
					{
						ID1 = "0";
					}
				 algName1 = fetch_Algo(ID1);
			   }
			   else if(ps1 ==1)
			   {
				   if(algo1 == 1)
					{
						ID1 = "0";
					}
					else if(algo1 == 2)
					{
						ID1 = "0";
					}
					else if(algo1 == 3)
					{
						ID1 = "S8";
					}
					else if(algo1 == 4)
					{
						ID1 = "S8";
					}
					 else if(algo1 == 5)
					{
						ID1 = "S2";
					}
					 else if(algo1 == 6)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 7)
					{
						ID1 = "S2";
					}
					else if(algo1 == 8)
					{
						ID1 = "S2";
					}
				   algName1 = fetch_Algo(ID1);
			  }
			}
		 // /*
			if(algo2 != 0)
			{
				if(algo2 == 1)
				{
					ID2 = "H8";
				}
				else if(algo2 == 2)
				{
					ID2 = "H8";
				}
				else if(algo2 == 3)
				{
					ID2 = "H8";
				}
				else if(algo2 == 4)
				{
					ID2 = "H8";
				}
				else if(algo2 == 5)
				{
					ID2 = "H12";
				}
				else if(algo2 == 6)
				{
					ID2 = "H12";
				}
				else if(algo2 == 7)
				{
					ID2 = "H12";
				}
				else if(algo2 == 8)
				{
					ID2 = "H12";
				}
				else
				{
					ID2 = "0";
				}
			  algName2 = fetch_Algo(ID2);
			}

			if(algo3 != 0)
			{
				if(algo3 == 1)
				{
					ID3 = "0";
				}
				else if(algo3 == 2)
				{
					ID3 = "0";
				}
				else if(algo3 == 3)
				{
					ID3 = "0";
				}
				else if(algo3 == 4)
				{
					ID3 = "0";
				}
				else if(algo3 == 5)
				{
					ID3 = "0";
				}
				else if(algo3 == 6)
				{
					ID3 = "0";
				}
				else if(algo3 == 7)
				{
					ID3 = "0";
				}
				else if(algo3 == 8)
				{
					ID3 = "0";
				}
				else
				{
					ID3 = "0";
				}
			 algName3 = fetch_Algo(ID3);
			}

			if(algo4 != 0)
			{
				if(ps4 != 1)
				{
					if(algo4 == 1)
					{
						ID4 = "B14";
					}
					else if(algo4 == 2)
					{
						ID4 = "B13";
					}
					else if(algo4 == 3)
					{
						ID4 = "B14";
					}
					else if(algo4 == 4)
					{
						ID4 = "B13";
					}
					else if(algo4 == 5)
					{
						ID4 = "B25";
					}
					else if(algo4 == 6)
					{
						ID4 = "B32";
					}
					else if(algo4 == 7)
					{
						ID4 = "B18";
					}
					else if(algo4 == 8)
					{
						ID4 = "B17";
					}
					else
					{
						ID4 = "0";
					}
				 algName4 = fetch_Algo(ID4);
				}
				else if(ps4 == 1)
				{
					if(algo4 == 1)
					{
						ID4 = "0";
					}
					else if(algo4 == 2)
					{
						ID4 = "0";
					}
					else if(algo4 == 3)
					{
						ID4 = "S8";
					}
					else if(algo4 == 4)
					{
						ID4 = "S8";
					}
					else if(algo4 == 5)
					{
						ID4 = "S2";
					}
					else if(algo4 == 6)
					{
						ID4 = "S5";
					}
					 else if(algo4 == 7)
					{
						ID4 = "S2";
					}
					else if(algo4 == 8)
					{
						ID4 = "S2";
					}
				  algName4 = fetch_Algo(ID4);
				}
			}

			if(algo5 != 0)
			{
				if(algo5 == 1)
				{
					ID5 = "0";
				}
				else if(algo5 == 2)
				{
					ID5 = "0";
				}
				else if(algo5 == 3)
				{
					ID5 = "0";
				}
				else if(algo5 == 4)
				{
					ID5 = "0";
				}
				else if(algo5 == 5)
				{
					ID5 = "0";
				}
				else if(algo5 == 6)
				{
					ID5 = "0";
				}
				else if(algo5 == 7)
				{
					ID5 = "0";
				}
				else if(algo5 == 8)
				{
					ID5 = "0";
				}
				else
				{
					ID5 = "0";
				}
			  algName5 = fetch_Algo(ID5);
			}

			if(algo6 != 0)
			{
			   if(ps6 != 1) //
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0";
					}
					else if(algo6 == 3)
					{
						ID6 = "0";
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";// A3
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
					else
					{
						ID6 = "0";
					}
				 algName6 =  fetch_Algo(ID6);
			   }
			   else if(ps6 == 1)
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0";
					}
					else if(algo6 == 3)
					{
						ID6 = "A10";
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
				   algName6 = fetch_Algo(ID6);
			   }
			}
	}
	else if(type == "MSP")
	{
		if(algo1 != 0)
			{
			   if(ps1 != 1)
			   {
					if(algo1 == 1)
					{
						ID1 = "B14";
					}
					else if(algo1 == 2)
					{
						ID1 = "B13";
					}
					else if(algo1 == 3)
					{
						ID1 = "B14";
					}
					else if(algo1 == 4)
					{
						ID1 = "B13";
					}
					else if(algo1 == 5)
					{
						ID1 = "B25";
					}
					 else if(algo1 == 6)
					{
						ID1 = "B32";
					}
					else if(algo1 == 7)
					{
						ID1 = "B34";
					}
					else if(algo1 == 8)
					{
						ID1 = "B34";
					}
					else
					{
						ID1 = "0";
					}
				 algName1 = fetch_Algo(ID1);
			   }
			   else if(ps1 ==1)
			   {
				   if(algo1 == 1)
					{
						ID1 = "S8";
					}
					else if(algo1 == 2)
					{
						ID1 = "S8";
					}
					else if(algo1 == 3)
					{
						ID1 = "S2";
					}
					else if(algo1 == 4)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 5)
					{
						ID1 = "S2";
					}
					 else if(algo1 == 6)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 7)
					{
						ID1 = "S2";
					}
					else if(algo1 == 8)
					{
						ID1 = "S5";
					}
				   algName1 = fetch_Algo(ID1);
			  }
			}
		 // /*
			if(algo2 != 0)
			{
				if(algo2 == 1)
				{
					ID2 = "H8";
				}
				else if(algo2 == 2)
				{
					ID2 = "H8";
				}
				else if(algo2 == 3)
				{
					ID2 = "H8";
				}
				else if(algo2 == 4)
				{
					ID2 = "H8";
				}
				else if(algo2 == 5)
				{
					ID2 = "H12";
				}
				else if(algo2 == 6)
				{
					ID2 = "H12";
				}
				else if(algo2 == 7)
				{
					ID2 = "H12";
				}
				else if(algo2 == 8)
				{
					ID2 = "H12";
				}
				else
				{
					ID2 = "0";
				}
			  algName2 = fetch_Algo(ID2);
			}

			if(algo3 != 0)
			{
				if(algo3 == 1)
				{
					ID3 = "0";
				}
				else if(algo3 == 2)
				{
					ID3 = "0";
				}
				else if(algo3 == 3)
				{
					ID3 = "0";
				}
				else if(algo3 == 4)
				{
					ID3 = "0";
				}
				else if(algo3 == 5)
				{
					ID3 = "0";
				}
				else if(algo3 == 6)
				{
					ID3 = "0";
				}
				else if(algo3 == 7)
				{
					ID3 = "0";
				}
				else if(algo3 == 8)
				{
					ID3 = "0";
				}
				else
				{
					ID3 = "0";
				}
			 algName3 = fetch_Algo(ID3);
			}

			if(algo4 != 0)
			{
				if(ps4 != 1)
				{
					if(algo4 == 1)
					{
						ID4 = "B14";
					}
					else if(algo4 == 2)
					{
						ID4 = "B13";
					}
					else if(algo4 == 3)
					{
						ID4 = "B14";
					}
					else if(algo4 == 4)
					{
						ID4 = "B13";
					}
					else if(algo4 == 5)
					{
						ID4 = "B25";
					}
					else if(algo4 == 6)
					{
						ID4 = "B32";
					}
					else if(algo4 == 7)
					{
						ID4 = "B34";
					}
					else if(algo4 == 8)
					{
						ID4 = "B34";
					}
					else
					{
						ID4 = "0";
					}
				 algName4 = fetch_Algo(ID4);
				}
				else if(ps4 == 1)
				{
					if(algo4 == 1)
					{
						ID4 = "S8";
					}
					else if(algo4 == 2)
					{
						ID4 = "S8";
					}
					else if(algo4 == 3)
					{
						ID4 = "S2";
					}
					else if(algo4 == 4)
					{
						ID4 = "S5";
					}
					else if(algo4 == 5)
					{
						ID4 = "S2";
					}
					else if(algo4 == 6)
					{
						ID4 = "S5";
					}
					 else if(algo4 == 7)
					{
						ID4 = "S2";
					}
					else if(algo4 == 8)
					{
						ID4 = "S5";
					}
				  algName4 = fetch_Algo(ID4);
				}
			}

			if(algo5 != 0)
			{
				if(algo5 == 1)
				{
					ID5 = "0";
				}
				else if(algo5 == 2)
				{
					ID5 = "0";
				}
				else if(algo5 == 3)
				{
					ID5 = "0";
				}
				else if(algo5 == 4)
				{
					ID5 = "0";
				}
				else if(algo5 == 5)
				{
					ID5 = "0";
				}
				else if(algo5 == 6)
				{
					ID5 = "0";
				}
				else if(algo5 == 7)
				{
					ID5 = "0";
				}
				else if(algo5 == 8)
				{
					ID5 = "0";
				}
				else
				{
					ID5 = "0";
				}
			  algName5 = fetch_Algo(ID5);
			}

			if(algo6 != 0)
			{
			   if(ps6 != 1) //
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0";
					}
					else if(algo6 == 3)
					{
						ID6 = "0";
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";// A3
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
					else
					{
						ID6 = "0";
					}
				 algName6 =  fetch_Algo(ID6);
			   }
			   else if(ps6 == 1)
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0"; //
					}
					else if(algo6 == 3)
					{
						ID6 = "0"; //
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
				   algName6 = fetch_Algo(ID6);
			   }
			}
	}
	else if(type == "ARM")
	{
		if(algo1 != 0)
			{
			   if(ps1 != 1)
			   {
					if(algo1 == 1)
					{
						ID1 = "B14";
					}
					else if(algo1 == 2)
					{
						ID1 = "B13";
					}
					else if(algo1 == 3)
					{
						ID1 = "B14";
					}
					else if(algo1 == 4)
					{
						ID1 = "B25";
					}
					else if(algo1 == 5)
					{
						ID1 = "B25";
					}
					 else if(algo1 == 6)
					{
						ID1 = "B34";
					}
					else if(algo1 == 7)
					{
						ID1 = "B43";
					}
					else if(algo1 == 8)
					{
						ID1 = "B31";
					}
					else
					{
						ID1 = "0";
					}
				 algName1 = fetch_Algo(ID1);
			   }
			   else if(ps1 ==1)
			   {
				   if(algo1 == 1)
					{
						ID1 = "S2";
					}
					else if(algo1 == 2)
					{
						ID1 = "S8";
					}
					else if(algo1 == 3)
					{
						ID1 = "S2";
					}
					else if(algo1 == 4)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 5)
					{
						ID1 = "S2";
					}
					 else if(algo1 == 6)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 7)
					{
						ID1 = "S2";
					}
					else if(algo1 == 8)
					{
						ID1 = "S5";
					}
				   algName1 = fetch_Algo(ID1);
			  }
			}

			if(algo2 != 0)
			{
				if(algo2 == 1)
				{
					ID2 = "H8";
				}
				else if(algo2 == 2)
				{
					ID2 = "H8";
				}
				else if(algo2 == 3)
				{
					ID2 = "H8";
				}
				else if(algo2 == 4)
				{
					ID2 = "H8";
				}
				else if(algo2 == 5)
				{
					ID2 = "H12";
				}
				else if(algo2 == 6)
				{
					ID2 = "H12";
				}
				else if(algo2 == 7)
				{
					ID2 = "H12";
				}
				else if(algo2 == 8)
				{
					ID2 = "H12";
				}
				else
				{
					ID2 = "0";
				}
			  algName2 = fetch_Algo(ID2);
			}

			if(algo3 != 0)
			{
				if(algo3 == 1)
				{
					ID3 = "0";
				}
				else if(algo3 == 2)
				{
					ID3 = "0";
				}
				else if(algo3 == 3)
				{
					ID3 = "0";
				}
				else if(algo3 == 4)
				{
					ID3 = "0";
				}
				else if(algo3 == 5)
				{
					ID3 = "0";
				}
				else if(algo3 == 6)
				{
					ID3 = "0";
				}
				else if(algo3 == 7)
				{
					ID3 = "0";
				}
				else if(algo3 == 8)
				{
					ID3 = "0";
				}
				else
				{
					ID3 = "0";
				}
			 algName3 = fetch_Algo(ID3);
			}

			if(algo4 != 0)
			{
				if(ps4 != 1)
				{
					if(algo4 == 1)
					{
						ID4 = "B14";
					}
					else if(algo4 == 2)
					{
						ID4 = "B13";
					}
					else if(algo4 == 3)
					{
						ID4 = "14";
					}
					else if(algo4 == 4)
					{
						ID4 = "B25";
					}
					else if(algo4 == 5)
					{
						ID4 = "B25";
					}
					else if(algo4 == 6)
					{
						ID4 = "B34";
					}
					else if(algo4 == 7)
					{
						ID4 = "B43";
					}
					else if(algo4 == 8)
					{
						ID4 = "B31";
					}
					else
					{
						ID4 = "0";
					}
				 algName4 = fetch_Algo(ID4);
				}
				else if(ps4 == 1)
				{
					if(algo4 == 1)
					{
						ID4 = "S2";
					}
					else if(algo4 == 2)
					{
						ID4 = "S8";
					}
					else if(algo4 == 3)
					{
						ID4 = "S2";
					}
					else if(algo4 == 4)
					{
						ID4 = "S5";
					}
					else if(algo4 == 5)
					{
						ID4 = "S2";
					}
					else if(algo4 == 6)
					{
						ID4 = "S5";
					}
					 else if(algo4 == 7)
					{
						ID4 = "S2";
					}
					else if(algo4 == 8)
					{
						ID4 = "S5";
					}
				  algName4 = fetch_Algo(ID4);
				}
			}

			if(algo5 != 0)
			{
				if(algo5 == 1)
				{
					ID5 = "0";
				}
				else if(algo5 == 2)
				{
					ID5 = "0";
				}
				else if(algo5 == 3)
				{
					ID5 = "0";
				}
				else if(algo5 == 4)
				{
					ID5 = "0";
				}
				else if(algo5 == 5)
				{
					ID5 = "0";
				}
				else if(algo5 == 6)
				{
					ID5 = "0";
				}
				else if(algo5 == 7)
				{
					ID5 = "0";
				}
				else if(algo5 == 8)
				{
					ID5 = "0";
				}
				else
				{
					ID5 = "0";
				}
			  algName5 = fetch_Algo(ID5);
			}

			if(algo6 != 0)
			{
			   if(ps6 != 1) //
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0";
					}
					else if(algo6 == 3)
					{
						ID6 = "0";
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";// A3
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
					else
					{
						ID6 = "0";
					}
				 algName6 =  fetch_Algo(ID6);
			   }
			   else if(ps6 == 1)
			   {
					if(algo6 == 1)
					{
						ID6 = "0";
					}
					else if(algo6 == 2)
					{
						ID6 = "0"; //
					}
					else if(algo6 == 3)
					{
						ID6 = "0"; //
					}
					else if(algo6 == 4)
					{
						ID6 = "0";
					}
					else if(algo6 == 5)
					{
						ID6 = "0";
					}
					else if(algo6 == 6)
					{
						ID6 = "0";
					}
					else if(algo6 == 7)
					{
						ID6 = "0";
					}
					else if(algo6 == 8)
					{
						ID6 = "0";
					}
				   algName6 = fetch_Algo(ID6);
			   }
			}
	}
	else
	{
		if(algo1 != 0)
			{
			   if(ps1 != 1)
			   {
					if(algo1 == 1)
					{
						ID1 = "B14";
					}
					else if(algo1 == 2)
					{
						ID1 = "B13";
					}
					else if(algo1 == 3)
					{
						ID1 = "B14";
					}
					else if(algo1 == 4)
					{
						ID1 = "B13";
					}
					else if(algo1 == 5)
					{
						ID1 = "B25";
					}
					 else if(algo1 == 6)
					{
						ID1 = "B32";
					}
					else if(algo1 == 7)
					{
						ID1 = "B18";
					}
					else if(algo1 == 8)
					{
						ID1 = "B17";
					}
					else
					{
						ID1 = "0";
					}
				 algName1 = fetch_Algo(ID1);
			   }
			   else if(ps1 ==1)
			   {
				   if(algo1 == 1)
					{
						ID1 = "S8";
					}
					else if(algo1 == 2)
					{
						ID1 = "S8";
					}
					else if(algo1 == 3)
					{
						ID1 = "S2";
					}
					else if(algo1 == 4)
					{
						ID1 = "S8";
					}
					 else if(algo1 == 5)
					{
						ID1 = "S2";
					}
					 else if(algo1 == 6)
					{
						ID1 = "S5";
					}
					 else if(algo1 == 7)
					{
						ID1 = "S2";
					}
					else if(algo1 == 8)
					{
						ID1 = "S5";
					}
				   algName1 = fetch_Algo(ID1);
			  }
			}

			if(algo2 != 0)
			{
				if(algo2 == 1)
				{
					ID2 = "H8";
				}
				else if(algo2 == 2)
				{
					ID2 = "H8";
				}
				else if(algo2 == 3)
				{
					ID2 = "H8";
				}
				else if(algo2 == 4)
				{
					ID2 = "H8";
				}
				else if(algo2 == 5)
				{
					ID2 = "H12";
				}
				else if(algo2 == 6)
				{
					ID2 = "H12";
				}
				else if(algo2 == 7)
				{
					ID2 = "H12";
				}
				else if(algo2 == 8)
				{
					ID2 = "H12";
				}
				else
				{
					ID2 = "0";
				}
			  algName2 = fetch_Algo(ID2);
			}

			if(algo3 != 0)
			{
				if(algo3 == 1)
				{
					ID3 = "0";
				}
				else if(algo3 == 2)
				{
					ID3 = "0";
				}
				else if(algo3 == 3)
				{
					ID3 = "0";
				}
				else if(algo3 == 4)
				{
					ID3 = "0";
				}
				else if(algo3 == 5)
				{
					ID3 = "0";
				}
				else if(algo3 == 6)
				{
					ID3 = "0";
				}
				else if(algo3 == 7)
				{
					ID3 = "0";
				}
				else if(algo3 == 8)
				{
					ID3 = "0";
				}
				else
				{
					ID3 = "0";
				}
			 algName3 = fetch_Algo(ID3);
			}

			if(algo4 != 0)
			{
				if(ps4 != 1)
				{
					if(algo4 == 1)
					{
						ID4 = "B14";
					}
					else if(algo4 == 2)
					{
						ID4 = "B13";
					}
					else if(algo4 == 3)
					{
						ID4 = "B14";
					}
					else if(algo4 == 4)
					{
						ID4 = "B13";
					}
					else if(algo4 == 5)
					{
						ID4 = "B25";
					}
					else if(algo4 == 6)
					{
						ID4 = "B32";
					}
					else if(algo4 == 7)
					{
						ID4 = "B18";
					}
					else if(algo4 == 8)
					{
						ID4 = "B17";
					}
					else
					{
						ID4 = "0";
					}
				 algName4 = fetch_Algo(ID4);
				}
				else if(ps4 == 1)
				{
					if(algo4 == 1)
					{
						ID4 = "S8";
					}
					else if(algo4 == 2)
					{
						ID4 = "S8";
					}
					else if(algo4 == 3)
					{
						ID4 = "S2";
					}
					else if(algo4 == 4)
					{
						ID4 = "S5";
					}
					else if(algo4 == 5)
					{
						ID4 = "S2";
					}
					else if(algo4 == 6)
					{
						ID4 = "S5";
					}
					 else if(algo4 == 7)
					{
						ID4 = "S2";
					}
					else if(algo4 == 8)
					{
						ID4 = "S5";
					}
				  algName4 = fetch_Algo(ID4);
				}
			}

			if(algo5 != 0)
			{
				if(algo5 == 1)
				{
					ID5 = "0";
				}
				else if(algo5 == 2)
				{
					ID5 = "0";
				}
				else if(algo5 == 3)
				{
					ID5 = "0";
				}
				else if(algo5 == 4)
				{
					ID5 = "0";
				}
				else if(algo5 == 5)
				{
					ID5 = "0";
				}
				else if(algo5 == 6)
				{
					ID5 = "0";
				}
				else if(algo5 == 7)
				{
					ID5 = "0";
				}
				else if(algo5 == 8)
				{
					ID5 = "0";
				}
				else
				{
					ID5 = "0";
				}
			  algName5 = fetch_Algo(ID5);
			}

			if(algo6 != 0)
			{
			   if(ps6 != 1) //
			   {
					if(algo6 == 1)
					{
						ID6 = "A1";
					}
					else if(algo6 == 2)
					{
						ID6 = "A1";
					}
					else if(algo6 == 3)
					{
						ID6 = "A13";
					}
					else if(algo6 == 4)
					{
						ID6 = "A12";
					}
					else if(algo6 == 5)
					{
						ID6 = "A9";
					}
					else if(algo6 == 6)
					{
						ID6 = "A9";
					}
					else if(algo6 == 7)
					{
						ID6 = "A7";
					}
					else if(algo6 == 8)
					{
						ID6 = "A7";
					}
					else
					{
						ID6 = "0";
					}
				 algName6 =  fetch_Algo(ID6);
			   }
			   else if(ps6 == 1)
			   {
					if(algo6 == 1)
					{
						ID6 = "A10";
					}
					else if(algo6 == 2)
					{
						ID6 = "A10";
					}
					else if(algo6 == 3)
					{
						ID6 = "A10";
					}
					else if(algo6 == 4)
					{
						ID6 = "A9";
					}
					else if(algo6 == 5)
					{
						ID6 = "A9";
					}
					else if(algo6 == 6)
					{
						ID6 = "A9";
					}
					else if(algo6 == 7)
					{
						ID6 = "A9";
					}
					else if(algo6 == 8)
					{
						ID6 = "A9";
					}
				   algName6 = fetch_Algo(ID6);
			   }
			}
	}
  // */
  return result {algName1, algName2, algName3, algName4, algName5, algName6};
}

void Processing_and_Output::format_Print_output(string s1, string s2, string s3, string s4, string s5, string s6, int f1, int f2, int f3, int f4, int f5, int f6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6)
{
     if(algo_name1.empty())
     {
         algo_name1 = "*No matching Algo found!";
     }
     if(algo_name2.empty())
     {
         algo_name2 = "*No matching Algo found!";
     }
     if(algo_name3.empty())
     {
         algo_name3 = "*No matching Algo found!";
     }
     if(algo_name4.empty())
     {
         algo_name4 = "*No matching Algo found!";
     }
     if(algo_name5.empty())
     {
         algo_name5 = "*No matching Algo found!";
     }
     if(algo_name6.empty())
     {
         algo_name6 = "*No matching Algo found!";
     }


                cout << left << setw(38) << setfill('-') << left << '+'
                << setw(30) << setfill('-') << left << '+'
                << setw(26)<< setfill('-') << '+' << '+' << endl;

                cout << setfill(' ') << '|' << left << setw(37) << "SECURITY REQUIREMENT(S)"
                << setfill(' ') << '|' << setw(29) << "SECURITY MECHANISM(S)"
                << setfill(' ') << '|' << left << setw(25) << "SECURITY ALGORITHM(S)" << '|' << endl;

                 cout << left << setw(38) << setfill('-') << left<< '+'
                 << setw(30) << setfill('-') << left << '+'
                 << setw(26) << setfill('-') << '+' << '+' << endl;

                 if(f1 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s1
                    << setfill(' ') << '|' << setw(29) << "Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name1 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f2 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s2
                    << setfill(' ') << '|' << setw(29) << "Hash Function"
                    << setfill(' ') << '|' << left << setw(25) << algo_name2 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f3 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s3
                    << setfill(' ') << '|' << setw(29) << "Message Authentication Code"
                    << setfill(' ') << '|' << left << setw(25) << algo_name3 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f4 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s4
                    << setfill(' ') << '|' << setw(29) << "Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name4 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f5 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s5
                    << setfill(' ') << '|' << setw(29) << "Digital Signature"
                    << setfill(' ') << '|' << left << setw(25) << algo_name5 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f6 == 1)
                 {
                     cout << setfill(' ') << '|' << left << setw(37) << s6
                    << setfill(' ') << '|' << setw(29) << "Authenticated Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name6 << '|' << endl;

                    cout << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }

    if((algo_name1 == "*No matching Algo found!" && f1 == 1) || (algo_name2 == "*No matching Algo found!" && f2 == 1) || (algo_name3 == "*No matching Algo found!" && f3 == 1) || (algo_name4 == "*No matching Algo found!" && f4 == 1) || (algo_name5 == "*No matching Algo found!" && f5 == 1) || (algo_name6 == "*No matching Algo found!" && f6 == 1))
    {
        cout << "\n *No algorithm matching the security requirement is found!" << endl;
    }
}

void Processing_and_Output::format_TextOutput(string s1, string s2, string s3, string s4, string s5, string s6, int f1, int f2, int f3, int f4, int f5, int f6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight,  double fms, double rs, double fms_, double rs_, string request_id)
{
     if(algo_name1.empty())
     {
         algo_name1 = "*No matching Algo found!";
     }
     if(algo_name2.empty())
     {
         algo_name2 = "*No matching Algo found!";
     }
     if(algo_name3.empty())
     {
         algo_name3 = "*No matching Algo found!";
     }
     if(algo_name4.empty())
     {
         algo_name4 = "*No matching Algo found!";
     }
     if(algo_name5.empty())
     {
         algo_name5 = "*No matching Algo found!";
     }
     if(algo_name6.empty())
     {
         algo_name6 = "*No matching Algo found!";
     }

     fstream file;
     file.open("Final_Result.txt", ios::out | ios::trunc);
     if(file.is_open())
     {
        file << "\n" "*****************************************************************************************************************" << endl;
        file << " FINAL RESULTS FOR THE USER WITH REQUEST ID No.: " << request_id << endl << endl;

         if(total_reqWeight == 2.5)
         {
            file << "\nYOUR SECURITY REQUIREMENT AND RECOMMENDED SECURITY MECHANISM AND SECURITY ALGORITHM ARE: \n" << endl;
         }
         else
         {
            file << "\nYOUR SECURITY REQUIREMENTS AND RECOMMENDED SECURITY MECHANISMS AND SECURITY ALGORITHMS ARE: \n" << endl;
         }
          file << left << setw(38) << setfill('-') << left << '+'
                << setw(30) << setfill('-') << left << '+'
                << setw(26)<< setfill('-') << '+' << '+' << endl;

           file << setfill(' ') << '|' << left << setw(37) << "SECURITY REQUIREMENT(S)"
                << setfill(' ') << '|' << setw(29) << "SECURITY MECHANISM(S)"
                << setfill(' ') << '|' << left << setw(25) << "SECURITY ALGORITHM(S)" << '|' << endl;

           file << left << setw(38) << setfill('-') << left<< '+'
                 << setw(30) << setfill('-') << left << '+'
                 << setw(26) << setfill('-') << '+' << '+' << endl;

                 if(f1 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s1
                    << setfill(' ') << '|' << setw(29) << "Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name1 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f2 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s2
                    << setfill(' ') << '|' << setw(29) << "Hash Function"
                    << setfill(' ') << '|' << left << setw(25) << algo_name2 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f3 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s3
                    << setfill(' ') << '|' << setw(29) << "Message Authentication Code"
                    << setfill(' ') << '|' << left << setw(25) << algo_name3 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f4 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s4
                    << setfill(' ') << '|' << setw(29) << "Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name4 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f5 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s5
                    << setfill(' ') << '|' << setw(29) << "Digital Signature"
                    << setfill(' ') << '|' << left << setw(25) << algo_name5 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }
                 if(f6 == 1)
                 {
                     file << setfill(' ') << '|' << left << setw(37) << s6
                    << setfill(' ') << '|' << setw(29) << "Authenticated Encryption"
                    << setfill(' ') << '|' << left << setw(25) << algo_name6 << '|' << endl;

                    file << left << setw(38) << setfill('-') << left<< '+'
                     << setw(30) << setfill('-') << left << '+'
                     << setw(26) << setfill('-') << '+' << '+' << endl;
                 }

            if((algo_name1 == "*No matching Algo found!" && f1 == 1) || (algo_name2 == "*No matching Algo found!" && f2 == 1) || (algo_name3 == "*No matching Algo found!" && f3 == 1) || (algo_name4 == "*No matching Algo found!" && f4 == 1) || (algo_name5 == "*No matching Algo found!" && f5 == 1) || (algo_name6 == "*No matching Algo found!" && f6 == 1))
            {
                file << "\n *No algorithm matching the security requirement is found!" << endl; //Prints the full meaning of "*No matching Algo found"
            }

            if(total_reqWeight > 5.0 && fms < fms_ || rs < rs_)
            {
                file << "\n\n\t\t\t\t WARNING! LIMITED RESOURCES  " << endl;
                file << "\t      Implementing all algorithms may have negative impact on performance." << endl;
            }

            file.close();
     }
     else
     {
        cout <<"\n\tFile failed to open!" << endl;
     }
}

double Processing_and_Output::reqWeighting(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6)
{
    double total_reqWeight = 0, reqWeight1 = 0, reqWeight2 = 0, reqWeight3 = 0, reqWeight4 = 0, reqWeight5 = 0, reqWeight6 = 0;

    if(flag1 == 1 && flag4 ==1)
    {
        reqWeight1 = 2.5;
    }
    else if(flag1 == 1 && flag4 !=1)
    {
         reqWeight1 = 2.5;
    }
    if(flag2 == 1)
    {
        reqWeight2 = 2.5;
    }
    if(flag3 ==1)
    {
      reqWeight3 = 2.5;
    }
    if(flag4 ==1 && flag1 != 1)
    {
         reqWeight4 = 2.5;
    }
    if(flag5 == 1)
    {
       reqWeight5 = 2.5;
    }
    if(flag6 ==1)
    {
        reqWeight6 = 2.5;
    }

    total_reqWeight = reqWeight1 + reqWeight2 + reqWeight3 + reqWeight4 + reqWeight5 + reqWeight6;

    return total_reqWeight;
}

void Processing_and_Output::displayReq_Mech_mapping(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight, int warn1, string request_id)
{
        std::cout << "\n" "***********************************************************************************************************" << endl;
        std::cout<<"\t\t FINAL RESULTS FOR THE USER WITH REQUEST ID No.: " << request_id << endl << endl;


    string s1, s2, s3, s4, s5, s6;
    s1.erase(); s2.erase(); s3.erase(); s4.erase(); s5.erase(); s6.erase();
    int flag_1, flag_2, flag_3, flag_4, flag_5, flag_6;

    if(flag1 == 1 && flag4 ==1)
    {
        s1 = "Data Confidentiality/User Privacy";
        flag_1 = 1;
    }
    else if(flag1 == 1 && flag4 !=1)
    {
         s1 ="Data Confidentiality";
         flag_1 = 1;
    }
    if(flag2 == 1)
    {
        s2 = "Message Integrity";
        flag_2 = 1;
    }
    if(flag3 ==1)
    {
      s3 = "Authentication";
      flag_3 = 1;
    }
    if(flag4 ==1 && flag1 != 1)
    {
         s4 = "User Privacy";
         flag_4 = 1;
    }
    if(flag5 == 1)
    {
       s5 = "Non-repudiation";
       flag_5 = 1;
    }
    if(flag6 ==1)
    {
        s6 = "Confidentiality & Authenticity";
        flag_6 = 1;
    }

    if(total_reqWeight == 2.5)
    {
        cout << "\n YOUR SECURITY REQUIREMENT AND RECOMMENDED SECURITY MECHANISM AND SECURITY ALGORITHM ARE: \n" << endl;
    }
    else
    {
        cout << "\n YOUR SECURITY REQUIREMENTS AND RECOMMENDED SECURITY MECHANISMS AND SECURITY ALGORITHMS ARE: \n" << endl;
    }

    format_Print_output(s1, s2, s3, s4, s5, s6, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6);

        Report report;

        string REQST_id,	Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15;
                REQST_id = request_id;

                string findbyID_query = "select * from requirements_for_report where REQST_id = " + ("'"+REQST_id+"'");
                        const char* qn = findbyID_query.c_str();
                        qstate = mysql_query(conn, qn);

                        if(!qstate)
                        {
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                Re_1 = row[1];
                                Re_2 = row[2];
                                Re_3 = row[3];
                                Re_4 = row[4];
                                Re_5 = row[5];
                                Re_6 = row[6];
                                Re_7 = row[7];
                                Re_8 = row[8];
                                Re_9 = row[9];
                                Re_10 = row[10];
                                Re_11 = row[11];
                                Re_12 = row[12];
                                Re_13 = row[13];
                                Re_14 = row[14];
                                Re_15 = row[15];
                            }
                        }
                        else
                        {
                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                        }

                    char ch;
                    level:
                        int flac = 0;

                    if((!algo_name1.empty() || !algo_name2.empty() || !algo_name1.empty() || !algo_name4.empty() || !algo_name5.empty() || !algo_name6.empty()) && (!Re_6.empty() || !Re_7.empty() || !Re_8.empty() || !Re_9.empty() || !Re_10.empty() || !Re_11.empty() || !Re_12.empty() || !Re_13.empty() || !Re_14.empty() || !Re_15.empty()))
                    {
                         flac = 1;
                         std::cout << "\n  Would you like to see a detailed report on the recommended algorithms and the other requirements?: \n";
                    }
                    else if(!algo_name1.empty() || !algo_name2.empty() || !algo_name1.empty() || !algo_name4.empty() || !algo_name5.empty() || !algo_name6.empty())
                    {
                        flac = 2;
                        std::cout << "\n   \tWould you like to see a detailed report on the recommended algorithms?: \n";
                    }
                    else
                    {
                        std::cout << "\n\n\n  You don't have any security requirement, or no algorithms matching your security requirements are found.\n";
                        cout << "\n\n\t\t\t\tPress Enter to return to MAIN MENU \n";
                        return;
                    }

                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No, thank you";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

						std::cin>>ch;

						switch(ch)
						{
						case '1':
                                 {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************" << endl;
                                    std::cout<<"\t\t FINAL RESULTS FOR USER WITH REQUEST ID No.: " << request_id << endl << endl;


                                        string s1, s2, s3, s4, s5, s6;
                                        s1.erase(); s2.erase(); s3.erase(); s4.erase(); s5.erase(); s6.erase();
                                        int flag_1, flag_2, flag_3, flag_4, flag_5, flag_6;

                                        if(flag1 == 1 && flag4 ==1)
                                        {
                                            s1 = "Data Confidentiality/User Privacy";
                                            flag_1 = 1;
                                        }
                                        else if(flag1 == 1 && flag4 !=1)
                                        {
                                             s1 ="Data Confidentiality";
                                             flag_1 = 1;
                                        }
                                        if(flag2 == 1)
                                        {
                                            s2 = "Message Integrity";
                                            flag_2 = 1;
                                        }
                                        if(flag3 ==1)
                                        {
                                          s3 = "Authentication";
                                          flag_3 = 1;
                                        }
                                        if(flag4 ==1 && flag1 != 1)
                                        {
                                             s4 = "User Privacy";
                                             flag_4 = 1;
                                        }
                                        if(flag5 == 1)
                                        {
                                           s5 = "Non-repudiation";
                                           flag_5 = 1;
                                        }
                                        if(flag6 ==1)
                                        {
                                            s6 = "Confidentiality & Authenticity";
                                            flag_6 = 1;
                                        }

                                        if(total_reqWeight == 2.5)
                                        {
                                            cout << "\n YOUR SECURITY REQUIREMENT AND RECOMMENDED SECURITY MECHANISM AND SECURITY ALGORITHM ARE: \n" << endl;
                                        }
                                        else
                                        {
                                            cout << "\n YOUR SECURITY REQUIREMENTS AND RECOMMENDED SECURITY MECHANISMS AND SECURITY ALGORITHMS ARE: \n" << endl;
                                        }

                                        format_Print_output(s1, s2, s3, s4, s5, s6, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6);


                                    report.formatReport_for_Consle(request_id, flac, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15);
                            break;
                            }
                        case '2':

                            break;
						default:
							system("cls");
							std::cout << "\n\t\tSorry! Wrong option selected." << std:: endl;
                            goto level;
						}

                        flac = 0;

    if(warn1 == 1)
    {

    }
    else
    {
        cout << "\n\n\t\t\t\tPress Enter to return to MAIN MENU \n";
    }
}

void Processing_and_Output::write_Req_Mech_mapping(int flag1, int flag2, int flag3, int flag4, int flag5, int flag6, string algo_name1, string algo_name2, string algo_name3, string algo_name4, string algo_name5, string algo_name6, double total_reqWeight, double fms, double rs, double fms_, double rs_, string request_id)
{
    string s1, s2, s3, s4, s5, s6;
    s1.erase(); s2.erase(); s3.erase(); s4.erase(); s5.erase(); s6.erase();
    int flag_1, flag_2, flag_3, flag_4, flag_5, flag_6;

    if(flag1 == 1 && flag4 ==1)
    {
        s1 = "Data Confidentiality/User Privacy";
        flag_1 = 1;
    }
    else if(flag1 == 1 && flag4 !=1)
    {
         s1 ="Data Confidentiality";
         flag_1 = 1;
    }
    if(flag2 == 1)
    {
        s2 = "Message Integrity";
        flag_2 = 1;
    }
    if(flag3 ==1)
    {
      s3 = "Authentication";
      flag_3 = 1;
    }
    if(flag4 ==1 && flag1 != 1)
    {
         s4 = "User Privacy";
         flag_4 = 1;
    }
    if(flag5 == 1)
    {
       s5 = "Non-repudiation";
       flag_5 = 1;
    }
    if(flag6 ==1)
    {
        s6 = "Confidentiality & Authenticity";
        flag_6 = 1;
    }

    format_TextOutput(s1, s2, s3, s4, s5, s6, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6, total_reqWeight, fms, rs, fms_, rs_, request_id);

    Report report;

     string REQST_id,	Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15;
                REQST_id = request_id;

                string findbyID_query = "select * from requirements_for_report where REQST_id = " + ("'"+REQST_id+"'");
                        const char* qn = findbyID_query.c_str();
                        qstate = mysql_query(conn, qn);

                        if(!qstate)
                        {
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                Re_1 = row[1];
                                Re_2 = row[2];
                                Re_3 = row[3];
                                Re_4 = row[4];
                                Re_5 = row[5];
                                Re_6 = row[6];
                                Re_7 = row[7];
                                Re_8 = row[8];
                                Re_9 = row[9];
                                Re_10 = row[10];
                                Re_11 = row[11];
                                Re_12 = row[12];
                                Re_13 = row[13];
                                Re_14 = row[14];
                                Re_15 = row[15];
                            }
                        }
                        else
                        {
                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                        }

                    int flac = 0;

                    if((!algo_name1.empty() || !algo_name2.empty() || !algo_name1.empty() || !algo_name4.empty() || !algo_name5.empty() || !algo_name6.empty()) && (!Re_6.empty() || !Re_7.empty() || !Re_8.empty() || !Re_9.empty() || !Re_10.empty() || !Re_11.empty() || !Re_12.empty() || !Re_13.empty() || !Re_14.empty() || !Re_15.empty()))
                    {
                         flac = 1;
                    }
                    else if(!algo_name1.empty() || !algo_name2.empty() || !algo_name1.empty() || !algo_name4.empty() || !algo_name5.empty() || !algo_name6.empty())
                    {
                        flac = 2;
                    }

    report.formatReport_for_TextFile(request_id, flac, algo_name1, algo_name2, algo_name3, algo_name4, algo_name5, algo_name6, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15);

    std::ofstream Detail_Results_Combined("Detail_Results_Combined");
    if(report.mergeFiles("C:\\Users\\Admin\\Desktop\\My_WorkSpace\\Tool_with_passwordAndSalt\\Final_Result.txt",  Detail_Results_Combined));
    if(report.mergeFiles("C:\\Users\\Admin\\Desktop\\My_WorkSpace\\Tool_with_passwordAndSalt\\Detail_Result.txt",  Detail_Results_Combined));
}

class UserInput
{
   friend class LoginManager;

   public:
   string Request_ID, Hardware_type, CPU, FlashMem_size, Ram_size, Clock_speed, Applic_Domain, Payload_size, Req_1, Req_2, Req_3, Req_4, Req_5, Req_6, Energy, cct_area_1 = "", tp_1 = "", cct_area_2, tp_2, cct_area_3, tp_3, cct_area_4, tp_4, cct_area_5, tp_5, cct_area_6, tp_6;
   string Reqst_ID, state, Domain, anyUsr, anyUsrLogin, holdUsrInfo, storeAnyInfo, sensitivOfInfo, infoSent2E, connected, dataSent2Cloud, dataStoredInDb, regulaUpdate, use3rdPrtySfw, possibltOfEvesdrop, possibltOfCapt_Resent, possibltOfImpersontUsr, possibltOfPhysiclAcces;
   string Reqmt_1, Reqmt_2, Reqmt_3, Reqmt_4, Reqmt_5, Reqmt_6, Reqmt_7, Reqmt_8, Reqmt_9, Reqmt_10, Reqmt_11, Reqmt_12, Reqmt_13, Reqmt_14, Reqmt_15;
   string REQST_id,	Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15;
   string FM_1, RAM_1, FM_2, RAM_2, FM_3, RAM_3, FM_4, RAM_4, FM_5, RAM_5, FM_6, RAM_6;
   string Status, Struct1, Struct2, Struct3, Struct4, Struct5, Struct6, Struct7, Struct8, Struct9, Struct10, Struct11, usrRegist, typeOfRegist, usrInput, typeOfAUTH, useDb, typeOfDataStorg, typeOfDb, progrm1, progrm2, progrm3, progrm4, progrm5, progrm6, progrm7, progrm8, fileUpload, sysLog;

   UserInput();
   auto countDigits_lengthOfString_firstCharacter(string& st);
   void getUserInput_RE();
   void modifyUserRequirements_Elicitation_requests();
   void deleteRequest_RE();
   void showAndDeleteUser_Request_RE();
   void getUserInput();
   void selectSecurityRequirements_Software();
   void selectSecurityRequirements_Hardware();
   void importSecReqmts_Software();
   void importSecReqmts_Hardware();
   void getOther_inputs();
   void getInput_for_HardwareImplementaion();
   void getInput_for_softwareImplementaion();
   void showAndModifyUser_request();
   void modifySoftware_request();
   void modifyHardware_request();
   void deleteRequest();
   void showAndDeleteUser_Request();
   void selectSecurityRequirements_existing();
   void getUserInput_BestPractGuide();
   void modifyBestPractGuide_requests();
   void deleteBestPractGuide();
   void showAndDeleteUser_BestPractGuide();

   friend class SecurityMngr;
};

	UserInput::UserInput()
	{
		conn = mysql_init(0);
		if(conn)
			cout << "Connection object is OK, conn = " << conn << endl;
		else
			cout << "Connection object problem: " << mysql_error(conn);

		conn = mysql_real_connect(conn,"localhost","root","tryit123","iot-harpseca_db",0,NULL,0);
		if(conn)
        {
         cout << "Connection to database is successful!" << endl;
        }
	   else
       {
        cout << "Connection problem: " << mysql_error(conn) << endl;
       }
	}

    auto UserInput::countDigits_lengthOfString_firstCharacter(string& st)
    {
       struct result
                {
                    int n1;
                    int n2;
                    char c;
                };

      int count_=0;
      for(int i=0;i<st.size();i++)
         if(isdigit(st[i])) count_++;

        int length = st.length();

        char first_character = st.at(0);

         return result {count_, length, first_character};
    }

	void UserInput::getUserInput_RE()
	{
	    Preliminary pre;

            int num_digits;
            int string_length;
           char first_letter;

           system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\t\t\t\tNEW REQUIREMENT ELICITATION REQUEST \n\n";
            std::cout << "\n\t\t   YOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH AN R,"<< endl;
            std::cout <<"\t\t\t\t  FOLLOWED BY 4 INTEGERS (e.g., R1234)" << endl;
            std::cout << "\n\t\t\t\tPlease enter your unique request ID: ";
            std::cin >> Reqst_ID;

           pre.convert_lowerC_to_upperC(Reqst_ID);

            auto collector = countDigits_lengthOfString_firstCharacter(Reqst_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

            while(num_digits !=4 || string_length != 5 || first_letter != 'R')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t     ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t   YOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH AN R,"<< endl;
                std::cout <<"\t\t\t  FOLLOWED BY 4 INTEGERS (e.g., R1234)" << endl;
                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Reqst_ID;

               pre.convert_lowerC_to_upperC(Reqst_ID);

                auto collector = countDigits_lengthOfString_firstCharacter(Reqst_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

             char ch;
         level0:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	std::cout << "\n    THIS TOOL WILL GENERATE THE SECURITY REQUIREMENTS OF YOUR  SYSTEM BASED ON THE ANSWERS YOU PROVIDE.\n\n" << endl;
           	std::cout << "\n\n\n\n\n\t\t\t\t\t   Press enter to start. ";
            cin.get() != '\n';

	    std::cin.ignore();
	    int choice;
         level:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	std::cout << "\n\tSelect your application domain: \n";

                std::cout << "\n\t1) Smart Home";
                std::cout << "\n\t2) Smart City";
                std::cout << "\n\t3) Smart Agriculture";
                std::cout << "\n\t4) Smart Grid";
                std::cout << "\n\t5) Smart Healthcare";
                std::cout << "\n\t6) Smart Elderly Monitoring";
                std::cout << "\n\t7) Smart Kid Monitoring";
                std::cout << "\n\t8) Smart pet Monitoring";
                std::cout << "\n\t9) Smart Banking/Financial applications";
                std::cout << "\n\t10) Industrial Automation";
                std::cout << "\n\t11) Smart Supply Chain";
                std::cout << "\n\t12) Smart Retail";
                std::cout << "\n\t13) Smart Environmental Monitoring";
                std::cout << "\n\t14) Smart Automotive/Transportation";
                std::cout << "\n\t15) Smart Toy";
                std::cout << "\n\t16) Wearable";
                std::cout << "\n\t17) Connected Car";
                std::cout << "\n\t18) Other Domain";

            cout << endl << "\n\tEnter the S/N of your option (1-18) and Press enter: ";
            cin >> choice;

                switch(choice)
                {
                    case 1:
                        Domain = "Home";
                         break;
                    case 2:
                        Domain = "City";
                        break;
                     case 3:
                        Domain = "Agriculture";
                        break;
                      case 4:
                        Domain = "Grid";
                        break;
                      case 5:
                        Domain = "Healthcare";
                        break;
                      case 6:
                        Domain = "Elderly";
                        break;
                      case 7:
                        Domain = "Kid";
                        break;
                        case 8:
                            Domain = "Pet";
                            break;
                        case 9:
                            Domain = "Financial";
                            break;
                        case 10:
                            Domain = "Industrial";
                            break;
                        case 11:
                            Domain = "Supply_Chain";
                            break;
                        case 12:
                            Domain = "Retail";
                            break;
                        case 13:
                            Domain = "Environmental";
                            break;
                        case 14:
                            Domain = "Transportation";
                            break;
                         case 15:
                            Domain = "Toy";
                            break;
                         case 16:
                            Domain = "Wearable";
                            break;
                        case 17:
                            Domain = "Connected_Car";
                            break;
                         case 18:
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tEnter one word that best describes your domain: ";
                            cin >> Domain;
                            break;
                        default: cout << "Please choose between 1-18 (Press Enter to continue ...)";
                            goto level;
                            break;
                }


            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system? \n";

                        std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                        std::cout<<"\n\t\t2. Existing System";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

                       string state1;
						std::cin>>ch;

						switch(ch)
						{
						case '1':
                            state1 = "0";
                            state = "Off";
                            break;
                        case '2':
                             state1= "1";
                             state = "On";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level0;
						}


                    //std::cin.ignore();
                    char cho;
                    level2:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";

                     if(state1 == "1")
                    {
                        std::cout << "\n\tDoes the system have a user? \n";
                    }
                    else
                    {
                        std::cout << "\n\tWill the system have a user? \n";
                    }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>cho;

						switch(cho)
						{
						case '1':
                            anyUsr= "Yes";
                            break;
                        case '2':
                            anyUsr = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level2;
						}

                    char choi;
                    level3:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    int flag_1 = 0;
                    if(anyUsr == "Yes")
                    {
                        if(state1 == "1")
                            {
                                std::cout << "\n\tDoes the system have a user LogIn? \n";
                            }
                            else
                            {
                                std::cout << "\n\tWill the system have a user LogIn? \n";
                            }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choi;

                                        switch(choi)
                                        {
                                        case '1':
                                            anyUsrLogin= "Yes";
                                            break;
                                        case '2':
                                            anyUsrLogin = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level3;
                                        }

                             char choic;
                             level4:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                if(state1 == "1")
                                {
                                    std::cout << "\n\tDoes the system store user information? \n";
                                }
                                else
                                {
                                    std::cout << "\n\tWill the system store any user information? \n";
                                }
                                            std::cout<<"\n\t\t1. Yes ";
                                            std::cout<<"\n\t\t2. No";
                                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                            std::cin>>choic;

                                            switch(choic)
                                            {
                                            case '1':
                                                holdUsrInfo = "Yes";
                                                break;
                                            case '2':
                                                holdUsrInfo = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level4;
                                            }

                             char choic_;
                             level4_:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                if(state1 == "1")
                                {
                                    flag_1 = 1;
                                    std::cout << "\n\tDoes the system store any other information? \n";
                                }
                                else
                                {
                                    flag_1 = 1;
                                    std::cout << "\n\tWill the system store any other information? \n";
                                }
                                            std::cout<<"\n\t\t1. Yes ";
                                            std::cout<<"\n\t\t2. No";
                                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                            std::cin>>choic_;

                                            switch(choic_)
                                            {
                                            case '1':
                                                storeAnyInfo = "Yes";//This variable also serves as other info aside from usr info
                                                break;
                                            case '2':
                                                storeAnyInfo = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level4_;
                                            }
                    }


            if(holdUsrInfo != "Yes" && flag_1 != 1)
            {
                  char choict;
                level5:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state1 == "1")
                {
                    std::cout << "\n\tDoes the system store any kind of information? \n";
                }
                else
                {
                    std::cout << "\n\tWill the system store any kind of information? \n";
                }
                            std::cout<<"\n\t\t1. Yes ";
                            std::cout<<"\n\t\t2. No";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                            std::cin>>choict;

                            switch(choict)
                            {
                            case '1':
                                storeAnyInfo = "Yes";
                                break;
                            case '2':
                                storeAnyInfo = "No";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level5;
                            }
            }
                flag_1 = 0;

            if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
            {
                 char choicn;
                level6:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state1 == "1")
                {
                     std::cout << "\n\tWhat type of information does the system store? \n";
                }
                else
                {
                     std::cout << "\n\tWhat type of information will the system store? \n";
                }

                            std::cout<<"\n\t\t1. Normal Information ";
                            std::cout<<"\n\t\t2. Sensitive Information";
                            std::cout<<"\n\t\t3. Critical Information";

                            std::cout<<"\n\n\tSelect Your Option (1-3): ";
                            std::cin>>choicn;

                            switch(choicn)
                            {
                            case '1':
                                sensitivOfInfo = "Normal";
                                break;
                            case '2':
                                sensitivOfInfo = "Sensitive";
                                break;
                            case '3':
                                sensitivOfInfo = "Critical";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level6;
                            }
            }


             if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
            {
                 char choicm;
                level7:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state1 == "1")
                {
                    std::cout << "\n\tDoes the system send the information to an entity? \n";
                }
                else
                {
                    std::cout << "\n\tWill the information be sent to an entity? \n";
                }
                            std::cout<<"\n\t\t1. Yes ";
                            std::cout<<"\n\t\t2. No";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                            std::cin>>choicm;

                            switch(choicm)
                            {
                            case '1':
                                infoSent2E = "Yes";
                                break;
                            case '2':
                               infoSent2E = "No";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level7;
                            }
            }


              char choa;
         level8:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	if(state1 == "1")
            {
                std::cout << "\n\tIs the system connected to the Internet? \n";
            }
            else
            {
                std::cout << "\n\tWill the system be connected to the Internet? \n";
            }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choa;

						switch(choa)
						{
						case '1':
                            connected = "Yes";
                            break;
                        case '2':
                            connected = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level8;
						}


                char choe;
         level9:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            if(state1 == "1")
            {
                std::cout << "\n\tDoes it send data to a cloud? \n";
            }
            else
            {
                std::cout << "\n\tWill it send its data to a cloud? \n";
            }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choe;

						switch(choe)
						{
						case '1':
                            dataSent2Cloud = "Yes";
                            break;
                        case '2':
                            dataSent2Cloud= "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level9;
						}

                char chou;
                level10:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state1 == "1")
                {
                    std::cout << "\n\tDoes it store data in a database? \n";
                }
                else
                {
                    std::cout << "\n\tWill it store data in a database? \n";
                }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>chou;

						switch(chou)
						{
						case '1':
                            dataStoredInDb = "Yes";
                            break;
                        case '2':
                            dataStoredInDb = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level10;
						}

                char chok;
                level11:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";

                if(state1 == "1")
                {
                    std::cout << "\n\tDoes the system receive regular updates?  \n";
                }
                else
                {
                    std::cout << "\n\tWill the system receive regular updates?  \n";
                }

                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>chok;

						switch(chok)
						{
						case '1':
                            regulaUpdate = "Yes";
                            break;
                        case '2':
                            regulaUpdate = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level11;
						}

				char choke;
                level12:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state1 == "1")
                {
                    std::cout << "\n\tDoes the system use third-party software?  \n";
                }
                else
                {
                    std::cout << "\n\tWill the system use third-party software?  \n";
                }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choke;

						switch(choke)
						{
						case '1':
                            use3rdPrtySfw = "Yes";
                            break;
                        case '2':
                            use3rdPrtySfw = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level12;
						}


                     if(infoSent2E == "Yes" || connected == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes" || regulaUpdate == "Yes")
                     {
                         char chokey;
                        level13:
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        std::cout << "\n\tIs there a possibility of the communications being eavesdropped? \n";
                                    std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>chokey;

						switch(chokey)
						{
						case '1':
                            possibltOfEvesdrop = "Yes";
                            break;
                        case '2':
                            possibltOfEvesdrop = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level13;
						}
                     }


                    if(infoSent2E == "Yes" || connected == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes" || regulaUpdate == "Yes")
                    {
                         char okey;
                            level14:
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tCould the messages sent between the system components be captured and resend? \n";

                            std::cout<<"\n\t\t1. Yes ";
                            std::cout<<"\n\t\t2. No";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                            std::cin>>okey;

                            switch(okey)
                            {
                            case '1':
                                possibltOfCapt_Resent = "Yes";
                                break;
                            case '2':
                                possibltOfCapt_Resent = "No";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level14;
                            }
                    }


                     if(anyUsr == "Yes")
                     {
                        char key;
                            level15:
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tCan someone try to impersonate a user to gain access to private information? \n";

                            std::cout<<"\n\t\t1. Yes ";
                            std::cout<<"\n\t\t2. No";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                            std::cin>>key;

                            switch(key)
                            {
                            case '1':
                                possibltOfImpersontUsr = "Yes";
                                break;
                            case '2':
                                possibltOfImpersontUsr = "No";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level15;
                            }
                     }

                        char keya;
                        level16:
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        std::cout << "\n\tCan someone with bad intentions gain physical access to the system? \n";

                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>keya;

						switch(keya)
						{
						case '1':
                            	possibltOfPhysiclAcces = "Yes";
                            break;
                        case '2':
                            	possibltOfPhysiclAcces = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level16;
						}

               string request_query = "insert into users_requests_re (Reqst_ID, state, Domain, anyUsr, anyUsrLogin, holdUsrInfo, storeAnyInfo, sensitivOfInfo, infoSent2E, connected, dataSent2Cloud, dataStoredInDb, regulaUpdate, use3rdPrtySfw, possibltOfEvesdrop, possibltOfCapt_Resent, possibltOfImpersontUsr, possibltOfPhysiclAcces) values('"+Reqst_ID+"', '"+state+"', '"+Domain +"', '"+anyUsr+"', '"+anyUsrLogin +"', '"+holdUsrInfo +"', '"+storeAnyInfo +"', '"+sensitivOfInfo +"', '"+infoSent2E +"', '"+connected +"', '"+dataSent2Cloud +"', '"+dataStoredInDb +"', '"+regulaUpdate +"', '"+use3rdPrtySfw +"', '"+possibltOfEvesdrop +"', '"+possibltOfCapt_Resent +"', '"+possibltOfImpersontUsr +"', '"+possibltOfPhysiclAcces+"')";

              const char* qr = request_query.c_str();
              qstate = mysql_query(conn, qr);

                if(!qstate)
                {
                     system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "\n\n\t\tData being saved .....\n";
                     sensitivOfInfo.erase(); infoSent2E.erase();

                    cout << endl << "\n\n\t\tRequest Successfully added in the database!" << endl;

                    cout << endl << "\n\n\t\tPress Enter to go back to the Main Menu." << endl;
                }
                else
                {
                    cout << "\n\n\tQuery Execution Problem! Error Number: " << mysql_errno(conn) << endl;
                    cout << "\n\n\tError Number 1062 implies that the entered Request ID already exist in database.\n" << endl;
                    cout << endl << "\n\n\tPlease press Enter to go back to the Main Menu and repeat the process with a unique ID." << endl;
                }

	}

	void UserInput::getUserInput_BestPractGuide()
	{
	    Preliminary pre;

            int num_digits;
            int string_length;
           char first_letter;

           system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\t\t   NEW BEST PRACTICE GUIDE FOR SECURE DEVELOPMENT REQUEST \n\n";
            std::cout << "\n\t\t   YOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH A 'B',"<< endl;
            std::cout <<"\t\t\t\t  FOLLOWED BY 4 INTEGERS (e.g., B1234)" << endl;
            std::cout << "\n\t\t\t\tPlease enter your unique request ID: ";
            std::cin >> Request_ID;

           pre.convert_lowerC_to_upperC(Request_ID);

            auto collector = countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

            while(num_digits !=4 || string_length != 5 || first_letter != 'B')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t     ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t   YOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH A B,"<< endl;
                std::cout <<"\t\t\t  FOLLOWED BY 4 INTEGERS (e.g., B1234)" << endl;
                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

               pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

             char ch;
         level0:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	std::cout << "\n    THIS TOOL WILL GENERATE A BEST PRACTICE GUIDE FOR YOUR SYSTEM BASED ON THE ANSWERS YOU PROVIDE.\n\n" << endl;
           	std::cout << "\n\n\n\n\n\t\t\t\t\t   Press enter to start. ";
            cin.get() != '\n';


	    system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system?  \n";

                        std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                        std::cout<<"\n\t\t2. Existing System ";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

                       string state;
						std::cin>>ch;

						switch(ch)
						{
						case '1':
                            state = "0";
                            Status = "NotYet";
                            break;
                        case '2':
                            state = "1";
                            Status = "Exist";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level0;
						}


        int choose;
         level_tk:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "  Choose what best describes your IoT System architecture (you can choose multiple options) \n";

        do{
                std::cout << "\n\t1) Device Management (e.g., Sensors, Actuators, Gateways)";
                std::cout << "\n\t2) Data Collection";
                std::cout << "\n\t3) Connectivity Management";
                std::cout << "\n\t4) API Services";
                std::cout << "\n\t5) Data Management";
                std::cout << "\n\t6) Data Processing";
                std::cout << "\n\t7) Big Data Analytics/Advanced Analytics";
                std::cout << "\n\t8) Data Center and Cloud Services";
                std::cout << "\n\t9) Web Services/Web apps (e.g., Web apps, Mobile apps, Desktop apps development, etc.)";
                std::cout << "\n\t10) Embedded Systems";
                std::cout << "\n\t11) Other";
                std::cout << "\n\t12) Done! \n";

            cout << endl << "  Enter the S/N of your option (1-11) and press enter each time, and 12 when you are done: ";
            cin >> choose;

            switch(choose)
            {
                case 1:
                    Struct1 = "Device_Mgmt";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Device Management! Select other IoT System Structure or Done." <<endl;
                     break;
                case 2:
                Struct2 = "Data_Collect";
                 system("cls");
                 std::cout<<"\n" "***********************************************************************************************************\n";
                  cout << "\n\tYou have selected Data Collection! Select other IoT System Structure or Done." <<endl;
                    break;
                  case 3:
                   Struct3 = "Connect_Mgmt";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Connectivity Management! Select other IoT System Structure or Done." <<endl;
                    break;
                  case 4:
                   Struct4 = "API_Service";
                   system("cls");
                   std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected API Services! Select other IoT System Structure or Done." <<endl;
                    break;
                  case 5:
                   Struct5 = "Data_Mgmt";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Data Management! Select other IoT System Structure or Done." <<endl;
                    break;
                case 6:
                   Struct6 = "Data_Process";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Data Processing! Select other IoT System Structure or Done." <<endl;
                    break;
                case 7:
                    Struct7 = "Analytics";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Big Data Analytics/Advanced Analytics! Select other IoT System Structure or Done." <<endl;
                     break;
                case 8:
                    Struct8 = "Cloud_Service";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Data Center and Cloud Services! Select other IoT System Structure or Done." <<endl;
                     break;
                case 9:
                    Struct9 = "Web";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Web Services/Web apps! Select other IoT System Structure or Done." <<endl;
                     break;
                case 10:
                    Struct10 = "Embedded_Sys";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                     cout << "\n\tYou have selected Visualization! Select other IoT System Structure or Done." <<endl;
                     break;
                case 11:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "\n\tEnter one word that best describes your IoT system structure: ";
                    cin >> Struct11;
                     break;
                case 12:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                  cout << "\n\tDone!" <<endl;
                    break;

                default: cout << "Please choose between 1-8 (Press Enter to continue ...)";
                goto level_tk;
                break;
            }

        }while(choose != 12);
                    char cho;
                    level2:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";

                     if(state == "1")
                    {
                        std::cout << "\n\tDoes the system have a user? \n";
                    }
                    else
                    {
                        std::cout << "\n\tWill the system have a user? \n";
                    }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>cho;

						switch(cho)
						{
						case '1':
                            anyUsr= "Yes";
                            break;
                        case '2':
                            anyUsr = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;//
                        goto level2;
						}

                    char chic;
                    level2a:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    if(anyUsr == "Yes")
                    {
                         if(state == "1")
                            {
                                std::cout << "\n\tDoes the system have a provision for user registration? \n";
                            }
                            else
                            {
                                std::cout << "\n\tWill the system have any provision for user registration? \n";
                            }
                                std::cout<<"\n\t\t1. Yes ";
                                std::cout<<"\n\t\t2. No";
                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                std::cin>>chic;

                                switch(chic)
                                {
                                case '1':
                                    usrRegist= "Yes";
                                    break;
                                case '2':
                                    usrRegist = "No";
                                    break;
                                default:
                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                goto level2a;
                                }
                    }

                    char chac;
                    level2b:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    if(anyUsr == "Yes" && usrRegist == "Yes")
                    {
                         if(state == "1")
                            {
                                std::cout << "\n\tWho registers users? \n";
                            }
                            else
                            {
                                std::cout << "\n\tWho will register users? \n";
                            }
                                std::cout<<"\n\t\t1. Users themselves ";
                                std::cout<<"\n\t\t2. An administrator";
                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                std::cin>>chac;

                                switch(chac)
                                {
                                case '1':
                                    typeOfRegist= "Users";
                                    break;
                                case '2':
                                    typeOfRegist = "Admin";
                                    break;
                                default:
                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                goto level2b;
                                }
                    }


                    char choi;
                    level3:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    if(anyUsr == "Yes" && usrRegist == "Yes")
                    {
                        if(state == "1")
                            {
                                std::cout << "\n\tDoes the system have a user LogIn? \n";
                            }
                            else
                            {
                                std::cout << "\n\tWill the system have a user LogIn? \n";
                            }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choi;

                                        switch(choi)
                                        {
                                        case '1':
                                            anyUsrLogin= "Yes";
                                            break;
                                        case '2':
                                            anyUsrLogin = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;//
                                        goto level3;
                                        }
                    }

                    char choia;
                    level3a:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    int flag_1 = 0;
                    if(anyUsr == "Yes")
                    {
                        if(state == "1")
                            {
                                std::cout << "\n\tDoes the system allow users to enter any input? \n";
                            }
                            else
                            {
                                std::cout << "\n\tWill the system allow users to enter any input? \n";
                            }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choia;

                                        switch(choia)
                                        {
                                        case '1':
                                            usrInput= "Yes";
                                            break;
                                        case '2':
                                            usrInput = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level3a;
                                        }
                        }

                                char choic;
                                level4:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                 if(anyUsr == "Yes")
                                 {
                                     if(state == "1")
                                        {
                                            std::cout << "\n\tDoes the system store user information? \n";
                                        }
                                        else
                                        {
                                            std::cout << "\n\tWill the system store any user information? \n";
                                        }
                                                    std::cout<<"\n\t\t1. Yes ";
                                                    std::cout<<"\n\t\t2. No";
                                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                    std::cin>>choic;

                                                    switch(choic)
                                                    {
                                                    case '1':
                                                        holdUsrInfo = "Yes";
                                                        break;
                                                    case '2':
                                                        holdUsrInfo = "No";
                                                        break;
                                                    default:
                                                        std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                    goto level4;
                                                    }
                                 }

                             char choic_;
                             level4_:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                if(holdUsrInfo == "Yes")
                                {
                                    if(state == "1")
                                        {
                                            flag_1 = 1;
                                            std::cout << "\n\tDoes the system store any other information? \n";
                                        }
                                        else
                                        {
                                            flag_1 = 1;
                                            std::cout << "\n\tWill the system store any other information? \n";
                                        }
                                                    std::cout<<"\n\t\t1. Yes ";
                                                    std::cout<<"\n\t\t2. No";
                                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                    std::cin>>choic_;

                                                    switch(choic_)
                                                    {
                                                    case '1':
                                                        storeAnyInfo = "Yes";
                                                        break;
                                                    case '2':
                                                        storeAnyInfo = "No";
                                                        break;
                                                    default:
                                                        std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                    goto level4_;
                                                    }
                                }

                            //


            if(holdUsrInfo != "Yes" && flag_1 != 1)
            {
                  char choict;
                level5:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state == "1")
                {
                    std::cout << "\n\tDoes the system store any kind of information? \n";
                }
                else
                {
                    std::cout << "\n\tWill the system store any kind of information? \n";
                }
                            std::cout<<"\n\t\t1. Yes ";
                            std::cout<<"\n\t\t2. No";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                            std::cin>>choict;

                            switch(choict)
                            {
                            case '1':
                                storeAnyInfo = "Yes";
                                break;
                            case '2':
                                storeAnyInfo = "No";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level5;
                            }
            }
                flag_1 = 0;

            if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
            {
                 char choicn;
                level6:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state == "1")
                {
                     std::cout << "\n\tWhat type of information does the system store? \n";
                }
                else
                {
                     std::cout << "\n\tWhat type of information will the system store? \n";
                }

                            std::cout<<"\n\t\t1. Normal Information ";
                            std::cout<<"\n\t\t2. Sensitive Information";
                            std::cout<<"\n\t\t3. Critical Information";

                            std::cout<<"\n\n\tSelect Your Option (1-3): ";
                            std::cin>>choicn;

                            switch(choicn)
                            {
                            case '1':
                                sensitivOfInfo = "Normal";
                                break;
                            case '2':
                                sensitivOfInfo = "Sensitive";
                                break;
                            case '3':
                                sensitivOfInfo = "Critical";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level6;
                            }
            }


                 char choicm;
                level7:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state == "1")
                {
                    std::cout << "\n\tWhat type of authentication is implemented in the system? \n";
                }
                else
                {
                    std::cout << "\n\tWhat type of authentication will be implemented in the system? \n";
                }
                            std::cout<<"\n\t\t1. No Authentication ";
                            std::cout<<"\n\t\t2. Username and Password";
                            std::cout<<"\n\t\t3. Social Networks/Email Authentication";
                            std::cout<<"\n\t\t4. SmartCard";
                            std::cout<<"\n\t\t5. Biometrics";
                            std::cout<<"\n\t\t6. Two Factor Authentication ";
                            std::cout<<"\n\t\t7. Multi Factor Authentication ";
                            std::cout<<"\n\n\tSelect Your Option (1-7): ";
                            std::cin>>choicm;

                            switch(choicm)
                            {
                            case '1':
                                typeOfAUTH = "No_AUTH";
                                break;
                            case '2':
                               typeOfAUTH = "usernam_passw";
                                break;
                            case '3':
                               typeOfAUTH = "SociNet_Email";
                                break;
                            case '4':
                               typeOfAUTH = "SmartCard";
                                break;
                            case '5':
                               typeOfAUTH = "Biometrics";
                                break;
                            case '6':
                               typeOfAUTH = "2Factor_AUTH";
                                break;
                            case '7':
                               typeOfAUTH = "MultFact_AUTH";
                                break;
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level7;
                            }

              char chou;
                level8:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state == "1")
                {
                    std::cout << "\n\tDoes it store data in a database? \n";
                }
                else
                {
                    std::cout << "\n\tWill it store data in a database? \n";
                }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>chou;

						switch(chou)
						{
						case '1':
                            useDb = "Yes";
                            break;
                        case '2':
                            useDb = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level8;
						}

            char choa;
            level9:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            if(useDb == "Yes")
            {
                 if(state == "1")
                    {
                        std::cout << "\n\tWhat is the type of data storage? \n";
                    }
                    else
                    {
                        std::cout << "\n\tWhat will be the type of data storage? \n";
                    }
                                std::cout<<"\n\t\t1. SQL ";
                                std::cout<<"\n\t\t2. NoSQL ";
                                std::cout<<"\n\t\t3. Local Storage";
                                std::cout<<"\n\t\t4. Distributed Storage";
                                std::cout<<"\n\n\tSelect Your Option (1-4): ";
                                std::cin>>choa;

                                switch(choa)
                                {
                                case '1':
                                    typeOfDataStorg = "SQL";
                                    break;
                                case '2':
                                    typeOfDataStorg = "NoSQL";
                                    break;
                                case '3':
                                    typeOfDataStorg = "Local_Storage";
                                    break;
                                case '4':
                                    typeOfDataStorg = "Distr_Storage";
                                    break;
                                default:
                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                goto level9;
                                }
            }

            char choae;
            level10:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            if(useDb == "Yes")
            {
                 if(state == "1")
                    {
                        std::cout << "\n\tWhat type of database is used? \n";
                    }
                    else
                    {
                        std::cout << "\n\tWhat type of database will be used? \n";
                    }
                                std::cout<<"\n\t\t1. SQL Server ";
                                std::cout<<"\n\t\t2. MySQL ";
                                std::cout<<"\n\t\t3. PostgreSQL";
                                std::cout<<"\n\t\t4. SQLite";
                                std::cout<<"\n\t\t5. OracleDB";
                                std::cout<<"\n\t\t6. MariaDB";
                                std::cout<<"\n\t\t7. MongoDB";
                                std::cout<<"\n\t\t8. CosmosDB";
                                std::cout<<"\n\t\t9. DynamoDB";
                                std::cout<<"\n\t\t10. Cassandra";
                                std::cout<<"\n\t\t11. Other";
                                std::cout<<"\n\n\tSelect Your Option (1-11): ";
                                std::cin>>choae;

                                switch(choae)
                                {
                                case '1':
                                    typeOfDb = "SQL_Server";
                                    break;
                                case '2':
                                    typeOfDb = "MySQL";
                                    break;
                                case '3':
                                    typeOfDb = "PostgreSQL";
                                    break;
                                case '4':
                                    typeOfDb = "SQLite";
                                    break;
                                case '5':
                                    typeOfDb = "OracleDB";
                                    break;
                                case '6':
                                    typeOfDb = "MariaDB";
                                    break;
                                case '7':
                                    typeOfDb = "MongoDB";
                                    break;
                                case '8':
                                    typeOfDb = "CosmosDB";
                                    break;
                                case '9':
                                    typeOfDb = "DynamoDB";
                                    break;
                                case '10':
                                    typeOfDb = "Cassandra";
                                    break;
                                case '11':
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    std::cout << "\n\tEnter one word that best describes the database: ";
                                    cin >> typeOfDb;
                                    break;
                                default:
                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                goto level10;
                                }
            }

            if(state == "1")
            {
                int chuse;
                    level_11:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "  Select the programming language(s) used in the implementation (you can choose multiple options) \n";

                    do{
                            std::cout << "\n\t1) C#";
                            std::cout << "\n\t2) C/C++";
                            std::cout << "\n\t3) Java";
                            std::cout << "\n\t4) Javascript";
                            std::cout << "\n\t5) PHP";
                            std::cout << "\n\t6) Python ";
                            std::cout << "\n\t7) Ruby ";
                            std::cout << "\n\t8) Other";
                            std::cout << "\n\t9) Done! \n";

                        cout << endl << "  Enter the S/N of your option (1-8) and press enter each time, and 9 when you are done: ";
                        cin >> chuse;

                        switch(chuse)
                        {
                            case 1:
                                progrm1 = "C#";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected C#! Select other programing language or Done." <<endl;
                                 break;
                            case 2:
                            progrm2 = "C/C++";
                             system("cls");
                             std::cout<<"\n" "***********************************************************************************************************\n";
                              cout << "\n\tYou have selected C/C++! Select other programing language or Done." <<endl;
                                break;
                              case 3:
                               progrm3 = "Java";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Java! Select other programing language or Done." <<endl;
                                break;
                              case 4:
                               progrm4 = "JavaSc";
                               system("cls");
                               std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Javascript! Select other programing language or Done." <<endl;
                                break;
                              case 5:
                               progrm5 = "PHP";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected PHP! Select other programing language or Done." <<endl;
                                break;
                            case 6:
                               progrm6 = "Python";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Python! Select other programing language or Done." <<endl;
                                break;
                            case 7:
                                progrm7 = "Ruby";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Ruby! Select other programing language or Done." <<endl;
                                 break;
                            case 8:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                std::cout << "\n\tEnter one word that best describes the programming language: ";
                                cin >> progrm8;
                                 break;
                            case 9:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                              cout << "\n\tDone!" <<endl;
                                break;

                            default: cout << "Please choose between 1-8 (Press Enter to continue ...)";
                            goto level_11;
                            break;
                        }

                    }while(chuse != 9);
            }
            else
            {
                int chuse;
                    level_11b:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "  Select the programming language(s) to be used in the implementation (you can choose multiple options) \n";

                    do{
                            std::cout << "\n\t1) C#";
                            std::cout << "\n\t2) C/C++";
                            std::cout << "\n\t3) Java";
                            std::cout << "\n\t4) Javascript";
                            std::cout << "\n\t5) PHP";
                            std::cout << "\n\t6) Python ";
                            std::cout << "\n\t7) Ruby ";
                            std::cout << "\n\t8) Other";
                            std::cout << "\n\t9) Done! \n";

                        cout << endl << "  Enter the S/N of your option (1-8) and press enter each time, and 9 when you are done: ";
                        cin >> chuse;

                        switch(chuse)
                        {
                            case 1:
                                progrm1 = "C#";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected C#! Select other programing language or Done." <<endl;
                                 break;
                            case 2:
                            progrm2 = "C/C++";
                             system("cls");
                             std::cout<<"\n" "***********************************************************************************************************\n";
                              cout << "\n\tYou have selected C/C++! Select other programing language or Done." <<endl;
                                break;
                              case 3:
                               progrm3 = "Java";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Java! Select other programing language or Done." <<endl;
                                break;
                              case 4:
                               progrm4 = "JavaSc";
                               system("cls");
                               std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Javascript! Select other programing language or Done." <<endl;
                                break;
                              case 5:
                               progrm5 = "PHP";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected PHP! Select other programing language or Done." <<endl;
                                break;
                            case 6:
                               progrm6 = "Python";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Python! Select other programing language or Done." <<endl;
                                break;
                            case 7:
                                progrm7 = "Ruby";
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                cout << "\n\tYou have selected Ruby! Select other programing language or Done." <<endl;
                                 break;
                            case 8:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                std::cout << "\n\tEnter one word that best describes the programming language: ";
                                cin >> progrm8;
                                 break;
                            case 9:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                              cout << "\n\tDone!" <<endl;
                                break;

                            default: cout << "Please choose between 1-8 (Press Enter to continue ...)";
                            goto level_11b;
                            break;
                        }

                    }while(chuse != 9);
            }

                char choe;
         level11:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            if(state == "1")
            {
                std::cout << "\n\tDoes it allow file uploads? \n";
            }
            else
            {
                std::cout << "\n\tWill it allow file uploads? \n";
            }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choe;

						switch(choe)
						{
						case '1':
                            	fileUpload = "Yes";
                            break;
                        case '2':
                            	fileUpload= "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level11;
						}

				char choke;
                level12:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                if(state == "1")
                {
                    std::cout << "\n\tDoes the system generate a log file?  \n";
                }
                else
                {
                    std::cout << "\n\tWill the system generate a log file?  \n";
                }
                        std::cout<<"\n\t\t1. Yes ";
                        std::cout<<"\n\t\t2. No";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choke;

						switch(choke)
						{
						case '1':
                            sysLog = "Yes";
                            break;
                        case '2':
                            sysLog = "No";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level12;
						}

            string request_query = "insert into users_requests_bp (Request_ID, Status, Struct1, Struct2, Struct3, Struct4, Struct5, Struct6, Struct7, Struct8, Struct9, Struct10, Struct11, anyUsr, usrRegist, typeOfRegist,  anyUsrLogin, usrInput, holdUsrInfo, storeAnyInfo, sensitivOfInfo, typeOfAUTH, useDb, typeOfDataStorg, typeOfDb, progrm1, progrm2, progrm3, progrm4, progrm5, progrm6, progrm7, progrm8, fileUpload, sysLog) values('"+Request_ID+"', '"+Status+"', '"+Struct1+"', '"+Struct2+"', '"+Struct3+"', '"+Struct4+"', '"+Struct5+"', '"+Struct6+"', '"+Struct7+"', '"+Struct8+"', '"+Struct9+"', '"+Struct10+"', '"+Struct11+"', '"+anyUsr+"', '"+usrRegist+"', '"+typeOfRegist+"', '"+anyUsrLogin+"', '"+usrInput+"', '"+holdUsrInfo+"', '"+storeAnyInfo+"', '"+sensitivOfInfo+"', '"+typeOfAUTH+"', '"+useDb+"', '"+typeOfDataStorg+"', '"+typeOfDb+"', '"+progrm1+"', '"+progrm2+"', '"+progrm3+"', '"+progrm4+"', '"+progrm5+"', '"+progrm6+"', '"+progrm7+"', '"+progrm8+"', '"+fileUpload+"', '"+sysLog+"')";

              const char* qr = request_query.c_str();
              qstate = mysql_query(conn, qr);

                if(!qstate)
                {
                     system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "\n\n\t\tData being saved .....\n";
                     sensitivOfInfo.erase();

                    cout << endl << "\n\n\t\tRequest Successfully added in the database!" << endl;

                    cout << endl << "\n\n\t\tPress Enter to go back to the Main Menu." << endl;
                }
                else
                {
                    cout << "\n\n\tQuery Execution Problem! Error Number: " << mysql_errno(conn) << endl;
                    cout << "\n\n\tError Number 1062 implies that the entered Request ID already exist in database.\n" << endl;
                    cout << endl << "\n\n\tPlease press Enter to go back to the Main Menu and repeat the process with a unique ID." << endl;
                }

	}

	void UserInput::modifyUserRequirements_Elicitation_requests()
	{
        Processing_and_Output po;
        UserInput usrIp;

        system("cls");
        std::cout << "\n" "***********************************************************************************************************\n";
        std::cout<<"\t\tMODIFY REQUEST\n\n";
        std::cout << "\n\t Enter your Request ID: "; std::cin >> Reqst_ID;

        Preliminary pre;

            pre.convert_lowerC_to_upperC(Reqst_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'R')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Reqst_ID;

                pre.convert_lowerC_to_upperC(Reqst_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

        string findbyRequestID_query = "select * from users_requests_re where Reqst_ID like '%"+Reqst_ID+"%'";
		const char* qr = findbyRequestID_query.c_str();
		qstate = mysql_query(conn, qr);

		string additionalInfo = "";
        string userInfo = "";
        string state2 = "";

         system("cls");
         std::cout<<"\n" "***********************************************************************************************************\n";
		cout << endl << "\tShowing your requests ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{

				cout << "\t\tRequest ID: " << row[0] << endl;
				state2 = row[1];
                additionalInfo = row[6];
               userInfo = row[5];
				cout << "\t\tApplication Domain: " << row[2] << endl;
				if(state2 == "On")
                {
                    cout << "\t\tDoes the system have a user? " << row[3] << endl;
                }
                else
                {
                    cout << "\t\tWill the system have a user? " << row[3] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes the system have user LogIn? " << row[4] << endl;
                }
                else
                {
                    cout << "\t\tWill the system have user LogIn? " << row[4] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes the system store any user information? " << row[5] << endl;
                }
                else
                {
                    cout << "\t\tWill the system hold any user information? " << row[5] << endl;
                }
                if(userInfo == "Yes")
                {
                    if(state2 == "On")
                    {
                        cout << "\t\tDoes the system store other information aside from the user information? " << row[6] << endl;
                    }
                    else
                    {
                        cout << "\t\tWill the system store other information aside from the user information? " << row[6] << endl;
                    }
                }
                else
                {
                    if(state2 == "On")
                    {
                        cout << "\t\tDoes the system store any kind of information? " << row[6] << endl;
                    }
                    else
                    {
                        cout << "\t\tWill the system store any kind of information? " << row[6] << endl;
                    }
                }


				if(state2 == "On")
                {
                    cout << "\t\tWhat type of information does the system store? " << row[7] << endl;
                }
                else
                {
                    cout << "\t\tWhat type of information will the system store? " << row[7] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes the system send information to an entity: " << row[8] << endl;
                }
                else
                {
                    cout << "\t\tWill this information be sent to an entity: " << row[8] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tIs the system connected to the Internet? " << row[9] << endl;
                }
                else
                {
                    cout << "\t\tWill the system be connected to the Internet? " << row[9] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes it send any data to a cloud? " << row[10] << endl;
                }
                else
                {
                    cout << "\t\tWill it send any data to a cloud? " << row[10] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes it store data in a db? " << row[11] << endl;
                }
                else
                {
                    cout << "\t\tWill it store data in a db? " << row[11] << endl;
                }
				if(state2 == "On")
                {
                    cout << "\t\tDoes it receive regular updates? " << row[12] << endl;
                }
                else
                {
                    cout << "\t\tWill the system receive regular updates? " << row[12] << endl;
                }
				if(state2 == "On")
                {
                   cout << "\t\tDoes the system use third-party software? " << row[13] << endl;
                }
                else
                {
                    cout << "\t\tWill the system use third-party software? " << row[13] << endl;
                }
                    cout << "\t\tIs there a possibility of the communications being eavesdropped?: " << row[14] << endl;
                    cout << "\t\tCould the messages sent between the system components be captured and resend?: " << row[15] << endl;
                    cout << "\t\tCan someone try to impersonate a user to gain access to private information?: " << row[16] << endl;
                    cout << "\t\tCan someone with bad intentions gain physical access to the system?: " << row[17] << endl;
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}

		string ID; char ch;
		cout << endl;
		cout << "\tDo you wish to modify your answers? (y/n): "; cin >> ch;

		if(ch == 'y' || ch == 'Y')
		{
            string update_query, state1;

            int choice;

            do{
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                std::cout << "\n\tYou can change your Domain or the answer to one or more questions by entering the S/No. below: \n" << endl;

                    cout << "\t\t1. Application Domain " << endl;

                    if(state2 == "On")
                    {
                        cout << "\t\t2. Does the system have a user? " << endl;
                    }
                    else
                    {
                        cout << "\t\t2. Will the system have a user? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t3. Does the system have user LogIn? " << endl;
                    }
                    else
                    {
                        cout << "\t\t3. Will the system have user LogIn? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t4. Does the system store any user information? " << endl;
                    }

                    {
                        cout << "\t\t4. Will the system hold any user information? " << endl;
                    }
                     if(userInfo == "Yes")
                    {
                        if(state2 == "On")
                        {
                            cout << "\t\t5. Does the system store other information aside from the user information? " << endl;
                        }
                        else
                        {
                            cout << "\t\t5. Will the system store other information aside from the user information? " << endl;
                        }
                    }
                    else
                    {
                        if(state2 == "On")
                        {
                            cout << "\t\t5. Does the system store any kind of information? " << endl;
                        }
                        else
                        {
                            cout << "\t\t5. Will the system store any kind of information? " << endl;
                        }
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t6. What type of information does the system store? " << endl;
                    }
                    else
                    {
                        cout << "\t\t6. What type of information will the system store? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t7. Does the system send information to an entity? " << endl;
                    }
                    else
                    {
                        cout << "\t\t7. Will this information be sent to an entity? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t8. Is the system connected to the Internet? " << endl;
                    }
                    else
                    {
                        cout << "\t\t8. Will the system be connected to the Internet? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t9. Does it send any data to a cloud? " << endl;
                    }
                    else
                    {
                        cout << "\t\t9. Will it send any data to a cloud? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t10. Does it store data in a database? " << endl;
                    }
                    else
                    {
                        cout << "\t\t10. Will it store data in a database? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t11. Does it receive regular updates? " << endl;
                    }
                    else
                    {
                        cout << "\t\t11. Will the system receive regular updates? " << endl;
                    }
                    if(state2 == "On")
                    {
                        cout << "\t\t12. Does the system use third-party software? " << endl;
                    }
                    else
                    {
                        cout << "\t\t12. Will the system use third-party software? " << endl;
                    }
                    cout << "\t\t13. Is there a possibility of the communications being eavesdropped? " << endl;
                    cout << "\t\t14. Could the messages sent between the system components be captured and resend? " << endl;
                    cout << "\t\t15. Can someone try to impersonate a user to gain access to private information? " << endl;
                    cout << "\t\t16. Can someone with bad intentions gain physical access to the system? " << endl;
                    cout << "\t\t17. Done!" << endl << endl;

                    cout << "\tEnter a S/No. one at a time and press Enter, and enter 14 when you are done:  "; cin >> choice;

                    switch(choice)
                    {
                        case 1:
                                int choice;
                                level:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                std::cout << "\n\tSelect your application domain: \n";

                                std::cout << "\n\t1) Smart Home";
                                std::cout << "\n\t2) Smart City";
                                std::cout << "\n\t3) Smart Agriculture";
                                std::cout << "\n\t4) Smart Grid";
                                std::cout << "\n\t5) Smart Healthcare";
                                std::cout << "\n\t6) Smart Elderly Monitoring";
                                std::cout << "\n\t7) Smart Kid Monitoring";
                                std::cout << "\n\t8) Smart pet Monitoring";
                                std::cout << "\n\t9) Smart Banking/Financial applications";
                                std::cout << "\n\t10) Industrial Automation";
                                std::cout << "\n\t11) Smart Supply Chain";
                                std::cout << "\n\t12) Smart Retail";
                                std::cout << "\n\t13) Smart Environmental Monitoring";
                                std::cout << "\n\t14) Smart Automotive/Transportation";
                                std::cout << "\n\t15) Smart Toy";
                                std::cout << "\n\t16) Wearable";
                                std::cout << "\n\t17) Connected Car";
                                std::cout << "\n\t18) Other Domain";

                                cout << endl << "\n\tEnter the S/N of your option (1-18) and Press enter: ";
                                cin >> choice;

                                switch(choice)
                                {
                                    case 1:
                                        Domain = "Home";
                                         break;
                                    case 2:
                                        Domain = "City";
                                        break;
                                    case 3:
                                        Domain = "Agriculture";
                                        break;
                                    case 4:
                                        Domain = "Grid";
                                        break;
                                    case 5:
                                        Domain = "Healthcare";
                                        break;
                                    case 6:
                                        Domain = "Elderly";
                                        break;
                                    case 7:
                                        Domain = "Kid";
                                        break;
                                    case 8:
                                        Domain = "Pet";
                                        break;
                                    case 9:
                                        Domain = "Financial";
                                        break;
                                    case 10:
                                        Domain = "Industrial";
                                        break;
                                    case 11:
                                        Domain = "Supply_Chain";
                                        break;
                                    case 12:
                                        Domain = "Retail";
                                        break;
                                    case 13:
                                        Domain = "Environmental";
                                        break;
                                    case 14:
                                        Domain = "Transportation";
                                        break;
                                     case 15:
                                        Domain = "Toy";
                                        break;
                                     case 16:
                                        Domain = "Wearable";
                                        break;
                                    case 17:
                                        Domain = "Connected_Car";
                                        break;
                                     case 18:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        std::cout << "\n\tEnter one word that best describes your domain: ";
                                        cin >> Domain;
                                        break;
                                    default: cout << "Please choose between 1-18 (Press Enter to continue ...)";
                                        goto level;
                                        break;
                                }
                                        update_query = "UPDATE `users_requests_re` SET `Domain` = '"+Domain+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                        case 2:
                                char cho;
                                 level2:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                     if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes the system have a user? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system have a user? \n";
                                    }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>cho;

                                        switch(cho)
                                        {
                                            case '1':
                                                anyUsr = "Yes";
                                                break;
                                            case '2':
                                                anyUsr = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level2;
                                        }
                                        update_query = "UPDATE `users_requests_re` SET `anyUsr` = '"+anyUsr+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 3:
                                    char choi;
                                    level3:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes the system have a user LogIn? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system have a user LogIn? \n";
                                    }


                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choi;

                                        switch(choi)
                                        {
                                            case '1':
                                                anyUsrLogin= "Yes";
                                                break;
                                            case '2':
                                                anyUsrLogin = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level3;
                                        }
                                        update_query = "UPDATE `users_requests_re` SET `anyUsrLogin` = '"+anyUsrLogin+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                        case 4:
                                    char choic;
                                    level4:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes the system store user information? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system hold any user information? \n";
                                    }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>choic;

                                    switch(choic)
                                    {
                                        case '1':
                                            holdUsrInfo = "Yes";
                                            break;
                                        case '2':
                                            holdUsrInfo = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level4;
                                    }
                                    update_query = "UPDATE `users_requests` SET `Ram_size` = '"+Ram_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 5:
                                        std::cin.ignore();
                                          char choict;
                                        level5:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";

                                        if(userInfo == "Yes")
                                        {
                                            if(state2 == "On")
                                            {
                                                cout << "\t\tDoes the system store other information aside from the user information? " << endl;
                                            }
                                            else
                                            {
                                                cout << "\t\tWill the system store other information aside from the user information? " << endl;
                                            }
                                        }
                                        else
                                        {
                                            if(state2 == "On")
                                            {
                                                cout << "\t\tDoes the system store any kind of information? " << endl;
                                            }
                                            else
                                            {
                                                cout << "\t\tWill the system store any kind of information? " << endl;
                                            }
                                        }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choict;

                                        switch(choict)
                                        {
                                            case '1':
                                                storeAnyInfo = "Yes";
                                                break;
                                            case '2':
                                                storeAnyInfo = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level5;
                                        }
                                    update_query = "UPDATE `users_requests_re` SET `storeAnyInfo` = '"+storeAnyInfo+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 6:
                                         char choicn;
                                        level6:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        if(state2 == "On")
                                        {
                                             std::cout << "\n\tWhat type of information does the system store? \n";
                                        }
                                        else
                                        {
                                             std::cout << "\n\tWhat type of information will the system store? \n";
                                        }

                                        std::cout<<"\n\t\t1. Normal Information ";
                                        std::cout<<"\n\t\t2. Sensitive Information";
                                        std::cout<<"\n\t\t3. Critical Information";

                                        std::cout<<"\n\n\tSelect Your Option (1-3): ";
                                        std::cin>>choicn;

                                        switch(choicn)
                                        {
                                            case '1':
                                                sensitivOfInfo = "Normal";
                                                break;
                                            case '2':
                                                sensitivOfInfo = "Sensitive";
                                                break;
                                            case '3':
                                                sensitivOfInfo = "Critical";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level6;
                                        }
                                    update_query = "UPDATE `users_requests_re` SET `sensitivOfInfo` = '"+sensitivOfInfo+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 7:
                                         char choicm;
                                        level7:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        if(state2 == "On")
                                        {
                                            std::cout << "\n\tDoes the system send information to an entity? \n";
                                        }
                                        else
                                        {
                                            std::cout << "\n\tWill the information be sent to an entity? \n";
                                        }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>choicm;

                                        switch(choicm)
                                        {
                                            case '1':
                                                infoSent2E = "Yes";
                                                break;
                                            case '2':
                                               infoSent2E = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level7;
                                        }
                                    update_query = "UPDATE `users_requests_re` SET `infoSent2E` = '"+infoSent2E+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 8:
                                    char choa;
                                    level8:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tIs the system connected to the Internet? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system be connected to the Internet? \n";
                                    }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>choa;

                                    switch(choa)
                                    {
                                        case '1':
                                            connected = "Yes";
                                            break;
                                        case '2':
                                            connected = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level8;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `connected` = '"+connected+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 9:
                                    char choe;
                                    level9:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes it send data to a cloud? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill it send its data to a cloud? \n";
                                    }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>choe;

                                    switch(choe)
                                    {
                                        case '1':
                                            dataSent2Cloud = "Yes";
                                            break;
                                        case '2':
                                            dataSent2Cloud= "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level9;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `dataSent2Cloud` = '"+dataSent2Cloud+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 10:
                                    char chou;
                                    level10:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes it store data in a database? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill it store data in a database? \n";
                                    }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>chou;

                                    switch(chou)
                                    {
                                        case '1':
                                            dataStoredInDb = "Yes";
                                            break;
                                        case '2':
                                            dataStoredInDb = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level10;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `dataStoredInDb` = '"+dataStoredInDb+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 11:
                                    char chok;
                                    level11:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes the system receive regular updates?  \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system receive regular updates?  \n";
                                    }

                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>chok;

                                    switch(chok)
                                    {
                                        case '1':
                                            regulaUpdate = "Yes";
                                            break;
                                        case '2':
                                            regulaUpdate = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level11;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `regulaUpdate` = '"+regulaUpdate+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 12:
                                    char choke;
                                    level12:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(state2 == "On")
                                    {
                                        std::cout << "\n\tDoes the system use third-party software?  \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system use third-party software?  \n";
                                    }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>choke;

                                    switch(choke)
                                    {
                                        case '1':
                                            use3rdPrtySfw = "Yes";
                                            break;
                                        case '2':
                                            use3rdPrtySfw = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level12;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `use3rdPrtySfw` = '"+use3rdPrtySfw+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                        case 13:
                                    char chokey;
                                    level13:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    std::cout << "\n\tIs there a possibility of the communications being eavesdropped? \n";
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>chokey;

                                    switch(chokey)
                                    {
                                        case '1':
                                            possibltOfEvesdrop = "Yes";
                                            break;
                                        case '2':
                                            possibltOfEvesdrop = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level13;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `possibltOfEvesdrop` = '"+possibltOfEvesdrop+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 14:
                                    char okey;
                                    level14:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    std::cout << "\n\tCould the messages sent between the system components be captured and resend? \n";

                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>okey;

                                    switch(okey)
                                    {
                                        case '1':
                                            possibltOfCapt_Resent = "Yes";
                                            break;
                                        case '2':
                                            possibltOfCapt_Resent = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level14;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `possibltOfCapt_Resent` = '"+possibltOfCapt_Resent+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 15:
                                    char key;
                                    level15:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    std::cout << "\n\tCan someone try to impersonate a user to gain access to private information? \n";
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>key;

                                    switch(key)
                                    {
                                        case '1':
                                            possibltOfImpersontUsr = "Yes";
                                            break;
                                        case '2':
                                            possibltOfImpersontUsr = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level15;
                                    }
                                    update_query = "UPDATE `users_requests_re` SET `possibltOfImpersontUsr` = '"+possibltOfImpersontUsr+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 16:
                                    char keya;
                                    level16:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    std::cout << "\n\tCan someone with bad intentions gain physical access to the system? \n";
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>keya;

                                    switch(keya)
                                    {
                                        case '1':
                                                possibltOfPhysiclAcces = "Yes";
                                            break;
                                        case '2':
                                                possibltOfPhysiclAcces = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level16;
                                    }
                                                update_query = "UPDATE `users_requests_re` SET `possibltOfPhysiclAcces` = '"+possibltOfPhysiclAcces+"' WHERE `Reqst_ID` = '"+Reqst_ID+"'";
                                break;
                         case 17:
                               system("cls");
                               std::cout<<"\n" "***********************************************************************************************************\n";
                               std::cout << endl << "\n\t\t\t Done!" << endl;
                                break;

                        default:
                                cout << "Please choose a correct number" << endl;
                    }
                    const char* qm = update_query.c_str();
                    qstate = mysql_query(conn, qm);

                    if(!qstate)
                    {
                        cout << endl << "\t\t\t Database successfully updated." << endl;
                        cout << "\n\n\t\t\t Press Enter to return to the Admin Menu. ";
                    }
                    else
                    {
                        cout << "\tQuery Execution Problem!" << mysql_errno(conn) << endl;
                    }

            }while(choice != 17);
            state2.erase();
		}
		else
		{
			system("cls");
			std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "\n\tPress Enter to return to the Main Menu. ";
			return;
		}

	}

	void UserInput::modifyBestPractGuide_requests()
	{
         Processing_and_Output po;
         UserInput usrIp;

        system("cls");
        std::cout << "\n" "***********************************************************************************************************\n";
        std::cout<<"\t\tMODIFY REQUEST\n\n";
        std::cout << "\n\t Enter your Request ID: "; std::cin >> Request_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Request_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'B')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

        string findbyRequestID_query = "select * from users_requests_bp where Request_ID like '%"+Request_ID+"%'";
		const char* qr = findbyRequestID_query.c_str();
		qstate = mysql_query(conn, qr);

		string Stat ="";
		string anyUsr = "";
        string usrRegist = "";
        string holdUsrInfo = "";
        string storeAnyInfo = "";
        string useDb = "";
        int flag_1 = 0;
        string state2;
        string userInfo;

         system("cls");
         std::cout<<"\n" "***********************************************************************************************************\n";
		cout << endl << "\tShowing your requests ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
				cout << "\t\tRequest ID: " << row[0] << endl;
				Stat = row[1];
				anyUsr= row[13];
				usrRegist = row[14];
				holdUsrInfo = row[18];
				storeAnyInfo = row[19];
				useDb = row[22];
                Struct1 = row[2]; Struct2 = row[3]; Struct3 = row[4]; Struct4 = row[5]; Struct5 = row[6]; Struct6 = row[7];
                Struct7 = row[8]; Struct8 = row[9]; Struct9 = row[10]; Struct10 = row[11]; Struct11 = row[12];
                progrm1 = row[25]; progrm2 = row[26]; progrm3 = row[27]; progrm4 = row[28]; progrm5 = row[29]; progrm6 = row[30]; progrm7 = row[31]; progrm8 = row[32];

				std::cout << "\t\tWhat's the category of your IoT System Structure? (you can choose multiple options) " << endl;
				if(!Struct1.empty())
                {
                    cout << "\t\t  - " << row[2] << endl;
                }
                if(!Struct2.empty())
                {
                    cout << "\t\t  - " << row[3] << endl;
                }
                if(!Struct3.empty())
                {
                    cout << "\t\t  - " << row[4] << endl;
                }
                if(!Struct4.empty())
                {
                    cout << "\t\t  - " << row[5] << endl;
                }
                if(!Struct5.empty())
                {
                    cout << "\t\t  - " << row[6] << endl;
                }
                if(!Struct6.empty())
                {
                    cout << "\t\t  - " << row[7] << endl;
                }
                if(!Struct7.empty())
                {
                    cout << "\t\t  - " << row[8] << endl;
                }
                if(!Struct8.empty())
                {
                    cout << "\t\t  - " << row[9] << endl;
                }
                if(!Struct9.empty())
                {
                    cout << "\t\t  - " << row[10] << endl;
                }
                if(!Struct10.empty())
                {
                    cout << "\t\t  - " << row[11] << endl;
                }
                if(!Struct11.empty())
                {
                    cout << "\t\t  - " << row[12] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes the system have a user? - " << row[13] << endl;
                }
                else
                {
                    std::cout << "\t\tWill the system have a user? - " << row[13] << endl;
                }
				if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tDoes the system have a provision for user registration? - " << row[14] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system have any provision for user registration? - " << row[14] << endl;
                    }
                }

                if(usrRegist == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tWho registers users? - " << row[15] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWho will register users? - " << row[15] << endl;
                    }
                }
                if(anyUsr == "Yes" && usrRegist == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tDoes the system have a user LogIn? - " << row[16] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system have a user LogIn? - " << row[16] << endl;
                    }
                }
                if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system allow users to enter any input? - " << row[17] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system allow users to enter any input? - " << row[17] << endl;
                    }
                }
                if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system store user information? - " << row[18] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system store any user information? - " << row[18] << endl;
                    }
                }
                if(holdUsrInfo == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         flag_1 = 1;
                         std::cout << "\t\tDoes the system store any other information? - " << row[19] << endl;
                    }
                    else
                    {
                        flag_1 = 1;
                        std::cout << "\t\tWill the system store any other information? - " << row[19] << endl;
                    }
                }
                if(holdUsrInfo != "Yes" && flag_1 != 1)
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system store any kind of information? - " << row[19] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system store any kind of information? - " << row[19] << endl;
                    }
                }
                if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat type of information does the system store? - " << row[20] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat type of information will the system store? - " << row[20] << endl;
                    }
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tWhat type of authentication is implemented in the system? - " << row[21] << endl;
                }
                else
                {
                    std::cout << "\t\tWhat type of authentication will be implemented in the system? - " << row[21] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes it store data in a database? - " << row[22] << endl;
                }
                else
                {
                    std::cout << "\t\tWill it store data in a database? - " << row[22] << endl;
                }
                if(useDb == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat is the type of data storage? - " << row[23] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat will be the type of data storage? - " << row[23] << endl;
                    }
                }
                if(useDb == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat type of database is used? - " << row[24] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat type of database will be used? - " << row[24] << endl;
                    }
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tWhat's the programming language used? (you can choose multiple options) \n";
                }
                else
                {
                    std::cout << "\t\tWhat programming language will be used? (you can choose multiple options) \n";
                }
				if(!progrm1.empty())
                {
                    cout << "\t\t  - " << row[25] << endl;
                }
                if(!progrm2.empty())
                {
                    cout << "\t\t  - " << row[26] << endl;
                }
                if(!progrm3.empty())
                {
                    cout << "\t\t  - " << row[27] << endl;
                }
                if(!progrm4.empty())
                {
                    cout << "\t\t  - " << row[28] << endl;
                }
                if(!progrm5.empty())
                {
                    cout << "\t\t  - " << row[29] << endl;
                }
                if(!progrm6.empty())
                {
                    cout << "\t\t  - " << row[30] << endl;
                }
                if(!progrm7.empty())
                {
                    cout << "\t\t  - " << row[31] << endl;
                }
                if(!progrm8.empty())
                {
                    cout << "\t\t  - " << row[32] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes it allow file uploads? - " << row[33] << endl;
                }
                else
                {
                    std::cout << "\t\tWill it allow file uploads? - " << row[33] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes the system generate a log file? - " << row[34] << endl;
                }
                else
                {
                    std::cout << "\t\tWill the system generate a log file? - " << row[34] << endl;
                }
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}

		string ID; char ch;
		cout << endl;
		cout << "\tDo you wish to modify your answers? (y/n): "; cin >> ch;

		bool validWord = false;

		if(ch == 'y' || ch == 'Y')
		{
            string update_query, state1;

            int choice;

            do{
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                std::cout << "\n\tYou can change the answer to one or more questions by entering the S/No. below: \n" << endl;
                    cout << "\t    --------------------------------------------------------------------------------------- " << endl;
                    cout << "\t    Select the category of IoT System Structure to change (you can choose multiple options) " << endl;
                    std::cout << "\t\t1. Device Management (e.g., Sensors, Actuators, Gateways)";
                    std::cout << "\n\t\t2. Data Collection";
                    std::cout << "\n\t\t3. Connectivity Management";
                    std::cout << "\n\t\t4. API Services";
                    std::cout << "\n\t\t5. Data Management";
                    std::cout << "\n\t\t6. Data Processing";
                    std::cout << "\n\t\t7. Big Data Analytics/Advanced Analytics";
                    std::cout << "\n\t\t8. Data Center and Cloud Services";
                    std::cout << "\n\t\t9. Web Services/Web apps (e.g., Mobile apps, Desktop apps development, etc.)";
                    std::cout << "\n\t\t10. Embedded Systems";
                    std::cout << "\n\t\t11. Other" << endl;
                    cout << "\t        ----------------------------------------------------------------------------------- " << endl;

                    if(Stat == "Exist")
                    {
                        cout << "\t\t12. Does the system have a user? " << endl;
                    }
                    else
                    {
                        cout << "\t\t12. Will the system have a user? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t13. Does the system have a provision for user registration? " << endl;
                    }
                    else
                    {
                        cout << "\t\t13. Will the system have any provision for user registration? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t14. Who registers users? " << endl;
                    }
                    else
                    {
                        cout << "\t\t14. Who will register users? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t15. Does the system have a user LogIn? " << endl;
                    }
                    else
                    {
                        cout << "\t\t15. Will the system have a user LogIn? " << endl;
                    }

                    if(Stat == "Exist")
                    {
                        cout << "\t\t16. Does the system allow users to enter any input? " << endl;
                    }
                    else
                    {
                        cout << "\t\t16. Will the system allow users to enter any input? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t17. Does the system store user information? " << endl;
                    }
                    else
                    {
                        cout << "\t\t17. Will the system store any user information? " << endl;
                    }
                    if(holdUsrInfo == "Yes")
                    {
                        if(Stat == "Exist")
                        {
                            cout << "\t\t18. Does the system store any other information? " << endl;
                        }
                        else
                        {
                            cout << "\t\t18. Will the system store any other information? " << endl;
                        }
                    }
                    else if(holdUsrInfo != "Yes" && flag_1 != 1)
                    {
                        if(Stat == "Exist")
                        {
                            cout << "\t\t18. Does the system store any kind of information? " << endl;
                        }
                        else
                        {
                            cout << "\t\t18. Will the system store any kind of information? " << endl;
                        }
                    }
                    if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
                    {
                        if(Stat == "Exist")
                        {
                            cout << "\t\t19. What type of information does the system store? " << endl;
                        }
                        else
                        {
                            cout << "\t\t19. What type of information will the system store? " << endl;
                        }
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t20. What type of authentication is implemented in the system? " << endl;
                    }
                    else
                    {
                        cout << "\t\t20. What type of authentication will be implemented in the system? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t21. Does it store data in a database? " << endl;
                    }
                    else
                    {
                        cout << "\t\t21. Will it store data in a database? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t22. What is the type of data storage? " << endl;
                    }
                    else
                    {
                        cout << "\t\t22. What will be the type of data storage? " << endl;
                    }
                    if(useDb == "Yes")
                    {
                        if(Stat == "Exist")
                        {
                            cout << "\t\t23. What type of database is used? " << endl;
                        }
                        else
                        {
                            cout << "\t\t23. What type of database will be used? " << endl;
                        }
                    }
                    cout << "\t        ----------------------------------------------------------------------------------- " << endl;
                    if(Stat == "Exist")
                    {

                        cout << "\t\tWhat's the programming language used? (you can choose multiple options) " << endl;
                    }
                    else
                    {
                        cout << "\t\t What programming language will be used? (you can choose multiple options) " << endl;
                    }
                            std::cout << "\t\t24. C#";
                            std::cout << "\n\t\t25. C/C++";
                            std::cout << "\n\t\t26. Java";
                            std::cout << "\n\t\t27. Javascript";
                            std::cout << "\n\t\t28. PHP";
                            std::cout << "\n\t\t29. Python ";
                            std::cout << "\n\t\t30. Ruby ";
                            std::cout << "\n\t\t31. Other\n";
                     cout << "\t        ----------------------------------------------------------------------------------- " << endl;
                    if(Stat == "Exist")
                    {
                        cout << "\t\t32. Does it allow file uploads? " << endl;
                    }
                    else
                    {
                        cout << "\t\t32. Will it allow file uploads? " << endl;
                    }
                    if(Stat == "Exist")
                    {
                        cout << "\t\t33. Does the system generate any log file? " << endl;
                    }
                    else
                    {
                        cout << "\t\t33. Will the system generate any log file? " << endl;
                    }
                    cout << "\t\t34. Done!" << endl << endl;

                    cout << "\tEnter a S/No. one at a time and press Enter, and enter 35 when you are done:  "; cin >> choice;


                    switch(choice)
                    {
                        case 1:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Device_Mgmt or ' '> to Add or Delete Device Management: "; getline(cin, Struct1);
                                   }while(Struct1 != "Device_Mgmt" && Struct1 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `Struct1` = '"+Struct1+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                        case 2:
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <Data_Collect or ' '> to Add or Delete Data Collection: "; getline(cin, Struct2);
                                    }while(Struct2 != "Data_Collect" && Struct2 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct2` = '"+Struct2+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 3:
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <Connect_Mgmt or ' '> to Add or Delete Connectivity Management: "; getline(cin, Struct3);
                                    }while(Struct3 != "Connect_Mgmt" && Struct3 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct3` = '"+Struct3+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                        case 4:
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <API_Service or ' '> to Add or Delete selected API Services: "; getline(cin, Struct4);
                                    }while(Struct4 != "API_Service" && Struct4 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct4` = '"+Struct4+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 5:
                                  do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Data_Mgmt or ' '> to Add or Delete Data Management: "; getline(cin, Struct5);
                                    }while(Struct5 != "Data_Mgmt" && Struct5 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct5` = '"+Struct5+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 6:
                                    do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Data_Process or ' '> to Add or Delete Data Processing: "; getline(cin, Struct6);
                                    }while(Struct6 != "Data_Process" && Struct6 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct6` = '"+Struct6+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 7:
                                  do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Analytics or ' '> to Add or Delete Big Data Analytics/Advanced Analytics: "; getline(cin, Struct7);
                                    }while(Struct7 != "Analytics" && Struct7 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `Struct7` = '"+Struct7+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 8:
                                    do{
                                         system("cls");
                                         std::cout<<"\n" "***********************************************************************************************************\n";
                                         cout << endl << "\tType <Cloud_Service or ' '> to Add or Delete Data Center and Cloud Services: "; getline(cin, Struct8);
                                    }while(Struct8 != "Cloud_Service" && Struct8 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct8` = '"+Struct8+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 9:
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <Web or ' '> to Add or Delete Web Services/Web apps: "; getline(cin, Struct9);
                                     }while(Struct9 != "Web" && Struct9 != "' '");
                                     update_query = "UPDATE `users_requests_bp` SET `Struct9` = '"+Struct9+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 10:
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <Embedded_Sys or ' '> to Add or Delete Embedded Systems: "; getline(cin, Struct10);
                                     }while(Struct10 != "Embedded_Sys" && Struct10 != "' '");
                                     update_query = "UPDATE `users_requests_bp` SET `Struct10` = '"+Struct10+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 11:
                                  do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        std::cout << "\n\tEnter one word that best describes your IoT system structure or ' ' to delete IoT system structure: "; getline(cin, Struct11);
                                         validWord = pre.validString(Struct11);
                                     }while(validWord != true && Struct11 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `Struct11` = '"+Struct11+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 12:
                                char cho;
                                level2:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";

                                 if(Stat == "Exist")
                                {
                                    std::cout << "\n\tDoes the system have a user? \n";
                                }
                                else
                                {
                                    std::cout << "\n\tWill the system have a user? \n";
                                }
                                    std::cout<<"\n\t\t1. Yes ";
                                    std::cout<<"\n\t\t2. No";
                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                    std::cin>>cho;

                                    switch(cho)
                                    {
                                    case '1':
                                        anyUsr= "Yes";
                                        break;
                                    case '2':
                                        anyUsr = "No";
                                        break;
                                    default:
                                        std::cout << "\tSorry! Wrong option selected." << std:: endl;//
                                    goto level2;
                                    }
                                    update_query = "UPDATE `users_requests_bp` SET `anyUsr` = '"+anyUsr+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                        case 13:
                                   char chic;
                                    level2a:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(anyUsr == "Yes")
                                    {
                                         if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tDoes the system have a provision for user registration? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWill the system have any provision for user registration? \n";
                                            }
                                                std::cout<<"\n\t\t1. Yes ";
                                                std::cout<<"\n\t\t2. No";
                                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                std::cin>>chic;

                                                switch(chic)
                                                {
                                                case '1':
                                                    usrRegist= "Yes";
                                                    break;
                                                case '2':
                                                    usrRegist = "No";
                                                    break;
                                                default:
                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto level2a;
                                                }
                                    }
                                    update_query = "UPDATE `users_requests_bp` SET `usrRegist` = '"+usrRegist+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 14:
                                    char chac;
                                    level2b:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(usrRegist == "Yes")
                                    {
                                         if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tWho registers users? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWho will register users? \n";
                                            }
                                                std::cout<<"\n\t\t1. Users themselves ";
                                                std::cout<<"\n\t\t2. An administrator";
                                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                std::cin>>chac;

                                                switch(chac)
                                                {
                                                case '1':
                                                    typeOfRegist= "Users";
                                                    break;
                                                case '2':
                                                    typeOfRegist = "Admin";
                                                    break;
                                                default:
                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto level2b;
                                                }
                                    }
                                    update_query = "UPDATE `users_requests_bp` SET `typeOfRegist` = '"+typeOfRegist+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 15:
                                   char choi;
                                    level3:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                   // int flag_1 = 0;
                                    if(anyUsr == "Yes" && usrRegist == "Yes")
                                    {
                                        if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tDoes the system have a user LogIn? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWill the system have a user LogIn? \n";
                                            }
                                                        std::cout<<"\n\t\t1. Yes ";
                                                        std::cout<<"\n\t\t2. No";
                                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                        std::cin>>choi;

                                                        switch(choi)
                                                        {
                                                        case '1':
                                                            anyUsrLogin= "Yes";
                                                            break;
                                                        case '2':
                                                            anyUsrLogin = "No";
                                                            break;
                                                        default:
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;//
                                                        goto level3;
                                                        }
                                    }
                                    update_query = "UPDATE `users_requests_bp` SET `anyUsrLogin` = '"+anyUsrLogin+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 16:
                                    {
                                    char choia;
                                    level3a:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    int flag_1 = 0;
                                    if(anyUsr == "Yes")
                                    {
                                        if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tDoes the system allow users to enter any input? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWill the system allow users to enter any input? \n";
                                            }
                                                        std::cout<<"\n\t\t1. Yes ";
                                                        std::cout<<"\n\t\t2. No";
                                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                        std::cin>>choia;

                                                        switch(choia)
                                                        {
                                                        case '1':
                                                            usrInput= "Yes";
                                                            break;
                                                        case '2':
                                                            usrInput = "No";
                                                            break;
                                                        default:
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                        goto level3a;
                                                        }
                                        }
                                    update_query = "UPDATE `users_requests_bp` SET `usrInput` = '"+usrInput+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                                }
                         case 17:
                                 {
                                     char choic;
                                    level4:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                     if(anyUsr == "Yes")
                                     {
                                         if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tDoes the system store user information? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWill the system store any user information? \n";
                                            }
                                                        std::cout<<"\n\t\t1. Yes ";
                                                        std::cout<<"\n\t\t2. No";
                                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                        std::cin>>choic;

                                                        switch(choic)
                                                        {
                                                        case '1':
                                                            holdUsrInfo = "Yes";
                                                            break;
                                                        case '2':
                                                            holdUsrInfo = "No";
                                                            break;
                                                        default:
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                        goto level4;
                                                        }
                                     }
                                     update_query = "UPDATE `users_requests_bp` SET `holdUsrInfo` = '"+holdUsrInfo+"' WHERE `Request_ID` = '"+Request_ID+"'";

                                break;
                                }
                        case 18:
                                if(holdUsrInfo == "Yes")
                                {
                                    char choic_;
                                     level4_:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        if(holdUsrInfo == "Yes")
                                        {
                                            if(Stat == "Exist")
                                                {
                                                    flag_1 = 1;
                                                    std::cout << "\n\tDoes the system store any other information? \n";
                                                }
                                                else
                                                {
                                                    flag_1 = 1;
                                                    std::cout << "\n\tWill the system store any other information? \n";
                                                }
                                                            std::cout<<"\n\t\t1. Yes ";
                                                            std::cout<<"\n\t\t2. No";
                                                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                            std::cin>>choic_;

                                                            switch(choic_)
                                                            {
                                                            case '1':
                                                                storeAnyInfo = "Yes";//This variable also serves as other info aside from usr info
                                                                break;
                                                            case '2':
                                                                storeAnyInfo = "No";
                                                                break;
                                                            default:
                                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                            goto level4_;
                                                            }
                                        }
                                        update_query = "UPDATE `users_requests_bp` SET `storeAnyInfo` = '"+storeAnyInfo+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                }
                                else if(holdUsrInfo != "Yes" && flag_1 != 1)
                                {
                                        char choict;
                                        level5:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        if(Stat == "Exist")
                                        {
                                            std::cout << "\n\tDoes the system store any kind of information? \n";
                                        }
                                        else
                                        {
                                            std::cout << "\n\tWill the system store any kind of information? \n";
                                        }
                                                    std::cout<<"\n\t\t1. Yes ";
                                                    std::cout<<"\n\t\t2. No";
                                                    std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                    std::cin>>choict;

                                                    switch(choict)
                                                    {
                                                    case '1':
                                                        storeAnyInfo = "Yes";
                                                        break;
                                                    case '2':
                                                        storeAnyInfo = "No";
                                                        break;
                                                    default:
                                                        std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                    goto level5;
                                                    }
                                    }
                                        flag_1 = 0;
                                    update_query = "UPDATE `users_requests_bp` SET `storeAnyInfo` = '"+storeAnyInfo+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                        case 19:
                                 if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
                                 {
                                      char choicn;
                                        level6:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        if(Stat == "Exist")
                                        {
                                             std::cout << "\n\tWhat type of information does the system store? \n";
                                        }
                                        else
                                        {
                                             std::cout << "\n\tWhat type of information will the system store? \n";
                                        }

                                                    std::cout<<"\n\t\t1. Normal Information ";
                                                    std::cout<<"\n\t\t2. Sensitive Information";
                                                    std::cout<<"\n\t\t3. Critical Information";

                                                    std::cout<<"\n\n\tSelect Your Option (1-3): ";
                                                    std::cin>>choicn;

                                                    switch(choicn)
                                                    {
                                                    case '1':
                                                        sensitivOfInfo = "Normal";
                                                        break;
                                                    case '2':
                                                        sensitivOfInfo = "Sensitive";
                                                        break;
                                                    case '3':
                                                        sensitivOfInfo = "Critical";
                                                        break;
                                                    default:
                                                        std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                    goto level6;
                                                    }
                                 }
                                 update_query = "UPDATE `users_requests_bp` SET `sensitivOfInfo` = '"+sensitivOfInfo+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                 break;
                         case 20:
                                    char choicm;
                                    level7:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(Stat == "Exist")
                                    {
                                        std::cout << "\n\tWhat type of authentication is implemented in the system? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWhat type of authentication will be implemented in the system? \n";
                                    }
                                                std::cout<<"\n\t\t1. No Authentication ";
                                                std::cout<<"\n\t\t2. Username and Password";
                                                std::cout<<"\n\t\t3. Social Networks/Email Authentication";
                                                std::cout<<"\n\t\t4. SmartCard";
                                                std::cout<<"\n\t\t5. Biometrics";
                                                std::cout<<"\n\t\t6. Two Factor Authentication ";
                                                std::cout<<"\n\t\t7. Multi Factor Authentication ";
                                                std::cout<<"\n\n\tSelect Your Option (1-7): ";
                                                std::cin>>choicm;

                                                switch(choicm)
                                                {
                                                case '1':
                                                    typeOfAUTH = "No_AUTH";
                                                    break;
                                                case '2':
                                                   typeOfAUTH = "usernam_passw";
                                                    break;
                                                case '3':
                                                   typeOfAUTH = "SociNet_Email";
                                                    break;
                                                case '4':
                                                   typeOfAUTH = "SmartCard";
                                                    break;
                                                case '5':
                                                   typeOfAUTH = "Biometrics";
                                                    break;
                                                case '6':
                                                   typeOfAUTH = "2Factor_AUTH";
                                                    break;
                                                case '7':
                                                   typeOfAUTH = "MultFact_AUTH";
                                                    break;
                                                default:
                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto level7;
                                                }
                                    update_query = "UPDATE `users_requests_bp` SET `typeOfAUTH` = '"+typeOfAUTH+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 21:
                                 char chou;
                                level8:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                if(Stat == "Exist")
                                {
                                    std::cout << "\n\tDoes it store data in a database? \n";
                                }
                                else
                                {
                                    std::cout << "\n\tWill it store data in a database? \n";
                                }
                                        std::cout<<"\n\t\t1. Yes ";
                                        std::cout<<"\n\t\t2. No";
                                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                        std::cin>>chou;

                                        switch(chou)
                                        {
                                        case '1':
                                            useDb = "Yes";
                                            break;
                                        case '2':
                                            useDb = "No";
                                            break;
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level8;
                                        }
                                    update_query = "UPDATE `users_requests_bp` SET `useDb` = '"+useDb+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 22:
                                    char choa;
                                    level9:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(useDb == "Yes")
                                    {
                                         if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tWhat is the type of data storage? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWhat will be the type of data storage? \n";
                                            }
                                                        std::cout<<"\n\t\t1. SQL ";
                                                        std::cout<<"\n\t\t2. NoSQL ";
                                                        std::cout<<"\n\t\t3. Local Storage";
                                                        std::cout<<"\n\t\t4. Distributed Storage";
                                                        std::cout<<"\n\n\tSelect Your Option (1-4): ";
                                                        std::cin>>choa;

                                                        switch(choa)
                                                        {
                                                        case '1':
                                                            typeOfDataStorg = "SQL";
                                                            break;
                                                        case '2':
                                                            typeOfDataStorg = "NoSQL";
                                                            break;
                                                        case '3':
                                                            typeOfDataStorg = "Local_Storage";
                                                            break;
                                                        case '4':
                                                            typeOfDataStorg = "Distr_Storage";
                                                            break;
                                                        default:
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                        goto level9;
                                                        }
                                    }
                                  update_query = "UPDATE `users_requests_bp` SET `typeOfDataStorg` = '"+typeOfDataStorg+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 23:
                                    char choae;
                                    level10:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(useDb == "Yes")
                                    {
                                         if(Stat == "Exist")
                                            {
                                                std::cout << "\n\tWhat type of database is used? \n";
                                            }
                                            else
                                            {
                                                std::cout << "\n\tWhat type of database will be used? \n";
                                            }
                                                        std::cout<<"\n\t\t1. SQL Server ";
                                                        std::cout<<"\n\t\t2. MySQL ";
                                                        std::cout<<"\n\t\t3. PostgreSQL";
                                                        std::cout<<"\n\t\t4. SQLite";
                                                        std::cout<<"\n\t\t5. OracleDB";
                                                        std::cout<<"\n\t\t6. MariaDB";
                                                        std::cout<<"\n\t\t7. MongoDB";
                                                        std::cout<<"\n\t\t8. CosmosDB";
                                                        std::cout<<"\n\t\t9. DynamoDB";
                                                        std::cout<<"\n\t\t10. Cassandra";
                                                        std::cout<<"\n\t\t11. Other";
                                                        std::cout<<"\n\n\tSelect Your Option (1-11): ";
                                                        std::cin>>choae;

                                                        switch(choae)
                                                        {
                                                        case '1':
                                                            typeOfDb = "SQL_Server";
                                                            break;
                                                        case '2':
                                                            typeOfDb = "MySQL";
                                                            break;
                                                        case '3':
                                                            typeOfDb = "PostgreSQL";
                                                            break;
                                                        case '4':
                                                            typeOfDb = "SQLite";
                                                            break;
                                                        case '5':
                                                            typeOfDb = "OracleDB";
                                                            break;
                                                        case '6':
                                                            typeOfDb = "MariaDB";
                                                            break;
                                                        case '7':
                                                            typeOfDb = "MongoDB";
                                                            break;
                                                        case '8':
                                                            typeOfDb = "CosmosDB";
                                                            break;
                                                        case '9':
                                                            typeOfDb = "DynamoDB";
                                                            break;
                                                        case '10':
                                                            typeOfDb = "Cassandra";
                                                            break;
                                                        case '11':
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                            std::cout << "\n\tEnter one word that best describes the database: ";
                                                            cin >> typeOfDb;
                                                            break;
                                                        default:
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                        goto level10;
                                                        }
                                    }
                                   update_query = "UPDATE `users_requests_bp` SET `typeOfDb` = '"+typeOfDb+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 24:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <C# or ' '> to Add or Delete C#: "; getline(cin, progrm1);
                                        pre.convert_lowerC_to_upperC(progrm1);
                                   }while(progrm1 != "C#" && progrm1 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm1` = '"+progrm1+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 25:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <C/C++ or ' '> to Add or Delete C/C++: "; getline(cin, progrm2);
                                        pre.convert_lowerC_to_upperC(progrm2);
                                   }while(progrm2 != "C/C++" && progrm2 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm2` = '"+progrm2+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 26:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Java or ' '> to Add or Delete Java: "; getline(cin, progrm3);
                                   }while(progrm3 != "Java" && progrm3 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm3` = '"+progrm3+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 27:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <JavaSc or ' '> to Add or Delete Javascript: "; getline(cin, progrm4);
                                   }while(progrm4 != "JavaSc" && progrm4 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm4` = '"+progrm4+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 28:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <PHP or ' '> to Add or Delete PHP: "; getline(cin, progrm5);
                                       pre.convert_lowerC_to_upperC(progrm5);
                                   }while(progrm5 != "PHP" && progrm5 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm5` = '"+progrm5+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 29:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Python or ' '> to Add or Delete Python: "; getline(cin, progrm6);
                                   }while(progrm6 != "Python" && progrm6 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm6` = '"+progrm6+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 30:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tType <Ruby or ' '> to Add or Delete Ruby: "; getline(cin, progrm7);
                                   }while(progrm7 != "Ruby" && progrm7 != "' '");
                                   update_query = "UPDATE `users_requests_bp` SET `progrm7` = '"+progrm7+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 31:
                                 do{
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        std::cout << "\n\tEnter one word that best describes your progrm. language or ' ' to delete progrm. lang.: "; getline(cin, progrm8);
                                         validWord = pre.validString(progrm8);
                                     }while(validWord != true && progrm8 != "' '");
                                    update_query = "UPDATE `users_requests_bp` SET `progrm8` = '"+progrm8+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 32:
                                     char choe;
                                    level11:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(Stat == "Exist")
                                    {
                                        std::cout << "\n\tDoes it allow file uploads? \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill it allow file uploads? \n";
                                    }
                                                std::cout<<"\n\t\t1. Yes ";
                                                std::cout<<"\n\t\t2. No";
                                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                                std::cin>>choe;

                                                switch(choe)
                                                {
                                                case '1':
                                                        fileUpload = "Yes";
                                                    break;
                                                case '2':
                                                        fileUpload= "No";
                                                    break;
                                                default:
                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto level11;
                                                }
                                        update_query = "UPDATE `users_requests_bp` SET `fileUpload` = '"+fileUpload+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                   break;
                         case 33:
                                     char choke;
                                    level12:
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    if(Stat == "Exist")
                                    {
                                        std::cout << "\n\tDoes the system generate a log file?  \n";
                                    }
                                    else
                                    {
                                        std::cout << "\n\tWill the system generate a log file?  \n";
                                    }
                                            std::cout<<"\n\t\t1. Yes ";
                                            std::cout<<"\n\t\t2. No";
                                            std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                            std::cin>>choke;

                                            switch(choke)
                                            {
                                            case '1':
                                                sysLog = "Yes";
                                                break;
                                            case '2':
                                                sysLog = "No";
                                                break;
                                            default:
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                            goto level12;
                                            }
                                       update_query = "UPDATE `users_requests_bp` SET `sysLog` = '"+sysLog+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                break;
                         case 34:
                               system("cls");
                               std::cout<<"\n" "***********************************************************************************************************\n";
                               std::cout << endl << "\n\t\t\t Done!" << endl;
                                break;

                        default:
                                cout << "Please choose a correct number" << endl;
                    }
                    const char* qm = update_query.c_str();
                    qstate = mysql_query(conn, qm);

                    if(!qstate)
                    {
                        cout << endl << "\t\t\t Database successfully updated." << endl;
                        cout << "\n\n\t\t\t Press Enter to return to the Admin Menu. ";
                    }
                    else
                    {
                        cout << "\tQuery Execution Problem!" << mysql_errno(conn) << endl;
                    }

            }while(choice != 34);
		}
		else
		{
			system("cls");
			std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "\n\tPress Enter to return to the Main Menu. ";
			return;
		}
	}

	void UserInput::deleteRequest_RE()
	{
	    Processing_and_Output po;
        UserInput usrIp;

	    system("cls");
        std::cout << "\n***********************************************************************************************************\n";
        std::cout<<"\t\t\t\t   DELETE REQUIREMENTS ELICITATION REQUEST \n\n";
        cout << "\n\t\t   Enter your Request ID to delete your requirementS elicitation request: "; cin >> Reqst_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Reqst_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'R')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Reqst_ID;

                pre.convert_lowerC_to_upperC(Reqst_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

                        string delete_query = "delete from users_requests_re where Reqst_ID = '"+Reqst_ID+"'";
                        const char* qd = delete_query.c_str();
                        qstate = mysql_query(conn, qd);

                        if(!qstate)
                        {
                            system("cls");
                            cout << "\n\t\t\tSuccessfully Deleted from Database! \n\n\n";
                            std::cout << "\n\t\t\tPress Enter to return to the Main Menu. ";
                        }
                        else
                        {
                            system("cls");
                            cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                        }
	}

	void UserInput::deleteBestPractGuide()
	{
	    Processing_and_Output po;
        UserInput usrIp;

	    system("cls");
        std::cout << "\n***********************************************************************************************************\n";
        std::cout<<"\t\t\t\t   DELETE BEST PRACTICE GUIDE REQUEST \n\n";
        cout << "\n\t\t   Enter your Request ID to delete your requirementS elicitation request: "; cin >> Request_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Request_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'B')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }
                        string delete_query = "delete from users_requests_bp where Request_ID = '"+Request_ID+"'";
                        const char* qd = delete_query.c_str();
                        qstate = mysql_query(conn, qd);

                        if(!qstate)
                        {
                            system("cls");
                            cout << "\n\t\t\tSuccessfully Deleted from Database! \n\n\n";
                            std::cout << "\n\t\t\tPress Enter to return to the Main Menu. ";
                        }
                        else
                        {
                            system("cls");
                            cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                        }
	}

	void UserInput::showAndDeleteUser_Request_RE()
	{
                            level:
                            qstate = mysql_query(conn, "select * from users_requests_re");
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            cout << "         Showing Request IDs for all Requirements Elicitation users.... " << endl << endl;

                             res = mysql_use_result(conn);

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << "Request ID" << '|'<< endl;

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            if(!qstate)
                            {
                                 while((row = mysql_fetch_row(res)))
                                 {
                                        cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << row[0] << '|' << endl;
                                 }
                            }
                            else
                            {
                                cout << "Query error!" << mysql_errno(conn) << endl;
                            }
                            cout << "\t\t"<< left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            mysql_free_result(res);


                        string Request_ID; char ch;
                        cout << "\n\tDo you want to delete any user request? (y/n): "; cin >> ch;

                        if(ch == 'y' || ch == 'Y')
                        {

                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t\tDELETE  A REQUIREMENTS ELICITATION USER REQUEST\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    system("cls");
                                    std::cout<<"\n***********************************************************************************************************\n\n";
                                    cout << "\n\tEnter the request ID of the user request you want to delete: "; cin >> Reqst_ID;

                                     Preliminary pre;
                                     UserInput usrIp;

                                    pre.convert_lowerC_to_upperC(Reqst_ID);

                                    int num_digits;
                                    int string_length;
                                    char first_letter;

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;

                                    while(num_digits !=4 || string_length != 5 || first_letter != 'R')
                                    {
                                        system("cls");
                                        std::cout << "\n***********************************************************************************************************\n";
                                        std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                        std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                                        std::cin >> Reqst_ID;

                                        pre.convert_lowerC_to_upperC(Reqst_ID);

                                        auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                                        num_digits = collector.n1;
                                        string_length = collector.n2;
                                        first_letter = collector.c;
                                    }

                                    string delete_query = "delete from users_requests_re where Reqst_ID = '"+Reqst_ID+"'";
                                    const char* qd = delete_query.c_str();
                                    qstate = mysql_query(conn, qd);

                                    if(!qstate)
                                    {
                                        system("cls");
                                         std::cout<<"\n***********************************************************************************************************\n\n";
                                        cout << "\n\t\tSuccessfully Deleted from Database!\n" << endl;
                                        std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                                    }
                                    else
                                    {
                                        system("cls");
                                        cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                    }
                                }
                                else
                                {
                                    goto level;
                                }
                        }
                        else
                        {
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                            return;
                        }
	}

	void UserInput::showAndDeleteUser_BestPractGuide()
	{
                            level:
                            qstate = mysql_query(conn, "select * from users_requests_bp");
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            cout << "     Showing Request IDs for all Best Practice Guidelines for Secure Development users.... " << endl << endl;

                             res = mysql_use_result(conn);

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << "Request ID" << '|'<< endl;

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            if(!qstate)
                            {
                                 while((row = mysql_fetch_row(res)))
                                 {
                                        cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << row[0] << '|' << endl;
                                 }
                            }
                            else
                            {
                                cout << "Query error!" << mysql_errno(conn) << endl;
                            }
                            cout << "\t\t"<< left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            mysql_free_result(res);


                        string Request_ID; char ch;
                        cout << "\n\tDo you want to delete any user request? (y/n): "; cin >> ch;

                        if(ch == 'y' || ch == 'Y')
                        {

                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t\tDELETE  A BEST PRACTICE GUIDE FOR SECURE DEVELOPMENT USER REQUEST\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    system("cls");
                                    std::cout<<"\n***********************************************************************************************************\n\n";
                                    cout << "\n\tEnter the request ID of the user request you want to delete: "; cin >> Request_ID;

                                    Preliminary pre;
                                     UserInput usrIp;

                                    pre.convert_lowerC_to_upperC(Request_ID);

                                    int num_digits;
                                    int string_length;
                                    char first_letter;

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;

                                    while(num_digits !=4 || string_length != 5 || first_letter != 'B')
                                    {
                                        system("cls");
                                        std::cout << "\n***********************************************************************************************************\n";
                                        std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                        std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                                        std::cin >> Request_ID;

                                        pre.convert_lowerC_to_upperC(Request_ID);

                                        auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                        num_digits = collector.n1;
                                        string_length = collector.n2;
                                        first_letter = collector.c;
                                    }

                                    string delete_query = "delete from users_requests_bp where Request_ID = '"+Request_ID+"'";
                                    const char* qd = delete_query.c_str();
                                    qstate = mysql_query(conn, qd);

                                    if(!qstate)
                                    {
                                        system("cls");
                                         std::cout<<"\n***********************************************************************************************************\n\n";
                                        cout << "\n\t\tSuccessfully Deleted from Database!\n" << endl;
                                        std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                                    }
                                    else
                                    {
                                        system("cls");
                                        cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                    }
                                }
                                else
                                {
                                    goto level;
                                }
                        }
                        else
                        {
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                            return;
                        }
	}

    void UserInput::selectSecurityRequirements_Software()
    {
         int choose;
         level_tk:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "  Select your security requirements one at a time: \n";

        do{
                std::cout << "\n\t1) Confidentiality";
                std::cout << "\n\t2) Integrity";
                std::cout << "\n\t3) Authentication";
                std::cout << "\n\t4) Privacy";
                std::cout << "\n\t5) Non-Repudiation";
                std::cout << "\n\t6) Confidentiality & Authenticity";
                std::cout << "\n\t7) Select All";
                std::cout << "\n\t8) Done! \n";

            cout << endl << "  Enter the S/N of your option (1-6) and press enter each time, or enter 7 to select all; and 8 when done: ";
            cin >> choose;

            switch(choose)
            {
                case 1:
                    Req_1 = "CONF";
                    Re_1 = "CONF";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Confidentiality! Select other requirement or Done." <<endl;
                     break;
                case 2:
                Req_2 = "INTG";
                Re_2 = "INTG";
                 system("cls");
                 std::cout<<"\n" "***********************************************************************************************************\n";
                  cout << "\n\tYou have selected Integrity! Select other requirement or Done." <<endl;
                    break;
                  case 3:
                   Req_3 = "AUTH";
                   Re_3 = "AUTH";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Authentication! Select other requirement or Done." <<endl;
                    break;
                  case 4:
                   Req_4 = "PRIV";
                   Re_4 = "PRIV";
                   system("cls");
                   std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Privacy! Select other requirement or Done." <<endl;
                    break;
                  case 5:
                   Req_5 = "NONR";
                   Re_5 = "NONR";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n\n";
                    cout << "\n\tYou have selected Non-Repudiation! Select other requirement or Done." <<endl;
                    break;
                case 6:
                   Req_6 = "COAU";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected Confidentiality & Authenticity! Select other requirement or Done." <<endl;
                    break;
                case 7:
                    Req_1 = "CONF";
                    Re_1 = "CONF";
                    Req_2 = "INTG";
                    Re_2 = "INTG";
                    Req_3 = "AUTH";
                    Re_3 = "AUTH";
                    Req_4 = "PRIV";
                    Re_4 = "PRIV";
                    Req_5 = "NONR";
                    Re_5 = "NONR";
                    Req_6 = "COAU";
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tYou have selected all!" <<endl;
                     break;
                case 8:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                  cout << "\n\tDone!" <<endl;
                    break;

                default: cout << "Please choose between 1-8 (Press Enter to continue ...)";
                goto level_tk;
                break;
            }

        }while(choose != 8);
    }

     void UserInput::selectSecurityRequirements_existing()
    {
         std::cin.ignore();
            int choose;
            cout << endl;
            level_kl:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "\tSelect your security requirements one at a time: \n";

        do{

                std::cout << "\n\t\t1) Confidentiality";
                std::cout << "\n\t\t2) Integrity";
                std::cout << "\n\t\t3) Authentication";
                std::cout << "\n\t\t4) Privacy";
                std::cout << "\n\t\t5) Non-Repudiation";
                std::cout << "\n\t\t6) Confidentiality & Authenticity";
                std::cout << "\n\t\t7) Done! \n";

            cout << endl << "\tEnter the S/N of your option (1-6) and 7 when done. Press enter each time: ";
            cin >> choose;

            switch(choose)
            {
                case 1:
                             Req_1 = "CONF";

                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for confidentiality (in Bytes): "; cin >> FM_1;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for confidentiality (in Bytes): "; cin >> RAM_1;
                                    system("cls");
                                    cout << "\n\tYou have selected Confidentiality! Select other requirement or Done." <<endl;
                     break;

                case 2:
                     Req_2 = "INTG";
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for integrity (in Bytes): "; cin >> FM_2;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for integrity (in Bytes): "; cin >> RAM_2;
                                    system("cls");
                                    cout << "\n\tYou have selected Integrity! Select other requirement or Done." <<endl;
                     break;
                  case 3:
                       Req_3 = "AUTH";
                       system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for authentication (in Bytes): "; cin >> FM_3;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for authentication (in Bytes): "; cin >> RAM_3;
                                    system("cls");
                                    cout << "\n\tYou have selected Authentication! Select other requirement or Done." <<endl;
                       break;
                  case 4:

                        system("cls");

                             Req_4 = "PRIV";
							   system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for privacy (in Bytes): "; cin >> FM_4;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for privacy (in Bytes): "; cin >> RAM_4;
                                    system("cls");
                                    cout << "\n\tYou have selected Privacy! Select other requirement or Done." <<endl;

                       break;
                  case 5:
                       Req_5 = "NONR";
                       system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for non-repudiation (in Bytes): "; cin >> FM_5;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for non-repudiation (in Bytes): "; cin >> RAM_5;
                                    system("cls");
                                    cout << "\n\tYou have selected Non-Repudiation! Select other requirement or Done." <<endl;
                       break;
                case 6:
                       Req_6 = "COAU";
                       system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";

                                    cout << "\n\tEnter the available flash memory space for confidentiality & authenticity (in Bytes): "; cin >> FM_6;
                                    system("cls");
                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter the RAM space reserved for confidentiality & authenticity (in Bytes): "; cin >> RAM_6;
                                    system("cls");
                                    cout << "\n\tYou have selected Confidentiality & Authenticity! Select other requirement or Done." <<endl;
                       break;
                case 7:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tDone!" <<endl;
                    break;

                default: cout << "Please choose between 1-7 (Press Enter to continue ...)";
               goto level_kl;
                ; break;
            }

        }while(choose != 7);
    }

    void UserInput::selectSecurityRequirements_Hardware()
    {
         std::cin.ignore();
            int choose;
            cout << endl;
            level_kl:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "\tSelect your security requirements one at a time: \n";

        do{

                std::cout << "\n\t\t1) Confidentiality";
                std::cout << "\n\t\t2) Integrity";
                std::cout << "\n\t\t3) Authentication";
                std::cout << "\n\t\t4) Privacy";
                std::cout << "\n\t\t5) Non-Repudiation";
                std::cout << "\n\t\t6) Confidentiality & Authenticity";
                std::cout << "\n\t\t7) Done! \n";

            cout << endl << "\tEnter the S/N of your option (1-6) and 7 when done. Press enter each time: ";
            cin >> choose;

            switch(choose)
            {
                case 1:
                             Req_1 = "CONF";
                                if(Hardware_type == "FPGA")
                                {
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                    cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                    cout << "\n\tEstimate number of slices for confidentiality: "; cin >> cct_area_1;
                                    system("cls");
                                    cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                    cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                    cout << "\n\tEstimate max operating frequency needed for confidentiality(MHz): "; cin >> tp_1;
                                    system("cls");
                                    cout << "\n\tYou have selected Confidentiality! Select other requirement or Done." <<endl;
                                }
                                else if(Hardware_type == "ASIC")
                                {
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                    cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                    cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                    cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                    cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                    cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                    cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                    cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                    cout << "\n\tEstimate the gate equivalents (GE) for confidentiality: "; cin >> cct_area_1;
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                    cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                    cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                    cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                    cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                    cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                    cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                    cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                    cout << "\n\tEnter your desired throughput for confidentiality(kbps): "; cin >> tp_1;
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tYou have selected Confidentiality! Select other requirement or Done." <<endl;
                                }

                     break;

                case 2:
                     Req_2 = "INTG";
                     if(Hardware_type == "FPGA")
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEstimate number of slices for integrity: "; cin >> cct_area_2;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEstimate max operating frequency needed for integrity(MHz): "; cin >> tp_2;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\tYou have selected Integrity! Select other requirement or Done." <<endl;
                    }
                    else if(Hardware_type == "ASIC")
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                        cout << "\t\t738 - 864 \t\t 0.8 - 1.0\n";
                        cout << "\t\t865 - 1060 \t\t 0.3 - 2.8\n";
                        cout << "\t\t1061 - 1127 \t\t 0.5 - 17.8\n";
                        cout << "\t\t1128 - 1396 \t\t 1.0 - 2.7\n";
                        cout << "\t\t1397 - 2190 \t\t 2.7 - 17.8\n";
                        cout << "\t\t2191 - 4362 \t\t 0.4 - 50.0\n\n";
                        cout << "\n\tEstimate the gate equivalents (GE) for integrity: "; cin >> cct_area_2;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                        cout << "\t\t738 - 864 \t\t 0.8 - 1.0\n";
                        cout << "\t\t865 - 1060 \t\t 0.3 - 2.8\n";
                        cout << "\t\t1061 - 1127 \t\t 0.5 - 17.8\n";
                        cout << "\t\t1128 - 1396 \t\t 1.0 - 2.7\n";
                        cout << "\t\t1397 - 2190 \t\t 2.7 - 17.8\n";
                        cout << "\t\t2191 - 4362 \t\t 0.4 - 50.0\n\n";
                        cout << "\n\tEnter your desired throughput for integrity(kbps): "; cin >> tp_2;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\tYou have selected Integrity! Select other requirement or Done." <<endl;
                    }
                     break;
                  case 3:
                       Req_3 = "AUTH";
                       if(Hardware_type == "FPGA")
                       {
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                            cout << "\n\tEstimate number of slices for authentication: "; cin >> cct_area_3;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                            cout << "\n\tEstimate max operating frequency needed for authentication(MHz): "; cin >> tp_3;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n\tYou have selected Authentication! Select other requirement or Done." <<endl;
                       }
                    else if(Hardware_type == "ASIC")
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEstimate the gate equivalents (GE) for authentication: "; cin >> cct_area_3;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEnter your desired throughput for authentication(kbps): "; cin >> tp_3;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\tYou have selected Authentication! Select other requirement or Done." <<endl;
                    }
                       break;
                  case 4:

                        system("cls");

                             Req_4 = "PRIV";
							   if(Hardware_type == "FPGA")
							   {
									system("cls");
									std::cout<<"\n" "***********************************************************************************************************\n";
									cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                    cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
									cout << "\n\tEstimate number of slices for privacy: "; cin >> cct_area_4;
									system("cls");
									std::cout<<"\n" "***********************************************************************************************************\n";
									cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                    cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
									cout << "\n\tEstimate max operating frequency needed for privacy(MHz): "; cin >> tp_4;
									system("cls");
									std::cout<<"\n" "***********************************************************************************************************\n";
									cout << "\n\tYou have selected Privacy! Select other requirement or Done." <<endl;
							   }
							else if(Hardware_type == "ASIC")
							{
								system("cls");
								std::cout<<"\n" "***********************************************************************************************************\n";
								cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
								cout << "\n\tEstimate the gate equivalents (GE) for privacy: "; cin >> cct_area_4;
								system("cls");
								std::cout<<"\n" "***********************************************************************************************************\n";
								cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
								cout << "\n\tEnter your desired throughput for privacy(kbps): "; cin >> tp_4;
								system("cls");
								std::cout<<"\n" "***********************************************************************************************************\n";
								cout << "\n\tYou have selected Privacy! Select other requirement or Done." <<endl;
							}

                       break;
                  case 5:
                       Req_5 = "NONR";
                       if(Hardware_type == "FPGA")
                       {
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                            cout << "\n\tEstimate number of slices for non-repudiation: "; cin >> cct_area_5;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                            cout << "\n\tEstimate max operating frequency needed for non-repudiation(MHz): "; cin >> tp_5;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n\tYou have selected Non-Repudiation! Select other requirement or Done." <<endl;
                      }
                    else if(Hardware_type == "ASIC")
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEstimate the gate equivalents (GE) for non-repudiation: "; cin >> cct_area_5;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                        cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                        cout << "\n\tEnter your desired throughput for non-repudiation(kbps): "; cin >> tp_5;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\tYou have selected Non-Repudiation! Select other requirement or Done." <<endl;
                    }
                       break;
                case 6:
                       Req_6 = "COAU";
                       if(Hardware_type == "FPGA")
                       {
                            system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t No. of Slices (The lower the better)\tMax Operating Freq. (The higher the better) \n";
                        cout << "\t\t135 - 412.9 \t\t\t 1.0 - 389.0\n";
                        cout << "\t\t413 - 890.9 \t\t\t 1.0 - 347.0\n";
                        cout << "\t\t891 - 1347.9 \t\t\t 1.0 - 280.9\n";
                        cout << "\t\t1348 - 4500 \t\t\t 1.0 - 256.9\n\n";
                            cout << "\n\tEstimate number of slices for Confidentiality & Authenticity: "; cin >> cct_area_6;
                            system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t No. of Slices (The lower the better)\tMax Operating Freq. (The higher the better) \n";
                        cout << "\t\t135 - 412.9 \t\t\t 1.0 - 389.0\n";
                        cout << "\t\t413 - 890.9 \t\t\t 1.0 - 347.0\n";
                        cout << "\t\t891 - 1347.9 \t\t\t 1.0 - 280.9\n";
                        cout << "\t\t1348 - 4500 \t\t\t 1.0 - 256.9\n\n";
                            cout << "\n\tEstimate max operating frequency needed for Confidentiality & Authenticity(MHz): "; cin >> tp_6;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            cout << "\n\tYou have selected Confidentiality & Authenticity! Select other requirement or Done." <<endl;
                      }
                    else if(Hardware_type == "ASIC")
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                        cout << "\t\t2860 - 3099 \t\t 1.0 - 5.0\n";
                        cout << "\t\t3100 - 5999 \t\t 1.0 - 6.0\n";
                        cout << "\t\t6000 - 7949 \t\t 1.0 - 5.3\n";
                        cout << "\t\t7950 - 9000 \t\t 1.0 - 5.5\n\n";
                        cout << "\n\tEstimate the gate equivalents (GE) for Confidentiality & Authenticity: "; cin >> cct_area_6;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                        cout << "\t\t2860 - 3099 \t\t 1.0 - 5.0\n";
                        cout << "\t\t3100 - 5999 \t\t 1.0 - 6.0\n";
                        cout << "\t\t6000 - 7949 \t\t 1.0 - 5.3\n";
                        cout << "\t\t7950 - 9000 \t\t 1.0 - 5.5\n\n";
                        cout << "\n\tEnter your desired throughput for Confidentiality & Authenticity(Mbps): "; cin >> tp_6;
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        cout << "\n\tYou have selected Confidentiality & Authenticity! Select other requirement or Done." <<endl;
                    }
                       break;
                case 7:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    cout << "\n\tDone!" <<endl;
                    break;

                default: cout << "Please choose between 1-7 (Press Enter to continue ...)";
               goto level_kl;
                ; break;
            }

        }while(choose != 7);
    }

    void UserInput::importSecReqmts_Hardware()
    {
         cout << endl;

        char choa;
        levelk:
        system("cls");
        std::cout<<"\n" "***********************************************************************************************************\n";

        std::cout << "\n IF YOU HAVE USED THE SECURITY REQUIREMENTS ELICITATION (SRE) TOOL TO GENERATE YOUR SECURITY REQUIREMENTS,  \n";
        std::cout << "\t\t  YOU CAN ENTER YOUR SRE REQUEST ID TO IMPORT YOUR SECURITY REQUIREMENTS. \n\n\n";

        std::cout << "\n *NOTE THAT FOR HARDWARE IMPLEMATION REQUESTS, AFTER IMPORTING YOUR SECURITY REQUIREMENTS, YOU NEED TO GO  \n";
        std::cout << "  TO THE MAIN MENU AND SELECT OPTION 10 TO INCLUDE THE GEs AND THROUGHPUTS FOR THE GIVEN SECURITY REQMNTS. \n\n";



        std::cout << "\n\tHave you used the tool? \n";

        std::cout<<"\n\t\t1. Yes, I have used it and I want to import the generated security requirements.";
        std::cout<<"\n\t\t2. Yes, I have used the tool, but I want to select the security requirements manually.";
        std::cout<<"\n\t\t3. No, I have not used the tool. I will select the security requirements manually.";
        std::cout<<"\n\n\tSelect Your Option (1-3): ";
        std::cin>>choa;

            switch(choa)
            {
                case '1':
                    {
                        system("cls");
                        std::cout << "\n" "***********************************************************************************************************\n";
                        std::cout<<"\n\t\tYES, I HAVE USED IT AND I WANT TO IMPORT THE SECURITY REQUIREMENTS.\n\n";
                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                        std::cin.ignore();

                        if(cin.get() == '\n')
                        {
                            Processing_and_Output po;
                            UserInput usrIp;

                            string Reqst_ID;
                            system("cls");
                            std::cout << "\n***********************************************************************************************************\n";
                            cout << "\tPlease enter your Requirements Elicitation Request ID: "; cin >> Reqst_ID;

                            Preliminary pre;

                            pre.convert_lowerC_to_upperC(Reqst_ID);

                            int num_digits;
                            int string_length;
                            char first_letter;

                            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                            num_digits = collector.n1;
                            string_length = collector.n2;
                            first_letter = collector.c;

                            while(num_digits !=4 || string_length != 5 || first_letter != 'R')
                            {
                                system("cls");
                                std::cout << "\n***********************************************************************************************************\n";
                                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                std::cout << "\n\t\t\t\tPlease enter a valid Requirements Elicitation Request ID: ";
                                std::cin >> Reqst_ID;


                                pre.convert_lowerC_to_upperC(Reqst_ID);

                                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                                num_digits = collector.n1;
                                string_length = collector.n2;
                                first_letter = collector.c;
                            }

                            system("cls");
                            string findbyID_query = "select * from generated_requirements where Reqst_ID = " + ("'"+Reqst_ID+"'");
                            const char* qn = findbyID_query.c_str();
                            qstate = mysql_query(conn, qn);

                            if(!qstate)
                            {
                                res = mysql_store_result(conn);
                                while((row = mysql_fetch_row(res)))
                                {
                                    Re_1 = Reqmt_1 = row[1];
                                    Re_2 = Reqmt_2 = row[2];
                                    Re_3 =Reqmt_3 = row[3];
                                    Re_4 =  Reqmt_4 = row[4];
                                    Re_5 =  Reqmt_5 = row[5];
                                    Re_6 =  Reqmt_6 = row[6];
                                    Re_7 =  Reqmt_7 = row[7];
                                    Re_8 =  Reqmt_8 = row[8];
                                    Re_9 =  Reqmt_9 = row[9];
                                    Re_10 =  Reqmt_10 = row[10];
                                    Re_11 =  Reqmt_11 = row[11];
                                    Re_12 =  Reqmt_12 = row[12];
                                    Re_13 =  Reqmt_13 = row[13];
                                    Re_14 =  Reqmt_14 = row[14];
                                    Re_15 =  Reqmt_15 = row[15];

                                }
                            }
                            else
                            {
                                cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                            }
                                Req_1 = Reqmt_1;  Req_2 = Reqmt_2; Req_3 = Reqmt_3; Req_4 = Reqmt_4;  Req_5 = Reqmt_5;
                        }
                        else
                        {
                            goto levelk;
                        }
                    break;
                    }
                case '2':
                        system("cls");
                        std::cout << "\n" "***********************************************************************************************************\n";
                        std::cout<<"\n\t   YES, I HAVE USED THE TOOL, BUT I WANT TO SELECT THE SECURITY REQUIREMENTS MANUALLY.\n\n";
                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                        std::cin.ignore();

                        if(cin.get() == '\n')
                        {
                           selectSecurityRequirements_Hardware();
                        }
                        else
                        {
                            goto levelk;
                        }

                    break;
                case '3':
                        system("cls");
                        std::cout << "\n" "***********************************************************************************************************\n";
                        std::cout<<"\n\t   NO, I HAVE NOT USED THE TOOL. I WILL SELECT THE SECURITY REQUIREMENTS MANUALLY.\n\n";
                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                        std::cin.ignore();

                        if(cin.get() == '\n')
                        {
                           selectSecurityRequirements_Hardware();
                        }
                        else
                        {
                            goto levelk;
                        }
                    break;
                default:
                        std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto levelk;
            }
    }

    void UserInput::importSecReqmts_Software()
    {

        if(status == "new")
        {
                 cout << endl;

                char choa;
                levelk:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";

                std::cout << "\n IF YOU HAVE USED THE SECURITY REQUIREMENTS ELICITATION (SRE) TOOL TO GENERATE YOUR SECURITY REQUIREMENTS,  \n";
                std::cout << "\t\t  YOU CAN ENTER YOUR SRE REQUEST ID TO IMPORT YOUR SECURITY REQUIREMENTS. \n\n";

                std::cout << "\n\tHave you used the tool? \n";

                std::cout<<"\n\t\t1. Yes, I have used it and I want to import the generated security requirements.";
                std::cout<<"\n\t\t2. Yes, I have used the tool, but I want to select the security requirements manually.";
                std::cout<<"\n\t\t3. No, I have not used the tool. I will select the security requirements manually.";
                std::cout<<"\n\n\tSelect Your Option (1-3): ";
                std::cin>>choa;

                switch(choa)
                {
                    case '1':
                        {
                            system("cls");
                            std::cout << "\n" "***********************************************************************************************************\n";
                            std::cout<<"\n\t   YES, I HAVE USED IT AND I WANT TO IMPORT THE SECURITY REQUIREMENTS.\n\n";
                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                            std::cin.ignore();

                            if(cin.get() == '\n')
                            {
                               Processing_and_Output po;
                                UserInput usrIp;

                                string Reqst_ID;
                                system("cls");
                                std::cout << "\n***********************************************************************************************************\n";
                                cout << "\tPlease enter your Requirements Elicitation Request ID: "; cin >> Reqst_ID;

                                Preliminary pre;

                                pre.convert_lowerC_to_upperC(Reqst_ID);

                                int num_digits;
                                int string_length;
                                char first_letter;

                                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                                num_digits = collector.n1;
                                string_length = collector.n2;
                                first_letter = collector.c;

                                while(num_digits !=4 || string_length != 5 || first_letter != 'R')
                                {
                                    system("cls");
                                    std::cout << "\n***********************************************************************************************************\n";
                                    std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                    std::cout << "\n\t\t\t\tPlease enter a valid Requirements Elicitation Request ID: ";
                                    std::cin >> Reqst_ID;


                                    pre.convert_lowerC_to_upperC(Reqst_ID);

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;
                                }

                                system("cls");
                                string findbyID_query = "select * from generated_requirements where Reqst_ID = " + ("'"+Reqst_ID+"'");
                                const char* qn = findbyID_query.c_str();
                                qstate = mysql_query(conn, qn);

                                if(!qstate)
                                {
                                    res = mysql_store_result(conn);
                                    while((row = mysql_fetch_row(res)))
                                    {
                                        Re_1 = Reqmt_1 = row[1];
                                        Re_2 = Reqmt_2 = row[2];
                                        Re_3 = Reqmt_3 = row[3];
                                        Re_4 =  Reqmt_4 = row[4];
                                        Re_5 =  Reqmt_5 = row[5];
                                        Re_6 =  Reqmt_6 = row[6];
                                        Re_7 =  Reqmt_7 = row[7];
                                        Re_8 =  Reqmt_8 = row[8];
                                        Re_9 =  Reqmt_9 = row[9];
                                        Re_10 =  Reqmt_10 = row[10];
                                        Re_11 =  Reqmt_11 = row[11];
                                        Re_12 =  Reqmt_12 = row[12];
                                        Re_13 =  Reqmt_13 = row[13];
                                        Re_14 =  Reqmt_14 = row[14];
                                        Re_15 =  Reqmt_15 = row[15];
                                    }
                                }
                                else
                                {
                                    cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                                }
                                    Req_1 = Reqmt_1;  Req_2 = Reqmt_2; Req_3 = Reqmt_3; Req_4 = Reqmt_4;  Req_5 = Reqmt_5;
                            }
                            else
                            {
                                goto levelk;
                            }
                        break;
                        }
                    case '2':
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t   YES, I HAVE USED THE TOOL, BUT I WANT TO SELECT THE SECURITY REQUIREMENTS MANUALLY.\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    selectSecurityRequirements_Software();
                                }
                                else
                                {
                                    goto levelk;
                                }
                        break;
                    case '3':
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t   NO, I HAVE NOT USED THE TOOL. I WILL SELECT THE SECURITY REQUIREMENTS MANUALLY.\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    selectSecurityRequirements_Software();
                                }
                                else
                                {
                                    goto levelk;
                                }
                        break;
                    default:
                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto levelk;
                }
        }
        else if(status == "old")
        {
            selectSecurityRequirements_existing();
        }
    }

	void UserInput::getOther_inputs()
	{
         int choice = 0, choice3;
         std::cin.ignore();
         level_tt:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	std::cout << "\n\tSelect your application area: \n";

                std::cout << "\n\t1) Smart Home";
                std::cout << "\n\t2) Smart City";
                std::cout << "\n\t3) Smart Agriculture";
                std::cout << "\n\t4) Smart Grid";
                std::cout << "\n\t5) Smart Healthcare";
                std::cout << "\n\t6) Smart Elderly Monitoring";
                std::cout << "\n\t7) Smart Kid Monitoring";
                std::cout << "\n\t8) Smart pet Monitoring";
                std::cout << "\n\t9) Smart Banking/Financial applications";
                std::cout << "\n\t10) Industrial Automation";
                std::cout << "\n\t11) Smart Supply Chain";
                std::cout << "\n\t12) Smart Retail";
                std::cout << "\n\t13) Smart Environmental Monitoring";
                std::cout << "\n\t14) Smart Automotive/Transportation";
                std::cout << "\n\t15) Connected Car";
                std::cout << "\n\t16) Other Domain";

            cout << endl << "\n\tEnter the S/N of your option (1-16) and Press enter: ";
            cin >> choice;

            switch(choice)
            {
                case 1:
                    Applic_Domain = "Home";
                    cout << "\n\tYou have selected Smart Home" <<endl;
                     break;
                case 2:
                Applic_Domain = "City";
                  cout << "\n\tYou have selected Smart City" <<endl;
                    break;
                 case 3:
                   Applic_Domain = "Agriculture";
                   cout << "\n\tYou have selected Smart Agriculture" <<endl;
                    break;
                  case 4:
                   Applic_Domain = "Grid";
                    cout << "\n\tYou have selected Smart Grid" <<endl;
                    break;
                  case 5:
                   Applic_Domain = "Healthcare";
                    cout << "\n\tYou have selected Smart Healthcare" <<endl;
                    break;
                  case 6:
                   Applic_Domain = "Elderly";
                    cout << "\n\tYou have selected Smart Elderly Monitoring" <<endl;
                    break;
                  case 7:
                   Applic_Domain = "Kid";
                    cout << "\n\tYou have selected Smart Kid Monitoring" <<endl;
                    break;
                    case 8:
                   Applic_Domain = "Pet";
                    cout << "\n\tYou have selected Smart pet Monitoring" <<endl;
                    break;
                    case 9:
                   Applic_Domain = "Financial";
                    cout << "\n\tYou have selected Smart Banking/Financial applications" <<endl;
                    break;
                    case 10:
                   Applic_Domain = "Industrial";
                    cout << "\n\tYou have selected Industrial Automation" <<endl;
                    break;
                    case 11:
                   Applic_Domain = "Supply_Chain";
                    cout << "\n\tYou have selected Smart Supply Chain" <<endl;
                    break;
                    case 12:
                   Applic_Domain = "Retail";
                    cout << "\n\tYou have selected Smart Retail" <<endl;
                    break;
                    case 13:
                   Applic_Domain = "Environmental";
                    cout << "\n\tYou have selected Smart Environmental Monitoring" <<endl;
                    break;
                    case 14:
                   Applic_Domain = "Transportation";
                    cout << "\n\tYou have selected Smart Automotive/Transportation" <<endl;
                    break;
                    case 15:
                   Applic_Domain = "Connected_Car";
                    cout << "\n\tYou have selected Connected Car" <<endl;
                    break;
                     case 16:
                    std::cout << "\n\tEnter one word that best describes your domain: ";
                    cin >> Applic_Domain;
                    break;
                    default: cout << "Please choose between 1-16 (Press Enter to continue ...)";
                    goto level_tt;
                    break;
            }

            cout << endl;
                levle_tj:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
            	std::cout << "\n\tSelect your Payload Size: \n";

                std::cout << "\n\t1) Small (1-128 bytes)";
                std::cout << "\n\t2) Average (129-256 bytes)";
                std::cout << "\n\t3) Large (> 256 bytes)";
                std::cout << "\n\t4) Continuous";
                std::cout << "\n\t5) Unknown";

            cout << endl << "\n\tEnter the S/N of your option and Press enter: ";
            cin >> choice3;

            switch(choice3)
            {
                case 1:
                    Payload_size = "small";
                    cout << "\n\tYou have selected Small" <<endl;
                     break;
                case 2:
                Payload_size = "average";
                  cout << "\n\tYou have selected Average" <<endl;
                    break;
                 case 3:
                   Payload_size = "large";
                   cout << "\n\tYou have selected Large" <<endl;
                    break;
                  case 4:
                   Payload_size = "continuous";
                    cout << "\n\tYou have selected Continuous" <<endl;
                    break;
                  case 5:
                   Payload_size = "unknown";
                    cout << "\n\tYou have selected Unknown" <<endl;
                    break;
                    default: cout << "Please choose between 1-5 (Press Enter to continue ...)";
                    goto levle_tj;
                    ; break;
            }

                importSecReqmts_Software();
	}

	void UserInput::getInput_for_HardwareImplementaion()
	{
	    chrono::steady_clock::time_point start2 = chrono::steady_clock::now();

        system("cls");

                     char choice;

                    level:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                     std::cout << "\n\tSelect Hardware Type (FPGA or ASIC): \n";

						std::cout<<"\n\t\t1. Field-programmable Gate Array (FPGA) ";
                        std::cout<<"\n\t\t2. Application-specific Integrated Circuit(ASIC)";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choice;

						switch(choice)
						{
						case '1':
                            Hardware_type = "FPGA";
                            break;
                        case '2':
                            Hardware_type = "ASIC";
                            break;
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level;
						}

                int choice1;
            level_kg:
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
           	std::cout << "\n\tSelect your application area: \n";

                std::cout << "\n\t1) Smart Home";
                std::cout << "\n\t2) Smart City";
                std::cout << "\n\t3) Smart Agriculture";
                std::cout << "\n\t4) Smart Grid";
                std::cout << "\n\t5) Smart Healthcare";
                std::cout << "\n\t6) Smart Elderly Monitoring";
                std::cout << "\n\t7) Smart Kid Monitoring";
                std::cout << "\n\t8) Smart pet Monitoring";
                std::cout << "\n\t9) Smart Banking/Financial applications";
                std::cout << "\n\t10) Industrial Automation";
                std::cout << "\n\t11) Smart Supply Chain";
                std::cout << "\n\t12) Smart Retail";
                std::cout << "\n\t13) Smart Environmental Monitoring";
                std::cout << "\n\t14) Smart Automotive/Transportation";
                std::cout << "\n\t15) Connected Car";
                std::cout << "\n\t16) Other Domain";

            cout << endl << "\n\tEnter the S/N of your option (1-16) and Press enter: ";
            cin >> choice1;

            switch(choice1)
            {
                case 1:
                    Applic_Domain = "Home";
                    cout << "\n\tYou have selected Smart Home" <<endl;
                     break;
                case 2:
                Applic_Domain = "City";
                  cout << "\n\tYou have selected Smart City" <<endl;
                    break;
                 case 3:
                   Applic_Domain = "Agriculture";
                   cout << "\n\tYou have selected Smart Agriculture" <<endl;
                    break;
                  case 4:
                   Applic_Domain = "Grid";
                    cout << "\n\tYou have selected Smart Grid" <<endl;
                    break;
                  case 5:
                   Applic_Domain = "Healthcare";
                    cout << "\n\tYou have selected Smart Healthcare" <<endl;
                    break;
                  case 6:
                   Applic_Domain = "Elderly";
                    cout << "\n\tYou have selected Smart Elderly Monitoring" <<endl;
                    break;
                  case 7:
                   Applic_Domain = "Kid";
                    cout << "\n\tYou have selected Smart Kid Monitoring" <<endl;
                    break;
                    case 8:
                   Applic_Domain = "Pet";
                    cout << "\n\tYou have selected Smart pet Monitoring" <<endl;
                    break;
                    case 9:
                   Applic_Domain = "Financial";
                    cout << "\n\tYou have selected Smart Banking/Financial applications" <<endl;
                    break;
                    case 10:
                   Applic_Domain = "Industrial";
                    cout << "\n\tYou have selected Industrial Automation" <<endl;
                    break;
                    case 11:
                   Applic_Domain = "Supply_Chain";
                    cout << "\n\tYou have selected Smart Supply Chain" <<endl;
                    break;
                    case 12:
                   Applic_Domain = "Retail";
                    cout << "\n\tYou have selected Smart Retail" <<endl;
                    break;
                    case 13:
                   Applic_Domain = "Environmental";
                    cout << "\n\tYou have selected Smart Environmental Monitoring" <<endl;
                    break;
                    case 14:
                   Applic_Domain = "Transportation";
                    cout << "\n\tYou have selected Smart Automotive/Transportation" <<endl;
                    break;
                    case 15:
                   Applic_Domain = "Connected_Car";
                    cout << "\n\tYou have selected Connected Car" <<endl;
                    break;
                     case 16:
                    std::cout << "\n\tEnter one word that best describes your domain: ";
                    cin >> Applic_Domain;
                    break;
                    default: cout << "Please choose between 1-16";
                    goto level_kg;
                     break;
            }

                 std::cin.ignore();
                int choice3;
                  cout << endl;
                  level_kt:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
            	std::cout << "\n\tSelect your Payload Size: \n";

                std::cout << "\n\t1) Small (1-128 bytes)";
                std::cout << "\n\t2) Average (129-256 bytes)";
                std::cout << "\n\t3) Large (> 256 bytes)";
                std::cout << "\n\t4) Continuous";
                std::cout << "\n\t5) Unknown";

            cout << endl << "\n\tEnter the S/N of your option (1-5) and Press enter: ";
            cin >> choice3;

            switch(choice3)
            {
                case 1:
                    Payload_size = "small";
                    cout << "\n\tYou have selected Small" <<endl;
                     break;
                case 2:
                Payload_size = "average";
                  cout << "\n\tYou have selected Average" <<endl;
                    break;
                 case 3:
                   Payload_size = "large";
                   cout << "\n\tYou have selected Large" <<endl;
                    break;
                  case 4:
                   Payload_size = "continuous";
                    cout << "\n\tYou have selected Continuous" <<endl;
                    break;
                  case 5:
                   Payload_size = "unknown";
                    cout << "\n\tYou have selected Unknown" <<endl;
                    break;
                    default: cout << "Please choose between 1-5";
                    goto level_kt;
                    break;
            }

                    int choice2;
                    level2:
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                     std::cout << "\n\tSelect desired energy performance: \n";

						std::cout<<"\n\t\t1. Low Power";
                        std::cout<<"\n\t\t2. Ultra-low Power";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";
						std::cin>>choice2;

						switch(choice2)
						{
						case 1:
                            Energy = "Low";
                            break;
                        case 2:
                            Energy = "Ultra-low";
                            break;
						default :
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
							goto level2;
                            break;
						}


                    importSecReqmts_Hardware();

                     string request_query = "insert into users_requests_2 (Request_ID, Hardware_type, Applic_Domain, Payload_size, Energy, Req_1, cct_area_1, tp_1, Req_2, cct_area_2, tp_2, Req_3, cct_area_3, tp_3, Req_4, cct_area_4, tp_4, Req_5, cct_area_5, tp_5, Req_6, cct_area_6, tp_6) values('"+Request_ID+"', '"+Hardware_type+"', '"+Applic_Domain+"', '"+Payload_size+"', '"+Energy+"', '"+Req_1+"', '"+cct_area_1+"', '"+tp_1+"', '"+Req_2+"', '"+cct_area_2+"', '"+tp_2+"', '"+Req_3+"', '"+cct_area_3+"', '"+tp_3+"', '"+Req_4+"', '"+cct_area_4+"', '"+tp_4+"', '"+Req_5+"', '"+cct_area_5+"', '"+tp_5+"', '"+Req_6+"', '"+cct_area_6+"', '"+tp_6+"')";

              const char* qr = request_query.c_str();
              qstate = mysql_query(conn, qr);

                if(!qstate)
                {
                    std::cout << "\n\n\t\tData being saved .....\n";

                     Req_1.erase(); Req_2.erase(); Req_3.erase(); Req_4.erase(); Req_5.erase(); // This is to erase the previous value from the variable so that when a particular variable is not selected, its space will be empty, instead inserting the previous value.
                     cct_area_1.erase(); cct_area_2.erase(); cct_area_3.erase(); cct_area_4.erase(); cct_area_5.erase();
                      tp_1.erase(); tp_2.erase(); tp_3.erase(); tp_4.erase(); tp_5.erase();

                    cout << endl << "\n\n\t\tRequest Successfully added in the database!" << endl;

                    cout << endl << "\n\n\t\tPress Enter to go back to the Main Menu." << endl;
                }
                else
                {
                    cout << "\n\n\tQuery Execution Problem! Error Number: " << mysql_errno(conn) << endl;
                    cout << "\n\n\tError Number 1062 implies that the entered Request ID already exist in database.\n" << endl;
                    cout << endl << "\n\n\tPlease press Enter to go back to the Main Menu and repeat the process with a unique ID." << endl;
                }

                 REQST_id = Request_ID;
                string request_query2 = "insert into requirements_for_report (REQST_id, Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15) values('"+REQST_id+"', '"+Re_1+"', '"+Re_2+"', '"+Re_3+"', '"+Re_4+"', '"+Re_5+"', '"+Re_6+"', '"+Re_7+"', '"+Re_8+"', '"+Re_9+"', '"+Re_10+"', '"+Re_11+"', '"+Re_12+"', '"+Re_13+"', '"+Re_14+"', '"+Re_15+"')";

                const char* qr2 = request_query2.c_str();
                qstate = mysql_query(conn, qr2);

                if(!qstate)
                {
                    Re_1.erase(); Re_2.erase(); Re_3.erase(); Re_4.erase(); Reqmt_5.erase(); Re_6.erase(); Re_7.erase(); Re_8.erase(); Re_9.erase(); Re_10.erase(); Re_11.erase(); Re_12.erase(); Re_13.erase(); Re_14.erase(); Re_15.erase();
                }
                else
                {

                }

        chrono::steady_clock::time_point end2 = chrono::steady_clock::now();

        double elapsed_time2_ns = double(std::chrono::duration_cast <std::chrono::nanoseconds> (end2 -start2).count());
        std::cout << "\n\n\t\tElapsed Time for Hardware Request (s): " << elapsed_time2_ns / 1e9 << std::endl;
	}

	void UserInput::getInput_for_softwareImplementaion()
	{
      chrono::steady_clock::time_point start3 = chrono::steady_clock::now();

            level_:
                char ch;
            system("cls");
            std::cout<<"\n" "***********************************************************************************************************\n";
            cout << "\t\t\t\t\tSYSTEM DEVELOPMENT PHASE\n" << endl;

            std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system? \n";

                        std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                         std::cout<<"\n\t\t2. Existing System ";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

						std::cin>>ch;


						switch(ch)
						{
						case '1':
						     {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tCONCEPTION, PLANNING, ANALYSIS, DESIGN\n\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                        if(cin.get() == '\n')
                                        {
                                                status = "new";
                                                do{
                                                    system("cls");
                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                    cout << "\n Enter Hardware Type (Microntroller or Single Board Computer) [MCU or SBC]: ";
                                                    cin >> Hardware_type;
                                                    Preliminary pre;

                                                  pre.convert_lowerC_to_upperC(Hardware_type); //calling the conversion function

                                                        if(Hardware_type == "MCU")
                                                        {
                                                             char choice;

                                                             level:
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                             std::cout << "\n\tSelect your Microcontroller Type: \n";

                                                                std::cout<<"\n\t\t1. AVR (8 or 32-bit RISC CPU) ";
                                                                std::cout<<"\n\t\t2. MSP (16-bit RISC CPU)";
                                                                std::cout<<"\n\t\t3. ARM (32 or 64-bit RISC CPU)";
                                                                std::cout<<"\n\t\t4. PIC (8, 16 or 32-bit RISC CPU)";
                                                                std::cout<<"\n\t\t5. Other";
                                                                std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                                                std::cin>>choice;
                                                                Preliminary pre;
                                                                switch(choice)
                                                                {
                                                                case '1':
                                                                    Hardware_type = "AVR";
                                                                    break;
                                                                case '2':
                                                                    Hardware_type = "MSP";
                                                                    break;
                                                                case '3':
                                                                    Hardware_type = "ARM";
                                                                    break;
                                                                case '4':
                                                                    Hardware_type = "PIC";
                                                                    break;
                                                                case '5':
                                                                    cout << "\n\tEnter your MCU brand name (< or = 6 characters): "; cin >> Hardware_type;
                                                                   pre.convert_lowerC_to_upperC(Hardware_type);
                                                                    break;
                                                                default :
                                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                                    goto level;
                                                                }
                                                            break;
                                                        }
                                                }while(((Hardware_type != "SBC") && (Hardware_type != "MCU")));


                                                            int choice2;
                                                            level2:
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                             std::cout << "\n\tSelect your CPU Type: \n";

                                                                std::cout<<"\n\t\t1. 8-bit";
                                                                std::cout<<"\n\t\t2. 16-bit";
                                                                std::cout<<"\n\t\t3. 32-bit";
                                                                std::cout<<"\n\t\t4. 64-bit";
                                                                std::cout<<"\n\t\t5. Other";
                                                                std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                                                std::cin>>choice2;

                                                                switch(choice2)
                                                                {
                                                                case 1:
                                                                    CPU = "8";
                                                                    break;
                                                                case 2:
                                                                    CPU = "16";
                                                                    break;
                                                                case 3:
                                                                    CPU = "32";
                                                                    break;
                                                                case 4:
                                                                    CPU = "64";
                                                                    break;
                                                                case 5:
                                                                    cout << "\n\tEnter the bit number of your CPU(e.g., 4): "; cin >> CPU;
                                                                    break;
                                                                default :
                                                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                                    goto level2;
                                                                    break;
                                                                }
                                                     system("cls");
                                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                                    std::cout << "\n\tEnter flash memory size (in KB): ";
                                                    std::cin >> FlashMem_size;
                                                     system("cls");
                                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                                    std::cout << "\n\tEnter RAM size (in KB): ";
                                                    std::cin >> Ram_size;
                                                     system("cls");
                                                     std::cout<<"\n" "***********************************************************************************************************\n";
                                                    std::cout << "\n\tEnter processor speed or frequency (in MHz): ";
                                                    std::cin >> Clock_speed;

                                                    getOther_inputs();

                                                      string request_query = "insert into users_requests (Request_ID, Hardware_type, CPU, FlashMem_size, Ram_size, Clock_speed, Applic_Domain, Payload_size, Req_1, Req_2, Req_3, Req_4, Req_5, Req_6) values('"+Request_ID+"', '"+Hardware_type+"', '"+CPU+"', '"+FlashMem_size+"', '"+Ram_size+"', '"+Clock_speed+"', '"+Applic_Domain+"', '"+Payload_size+"', '"+Req_1+"', '"+Req_2+"', '"+Req_3+"', '"+Req_4+"', '"+Req_5+"', '"+Req_6+"')";

                                                      const char* qr = request_query.c_str();
                                                      qstate = mysql_query(conn, qr);

                                                        if(!qstate)
                                                        {
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                            std::cout << "\n\n\t\tData being saved .....\n";

                                                             Req_1.erase(); Req_2.erase(); Req_3.erase(); Req_4.erase(); Req_5.erase(); // This is to erase the variable in order to avoid doublicate entry.

                                                            status.erase();
                                                            cout << endl << "\n\n\t\tRequest Successfully added in the database!" << endl;

                                                            cout << endl << "\n\n\t\tPress Enter to go back to the Main Menu." << endl;
                                                        }
                                                        else
                                                        {
                                                            cout << "\n\n\t Query Execution Problem! Error Number: " << mysql_errno(conn) << endl;
                                                            cout << "\n\n\tError Number 1062 implies that the entered Request ID already exist in database.\n" << endl;
                                                             cout << endl << "\n\n\tPlease press Enter to go back to the Main Menu and repeat the process with a unique ID." << endl;
                                                        }


                                                         REQST_id = Request_ID;
                                                        string request_query2 = "insert into requirements_for_report (REQST_id, Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15) values('"+REQST_id+"', '"+Re_1+"', '"+Re_2+"', '"+Re_3+"', '"+Re_4+"', '"+Re_5+"', '"+Re_6+"', '"+Re_7+"', '"+Re_8+"', '"+Re_9+"', '"+Re_10+"', '"+Re_11+"', '"+Re_12+"', '"+Re_13+"', '"+Re_14+"', '"+Re_15+"')";

                                                        const char* qr2 = request_query2.c_str();
                                                        qstate = mysql_query(conn, qr2);

                                                        if(!qstate)
                                                        {
                                                            Re_1.erase(); Re_2.erase(); Re_3.erase(); Re_4.erase(); Reqmt_5.erase(); Re_6.erase(); Re_7.erase(); Re_8.erase(); Re_9.erase(); Re_10.erase(); Re_11.erase(); Re_12.erase(); Re_13.erase(); Re_14.erase(); Re_15.erase();
                                                        }
                                                        else
                                                        {

                                                        }

                                                      chrono::steady_clock::time_point end3 = chrono::steady_clock::now();

                                                    double elapsed_time3_ns = double(std::chrono::duration_cast <std::chrono::nanoseconds> (end3 -start3).count());//time difference
                                                    std::cout << "\n\n\t\tElapsed Time for Software Request (s): " << elapsed_time3_ns / 1e9 << std::endl;//print elapsed time for software request
                                        }
                                        else
                                        {
                                            goto level_;
                                        }
                                        break;
                                }
                        case '2':
                            {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tEXISTING SYSTEM\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                        {
                                           status = "old";
                                            do{
                                                    system("cls");
                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                    cout << "\n Enter Hardware Type (Microcontroller or Single Board Computer) [MCU or SBC]: ";
                                                    cin >> Hardware_type;
                                                    Preliminary pre;

                                                  pre.convert_lowerC_to_upperC(Hardware_type);

                                                        if(Hardware_type == "MCU")
                                                        {
                                                             int lia;

                                                           do
                                                           {
                                                               system("cls");
                                                               std::cout<<"\n" "***********************************************************************************************************\n";
                                                               std::cout << "\n\tSelect your Microcontroller Type: \n";

                                                                std::cout<<"\n\t\t1. AVR (8 or 32-bit RISC CPU) ";
                                                                std::cout<<"\n\t\t2. MSP (16-bit RISC CPU)";
                                                                std::cout<<"\n\t\t3. ARM (32 or 64-bit RISC CPU)";
                                                                std::cout<<"\n\t\t4. Other";
                                                                std::cout<<"\n\n\tSelect Your Option (1-4): ";
                                                                std::cin>>lia;

                                                                        while(std::cin.fail())
                                                                        {
                                                                            system("cls");
                                                                           std::cout << "\n" "***********************************************************************************************************\n";
                                                                            std::cout << "\n\t\tERROR! This is not an integer: ";
                                                                             std::cin.clear();
                                                                            std::cin.ignore(256,'\n');
                                                                            std::cin >> lia;
                                                                        }
                                                                Preliminary pre;
                                                                switch(lia)
                                                                {
                                                                case 1:
                                                                    Hardware_type = "AVR";
                                                                    break;
                                                                case 2:
                                                                    Hardware_type = "MSP";
                                                                    break;
                                                                case 3:
                                                                    Hardware_type = "ARM";
                                                                    break;
                                                                case 4:
                                                                    system("cls");
                                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                                    cout << "\n\tEnter your MCU brand name (< or = 6 characters): "; cin >> Hardware_type;
                                                                   pre.convert_lowerC_to_upperC(Hardware_type);
                                                                    break;
                                                                default :
                                                                    system("cls");
                                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                                    std::cout << "\tError! Wrong option selected." << std:: endl;
                                                                  }
                                                           }while(lia != 1 && lia != 2 && lia != 3 && lia != 4);
                                                           break;
                                                        }
                                                }while(((Hardware_type != "SBC") && (Hardware_type != "MCU")));


                                                            int lau;
                                                        do
                                                        {
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                             std::cout << "\n\tSelect your CPU Type: \n";

                                                                std::cout<<"\n\t\t1. 8-bit";
                                                                std::cout<<"\n\t\t2. 16-bit";
                                                                std::cout<<"\n\t\t3. 32-bit";
                                                                std::cout<<"\n\t\t4. 64-bit";
                                                                std::cout<<"\n\t\t5. Other";
                                                                std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                                                std::cin>> lau;

                                                                        while(std::cin.fail())
                                                                        {
                                                                            system("cls");
                                                                           std::cout << "\n" "***********************************************************************************************************\n";
                                                                            std::cout << "\n\t\tERROR! This is not an integer: ";
                                                                             std::cin.clear();
                                                                            std::cin.ignore(256,'\n');
                                                                            std::cin >> lau;
                                                                        }

                                                                switch(lau)
                                                                {
                                                                case 1:
                                                                    CPU = "8";
                                                                    break;
                                                                case 2:
                                                                    CPU = "16";
                                                                    break;
                                                                case 3:
                                                                    CPU = "32";
                                                                    break;
                                                                case 4:
                                                                    CPU = "64";
                                                                    break;
                                                                case 5:
                                                                    system("cls");
                                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                                    cout << "\n\tEnter the bit number of your CPU(e.g., 4): "; cin >> CPU;
                                                                    break;
                                                                default :
                                                                    system("cls");
                                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                                    std::cout << "\tError! Wrong option selected." << std:: endl;
                                                                }
                                                        }while(lau != 1 && lau != 2 && lau != 3 && lau != 4 && lau != 5);

                                                    system("cls");
                                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                                    std::cout << "\n\tEnter processor speed or frequency (in MHz): ";
                                                    std::cin >> Clock_speed;

                                                    getOther_inputs();

                                                      string request_query = "insert into users_requests_ (Request_ID, Hardware_type, CPU, Clock_speed, Applic_Domain, Payload_size, Req_1, FM_1, RAM_1, Req_2, FM_2, RAM_2, Req_3, FM_3, RAM_3, Req_4, FM_4, RAM_4, Req_5, FM_5, RAM_5, Req_6, FM_6, RAM_6) values('"+Request_ID+"', '"+Hardware_type+"', '"+CPU+"', '"+Clock_speed+"', '"+Applic_Domain+"', '"+Payload_size+"', '"+Req_1+"', '"+FM_1+"', '"+RAM_1+"', '"+Req_2+"', '"+FM_2+"', '"+RAM_2+"', '"+Req_3+"', '"+FM_3+"', '"+RAM_3+"', '"+Req_4+"', '"+FM_4+"', '"+RAM_4+"', '"+Req_5+"', '"+FM_5+"', '"+RAM_5+"', '"+Req_6+"', '"+FM_6+"', '"+RAM_6+"')";

                                                      const char* qr = request_query.c_str();
                                                      qstate = mysql_query(conn, qr);

                                                        if(!qstate)
                                                        {
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                            std::cout << "\n\n\t\tData being saved .....\n";

                                                             Req_1.erase(); Req_2.erase(); Req_3.erase(); Req_4.erase(); Req_5.erase();

                                                            status.erase();
                                                            cout << endl << "\n\n\t\tRequest Successfully added in the database!" << endl;

                                                            cout << endl << "\n\n\t\tPress Enter to go back to the Main Menu." << endl;
                                                        }
                                                        else
                                                        {
                                                            cout << "\n\n\t Query Execution Problem! Error Number: " << mysql_errno(conn) << endl;
                                                            cout << "\n\n\tError Number 1062 implies that the entered Request ID already exist in database.\n" << endl;
                                                             cout << endl << "\n\n\tPlease press Enter to go back to the Main Menu and repeat the process with a unique ID." << endl;
                                                        }


                                                         REQST_id = Request_ID;
                                                        string request_query2 = "insert into requirements_for_report (REQST_id, Re_1, Re_2, Re_3, Re_4, Re_5, Re_6, Re_7, Re_8, Re_9, Re_10, Re_11, Re_12, Re_13, Re_14, Re_15) values('"+REQST_id+"', '"+Re_1+"', '"+Re_2+"', '"+Re_3+"', '"+Re_4+"', '"+Re_5+"', '"+Re_6+"', '"+Re_7+"', '"+Re_8+"', '"+Re_9+"', '"+Re_10+"', '"+Re_11+"', '"+Re_12+"', '"+Re_13+"', '"+Re_14+"', '"+Re_15+"')";

                                                        const char* qr2 = request_query2.c_str();
                                                        qstate = mysql_query(conn, qr2);

                                                        if(!qstate)
                                                        {
                                                            Re_1.erase(); Re_2.erase(); Re_3.erase(); Re_4.erase(); Reqmt_5.erase(); Re_6.erase(); Re_7.erase(); Re_8.erase(); Re_9.erase(); Re_10.erase(); Re_11.erase(); Re_12.erase(); Re_13.erase(); Re_14.erase(); Re_15.erase();
                                                        }
                                                        else
                                                        {

                                                        }

                                                      chrono::steady_clock::time_point end3 = chrono::steady_clock::now();

                                                    double elapsed_time3_ns = double(std::chrono::duration_cast <std::chrono::nanoseconds> (end3 -start3).count());
                                                    std::cout << "\n\n\t\tElapsed Time for Software Request (s): " << elapsed_time3_ns / 1e9 << std::endl;

                                        }
                                        else
                                        {
                                            goto level_;
                                        }
                                    break;
                                }
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level_;
						}
	}

	void UserInput::getUserInput()
	{
        Preliminary pre;

            int num_digits;
            int string_length;
           char first_letter;

           system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\t\t\t\tNEW REQUEST \n\n";
            string Hardware_type;
            std::cout << "\n\t\tYOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH AN "<< endl;
            std::cout <<"\t\tS OR H (if your Request is for Software or Hardware Implementation," << endl;
            std::cout <<"\t\t   respectively), FOLLOWED BY 4 INTEGERS (e.g., H1234 or S4567)" << endl;
            std::cout << "\n\t\t\t\tPlease enter your unique request ID: ";
            std::cin >> Request_ID;

            pre.convert_lowerC_to_upperC(Request_ID);

            auto collector = countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

            while(num_digits !=4 || string_length != 5 || (first_letter != 'S' && first_letter != 'H'))
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\tYOU NEED TO CHOOSE A UNIQUE REQUEST ID. THE ID SHOULD START WITH AN "<< endl;
                std::cout <<"\t\tS OR H (if your Request is for Software or Hardware Implementation," << endl;
                std::cout <<"\t\t   respectively), FOLLOWED BY 4 INTEGERS (e.g., H1234 or S4567)" << endl;
                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

		int implemtn_type = pre.determine_requestType(Request_ID);

        system("cls");
        switch(implemtn_type)
        {
            case 1:
                getInput_for_HardwareImplementaion();
                break;
            case 2:
                getInput_for_softwareImplementaion();
                break;
            default:
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                 std::cout << "\n\n\n\n\n\n\n\n\n\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n\n";
                 std::cout << "\n\tPress Enter to return to the Main Menu and try again.";
            break;
        }
    }

    void UserInput::modifyHardware_request()
    {
        string findbyRequestID_query = "select * from users_requests_2 where Request_ID like '%"+Request_ID+"%'";
		const char* qr = findbyRequestID_query.c_str();
		qstate = mysql_query(conn, qr);

        string type;
         system("cls");
         std::cout<<"\n" "***********************************************************************************************************\n";
		cout << endl << "\tShowing your requests ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
				cout << "\t\tRequest ID: " << row[0] << endl;
				cout << "\t\tHardware Type: " << row[1] << endl;
				cout << "\t\tApplication Area: " << row[2] << endl;
				cout << "\t\tPayload Size: " << row[3] << endl;
				cout << "\t\tEnergy: " << row[4] << endl;
                Req_1 = row[5]; Req_2 = row[8]; Req_3 = row[11]; Req_4 = row[14]; Req_5 = row[17]; Req_6 = row[20];
                string type2 = row[1];
                type = type2;

                cout << "\n\t  YOUR SECURITY REQUIREMENTS ARE:" << endl;
				if(!Req_1.empty())
                {
                    cout << "\t     Confidentiality " << endl;
                    cout << "\t       Estimated gate equivalents (GE)/number of slices for Confidentiality: " << row [6]<< endl;
                    cout << "\t       Desired throughput/Max. frequency for Confidentiality: " << row [7]<< endl;
                }
				if(!Req_2.empty())
                {
                   cout << "\t     Integrity " << endl;
                   cout << "\t       Estimated gate equivalents (GE)/number of slices for Integrity: " << row [9]<< endl;
                   cout << "\t       Desired throughput/Max. frequency for Integrity: " << row [10]<< endl;
                }
				if(!Req_3.empty())
                {
                    cout << "\t     Authentication " << endl;
                    cout << "\t       Estimated gate equivalents (GE)/number of slices for Authentication: " << row [12]<< endl;
                    cout << "\t       Desired throughput/Max. frequency for Authentication: " << row [13]<< endl;
                }
				if(!Req_4.empty())
                {
                    cout << "\t     Privacy " << endl;
                    cout << "\t       Estimated gate equivalents (GE)/number of slices for Privacy: " << row [15]<< endl;
                    cout << "\t       Desired throughput/Max. frequency for Privacy: " << row [16]<< endl;
                }

				if(!Req_5.empty())
                {
                   cout << "\t     Non-Repudiation " << endl;
                   cout << "\t       Estimated gate equivalents (GE)/number of slices for Non-Repudiation: " << row [18]<< endl;
                   cout << "\t       Desired throughput/Max. frequency for Non-Repudiation: " << row [19]<< endl;
                }

                if(!Req_6.empty())
                {
                   cout << "\t     Confidentiality & Authenticity " << endl;
                   cout << "\t       Estimated gate equivalents (GE)/No. of slices for Confidentiality & Authenticity: " << row [21]<< endl;
                   cout << "\t       Desired throughput/Max. frequency for Confidentiality & Authenticity: " << row [22]<< endl;
                }
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}

		string ID; char ch;
		cout << endl;
		cout << "\tDo you wish to modify your request? (y/n): "; cin >> ch;

		if(ch == 'y' || ch == 'Y')
		{

                string update_query;

                int choice;

                do{
                    system("cls");
                    std::cout<<"\n" "***********************************************************************************************************\n";
                    std::cout << "\n\tSelect specific inputs you want to update, one at a time: \n" << endl;


                    cout << "\t\t1. Hardware Type " << endl;
                    cout << "\t\t2. Application Area " << endl;
                    cout << "\t\t3. Payload Size " << endl;
                    cout << "\t\t4. Energy " << endl;
                    cout << "\t\t5. Add/Delete Confidentiality " << endl;
                    cout << "\t\t6. Add/Delete Integrity " << endl;
                    cout << "\t\t7. Add/Delete Authentication " << endl;
                    cout << "\t\t8. Add/Delete Privacy " << endl;
                    cout << "\t\t9. Add/Delete Non-Repudiation " << endl;
                    cout << "\t\t10. Add/Delete Confidentiality & Authenticity " << endl;
                    cout << "\t\t11. Done!" << endl << endl;

                    cout << "\tEnter the S/N of an input you want to update, and type 11 when done: "; cin >> choice;

                    Preliminary pre;

                    switch(choice)
                    {
                        case 1:
                                cin.ignore(); //
                                    system("cls");
                                    std::cout<<"\n" "***********************************************************************************************************\n";
                                    cout << "\n\tEnter new Hardware Type, FPGA or ASIC: ";
                                    getline(cin, Hardware_type);

                                    pre.convert_lowerC_to_upperC(Hardware_type);

                            update_query = "UPDATE `users_requests_2` SET `Hardware_type` = '"+Hardware_type+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                        case 2:
                               system("cls");
                               std::cout<<"\n" "***********************************************************************************************************\n";
                               cin.ignore();
                               std::cout << "\n\tType only the keyword in <> for the specific domain you want to update,";
                                std::cout << "\n\tor keyword of other domain: " << endl;
                                std::cout << "\n\t\t1) Smart <Home>";
                                std::cout << "\n\t\t2) Smart <City>";
                                std::cout << "\n\t\t3) Smart Agriculture";
                                std::cout << "\n\t\t4) Smart <Grid>";
                                std::cout << "\n\t\t5) Smart <Healthcare>";
                                std::cout << "\n\t\t6) Smart <Elderly> Monitoring";
                                std::cout << "\n\t\t7) Smart <Kid> Monitoring";
                                std::cout << "\n\t\t8) Smart <pet> Monitoring";
                                std::cout << "\n\t\t9) Smart Banking/<Financial> applications";
                                std::cout << "\n\t\t10) <Industrial> Automation";
                                std::cout << "\n\t\t11) Smart <Supply_Chain>";
                                std::cout << "\n\t\t12) Smart <Retail>";
                                std::cout << "\n\t\t13) Smart <Environmental> Monitoring";
                                std::cout << "\n\t\t14) Smart Automotive/<Transportation>";
                                std::cout << "\n\t\t15) <Connected_Car>";
                                std::cout << "\n\t\t16) Other Domain";
                                cout << endl << "\n\tType the keyword of your New Application area: "; getline(cin, Applic_Domain);
                            update_query = "UPDATE `users_requests_2` SET `Applic_Domain` = '"+Applic_Domain+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                         case 3:
                            cin.ignore();
                                system("cls");
                               std::cout << "\n   Enter the Payload Size (e.g., small or average): " << endl;
                                std::cout << "\n\t\t1) Small (1-128 bytes)";
                                std::cout << "\n\t\t2) Average (129-256 bytes)";
                                std::cout << "\n\t\t3) Large (> 256 bytes)";
                                std::cout << "\n\t\t4) Continuous";
                                std::cout << "\n\t\t5) Unknown\n";

                               do{
                                    cout << endl << "   Type your New Payload Size in lowercase characters (please ensure that there's no typo): "; getline(cin, Payload_size);
                               }while((Payload_size != "small") && (Payload_size != "average") && (Payload_size != "large") && (Payload_size != "continuous") && (Payload_size != "unknown"));

                            update_query = "UPDATE `users_requests_2` SET `Payload_size` = '"+Payload_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                            break;
                        case 4:
                                int choice2;
                            level2:
                           system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                             std::cout << "\n\tSelect desired energy performance: \n";

                                std::cout<<"\n\t\t1. Low Power";
                                std::cout<<"\n\t\t2. Ultra-low Power";
                                std::cout<<"\n\n\tSelect Your Option (1-2): ";
                                std::cin>>choice2;

                                switch(choice2)
                                {
                                case 1:
                                    Energy = "Low";
                                    break;
                                case 2:
                                    Energy = "Ultra_low";
                                    break;
                                default :
                                    std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                    goto level2;
                                    break;
                                }
                            update_query = "UPDATE `users_requests_2` SET `Energy` = '"+Energy+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                         case 5:
                               cin.ignore();
                               if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER CONF TO PROCEED \n\n";
                                            cout << endl << "\tType <CONF or ' '> to Add or Delete Confidentiality: "; getline(cin, Req_1);
                                       }while(Req_1 != "CONF" && Req_1 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Confidentiality: "; getline(cin, cct_area_1);
                                       }while(cin.fail() && cct_area_1 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Confidentiality: "; getline(cin, tp_1);
                                       }while(cin.fail() && tp_1 != "' '");
                               }
                               else if(type == "ASIC")
                               {
                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <CONF or ' '> to Add or Delete Confidentiality: "; getline(cin, Req_1);
                                       }while(Req_1 != "CONF" && Req_1 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                            cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                            cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                            cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                            cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                            cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                            cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                            cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Confidentiality: "; getline(cin, cct_area_1);
                                       }while(cin.fail() && cct_area_1 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                            cout << "\t\t810 - 970 \t\t 4.2 - 5.1\n";
                                            cout << "\t\t971 - 1110 \t\t 3.4 - 16.3\n";
                                            cout << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n";
                                            cout << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n";
                                            cout << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n";
                                            cout << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n";
                                            cout << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Confidentiality: "; getline(cin, tp_1);
                                       }while(cin.fail() && tp_1 != "' '");
                               }
                            update_query = "UPDATE `users_requests_2` SET `Req_1` = '"+Req_1+"', `cct_area_1` = '"+cct_area_1+"', `tp_1` = '"+tp_1+"' WHERE `Request_ID` = '"+Request_ID+"'";//This is how to update multiple columns in mysql table at the same time.
                        break;
                         case 6:
                               cin.ignore();
                               if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER INTG TO PROCEED \n\n";
                                            cout << endl << "\tType <INTG or ' '> to Add or Delete Integrity: "; getline(cin, Req_2);
                                       }while((Req_2 != "INTG") && Req_2 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Integrity: "; getline(cin, cct_area_2);
                                       }while(cin.fail() && cct_area_2 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Integrity: "; getline(cin, tp_2);
                                       }while(cin.fail() && tp_2 != "' '");
                               }
                               else if(type == "ASIC")
                               {

                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <INTG or ' '> to Add or Delete Integrity: "; getline(cin, Req_2);
                                       }while((Req_2 != "INTG") && Req_2 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                            cout << "\t\t738 - 864 \t\t 0.8 - 1.0\n";
                                            cout << "\t\t865 - 1060 \t\t 0.3 - 2.8\n";
                                            cout << "\t\t1061 - 1127 \t\t 0.5 - 17.8\n";
                                            cout << "\t\t1128 - 1396 \t\t 1.0 - 2.7\n";
                                            cout << "\t\t1397 - 2190 \t\t 2.7 - 17.8\n";
                                            cout << "\t\t2191 - 4362 \t\t 0.4 - 50.0\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Integrity: "; getline(cin, cct_area_2);
                                       }while(cin.fail() && cct_area_2 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n";
                                            cout << "\t\t738 - 864 \t\t 0.8 - 1.0\n";
                                            cout << "\t\t865 - 1060 \t\t 0.3 - 2.8\n";
                                            cout << "\t\t1061 - 1127 \t\t 0.5 - 17.8\n";
                                            cout << "\t\t1128 - 1396 \t\t 1.0 - 2.7\n";
                                            cout << "\t\t1397 - 2190 \t\t 2.7 - 17.8\n";
                                            cout << "\t\t2191 - 4362 \t\t 0.4 - 50.0\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Integrity: "; getline(cin, tp_2);
                                       }while(cin.fail() && tp_2 != "' '");
                               }
                        update_query = "UPDATE `users_requests_2` SET `Req_2` = '"+Req_2+"', `cct_area_2` = '"+cct_area_2+"', `tp_2` = '"+tp_2+"' WHERE `Request_ID` = '"+Request_ID+"'"; //This is how to update multiple columns in mysql table at the same time.
                        break;
                         case 7:
                              cin.ignore();
                              if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER AUTH TO PROCEED \n\n";
                                            cout << endl << "\tType <AUTH or ' '> to Add or Delete Authentication: "; getline(cin, Req_3);
                                       }while((Req_3 != "AUTH") && Req_3 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Authentication: "; getline(cin, cct_area_3);
                                       }while(cin.fail() && cct_area_3 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Authentication: "; getline(cin, tp_3);
                                       }while(cin.fail() && tp_3 != "' '");
                               }
                               else if(type == "ASIC")
                               {

                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER AUTH TO PROCEED \n\n";
                                            cout << endl << "\tType <AUTH or ' '> to Add or Delete Authentication: "; getline(cin, Req_3);
                                       }while((Req_3 != "AUTH") && Req_3 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Authentication: "; getline(cin, cct_area_3);
                                       }while(cin.fail() && cct_area_3 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Authentication: "; getline(cin, tp_3);
                                       }while(cin.fail() && tp_3 != "' '");
                               }
                            update_query = "UPDATE `users_requests_2` SET `Req_3` = '"+Req_3+"', `cct_area_3` = '"+cct_area_3+"', `tp_3` = '"+tp_3+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                         case 8:
                            cin.ignore();
                            if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER PRIV TO PROCEED \n\n";
                                            cout << endl << "\tType <PRIV or ' '> to Add or Delete Privacy: "; getline(cin, Req_4);
                                       }while(Req_4 != "PRIV" && Req_4 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Privacy: "; getline(cin, cct_area_4);
                                       }while(cin.fail() && cct_area_4 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Privacy: "; getline(cin, tp_4);
                                       }while(cin.fail() && tp_4 != "' '");
                               }
                               else if(type == "ASIC")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <PRIV or ' '> to Add or Delete Privacy: "; getline(cin, Req_4);
                                       }while(Req_4 != "PRIV" && Req_4 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n"
                                            << "\t\t810 - 970 \t\t 4.2 - 5.1\n"
                                            << "\t\t971 - 1110 \t\t 3.4 - 16.3\n"
                                            << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n"
                                            << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n"
                                            << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n"
                                            << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n"
                                            << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Privacy: "; getline(cin, cct_area_4);
                                       }while(cin.fail() && cct_area_4 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n"
                                            << "\t\t810 - 970 \t\t 4.2 - 5.1\n"
                                            << "\t\t971 - 1110 \t\t 3.4 - 16.3\n"
                                            << "\t\t1111 - 1400 \t\t 3.0 - 12.1\n"
                                            << "\t\t1401 - 1570 \t\t 177.8 - 237.0\n"
                                            << "\t\t1571 - 1799 \t\t 2.6 - 200.0\n"
                                            << "\t\t1800 - 2500 \t\t 2.8 - 193.9\n"
                                            << "\t\t2501 - 8600 \t\t 133.3 - 6400.1\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Privacy: "; getline(cin, tp_4);
                                       }while(cin.fail() && tp_4 != "' '");
                               }
                            update_query = "UPDATE `users_requests_2` SET `Req_4` = '"+Req_4+"', `cct_area_4` = '"+cct_area_4+"', `tp_4` = '"+tp_4+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                         case 9:
                              cin.ignore();
                              if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER NONR TO PROCEED \n\n";
                                            cout << endl << "\tType <NONR or ' '> to Add or Delete Non-Repudiation: "; getline(cin, Req_5);
                                       }while((Req_5 != "NONR") && Req_5 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Non-Repudiation: "; getline(cin, cct_area_5);
                                       }while(cin.fail() && cct_area_5 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Non-Repudiation: "; getline(cin, tp_5);
                                       }while(cin.fail() && tp_5 != "' '");
                               }
                               else if(type == "ASIC")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t\t\tBUT ENTER NONR TO PROCEED \n\n";
                                            cout << endl << "\tType <NONR or ' '> to Add or Delete Non-Repudiation: "; getline(cin, Req_5);
                                       }while((Req_5 != "NONR") && Req_5 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Non-Repudiation: "; getline(cin, cct_area_5);
                                       }while(cin.fail() && cct_area_5 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n   RIGHT NOW THERE IS NO SUITABLE ALGORITHM THAT HAS UNDERGONE A SUFFICIENT NUMBER OF EVALUATIONS \n";
                                            cout << "\n\t\t\t     JUST ENTER ANY NUMBER TO PROCEED \n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Non-Repudiation: "; getline(cin, tp_5);
                                       }while(cin.fail() && tp_5 != "' '");
                               }
                            update_query = "UPDATE `users_requests_2` SET `Req_5` = '"+Req_5+"', `cct_area_5` = '"+cct_area_5+"', `tp_5` = '"+tp_5+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                        case 10:
                              cin.ignore();
                              if(type == "FPGA")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <COAU or ' '> to Add or Delete Confidentiality & Authenticity: "; getline(cin, Req_6);
                                       }while((Req_6 != "COAU") && Req_6 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t No. of Slices (The lower the better)\tMax Operating Freq. (The higher the better) \n"
                                            << "\t\t135 - 412.9 \t\t\t 1.0 - 389.0\n"
                                            << "\t\t413 - 890.9 \t\t\t 1.0 - 347.0\n"
                                            << "\t\t891 - 1347.9 \t\t\t 1.0 - 280.9\n"
                                            << "\t\t1348 - 4500 \t\t\t 1.0 - 256.9\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete number of slices for Confidentiality & Authenticity: "; getline(cin, cct_area_6);
                                       }while(cin.fail() && cct_area_6 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                             cout << "\n\t No. of Slices (The lower the better)\tMax Operating Freq. (The higher the better) \n"
                                            << "\t\t135 - 412.9 \t\t\t 1.0 - 389.0\n"
                                            << "\t\t413 - 890.9 \t\t\t 1.0 - 347.0\n"
                                            << "\t\t891 - 1347.9 \t\t\t 1.0 - 280.9\n"
                                            << "\t\t1348 - 4500 \t\t\t 1.0 - 256.9\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete max freq. for Confidentiality & Authenticity: "; getline(cin, tp_6);
                                       }while(cin.fail() && tp_6 != "' '");
                               }
                               else if(type == "ASIC")
                               {
                                       do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tType <NONR or ' '> to Add or Delete Confidentiality & Authenticity: "; getline(cin, Req_6);
                                       }while((Req_6 != "COAU") && Req_6 != "' '");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n"
                                            << "\t\t2860 - 3099 \t\t 1.0 - 5.0\n"
                                            << "\t\t3100 - 5999 \t\t 1.0 - 6.0\n"
                                            << "\t\t6000 - 7949 \t\t 1.0 - 5.3\n"
                                            << "\t\t7950 - 9000 \t\t 1.0 - 5.5\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete GE for Confidentiality & Authenticity: "; getline(cin, cct_area_6);
                                       }while(cin.fail() && cct_area_6 != "' ' ");

                                    do{
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << "\n\t GE (The lower the better)\tThroughput (The higher the better) \n"
                                            << "\t\t2860 - 3099 \t\t 1.0 - 5.0\n"
                                            << "\t\t3100 - 5999 \t\t 1.0 - 6.0\n"
                                            << "\t\t6000 - 7949 \t\t 1.0 - 5.3\n"
                                            << "\t\t7950 - 9000 \t\t 1.0 - 5.5\n\n";
                                            cout << endl << "\tEnter new value or ' ' to Modify or Delete throughput for Confidentiality & Authenticity: "; getline(cin, tp_6);
                                       }while(cin.fail() && tp_6 != "' '");
                               }
                            update_query = "UPDATE `users_requests_2` SET `Req_6` = '"+Req_6+"', `cct_area_6` = '"+cct_area_6+"', `tp_6` = '"+tp_6+"' WHERE `Request_ID` = '"+Request_ID+"'";
                        break;
                         case 11:
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                               std::cout << endl << "\n\t\t\t Done!" << endl;
                           break;

                        default:
                                cout << "Please choose a correct number" << endl;
                    }
                    const char* qm = update_query.c_str();
                    qstate = mysql_query(conn, qm);

                    if(!qstate)
                    {
                        cout << endl << "\t\t\t Database successfully updated! \n";
                        cout << "\n\n\t\t\t Press Enter to return to the Admin Menu. ";
                    }
                    else
                    {
                        cout << "\tQuery Execution Problem!: " << mysql_errno(conn) << endl;
                    }
            }while(choice != 11);
        }
		else
		{
			system("cls");
			std::cout<<"\n" "***********************************************************************************************************\n";
			std::cout << "\n\tPress Enter to return to the Main Menu. ";
			return;
		}
    }

    void UserInput::modifySoftware_request()
    {
         level_:
             int state = 0;
        char ch;
        system("cls");
        std::cout<<"\n" "***********************************************************************************************************\n";
        std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system? \n";

                        std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                        std::cout<<"\n\t\t2. Existing System ";
                        std::cout<<"\n\n\tSelect Your Option (1-2): ";

						std::cin>>ch;

						switch(ch)
						{
						case '1':
						     {
                                    state = 1;

                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                     cout << "\t\t\t\t\tSYSTEM DEVELOPMENT PHASE\n" << endl;
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                    {
                                        status = "new";
                                        string findbyRequestID_query = "select * from users_requests where Request_ID like '%"+Request_ID+"%'";
                                        const char* qr = findbyRequestID_query.c_str();
                                        qstate = mysql_query(conn, qr);

                                         system("cls");
                                         std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tShowing your requests ...." << endl << endl;
                                        if(!qstate)
                                        {
                                            res = mysql_store_result(conn);
                                            while((row = mysql_fetch_row(res)))
                                            {
                                                cout << "\t\tRequest ID: " << row[0] << endl;
                                                cout << "\t\tHardware Type: " << row[1] << endl;
                                                cout << "\t\tCPU Type: " << row[2] << endl;
                                                cout << "\t\tFlash Memory Size: " << row[3] << endl;
                                                cout << "\t\tRam Size: " << row[4] << endl;
                                                cout << "\t\tClock Speed: " << row[5] << endl;
                                                cout << "\t\tApplication Area: " << row[6] << endl;
                                                cout << "\t\tPayload Size: " << row[7] << endl;
                                                Req_1 = row[8];Req_2 = row[9];Req_3 = row[10];Req_4 = row[11];Req_5 = row[12];Req_6 = row[13];

                                                cout << "\n\t\tYOUR SECURITY REQUIREMENTS ARE:" << endl;
                                                if(!Req_1.empty())
                                                cout << "\t\t  Confidentiality " << endl;
                                                if(!Req_2.empty())
                                                cout << "\t\t  Integrity " << endl;
                                                if(!Req_3.empty())
                                                cout << "\t\t  Authentication " << endl;
                                                if(!Req_4.empty())
                                                cout << "\t\t  Privacy " << endl;
                                                if(!Req_5.empty())
                                                cout << "\t\t  Non-Repudiation " << endl;
                                                if(!Req_6.empty())
                                                cout << "\t\t  Confidentiality & Authenticity " << endl;
                                            }
                                        }
                                        else
                                        {
                                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                                        }

                                    }
                                    else
                                    {
                                        goto level_;
                                    }
                                    break;
                                }
                        case '2':
                            {
                                    state = 2;

                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tEXISTING SYSTEM\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                    {
                                        status = "old";
                                        string findbyRequestID_query = "select * from users_requests_ where Request_ID like '%"+Request_ID+"%'";
                                        const char* qr = findbyRequestID_query.c_str();
                                        qstate = mysql_query(conn, qr);

                                         system("cls");
                                         std::cout<<"\n" "***********************************************************************************************************\n";
                                        cout << endl << "\tShowing your requests ...." << endl << endl;
                                        if(!qstate)
                                        {
                                            res = mysql_store_result(conn);
                                            while((row = mysql_fetch_row(res)))
                                            {
                                                cout << "\t\tRequest ID: " << row[0] << endl;
                                                cout << "\t\tHardware Type: " << row[1] << endl;
                                                cout << "\t\tCPU Type: " << row[2] << endl;
                                                cout << "\t\tClock Speed: " << row[3] << endl;
                                                cout << "\t\tApplication Area: " << row[4] << endl;
                                                cout << "\t\tPayload Size: " << row[5] << endl;
                                                Req_1 = row[6]; FM_1 = row[7]; RAM_1 = row[8]; Req_2 = row[9]; FM_2 = row[10]; RAM_2 = row[11]; Req_3 = row[12]; FM_3 = row[13]; RAM_3 = row[14]; Req_4 = row[15]; FM_4 = row[16]; RAM_4 = row[17]; Req_5 = row[18]; FM_5 = row[19]; RAM_5 = row[20]; Req_6 = row[21]; FM_6 = row[22]; RAM_6 = row[23];
                                                double FM1 = atof(FM_1.c_str()); double RAM1 = atof(RAM_1.c_str()); double FM2 = atof(FM_2.c_str()); double RAM2 = atof(RAM_2.c_str());
                                                double FM3 = atof(FM_3.c_str()); double RAM3 = atof(RAM_3.c_str()); double FM4 = atof(FM_4.c_str()); double RAM4 = atof(RAM_4.c_str());
                                                double FM5 = atof(FM_5.c_str()); double RAM5 = atof(RAM_5.c_str()); double FM6 = atof(FM_6.c_str()); double RAM6 = atof(RAM_6.c_str());

                                                cout << "\n\t\tYOUR SECURITY REQUIREMENTS ARE:" << endl;
                                                if(!Req_1.empty())
                                                cout << "\t\t  Confidentiality " << endl;
                                                if(FM1 != 0.0)
                                                cout << "\t\t   Available flash memory space for confidentiality: " << FM_1 << endl;
                                                if(RAM1 != 0.0)
                                                cout << "\t\t   Available RAM for confidentiality: " << RAM_1 << endl;
                                                if(!Req_2.empty())
                                                cout << "\t\t  Integrity " << endl;
                                                if(FM2 != 0.0)
                                                cout << "\t\t   Available flash memory space for integrity: " << FM_2 << endl;
                                                if(RAM2 != 0.0)
                                                cout << "\t\t   Available RAM for integrity: " << RAM_2 << endl;
                                                if(!Req_3.empty())
                                                cout << "\t\t  Authentication " << endl;
                                                if(FM3 != 0.0)
                                                cout << "\t\t   Available flash memory space for authentication: " << FM_3 << endl;
                                                if(RAM3 != 0.0)
                                                cout << "\t\t   Available RAM for authentication: " << RAM_3 << endl;
                                                if(!Req_4.empty())
                                                cout << "\t\t  Privacy " << endl;
                                                if(FM4 != 0.0)
                                                cout << "\t\t   Available flash memory space for privacy: " << FM_4 << endl;
                                                if(RAM4 != 0.0)
                                                cout << "\t\t   Available RAM for privacy: " << RAM_4 << endl;
                                                if(!Req_5.empty())
                                                cout << "\t\t  Non-Repudiation " << endl;
                                                if(FM5 != 0.0)
                                                cout << "\t\t   Available flash memory space for non-repudiation: " << FM_5 << endl;
                                                if(RAM5 != 0.0)
                                                cout << "\t\t   Available RAM for non-repudiation: " << RAM_5 << endl;
                                                if(!Req_6.empty())
                                                cout << "\t\t  Confidentiality & Authenticity " << endl;
                                                if(FM6 != 0.0)
                                                cout << "\t\t   Available flash memory space for confidentiality & authenticity: " << FM_6 << endl;
                                                if(RAM6 != 0.0)
                                                cout << "\t\t   Available RAM for confidentiality & authenticity: " << RAM_6 << endl;
                                            }
                                        }
                                        else
                                        {
                                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                                        }

                                    }
                                    else
                                    {
                                        goto level_;
                                    }
                                    break;
                                }
						default:
							std::cout << "\tSorry! Wrong option selected." << std:: endl;
                        goto level_;
						}

		string ID; char chi;
		cout << endl;
		launi:
		cout << "\tDo you wish to modify your request? (y/n): "; cin >> chi;
            if(state == 1)
            {
                if(chi == 'y' || chi == 'Y')
                {
                        string update_query;

                        int choice;

                        do{
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tSelect specific inputs you want to update, one at a time: \n" << endl;

                                cout << "\t\t1. Hardware Type " << endl;
                                cout << "\t\t2. CPU Type " << endl;
                                cout << "\t\t3. Flash Memory Size " << endl;
                                cout << "\t\t4. Ram Size " << endl;
                                cout << "\t\t5. Clock Speed " << endl;
                                cout << "\t\t6. Application Area " << endl;
                                cout << "\t\t7. Payload Size " << endl;
                                cout << "\t\t8. Add/Delete Confidentiality " << endl;
                                cout << "\t\t9. Add/Delete Integrity " << endl;
                                cout << "\t\t10. Add/Delete Authentication " << endl;
                                cout << "\t\t11. Add/Delete Privacy " << endl;
                                cout << "\t\t12. Add/Delete Non-Repudiation " << endl;
                                cout << "\t\t13. Add/Delete Confidentiality & Authenticity " << endl;
                                cout << "\t\t14. Done!" << endl << endl;

                                cout << "\tEnter the S/N of an input you want to update, and type 14 when done:  "; cin >> choice;

                                Preliminary pre;

                                switch(choice)
                                {
                                    case 1:
                                            cin.ignore(); //
                                        do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << "\n\tEnter Hardware Type (Microntroller-based or Single Board Computer) [MCU or SBC]: ";
                                                getline(cin, Hardware_type);

                                                pre.convert_lowerC_to_upperC(Hardware_type);

                                                if(Hardware_type == "MCU")
                                                {
                                                     char choice;
                                                     level:
                                                system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";

                                                     std::cout << "\n\tSelect your Microntroller Type: \n";

                                                    std::cout<<"\n\t\t1. AVR (8 or 32-bit RISC CPU) ";
                                                    std::cout<<"\n\t\t2. MSP (16-bit RISC CPU)";
                                                    std::cout<<"\n\t\t3. ARM (32 or 64-bit RISC CPU)";
                                                    std::cout<<"\n\t\t4. PIC (8, 16 or 32-bit RISC CPU)";
                                                    std::cout<<"\n\t\t5. Other";
                                                    std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                                        std::cin>>choice;

                                                        switch(choice)
                                                        {
                                                        case '1':
                                                            Hardware_type = "AVR";
                                                            break;
                                                        case '2':
                                                            Hardware_type = "MSP";
                                                            break;
                                                        case '3':
                                                            Hardware_type = "ARM";
                                                            break;
                                                        case '4':
                                                            Hardware_type = "PIC";
                                                            break;
                                                        case '5':
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                            cout << "\n\tEnter your MCU brand name (< or = 6 characters): "; cin >> Hardware_type;
                                                            pre.convert_lowerC_to_upperC(Hardware_type);
                                                            break;
                                                        default :
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                            goto level;
                                                        }
                                                    break;
                                                }

                                            }while(((Hardware_type != "SBC") && (Hardware_type != "MCU")));

                                        update_query = "UPDATE `users_requests` SET `Hardware_type` = '"+Hardware_type+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                    case 2:
                                       char choice;
                                        level2:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                         std::cout << "\n\t\tSelect your CPU Type: ";

                                            std::cout<<"\n\t\t1. 8-bit";
                                            std::cout<<"\n\t\t2. 16-bit";
                                            std::cout<<"\n\t\t3. 32-bit";
                                            std::cout<<"\n\t\t4. 64-bit";
                                            std::cout<<"\n\t\t5. Other";
                                            std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                            std::cin>>choice;

                                            switch(choice)
                                            {
                                            case '1':
                                                CPU = "8";
                                                break;
                                            case '2':
                                                CPU = "16";
                                                break;
                                            case '3':
                                                CPU = "32";
                                                break;
                                            case '4':
                                                CPU = "64";
                                                break;
                                            case '5':
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << "\n\tEnter the bit number of your CPU(e.g., 4): "; cin >> CPU;
                                                break;
                                            default :
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto level2;
                                                break;
                                            }


                                       update_query = "UPDATE `users_requests` SET `CPU` = '"+CPU+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                       break;
                                     case 3:
                                            cin.ignore();
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tEnter New Flash Memory Size: "; getline(cin, FlashMem_size);
                                        update_query = "UPDATE `users_requests` SET `FlashMem_size` = '"+FlashMem_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                    case 4:
                                           cin.ignore();
                                           system("cls");
                                           std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tEnter New Ram Size: "; getline(cin, Ram_size);
                                        update_query = "UPDATE `users_requests` SET `Ram_size` = '"+Ram_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 5:
                                            cin.ignore();
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tEnter New Clock Speed: "; getline(cin, Clock_speed);
                                        update_query = "UPDATE `users_requests` SET `Clock_speed` = '"+Clock_speed+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 6:
                                           cin.ignore();
                                           system("cls");
                                           std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << "\n\tType only keyword in <> for the specific domain you want to update, or keyword of other domain: " << endl;
                                            std::cout << "\n\t\t1) Smart <Home>";
                                            std::cout << "\n\t\t2) Smart <City>";
                                            std::cout << "\n\t\t3) Smart Agriculture";
                                            std::cout << "\n\t\t4) Smart <Grid>";
                                            std::cout << "\n\t\t5) Smart <Healthcare>";
                                            std::cout << "\n\t\t6) Smart <Elderly> Monitoring";
                                            std::cout << "\n\t\t7) Smart <Kid> Monitoring";
                                            std::cout << "\n\t\t8) Smart <pet> Monitoring";
                                            std::cout << "\n\t\t9) Smart Banking/<Financial> applications";
                                            std::cout << "\n\t\t10) <Industrial> Automation";
                                            std::cout << "\n\t\t11) Smart <Supply_Chain>";
                                            std::cout << "\n\t\t12) Smart <Retail>";
                                            std::cout << "\n\t\t13) Smart <Environmental> Monitoring";
                                            std::cout << "\n\t\t14) Smart Automotive/<Transportation>";
                                            std::cout << "\n\t\t15) <Connected_Car>";
                                            std::cout << "\n\t\t16) Other Domain";
                                            cout << endl << "\n\tType the keyword of your New Application area: "; getline(cin, Applic_Domain);
                                        update_query = "UPDATE `users_requests` SET `Applic_Domain` = '"+Applic_Domain+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 7:
                                        cin.ignore();
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << "\n\tEnter the Payload Size (e.g., small or average): " << endl;
                                            std::cout << "\n\t\t1) Small (1-128 bytes)";
                                            std::cout << "\n\t\t2) Average (129-256 bytes)";
                                            std::cout << "\n\t\t3) Large (> 256 bytes)";
                                            std::cout << "\n\t\t4) Continuous";
                                            std::cout << "\n\t\t5) Unknown";

                                           do{
                                                cout << endl << "\n\tType your New Payload Size in lowercase characters (please ensure that there's no typo): "; getline(cin, Payload_size);
                                           }while((Payload_size != "small") && (Payload_size != "average") && (Payload_size != "large") && (Payload_size != "continuous") && (Payload_size != "unknown"));

                                        update_query = "UPDATE `users_requests` SET `Payload_size` = '"+Payload_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                        break;
                                     case 8:
                                           cin.ignore();
                                           do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <CONF or ' '> to Add or Delete Confidentiality: "; getline(cin, Req_1);
                                           }while((Req_1 != "CONF") && Req_1 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_1` = '"+Req_1+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 9:
                                           cin.ignore();
                                           do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <INTG or ' '> to Add or Delete Integrity: "; getline(cin, Req_2);
                                           }while((Req_2 != "INTG") && Req_2 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_2` = '"+Req_2+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 10:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <AUTH or ' '> to Add or Delete Authentication: "; getline(cin, Req_3);
                                           }while((Req_3 != "AUTH") && Req_3 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_3` = '"+Req_3+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 11:
                                        cin.ignore();
                                        do{
                                              system("cls");
                                              std::cout<<"\n" "***********************************************************************************************************\n";
                                              cout << endl << "\tType <PRIV or ' '> to Add or Delete Privacy: "; getline(cin, Req_4);
                                           }while((Req_4 != "PRIV") && Req_4 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_4` = '"+Req_4+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 12:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <NONR or ' '> to Add or Delete Non-Repudiation: "; getline(cin, Req_5);
                                           }while((Req_5 != "NONR") && Req_5 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_5` = '"+Req_5+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                    case 13:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <COAU or ' '> to Add or Delete Confidentiality & Authenticity: "; getline(cin, Req_6);
                                           }while((Req_6 != "COAU") && Req_6 != "' '");
                                        update_query = "UPDATE `users_requests` SET `Req_6` = '"+Req_6+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 14:
                                           system("cls");
                                           std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << endl << "\n\t\t\t Done!" << endl;
                                            break;

                                    default:
                                            cout << "Please choose a correct number" << endl;
                                }
                                const char* qm = update_query.c_str();
                                qstate = mysql_query(conn, qm);

                                if(!qstate)
                                {
                                    cout << endl << "\t\t\t Database successfully updated." << endl;
                                    cout << "\n\n\t\t\t Press Enter to return to the Admin Menu. ";
                                }
                                else
                                {
                                    cout << "\tQuery Execution Problem!" << mysql_errno(conn) << endl;
                                }
                        }while(choice != 14);
                    }
                    else
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        std::cout << "\n\tPress Enter to return to the Main Menu. ";
                        return;
                    }
            }
            else if(state == 2)
            {
                if(chi == 'y' || chi == 'Y')
                    {


                        string update_query;

                        int choice;

                        do{
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tSelect specific inputs you want to update, one at a time: \n" << endl;

                                cout << "\t\t1. Hardware Type " << endl;
                                cout << "\t\t2. CPU Type " << endl;
                                cout << "\t\t3. Clock Speed " << endl;
                                cout << "\t\t4. Application Area " << endl;
                                cout << "\t\t5. Payload Size " << endl;
                                cout << "\t\t6. Add/Delete Confidentiality " << endl;
                                cout << "\t\t7. Add/Delete Integrity " << endl;
                                cout << "\t\t8. Add/Delete Authentication " << endl;
                                cout << "\t\t9. Add/Delete Privacy " << endl;
                                cout << "\t\t10. Add/Delete Non-Repudiation " << endl;
                                cout << "\t\t11. Add/Delete Confidentiality & Authenticity " << endl;
                                cout << "\t\t12. Done!" << endl << endl;

                                cout << "\tEnter the S/N of an input you want to update, and type 12 when done:  "; cin >> choice;

                                Preliminary pre;

                                switch(choice)
                                {
                                    case 1:
                                            cin.ignore(); //
                                        do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << "\n\tEnter Hardware Type (Microntroller-based or Single Board Computer) [MCU or SBC]: ";
                                                getline(cin, Hardware_type);

                                                pre.convert_lowerC_to_upperC(Hardware_type);

                                                if(Hardware_type == "MCU")
                                                {

                                                      char choice;
                                                    lev:
                                                system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";

                                                     std::cout << "\n\tSelect your Microntroller Type: \n";

                                                    std::cout<<"\n\t\t1. AVR (8 or 32-bit RISC CPU) ";
                                                    std::cout<<"\n\t\t2. MSP (16-bit RISC CPU)";
                                                    std::cout<<"\n\t\t3. ARM (32 or 64-bit RISC CPU)";
                                                    std::cout<<"\n\t\t4. Other";
                                                    std::cout<<"\n\n\tSelect Your Option (1-4): ";
                                                        std::cin>>choice;

                                                        switch(choice)
                                                        {
                                                        case '1':
                                                            Hardware_type = "AVR";
                                                            break;
                                                        case '2':
                                                            Hardware_type = "MSP";
                                                            break;
                                                        case '3':
                                                            Hardware_type = "ARM";
                                                            break;
                                                        case '4':
                                                            system("cls");
                                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                                            cout << "\n\tEnter your MCU brand name (< or = 6 characters): "; cin >> Hardware_type;
                                                            pre.convert_lowerC_to_upperC(Hardware_type);
                                                            break;
                                                        default :
                                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                            goto lev;

                                                        }
                                                    break;
                                                }

                                            }while(((Hardware_type != "SBC") && (Hardware_type != "MCU")));

                                        update_query = "UPDATE `users_requests_` SET `Hardware_type` = '"+Hardware_type+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                    case 2:
                                       char choice;
                                        logo:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                         std::cout << "\n\t\tSelect your CPU Type: ";

                                            std::cout<<"\n\t\t1. 8-bit";
                                            std::cout<<"\n\t\t2. 16-bit";
                                            std::cout<<"\n\t\t3. 32-bit";
                                            std::cout<<"\n\t\t4. 64-bit";
                                            std::cout<<"\n\t\t5. Other";
                                            std::cout<<"\n\n\tSelect Your Option (1-5): ";
                                            std::cin>>choice;

                                            switch(choice)
                                            {
                                            case '1':
                                                CPU = "8";
                                                break;
                                            case '2':
                                                CPU = "16";
                                                break;
                                            case '3':
                                                CPU = "32";
                                                break;
                                            case '4':
                                                CPU = "64";
                                                break;
                                            case '5':
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << "\n\tEnter the bit number of your CPU(e.g., 4): "; cin >> CPU;
                                                break;
                                            default :
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                                goto logo;
                                                break;
                                            }
                                       update_query = "UPDATE `users_requests_` SET `CPU` = '"+CPU+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                       break;
                                     case 3:
                                            cin.ignore();
                                            system("cls");
                                            std::cout<<"\n" "***********************************************************************************************************\n";
                                            cout << endl << "\tEnter New Clock Speed: "; getline(cin, Clock_speed);
                                        update_query = "UPDATE `users_requests_` SET `Clock_speed` = '"+Clock_speed+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 4:
                                           cin.ignore();
                                           system("cls");
                                           std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << "\n\tType only keyword in <> for the specific domain you want to update, or keyword of other domain: " << endl;
                                            std::cout << "\n\t\t1) Smart <Home>";
                                            std::cout << "\n\t\t2) Smart <City>";
                                            std::cout << "\n\t\t3) Smart Agriculture";
                                            std::cout << "\n\t\t4) Smart <Grid>";
                                            std::cout << "\n\t\t5) Smart <Healthcare>";
                                            std::cout << "\n\t\t6) Smart <Elderly> Monitoring";
                                            std::cout << "\n\t\t7) Smart <Kid> Monitoring";
                                            std::cout << "\n\t\t8) Smart <pet> Monitoring";
                                            std::cout << "\n\t\t9) Smart Banking/<Financial> applications";
                                            std::cout << "\n\t\t10) <Industrial> Automation";
                                            std::cout << "\n\t\t11) Smart <Supply_Chain>";
                                            std::cout << "\n\t\t12) Smart <Retail>";
                                            std::cout << "\n\t\t13) Smart <Environmental> Monitoring";
                                            std::cout << "\n\t\t14) Smart Automotive/<Transportation>";
                                            std::cout << "\n\t\t15) <Connected_Car>";
                                            std::cout << "\n\t\t16) Other Domain";
                                            cout << endl << "\n\tType the keyword of your New Application area: "; getline(cin, Applic_Domain);
                                        update_query = "UPDATE `users_requests_` SET `Applic_Domain` = '"+Applic_Domain+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 5:
                                        cin.ignore();
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << "\n\tEnter the Payload Size (e.g., small or average): " << endl;
                                            std::cout << "\n\t\t1) Small (1-128 bytes)";
                                            std::cout << "\n\t\t2) Average (129-256 bytes)";
                                            std::cout << "\n\t\t3) Large (> 256 bytes)";
                                            std::cout << "\n\t\t4) Continuous";
                                            std::cout << "\n\t\t5) Unknown";

                                           do{
                                                cout << endl << "\n\tType your New Payload Size in lowercase characters (please ensure that there's no typo): "; getline(cin, Payload_size);
                                           }while((Payload_size != "small") && (Payload_size != "average") && (Payload_size != "large") && (Payload_size != "continuous") && (Payload_size != "unknown"));

                                        update_query = "UPDATE `users_requests_` SET `Payload_size` = '"+Payload_size+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                        break;
                                     case 6:
                                           cin.ignore();
                                           do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <CONF or ' '> to Add or Delete Confidentiality: "; getline(cin, Req_1);
                                           }while((Req_1 != "CONF") && Req_1 != "' '");
                                        update_query = "UPDATE `users_requests_` SET `Req_1` = '"+Req_1+"' WHERE `Request_ID` = '"+Request_ID+"'";

                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "  Enter new a value or ' ' to Modify or Delete available flash memory space for confidentiality (Bytes): "; getline(cin, FM_1);
                                            }while(cin.fail() && FM_1 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for confidentiality (Bytes): "; getline(cin, RAM_1);
                                             }while(cin.fail() && RAM_1 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_1` = '"+Req_1+"', `FM_1` = '"+FM_1+"', `RAM_1` = '"+RAM_1+"' WHERE `Request_ID` = '"+Request_ID+"'";//This is how to update multiple columns in mysql table at the same time.
                                    break;
                                     case 7:
                                           cin.ignore();
                                           do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <INTG or ' '> to Add or Delete Integrity: "; getline(cin, Req_2);
                                           }while((Req_2 != "INTG") && Req_2 != "' '");
                                       do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "  Enter new a value or ' ' to Modify or Delete available flash memory space for integrity (Bytes): "; getline(cin, FM_2);
                                            }while(cin.fail() && FM_2 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for integrity (Bytes): "; getline(cin, RAM_2);
                                             }while(cin.fail() && RAM_2 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_2` = '"+Req_2+"', `FM_2` = '"+FM_2+"', `RAM_2` = '"+RAM_2+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 8:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <AUTH or ' '> to Add or Delete Authentication: "; getline(cin, Req_3);
                                           }while((Req_3 != "AUTH") && Req_3 != "' '");
                                        do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "  Enter new a value or ' ' to Modify or Delete available flash memory space for authentication (Bytes): "; getline(cin, FM_3);
                                            }while(cin.fail() && FM_3 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for authentication (Bytes): "; getline(cin, RAM_3);
                                             }while(cin.fail() && RAM_3 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_3` = '"+Req_3+"', `FM_3` = '"+FM_3+"', `RAM_3` = '"+RAM_3+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 9:
                                        cin.ignore();
                                        do{
                                              system("cls");
                                              std::cout<<"\n" "***********************************************************************************************************\n";
                                              cout << endl << "\tType <PRIV or ' '> to Add or Delete Privacy: "; getline(cin, Req_4);
                                           }while((Req_4 != "PRIV") && Req_4 != "' '");
                                        do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "  Enter new a value or ' ' to Modify or Delete available flash memory space for privacy (Bytes): "; getline(cin, FM_4);
                                            }while(cin.fail() && FM_4 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for privacy (Bytes): "; getline(cin, RAM_4);
                                             }while(cin.fail() && RAM_4 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_4` = '"+Req_4+"', `FM_4` = '"+FM_4+"', `RAM_4` = '"+RAM_4+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 10:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <NONR or ' '> to Add or Delete Non-Repudiation: "; getline(cin, Req_5);
                                           }while((Req_5 != "NONR") && Req_5 != "' '");
                                        do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "Enter new a value or ' ' to Modify or Delete available flash memory space for non-repudiation (Bytes): "; getline(cin, FM_5);
                                            }while(cin.fail() && FM_5 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for non-repudiation (Bytes): "; getline(cin, RAM_5);
                                             }while(cin.fail() && RAM_5 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_5` = '"+Req_5+"', `FM_5` = '"+FM_5+"', `RAM_5` = '"+RAM_5+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                    case 11:
                                          cin.ignore();
                                          do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "\tType <COAU or ' '> to Add or Delete Confidentiality & Authenticity: "; getline(cin, Req_6);
                                           }while((Req_6 != "COAU") && Req_6 != "' '");
                                        do{
                                                system("cls");
                                                std::cout<<"\n" "***********************************************************************************************************\n";
                                                cout << endl << "  Enter new a value or ' ' to Modify or Delete available flash memory space for confidentiality & authenticity (Bytes): "; getline(cin, FM_6);
                                            }while(cin.fail() && FM_6 != "' ' ");

                                            do{
                                                 system("cls");
                                                 std::cout<<"\n" "***********************************************************************************************************\n";
                                                 cout << endl << "  Enter new a value or ' ' to Modify or Delete RAM space for confidentiality & authenticity (Bytes): "; getline(cin, RAM_6);
                                             }while(cin.fail() && RAM_6 != "' '");
                                         update_query = "UPDATE `users_requests_` SET `Req_6` = '"+Req_6+"', `FM_6` = '"+FM_6+"', `RAM_6` = '"+RAM_6+"' WHERE `Request_ID` = '"+Request_ID+"'";
                                    break;
                                     case 12:
                                           system("cls");
                                           std::cout<<"\n" "***********************************************************************************************************\n";
                                           std::cout << endl << "\n\t\t\t Done!" << endl;
                                            break;

                                    default:
                                            cout << "Please choose a correct number" << endl;
                                }
                                const char* qm = update_query.c_str();
                                qstate = mysql_query(conn, qm);

                                if(!qstate)
                                {
                                    cout << endl << "\t\t\t Database successfully updated." << endl;
                                    cout << "\n\n\t\t\t Press Enter to return to the Admin Menu. ";
                                }
                                else
                                {
                                    cout << "\tQuery Execution Problem!" << mysql_errno(conn) << endl;
                                }
                        }while(choice != 12);
                    }
                    else
                    {
                        system("cls");
                        std::cout<<"\n" "***********************************************************************************************************\n";
                        std::cout << "\n\tPress Enter to return to the Main Menu. ";
                        return;
                    }
            }
            state == 0;

    }

   void UserInput::showAndModifyUser_request()
	{
        system("cls");
        std::cout << "\n" "***********************************************************************************************************\n";
        std::cout<<"\t\tMODIFY REQUEST\n\n";
        std::cout << "\n\t Enter your Request ID: "; std::cin >> Request_ID;

        Preliminary pre;

        pre.convert_lowerC_to_upperC(Request_ID);

       int implemtn_type = pre.determine_requestType(Request_ID);

        system("cls");
        switch(implemtn_type)
        {
            case 1:
                modifyHardware_request();
                break;
            case 2:
                modifySoftware_request();
                break;
            default:
                system("cls");
                 std::cout << "\n\n\n\n\n\n\n\n\n\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n\n";
                 std::cout << "\n\tPress Enter to return to the Main Menu and try again.";
            break;
        }
	}

	void UserInput::deleteRequest()
    {
        Processing_and_Output po;
        UserInput usrIp;

        system("cls");
        std::cout << "\n***********************************************************************************************************\n";
        std::cout<<"\t\tDELETE REQUEST \n\n";
        cout << "\n\tEnter Request ID to delete your request: "; cin >> Request_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Request_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || (first_letter != 'S' && first_letter != 'H'))
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

       int implemtn_type = pre.determine_requestType(Request_ID);

        system("cls");
        switch(implemtn_type)
        {
            case 1:
                    {
                        string delete_query = "delete from users_requests_2 where Request_ID = '"+Request_ID+"'";
                        const char* qd = delete_query.c_str();
                        qstate = mysql_query(conn, qd);

                        if(!qstate)
                        {
                            system("cls");
                            cout << "\n\tSuccessfully Deleted from Database! ";
                        }
                        else
                        {
                            system("cls");
                            cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                        }
                    }
                break;
            case 2:
                    {
                            level_:
                            char ch;
                            system("cls");
                            std::cout<<"\n" "***********************************************************************************************************\n";
                            std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system? \n";

                            std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                            std::cout<<"\n\t\t2. Existing System ";
                            std::cout<<"\n\n\tSelect Your Option (1-2): ";

                            std::cin>>ch;

                            switch(ch)
                            {
                            case '1':
                                 {
                                        system("cls");
                                        std::cout << "\n" "***********************************************************************************************************\n";
                                        std::cout<<"\n\t\tABOUT BE TO DESIGNED\n\n";
                                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                        std::cin.ignore();

                                        if(cin.get() == '\n')
                                        {
                                                string delete_query = "delete from users_requests where Request_ID = '"+Request_ID+"'";
                                                const char* qd = delete_query.c_str();
                                                qstate = mysql_query(conn, qd);

                                                if(!qstate)
                                                {
                                                    system("cls");
                                                    cout << "\n\tSuccessfully Deleted from Database! ";
                                                }
                                                else
                                                {
                                                    system("cls");
                                                    cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                                }
                                        }
                                        else
                                        {
                                            goto level_;
                                        }
                                        break;
                                    }
                            case '2':
                                {
                                        system("cls");
                                        std::cout << "\n" "***********************************************************************************************************\n";
                                        std::cout<<"\n\t\tEXISTING SYSTEM\n";
                                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                        std::cin.ignore();

                                        if(cin.get() == '\n')
                                        {
                                                string delete_query = "delete from users_requests_ where Request_ID = '"+Request_ID+"'";
                                                const char* qd = delete_query.c_str();
                                                qstate = mysql_query(conn, qd);

                                                if(!qstate)
                                                {
                                                    system("cls");
                                                    cout << "\n\tSuccessfully Deleted from Database! ";
                                                }
                                                else
                                                {
                                                    system("cls");
                                                    cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                                }
                                        }
                                        else
                                        {
                                            goto level_;
                                        }
                                        break;
                                    }
                            default:
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            goto level_;
                            }
                    break;
                    }
            default:
                system("cls");
                 std::cout << "\n\n\n\n\n\n\n\n\n\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n\n";
                 std::cout << "\n\tPress Enter to return to the Main Menu and try again.";
            break;
        }
    }

	void UserInput::showAndDeleteUser_Request()
	{
	     int choice;
	     level:
		 system("cls");
        std::cout<<"\n***********************************************************************************************************\n";
                            std::cout<<"\n\tDISPLAY LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION USER REQUEST IDs/DELETE A USER REQUEST\n";

        std::cout << "\n\t\tSelect Implementation Type (Hardware or Software): \n";

        std::cout<<"\n\t\t\t1. Hardware";
        std::cout<<"\n\t\t\t2. Software (Yet to be Implemented)";
        std::cout<<"\n\t\t\t3. Software (Existing Systems)";
        std::cout<<"\n\t\t\t4. Return to Admin Menu";
        std::cout<<"\n\n\t\tSelect Your Option (1-4): ";
        std::cin>> choice;

        switch(choice)
        {
            case 1:
                {
                     system("cls");
                    std::cout << "\n" "***********************************************************************************************************\n";
                    std::cout<<"\n\t\tSHOW REQUEST IDs FOR ALL HARDWARE IMPLEMENTATION USERS\n\n";
                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                    std::cin.ignore();

                    if(cin.get() == '\n')
                    {
                            qstate = mysql_query(conn, "select * from users_requests_2");
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            cout << "         Showing Request IDs for all hardware implementation users.... " << endl << endl;

                             res = mysql_use_result(conn);

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << "Request ID" << '|'<< endl;

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            if(!qstate)
                            {
                                 while((row = mysql_fetch_row(res)))
                                 {
                                        cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << row[0] << '|' << endl;
                                 }
                            }
                            else
                            {
                                cout << "Query error!" << mysql_errno(conn) << endl;
                            }
                            cout << "\t\t"<< left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            mysql_free_result(res);

                    }
                    else
                    {
                        goto level;
                    }

                        string Request_ID; char ch;
                        cout << "\n\tDo you want to delete any user request? (y/n): "; cin >> ch;

                        if(ch == 'y' || ch == 'Y')
                        {
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t\tDELETE  A HARDWARE IMPLEMENTATION USER REQUEST\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    system("cls");
                                    std::cout<<"\n***********************************************************************************************************\n\n";
                                    cout << "\n\tEnter the request ID of the user request you want to delete: "; cin >> Request_ID;

                                    Preliminary pre;
                                    UserInput usrIp;

                                    pre.convert_lowerC_to_upperC(Request_ID);

                                    int num_digits;
                                    int string_length;
                                    char first_letter;

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;

                                    while(num_digits !=4 || string_length != 5 || first_letter != 'H')
                                    {
                                        system("cls");
                                        std::cout << "\n***********************************************************************************************************\n";
                                        std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                        std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                                        std::cin >> Request_ID;

                                        pre.convert_lowerC_to_upperC(Request_ID);

                                        auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                        num_digits = collector.n1;
                                        string_length = collector.n2;
                                        first_letter = collector.c;
                                    }


                                    string delete_query = "delete from users_requests_2 where Request_ID = '"+Request_ID+"'";
                                    const char* qd = delete_query.c_str();
                                    qstate = mysql_query(conn, qd);

                                    if(!qstate)
                                    {
                                        system("cls");
                                         std::cout<<"\n***********************************************************************************************************\n\n";
                                        cout << "\n\t\tSuccessfully Deleted from Database!\n" << endl;
                                        std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                                    }
                                    else
                                    {
                                        system("cls");
                                        cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                    }
                                }
                                else
                                {
                                    goto level;
                                }
                        }
                        else
                        {
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                            return;
                        }
                    break;
                }
            case 2:
                {
                     system("cls");
                    std::cout << "\n" "***********************************************************************************************************\n";
                    std::cout<<"\n\t\tSHOW REQUEST IDs FOR ALL SOFTWARE IMPLEMENTATION USERS (Yet to be Implemented)\n\n";
                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                    std::cin.ignore();

                    if(cin.get() == '\n')
                    {
                            qstate = mysql_query(conn, "select * from users_requests");
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            cout << "         Showing Request IDs for all software implementation users (Yet to be Implemented).... " << endl << endl;

                             res = mysql_use_result(conn);

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << "Request ID" << '|'<< endl;

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            if(!qstate)
                            {
                                 while((row = mysql_fetch_row(res)))
                                 {
                                        cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << row[0] << '|' << endl;
                                 }
                            }
                            else
                            {
                                cout << "Query error!" << mysql_errno(conn) << endl;
                            }
                            cout << "\t\t"<< left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            mysql_free_result(res);

                    }
                    else
                    {
                        goto level;
                    }

                        string Request_ID; char ch;
                        cout << "\n\tDo you want to delete any user request? (y/n): "; cin >> ch;

                        if(ch == 'y' || ch == 'Y')
                        {
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t\tDELETE  A SOFTWARE IMPLEMENTATION USER REQUEST\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    system("cls");
                                    std::cout<<"\n***********************************************************************************************************\n\n";
                                    cout << "\n\tEnter the request ID of the user request you want to delete: "; cin >> Request_ID;

                                    Preliminary pre;
                                    UserInput usrIp;

                                    pre.convert_lowerC_to_upperC(Request_ID);

                                    int num_digits;
                                    int string_length;
                                    char first_letter;

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;

                                    while(num_digits !=4 || string_length != 5 || first_letter != 'S')
                                    {
                                        system("cls");
                                        std::cout << "\n***********************************************************************************************************\n";
                                        std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                        std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                                        std::cin >> Request_ID;

                                        pre.convert_lowerC_to_upperC(Request_ID);

                                        auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                        num_digits = collector.n1;
                                        string_length = collector.n2;
                                        first_letter = collector.c;
                                    }

                                    string delete_query = "delete from users_requests where Request_ID = '"+Request_ID+"'";
                                    const char* qd = delete_query.c_str();
                                    qstate = mysql_query(conn, qd);

                                    if(!qstate)
                                    {
                                        system("cls");
                                         std::cout<<"\n***********************************************************************************************************\n\n";
                                        cout << "\n\t\tSuccessfully Deleted from Database!\n" << endl;
                                        std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                                    }
                                    else
                                    {
                                        system("cls");
                                        cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                    }
                                }
                                else
                                {
                                    goto level;
                                }
                        }
                        else
                        {
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                            return;
                        }
                    break;
                }
             case 3:
                {
                     system("cls");
                    std::cout << "\n" "***********************************************************************************************************\n";
                    std::cout<<"\n\t\tSHOW REQUEST IDs FOR ALL SOFTWARE IMPLEMENTATION USERS (Existing Systems)\n\n";
                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                    std::cin.ignore();

                    if(cin.get() == '\n')
                    {
                            qstate = mysql_query(conn, "select * from users_requests_");
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            cout << "         Showing Request IDs for all software implementation users (Existing Systems).... " << endl << endl;

                             res = mysql_use_result(conn);

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << "Request ID" << '|'<< endl;

                            cout << "\t\t" << left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            if(!qstate)
                            {
                                 while((row = mysql_fetch_row(res)))
                                 {
                                        cout << "\t\t" << setfill(' ') << '|' << left << setw(10) << row[0] << '|' << endl;
                                 }
                            }
                            else
                            {
                                cout << "Query error!" << mysql_errno(conn) << endl;
                            }
                            cout << "\t\t"<< left << setw(11) << setfill('-') << left << '+'
                            << setw(1) << left << '+' << endl;

                            mysql_free_result(res);

                    }
                    else
                    {
                        goto level;
                    }

                        string Request_ID; char ch;
                        cout << "\n\tDo you want to delete any user request? (y/n): "; cin >> ch;

                        if(ch == 'y' || ch == 'Y')
                        {
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout<<"\n\t\tDELETE  A SOFTWARE IMPLEMENTATION USER REQUEST\n\n";
                                std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                std::cin.ignore();

                                if(cin.get() == '\n')
                                {
                                    system("cls");
                                    std::cout<<"\n***********************************************************************************************************\n\n";
                                    cout << "\n\tEnter the request ID of the user request you want to delete: "; cin >> Request_ID;

                                    Preliminary pre;
                                    UserInput usrIp;

                                    pre.convert_lowerC_to_upperC(Request_ID);

                                    int num_digits;
                                    int string_length;
                                    char first_letter;

                                    auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                    num_digits = collector.n1;
                                    string_length = collector.n2;
                                    first_letter = collector.c;

                                    while(num_digits !=4 || string_length != 5 || first_letter != 'S')
                                    {
                                        system("cls");
                                        std::cout << "\n***********************************************************************************************************\n";
                                        std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                                        std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                                        std::cin >> Request_ID;

                                        pre.convert_lowerC_to_upperC(Request_ID);

                                        auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                                        num_digits = collector.n1;
                                        string_length = collector.n2;
                                        first_letter = collector.c;
                                    }

                                    string delete_query = "delete from users_requests_ where Request_ID = '"+Request_ID+"'";
                                    const char* qd = delete_query.c_str();
                                    qstate = mysql_query(conn, qd);

                                    if(!qstate)
                                    {
                                        system("cls");
                                         std::cout<<"\n***********************************************************************************************************\n\n";
                                        cout << "\n\t\tSuccessfully Deleted from Database!\n" << endl;
                                        std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                                    }
                                    else
                                    {
                                        system("cls");
                                        cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
                                    }
                                }
                                else
                                {
                                    goto level;
                                }
                        }
                        else
                        {
                            system("cls");
                            std::cout<<"\n***********************************************************************************************************\n\n";
                            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
                            return;
                        }
                    break;
                }
            case 4:
                system("cls");
                 std::cout << "\n" "***********************************************************************************************************\n";
                std::cout << endl << endl;
                 std::cout << "\n\tPress Enter again to return to Admin Menu.";
                return;

            default:
                system("cls");
                 std::cout << "\n\tSorry! Wrong option selected. Press Enter to return to Main Menu.";
            break;
        }
	}

class Cipher
{
	public:
	string ID, cipher_name, block_size, key_size, ramFootPrint, code_size;

	void upLoadCipher();
	void updateCipher();
	void retrieveCipher();
	void deleteCipher();
	void show_add_update_or_deleteCipher();
};

  void Cipher::upLoadCipher()
	{
		cout << "\n\tUpload Ciphers into the Database" << endl;
		cin.ignore(1, '\n');
		cout << "\n\tEnter Cipher ID: "; getline(cin, ID);
		cout << "\n\tEnter Cipher Name: "; getline(cin, cipher_name);
		cout << "\n\tEnter Block Size: "; getline(cin, block_size);
		cout << "\n\tEnter Key Size: "; getline(cin, key_size);
		cout << "\n\tEnter Ram Foot Print: "; getline(cin, ramFootPrint);
		cout << "\n\tEnter Code Size: "; getline(cin, code_size);

		string insert_query = "insert into crypto_algor (ID, cipher_name, block_size, key_size, ramFootPrint, code_size) values('"+ID+"','"+cipher_name+"','"+block_size+"','"+key_size+"', '"+ramFootPrint+"', '"+code_size+"')";

		const char* qu = insert_query.c_str();
		qstate = mysql_query(conn, qu);

		if(!qstate)
		{
			cout << endl << "\n\tSuccessfully added into the database." << endl;
		}
		else
		{
			cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
		}
	}

	void Cipher::updateCipher()
    {
		std::cout << "\n\tEnter the cipher ID you want to update: "; cin >> ID;

		cout << "\n\tChoose the S\N of items you want to update one at a time: " << endl;

		string update_query;

		int choice;

		do{
                cout << "\t\t1. Cipher Name " << endl;
                cout << "\t\t2. Block Size " << endl;
                cout << "\t\t3. Key Size " << endl;
                cout << "\t\t4. Ram Foot Print " << endl;
                cout << "\t\t5. Side Size " << endl;
                cout << "\t\t6. Done!\n" << endl;

                cout << "\tTo update, type S\\N of item and press enter, and type 6 when done : "; cin >> choice;

                switch(choice)
                {
                    case 1:
                            cin.ignore();
                            cout << "\tEnter Cipher Name: ";
                            getline(cin, cipher_name);
                        update_query = "UPDATE `crypto_algor` SET `cipher_name` = '"+cipher_name+"' WHERE `ID` = '"+ID+"'";
                    break;
                     case 2:
                            cin.ignore();
                            cout << "\tEnter Block Size: "; getline(cin, block_size);
                        update_query = "UPDATE `crypto_algor` SET `block_size` = '"+block_size+"' WHERE `ID` = '"+ID+"'";
                    break;
                    case 3:
                            cin.ignore();
                            cout << "\tEnter Key Size: "; getline(cin, key_size);
                        update_query = "UPDATE `crypto_algor` SET `key_size` = '"+key_size+"' WHERE `ID` = '"+ID+"'";
                    break;
                     case 4:
                            cin.ignore();
                            cout << "\tEnter Ram Foot Print: "; getline(cin, ramFootPrint);
                        update_query = "UPDATE `crypto_algor` SET `ramFootPrint` = '"+ramFootPrint+"' WHERE `ID` = '"+ID+"'";
                    break;
                    case 5:
                            cin.ignore();
                            cout << "\tEnter Code Size: "; getline(cin, code_size);
                        update_query = "UPDATE `crypto_algor` SET `code_size` = '"+code_size+"' WHERE `ID` = '"+ID+"'";
                    break;
                     case 6:
                           std::cout << "\n\tDone!" << endl;
                            break;

                    default:
                            cout << "\tPlease choose a correct number" << endl;
                }
                const char* qm = update_query.c_str();
                qstate = mysql_query(conn, qm);
		}while(choice != 6);


        if(!qstate)
        {
            cout << endl << "\tDatabase successfully updated." << endl;
        }
        else
        {
            cout << "\tQuery Execution Problem!" << mysql_errno(conn) << endl;
        }
    }

	void Cipher::retrieveCipher()
	{
       cout << "Enter Cipher Name: "; cin >> cipher_name;

		string findbyname_query = "select * from crypto_algor where cipher_name like '%"+cipher_name+"%'";
		const char* qn = findbyname_query.c_str();
		qstate = mysql_query(conn, qn);

		cout << endl << "Showing Cipher ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
				cout << "Cipher ID: " << row[0] << endl;
				cout << "Cipher Name: " << row[1] << endl;
				cout << "Block Size: " << row[2] << endl;
				cout << "Key Size: " << row[3] << endl;
				cout << "Ram Foot Print: " << row[4] << endl;
				cout << "Code Size: " << row[5] << endl;
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}
	}

	void Cipher::deleteCipher()
	{
	    cout << "\n\tEnter the name of the cipher you want to delete: "; cin >> cipher_name;
        string delete_query = "delete from crypto_algor where cipher_name = '"+cipher_name+"'";
        const char* qd = delete_query.c_str();
        qstate = mysql_query(conn, qd);


        if(!qstate)
        {
            cout << "\n\tSuccessfully Deleted from Database. " << endl;
        }
        else
        {
            cout << "\n\tFailed to Delete!" << mysql_errno(conn) << endl;
        }
	}

    void Cipher::show_add_update_or_deleteCipher()
    {
           qstate = mysql_query(conn, "select * from crypto_algor");
           system("cls");
        std::cout << "\n" "***********************************************************************************************************\n";
            std::cout<<"\t\tSHOW AND UPDATE ALGORITHMS\n\n";
		cout << "\tShowing supported ciphers .... " << endl << endl;

		int choose;
                res = mysql_use_result(conn);

                cout << left << setw(4) << setfill('-') << left << '+'
                << setw(20) << setfill('-') << left << '+'
                << setw(11)<< setfill('-') << left << '+'
                << setw(9)<< setfill('-') << left << '+'
                << setw(14)<< setfill('-') << left << '+'
                << setw(14)<< setfill('-') << '+' << '+' << endl;

                cout << setfill(' ') << '|' << left << setw(3) << "ID"
                << setfill(' ') << '|' << setw(19) << "Cipher Name"
                << setfill(' ') << '|' << setw(10) << "Block Size"
                << setfill(' ') << '|' << setw(8) << "Key Size"
                << setfill(' ') << '|' << setw(13) << "Ram Size (B)"
                << setfill(' ') << '|' << left << setw(13) << "Code Size (B)" << '|' << endl; //The left can be changed to right

                 cout << left << setw(4) << setfill('-') << left<< '+'
                 << setw(20) << setfill('-') << left << '+'
                 << setw(11) << setfill('-') << left << '+'
                 << setw(9) << setfill('-') << left << '+'
                 << setw(14) << setfill('-') << left << '+'
                 << setw(14) << setfill('-') << '+' << '+' << endl;

		if(!qstate)
		{
                 while((row = mysql_fetch_row(res)))
                 {
                     cout << setfill(' ') << '|' << left << setw(3) << row[0]
                    << setfill(' ') << '|' << setw(19) << row[1]
                    << setfill(' ') << '|' << setw(10) << row[2]
                    << setfill(' ') << '|' << setw(8) << row[3]
                    << setfill(' ') << '|' << setw(13) << row[4]
                    << setfill(' ') << '|' << left << setw(13) << row[5] << '|' << endl;
                 }
		}
		else
		{
			cout << "Query error!" << mysql_errno(conn) << endl;
		}
		cout << left << setw(4) << setfill('-') << left << '+'
                << setw(20) << setfill('-') << left << '+'
                << setw(11)<< setfill('-') << left << '+'
                << setw(9)<< setfill('-') << left << '+'
                << setw(14)<< setfill('-') << left << '+'
                << setw(14)<< setfill('-') << '+' << '+' << endl;
		mysql_free_result(res);

      do{
            cout << "\n\tWhat do you want to do?" << endl;
            cout << "\t1. Add a Cipher " << endl;
            cout << "\t2. Update a Cipher " << endl;
            cout << "\t3. Delete a Cipher " << endl;
            cout << "\t4. Return to Admin Menu " << endl;
            cout << "\n\tSelect your choice: "; cin >> choose;

            switch(choose)
            {
                case 1:
                        upLoadCipher();
                        break;
                case 2:
                        updateCipher();
                        break;
                case 3:
                        deleteCipher();
                        break;
                case 4:
                        system("cls");
                        cout << "\n\n\n\n\n\n\t\t\tReturning to Admin Menu ..... " << endl;
                        cout << "\n\n\n\t\t\tPress Enter to continue ";
                        return;
                default:
                        cout << "Please choose a correct number" << endl;
            }
            cin.ignore();
            cin.get();
        }while(choose != 4);
    }

class SecurityMngr
{
	public:
	string ID, label, reqmnt;
	string M_ID, mechanism;


	void decisionMaker_RE();
	void decisionMaker_BP();
	void upLoadSecurity_Req();
	void retrieveSecurity_Req();
	void deleteSecurity_Req();
	void show_add_or_deleteSecurity_Req();
	void upLoadSecurity_Mech();
	void retrieveSecurity_Mech();
	void deleteSecurity_Mech();
	void show_add_or_deleteSecurity_Mech();
	void decisionMaker();


	friend class LoginManager;
};

    void SecurityMngr::decisionMaker_RE()
    {
             Processing_and_Output po;
             UserInput usrIp;

            string Reqst_ID;
            system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\tREQUEST REQUIREMENTS ELICITATION PROCESSING\n\n";
            cout << "\tPlease enter your Request ID: "; cin >> Reqst_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Reqst_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'R')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Reqst_ID;

                pre.convert_lowerC_to_upperC(Reqst_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Reqst_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

                po.write_security_requirements_in_textFile(Reqst_ID);

                        system("cls");
                        string findbyID_query = "select * from users_requests_re where Reqst_ID = " + ("'"+Reqst_ID+"'");
                        const char* qn = findbyID_query.c_str();
                        qstate = mysql_query(conn, qn);

                        string state, Domain, anyUsr, Login, stoUsrInfo, stoAnyInfo, InfoType, infoSent2E, connected, dataSent2Cloud, dataStoredInDb, update, use3rdPrtySfw, evesdrop, capt_Resent, impersontUsr, physiclAcces;

                        if(!qstate)
                        {
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                state = row[1];
                                Domain = row[2];
                                anyUsr = row[3];
                                Login = row[4];
                                stoUsrInfo = row[5];
                                stoAnyInfo = row[6];
                                InfoType = row[7];
                                infoSent2E = row[8];
                                connected = row[9];
                                dataSent2Cloud = row[10];
                                dataStoredInDb = row[11];
                                update = row[12];
                                use3rdPrtySfw = row[13];
                                evesdrop = row[14];
                                capt_Resent = row[15];
                                impersontUsr = row[16];
                                physiclAcces = row[17];
                            }
                        }
                        else
                        {
                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                        }

            system("cls");
            cout << "\n" "***********************************************************************************************************" << endl;
           cout << "\t   THE SECURITY REQUIREMENTS FOR THE IoT SYSTMEM OF THE USER WITH REQUEST ID No.: " << Reqst_ID << endl << endl;

                int domainSensitivity = po.checkSensitivity_of_User_ApplcArea(Domain);

                string flag1 = "1", flag1_1 = "1", flag2 = "1", flag3 = "1", flag4 = "1", flag5 = "1", flag6 = "1", flag7 = "1", flag8 = "1", flag9 = "", flag10 = "1", flag11 = "1", flag12 = "1", flag13 = "1", flag14 = "1", flag15 = "1", flag16 = "1", flag17 = "1", flag18 = "1", flag19 = "1", flag20 = "1";
                string flag21 = "1", flag22 = "1", flag23 = "1", flag24 = "1", flag25 = "1", flag26 = "1", flag27 = "1", flag28 = "1", flag29 = "1", flag30 = "1", flag6_, flag_6;
                string flag31 = "1", flag32 = "1", flag33 = "1", flag34 = "1", flag35 = "1", flag36 = "1", flag37 = "1", flag38 = "1", flag39 = "1", flag40 = "1", flag41 = "1", flag42 = "1", flag43 = "1", flag44 = "1";
                string Reqmt_1, Reqmt_2, Reqmt_3, Reqmt_4, Reqmt_5, Reqmt_6, Reqmt_7, Reqmt_8, Reqmt_9, Reqmt_10, Reqmt_11, Reqmt_12, Reqmt_13, Reqmt_14, Reqmt_15;

                cout << left << setw(21) << setfill('-') << left << '+'
                << setw(84) << setfill('-') << '+' << '+' << endl;

                cout << setfill(' ') << '|' << left << setw(20) << "SECURITY REQUIREMENT"
                << setfill(' ') << '|' << left << setw(83) << "DESCRIPTION" << '|' << endl;

                 cout << left << setw(21) << setfill('-') << left<< '+'
                 << setw(84) << setfill('-') << '+' << '+' << endl;

                 if(anyUsr == "Yes" && Login == "Yes")//
                 {
                    flag1 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                 if(stoUsrInfo == "Yes" && anyUsr == "Yes")
                 {
                    flag2 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Privacy"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, meani- " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_4 = "PRIV";
                 }
                 if(stoUsrInfo == "Yes" && stoAnyInfo == "Yes")
                 {
                    flag3 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_1 = "CONF";
                 }
                 if(stoAnyInfo == "Yes" && flag3 != "2")
                 {
                    flag4 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_1 = "CONF";
                 }
                 if(InfoType == "Normal" && flag2 != "2" && !stoUsrInfo.empty())
                 {
                    flag2 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Privacy"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, menani- " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_4 = "PRIV";
                 }
                 if(InfoType == "Normal" && flag3 != "2" && flag4 != "2")
                 {
                    flag6 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_1 = "CONF";
                 }
                 if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                 {
                     flag6_ = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Integrity"
                    << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_2 = "INTG";
                 }
                 if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                 {
                     flag_6 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Availability"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "usable upon demand by authorized entities." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_6 = "AVAI";
                 }

                 if(InfoType == "Normal" || InfoType == "Sensitive" || InfoType == "Critical")
                 {
                    flag7 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_7 = "PHYS";
                 }
                 if(InfoType == "Sensitive" && stoUsrInfo == "Yes")
                 {

                 }
                 if(InfoType == "Sensitive" && stoUsrInfo != "Yes")
                 {

                 }
                 if(InfoType == "Sensitive" && flag3 != "2" && flag4 != "2" && flag6 != "2")
                 {
                    flag8 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_1 = "CONF";
                 }
                 if(InfoType == "Sensitive")
                 {
                    flag9 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authorization"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_8 = "AUTR";
                 }
                 if(InfoType == "Sensitive")
                 {
                    flag10 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                    << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_9 = "FORE";
                 }
                 if(InfoType == "Sensitive" && flag1 != "2")
                 {
                    flag11 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                 if(InfoType == "Critical" && flag2 != "2" && flag5 != "2")
                 {
                    flag2 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Privacy"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to users control over the disclosure of their personal information, menani- " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ng that only the users should decide whether they want to share their data or not." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_4 = "PRIV";
                 }
                 if(InfoType == "Critical" && flag3 != "2" && flag4 != "2" && flag6 != "2" && flag8 != "2")
                 {
                    flag13 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confidentiality"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that information is not disclosed or made availa-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "ble to any unauthorized entity." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_1 = "CONF";
                 }
                 if(InfoType == "Critical" && flag7 != "2")
                 {
                    flag14 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_7 = "PHYS";
                 }
                 if(InfoType == "Critical" && flag9 != "2")
                 {
                    flag15 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authorization"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_8 = "AUTR";
                 }
                 if(InfoType == "Critical" && flag10 != "2")
                 {
                    flag16 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                    << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_9 = "FORE";
                 }
                 if(InfoType == "Critical" && domainSensitivity == 1)
                 {
                    flag17 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_5 = "NONR";
                 }
                 if(InfoType == "Critical" && flag1 != "2" && flag11 != "2")
                 {
                    flag18 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                 if(infoSent2E == "Yes" && flag17 != "2" && domainSensitivity == 1)
                 {
                     flag19 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_5 = "NONR";
                 }
                 if(infoSent2E == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2")
                 {
                    flag20 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                 if(infoSent2E == "Yes")
                 {
                    flag21 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confinement"
                    << setfill(' ') << '|' << left << setw(83) << "Ensures that even if a party is corrupted, the spreading of the effects of the" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "attack is as confined as possible." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_10 = "CFMT";
                 }
                 if(connected == "Yes" && flag17 != "2" && flag19 != "2" && domainSensitivity == 1)
                 {
                     flag22 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_5 = "NONR";
                 }
                 if(connected == "Yes" && domainSensitivity == 1)
                 {
                     flag23 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Accountability"
                    << setfill(' ') << '|' << left << setw(83) << "This is the property that ensures that every action can be traced back to a single " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "user or device." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_11 = "ACCT";
                 }
                 if(connected == "Yes")
                 {
                     flag24 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Reliability"
                    << setfill(' ') << '|' << left << setw(83) << "Is the property that guarantees consistent intended behavior of an IoT system." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_12 = "RELI";
                 }
                 if(dataSent2Cloud == "Yes" && flag6_ != "2")
                 {
                     flag25 = "2";
                     cout << setfill(' ') << '|' << left << setw(20) << "Integrity"
                    << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;


                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_2 = "INTG";
                 }
                 if(dataSent2Cloud == "Yes" && flag_6 != "2")
                 {
                     flag26 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Availability"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << " usable upon demand by authorized entities." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_6 = "AVAI";
                 }
                 if(dataSent2Cloud == "Yes")
                 {
                    flag27 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Data Freshness"
                    << setfill(' ') << '|' << left << setw(83) << "Ensures that data is the most recent, and that old messages cannot be replayed." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_13 = "DAFR";
                  }
                 if(dataSent2Cloud == "Yes" && flag10 != "2" && flag16 != "2")
                 {
                    flag28 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                    << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_9 = "FORE";
                 }
                 if(dataSent2Cloud == "Yes" && flag17 != "2" && flag19 != "2" && flag22 != "2" && domainSensitivity == 1)
                 {
                     flag29 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_5 = "NONR";
                 }
                 if(dataStoredInDb == "Yes" && flag7 != "2" && flag14 != "2" && flag22 != "2" )
                 {
                    flag30 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_7 = "PHYS";
                 }
                 if(dataStoredInDb == "Yes" && flag6_ != "2" && flag25 != "2")
                 {
                     flag31 = "2";
                     cout << setfill(' ') << '|' << left << setw(20) << "Integrity"
                    << setfill(' ') << '|' << left << setw(83) << "Is the property of safeguarding the correctness, consistency, and trustworthiness " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "of data over its entire life cycle in an IoT system." << '|' << endl;


                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_2 = "INTG";
                 }
                 if(dataStoredInDb == "Yes" && flag_6 != "2" && flag26 != "2")
                 {
                     flag32 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Availability"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "usable upon demand by authorized entities." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_6 = "AVAI";
                 }
                 if(dataStoredInDb == "Yes" && flag10 != "2" && flag16 != "2" && flag28 != "2")
                 {
                    flag33 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Forgery Resistance"
                    << setfill(' ') << '|' << left << setw(83) << "This is the propriety that ensures that the data shared between entities cannot be " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "forged by a third party trying to damage or harm the system or its users." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_9 = "FORE";
                 }
                 if(dataStoredInDb == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2")
                 {
                    flag34 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                 if(dataStoredInDb == "Yes" && flag17 != "2" && flag19 != "2" && flag22 != "2" && flag29 != "2" && domainSensitivity == 1)
                 {
                     flag35 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Non-Repudiation"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security property that ensures that the transfer of messages or cred-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "entials between 2 IoT entities is undeniable." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_5 = "NONR";
                 }
                 if(update == "Yes" && flag_6 != "2" && flag26 != "2" && flag32 != "2")
                 {
                     flag36 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Availability"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property which ensures that an IoT device or system is accessible and" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "usable upon demand by authorized entities." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_6 = "AVAI";
                 }
                 if(use3rdPrtySfw == "Yes")
                 {
                    cout << setfill(' ') << '|' << left << setw(20) << "Counterfeit "
                    << setfill(' ') << '|' << left << setw(83) << "Is the property that ensures effective validation of software such that any fake " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << "Resistance "
                    << setfill(' ') << '|' << left << setw(83) << "or maliciously modified software is rejected." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_14 = "CNFR";
                 }
                 if(use3rdPrtySfw == "Yes" && flag21 != "2")
                 {
                    flag37 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Confinement"
                    << setfill(' ') << '|' << left << setw(83) << "Ensures that even if a party is corrupted, the spreading of the effects of the" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "attack is as confined as possible." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_10 = "CFMT";
                 }

                 if(evesdrop == "Yes" && flag9 != "2" && flag15 != "2" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes"))
                 {
                    flag39 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authorization"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the property that determines whether the user or device has rights/privi-" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "leges to access a resource, or issue commands." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_8 = "AUTR";
                 }

                  if(capt_Resent == "Yes" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes") && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2" && flag34 != "2")
                 {
                    flag40 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                     cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }

                 if(capt_Resent == "Yes" && flag27 != "2" && (infoSent2E == "Yes" || dataSent2Cloud == "Yes" || dataStoredInDb == "Yes"))
                 {
                    flag41 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Data Freshness"
                    << setfill(' ') << '|' << left << setw(83) << "Ensures that data is the most recent, and that old messages cannot be replayed." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_13 = "DAFR";
                  }

                 if(impersontUsr == "Yes" && Login == "Yes" && flag1 != "2" && flag11 != "2" && flag18 != "2" && flag20 != "2" && flag34 != "2" && flag40 != "2")
                   {
                    flag42 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Authentication"
                    << setfill(' ') << '|' << left << setw(83) << "This is the assurance that information transaction is from the source it claims to" << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "be from." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_3 = "AUTH";
                 }
                if(physiclAcces == "Yes" && flag7 != "2" && flag14 != "2" && flag22 != "2" && flag30 != "2")
                 {
                    flag43 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Physical Security"
                    << setfill(' ') << '|' << left << setw(83) << "Refers to the security measures designed to deny unauthorized physical access to " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "IoT devices or systems, and to protect them from damage or tampering." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_7 = "PHYS";
                 }
                 if(physiclAcces == "Yes")
                 {
                     flag44 = "2";
                    cout << setfill(' ') << '|' << left << setw(20) << "Tamper Detection"
                    << setfill(' ') << '|' << left << setw(83) << "Ensures all devices are physically secured, such that any tampering attempt is " << '|' << endl;
                    cout << setfill(' ') << '|' << left << setw(20) << " "
                    << setfill(' ') << '|' << left << setw(83) << "detected." << '|' << endl;

                    cout << left << setw(21) << setfill('-') << left<< '+'
                    << setw(84) << setfill('-') << '+' << '+' << endl;
                    Reqmt_15 = "TAMD";
                 }
                 flag1.erase(); flag2.erase(); flag3.erase(); flag4.erase(); flag5.erase();
                 state.erase(); Domain.erase(); anyUsr.erase(); Login.erase(); stoUsrInfo.erase(); stoAnyInfo.erase(); InfoType.erase(); infoSent2E.erase(); connected.erase(); dataSent2Cloud.erase(); dataStoredInDb.erase(); update.erase(); use3rdPrtySfw.erase(); evesdrop.erase(); capt_Resent.erase(); impersontUsr.erase(); physiclAcces.erase();

                  string request_query = "insert into generated_requirements (Reqst_ID, Reqmt_1, Reqmt_2, Reqmt_3, Reqmt_4, Reqmt_5, Reqmt_6, Reqmt_7, Reqmt_8, Reqmt_9, Reqmt_10, Reqmt_11, Reqmt_12, Reqmt_13, Reqmt_14, Reqmt_15) values('"+Reqst_ID+"', '"+Reqmt_1+"', '"+Reqmt_2+"', '"+Reqmt_3+"', '"+Reqmt_4+"', '"+Reqmt_5+"', '"+Reqmt_6+"', '"+Reqmt_7+"', '"+Reqmt_8+"', '"+Reqmt_9+"', '"+Reqmt_10+"', '"+Reqmt_11+"', '"+Reqmt_12+"', '"+Reqmt_13+"', '"+Reqmt_14+"', '"+Reqmt_15+"')";

                  const char* qr = request_query.c_str();
                  qstate = mysql_query(conn, qr);

                    if(!qstate)
                    {
                         Reqmt_1.erase(); Reqmt_2.erase(); Reqmt_3.erase(); Reqmt_4.erase(); Reqmt_5.erase(); Reqmt_6.erase(); Reqmt_7.erase(); Reqmt_8.erase(); Reqmt_9.erase(); Reqmt_10.erase(); Reqmt_11.erase(); Reqmt_12.erase(); Reqmt_13.erase(); Reqmt_14.erase(); Reqmt_15.erase();
                    }
                    else
                    {

                    }

                    cout << "\n\n\t\tPress Enter to turn to the Main Menu" << endl;
    }

    void SecurityMngr::decisionMaker_BP()
    {
             Processing_and_Output po;
             UserInput usrIp;

            string Request_ID;
            system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\tBEST PRACTICE GUIDE FOR SECURE DEVELOPMENT REQUEST PROCESSING\n\n";
            cout << "\tPlease enter your Request ID: "; cin >> Request_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Request_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

             while(num_digits !=4 || string_length != 5 || first_letter != 'B')
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }


            string findbyID_query = "select * from users_requests_bp where Request_ID = " + ("'"+Request_ID+"'");
            const char* qn = findbyID_query.c_str();
            qstate = mysql_query(conn, qn);

            string Status, Struct1, Struct2, Struct3, Struct4, Struct5, Struct6, Struct7, Struct8, Struct9, Struct10, Struct11, anyUsr, usrRegist, typeOfRegist, anyUsrLogin, usrInput, holdUsrInfo, storeAnyInfo, sensitivOfInfo, typeOfAUTH, useDb;
            string typeOfDataStorg, typeOfDb, progrm1, progrm2, progrm3, progrm4, progrm5, progrm6, progrm7, progrm8, fileUpload, sysLog;

            if(!qstate)
            {
                res = mysql_store_result(conn);
                while((row = mysql_fetch_row(res)))
                {
                    Status = row[1];
                    Struct1 = row[2];
                    Struct2 = row[3];
                    Struct3 = row[4];
                    Struct4 = row[5];
                    Struct5 = row[6];
                    Struct6 = row[7];
                    Struct7 = row[8];
                    Struct8 = row[9];
                    Struct9 = row[10];
                    Struct10 = row[11];
                    Struct11 = row[12];
                    anyUsr = row[13];
                    usrRegist = row[14];
                    typeOfRegist = row[15];
                    anyUsrLogin = row[16];
                    usrInput = row[17];
                    holdUsrInfo = row[18];
                    storeAnyInfo = row[19];
                    sensitivOfInfo = row[20];
                    typeOfAUTH = row[21];
                    useDb = row[22];
                    typeOfDataStorg = row[23];
                    typeOfDb = row[24];
                    progrm1 = row[25];
                    progrm2 = row[26];
                    progrm3 = row[27];
                    progrm4 = row[28];
                    progrm5 = row[29];
                    progrm6 = row[30];
                    progrm7 = row[31];
                    progrm8 = row[32];
                    fileUpload = row[33];
                    sysLog = row[34];
                }
            }
            else
            {
                cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
            }


            system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\tTHE QUESTIONS AND ANSWERS PROVIDE BY THE USER WITH REQUEST ID No.: " << Request_ID << endl << endl;

                string findbyRequestID_query = "select * from users_requests_bp where Request_ID like '%"+Request_ID+"%'";
                const char* qr = findbyRequestID_query.c_str();
                qstate = mysql_query(conn, qr);
                int flag_1 = 0;

                if(!qstate)
                {
                    res = mysql_store_result(conn);
                    while((row = mysql_fetch_row(res)))
                    {
                        string Stat = Status;
                        anyUsr= row[13];
                        usrRegist = row[14];
                        holdUsrInfo = row[18];
                        storeAnyInfo = row[19];
                        useDb = row[22];
                        Struct1 = row[2]; Struct2 = row[3]; Struct3 = row[4]; Struct4 = row[5]; Struct5 = row[6]; Struct6 = row[7];
                        Struct7 = row[8]; Struct8 = row[9]; Struct9 = row[10]; Struct10 = row[11]; Struct11 = row[12];
                        progrm1 = row[25]; progrm2 = row[26]; progrm3 = row[27]; progrm4 = row[28]; progrm5 = row[29]; progrm6 = row[30]; progrm7 = row[31]; progrm8 = row[32];

                        std::cout << "\t\tWhat's the category of your IoT System Structure? (you can choose multiple options) " << endl;
				if(!Struct1.empty())
                {
                    cout << "\t\t  - " << row[2] << endl;
                }
                if(!Struct2.empty())
                {
                    cout << "\t\t  - " << row[3] << endl;
                }
                if(!Struct3.empty())
                {
                    cout << "\t\t  - " << row[4] << endl;
                }
                if(!Struct4.empty())
                {
                    cout << "\t\t  - " << row[5] << endl;
                }
                if(!Struct5.empty())
                {
                    cout << "\t\t  - " << row[6] << endl;
                }
                if(!Struct6.empty())
                {
                    cout << "\t\t  - " << row[7] << endl;
                }
                if(!Struct7.empty())
                {
                    cout << "\t\t  - " << row[8] << endl;
                }
                if(!Struct8.empty())
                {
                    cout << "\t\t  - " << row[9] << endl;
                }
                if(!Struct9.empty())
                {
                    cout << "\t\t  - " << row[10] << endl;
                }
                if(!Struct10.empty())
                {
                    cout << "\t\t  - " << row[11] << endl;
                }
                if(!Struct11.empty())
                {
                    cout << "\t\t  - " << row[12] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes the system have a user? - " << row[13] << endl;
                }
                else
                {
                    std::cout << "\t\tWill the system have a user? - " << row[13] << endl;
                }
				if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tDoes the system have a provision for user registration? - " << row[14] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system have any provision for user registration? - " << row[14] << endl;
                    }
                }

                if(usrRegist == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tWho registers users? - " << row[15] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWho will register users? - " << row[15] << endl;
                    }
                }
                if(anyUsr == "Yes" && usrRegist == "Yes")
                {
                    if(Stat == "Exist")
                    {
                        std::cout << "\t\tDoes the system have a user LogIn? - " << row[16] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system have a user LogIn? - " << row[16] << endl;
                    }
                }
                if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system allow users to enter any input? - " << row[17] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system allow users to enter any input? - " << row[17] << endl;
                    }
                }
                if(anyUsr == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system store user information? - " << row[18] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system store any user information? - " << row[18] << endl;
                    }
                }
                if(holdUsrInfo == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         flag_1 = 1;
                         std::cout << "\t\tDoes the system store any other information? - " << row[19] << endl;
                    }
                    else
                    {
                        flag_1 = 1;
                        std::cout << "\t\tWill the system store any other information? - " << row[19] << endl;
                    }
                }
                if(holdUsrInfo != "Yes" && flag_1 != 1)
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tDoes the system store any kind of information? - " << row[19] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWill the system store any kind of information? - " << row[19] << endl;
                    }
                }
                if(holdUsrInfo == "Yes" || storeAnyInfo == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat type of information does the system store? - " << row[20] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat type of information will the system store? - " << row[20] << endl;
                    }
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tWhat type of authentication is implemented in the system? - " << row[21] << endl;
                }
                else
                {
                    std::cout << "\t\tWhat type of authentication will be implemented in the system? - " << row[21] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes it store data in a database? - " << row[22] << endl;
                }
                else
                {
                    std::cout << "\t\tWill it store data in a database? - " << row[22] << endl;
                }
                if(useDb == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat is the type of data storage? - " << row[23] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat will be the type of data storage? - " << row[23] << endl;
                    }
                }
                if(useDb == "Yes")
                {
                    if(Stat == "Exist")
                    {
                         std::cout << "\t\tWhat type of database is used? - " << row[24] << endl;
                    }
                    else
                    {
                        std::cout << "\t\tWhat type of database will be used? - " << row[24] << endl;
                    }
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tWhat's the programming language used? (you can choose multiple options) \n";
                }
                else
                {
                    std::cout << "\t\tWhat programming language will be used? (you can choose multiple options) \n";
                }
				if(!progrm1.empty())
                {
                    cout << "\t\t  - " << row[25] << endl;
                }
                if(!progrm2.empty())
                {
                    cout << "\t\t  - " << row[26] << endl;
                }
                if(!progrm3.empty())
                {
                    cout << "\t\t  - " << row[27] << endl;
                }
                if(!progrm4.empty())
                {
                    cout << "\t\t  - " << row[28] << endl;
                }
                if(!progrm5.empty())
                {
                    cout << "\t\t  - " << row[29] << endl;
                }
                if(!progrm6.empty())
                {
                    cout << "\t\t  - " << row[30] << endl;
                }
                if(!progrm7.empty())
                {
                    cout << "\t\t  - " << row[31] << endl;
                }
                if(!progrm8.empty())
                {
                    cout << "\t\t  - " << row[32] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes it allow file uploads? - " << row[33] << endl;
                }
                else
                {
                    std::cout << "\t\tWill it allow file uploads? - " << row[33] << endl;
                }
                if(Stat == "Exist")
                {
                    std::cout << "\t\tDoes the system generate a log file? - " << row[34] << endl;
                }
                else
                {
                    std::cout << "\t\tWill the system generate a log file? - " << row[34] << endl;
                }
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}

         std::cout << endl << endl;

         std::cout<<"\t\tA BEST PRACTICE GUIDE FOR SECURE DEVELOPMENET OF IoT SYSTEMS IS BEING PREPARED  " << endl << endl;

         std::cout << "\n\n\n\n\t\t\t\t\t- - - - - - - - - -" <<endl ;

            fstream file;
            file.open("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\The_Tittle.md", ios::out | ios::trunc);
            if(file.is_open())
            {
                    file << "# The Best Practice Guidelines for Secure Development of IoT Systems for the User with Request ID Number: " << Request_ID << endl << endl;
					file.close();
             }
             else
             {
                cout <<"\n\tFile failed to open!" << endl;
             }

         Report r;

        std::string s1 = "Device_Mgmt",  s1_ = "Admin", s2 = "API_Service", s2_ = "Data_Collect", s3 = "Web", s3_ = "Embedded_Sys", s4 = "Data_Mgmt", s5 = "Data_Process", s6 = "Analytics", s7 = "Cloud_Service"; //s2_2 = "Yes", s3 = "No", s3_2 = "ng", s4 = "Yes";

        std::ofstream Best_Practice_Guide("Best_Practice_Guide_path");
        if(r.check_BP_condition("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\The_Tittle.md",  Best_Practice_Guide));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\IoT_Security_guide.md",  Best_Practice_Guide, Struct1, s1));
        if(Struct1.empty())
        {
             if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\IoT_Security_guide.md",  Best_Practice_Guide, Struct2, s2_));
        }
        if(Struct1.empty() && Struct2.empty())
        {
             if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\IoT_Security_guide.md",  Best_Practice_Guide, Struct10, s3_));
        }
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\API_guide.md",  Best_Practice_Guide, Struct4, s2));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Cross_Site_Scripting_guide.md",  Best_Practice_Guide, Struct9, s3));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Session_Management_guide.md",  Best_Practice_Guide, Struct9, s3));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Web_Service_guide.md",  Best_Practice_Guide, Struct9, s3));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Intrusion_Detection_guide.md",  Best_Practice_Guide, Struct5, s4));
        if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Access_Control_guide.md",  Best_Practice_Guide, typeOfRegist, s1_));
        if(Struct5.empty())
        {
             if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Intrusion_Detection_guide.md",  Best_Practice_Guide, Struct6, s5));
        }
        if(Struct5.empty() && Struct6.empty())
        {
             if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Intrusion_Detection_guide.md",  Best_Practice_Guide, Struct7, s6));
        }
        if(Struct5.empty() && Struct6.empty() && Struct7.empty())
        {
             if( r.check_BP_condition3("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Intrusion_Detection_guide.md",  Best_Practice_Guide, Struct8, s7));
        }
        if(r.check_BP_condition("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Authentication_guide.md",  Best_Practice_Guide));
        if(r.check_BP_condition2("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Input_Validation_guide.md",  Best_Practice_Guide, usrInput));
        if(r.check_BP_condition2("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\SQL_Injection_guide.md",  Best_Practice_Guide, useDb));
        if(r.check_BP_condition2("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\File_Upload_guide.md",  Best_Practice_Guide, fileUpload));
        if(r.check_BP_condition2("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Logging_guide.md",  Best_Practice_Guide, sysLog));
        if(r.check_BP_condition("C:\\Users\\Engr. M. G. Samaila\\Documents\\CodeBlocks_Projects\\IoT-HarPSecA_Tool\\Guides\\Cryptography_guide.md",  Best_Practice_Guide));

        cout << "\n\n\t\t\t\t   Press Enter to turn to the Main Menu" << endl;
    }

    void SecurityMngr::upLoadSecurity_Req()
    {
        cout << "\n\tUpload Security Requirements into the Database\n" << endl;
		cin.ignore(1, '\n');
		cout << "\tEnter Security Requirement ID: "; getline(cin, ID);
		cout << "\tEnter Acronym of Security Requirement: "; getline(cin, label);
		cout << "\tEnter Name of Security Requirement: "; getline(cin, reqmnt);

		string insert_query = "insert into security_reqmnts (ID, label, reqmnt) values('"+ID+"','"+label+"','"+reqmnt+"')";

		const char* qu = insert_query.c_str();
		qstate = mysql_query(conn, qu);

		if(!qstate)
		{
			cout << endl << "\tSuccessfully added into the database." << endl;
		}
		else
		{
			cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
		}
    }

    void SecurityMngr::retrieveSecurity_Req()
    {
        cout << "Enter the acronym of security requirement you want: "; cin >> label;

		string findbylabel_query = "select * from security_reqmnts where label like '%"+label+"%'";
		const char* ql = findbylabel_query.c_str();
		qstate = mysql_query(conn, ql);

		cout << endl << "Showing Cipher ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
				cout << "Requirement ID: " << row[0] << endl;
				cout << "Requirement Acronym: " << row[1] << endl;
				cout << "Security Requirement: " << row[2] << endl;
			}
		}
		else
		{
			cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
		}
    }

    void SecurityMngr::deleteSecurity_Req()
    {
        cout << "\n\tEnter the acronym of security requirement you want to delete: "; cin >> label;
        string delete_query = "delete from security_reqmnts where label = '"+label+"'";
        const char* qd = delete_query.c_str();
        qstate = mysql_query(conn, qd);

        if(!qstate)
        {
            cout << "\n\tSuccessfully Deleted from Database. " << endl;
        }
        else
        {
            cout << "\tFailed to Delete!" << mysql_errno(conn) << endl;
        }
    }

    void SecurityMngr::show_add_or_deleteSecurity_Req()
    {
         qstate = mysql_query(conn, "select * from security_reqmnts");
         system("cls");
		cout << "\tShowing supported security requirements .... " << endl << endl;

		if(!qstate)
		{
			res = mysql_store_result(conn);
			cout << "|ID |label |reqmnt|" << endl;
			cout << "---------------------" << endl;
			while((row = mysql_fetch_row(res)))
			{
				cout << "|" << row[0] << "|" << row[1] << "|" << row[2] << endl;
			}
		}
		else
		{
			cout << "Query error!" << mysql_errno(conn) << endl;
		}

        int choose;
      do{
            cout << "\n\tWhat do you want to do?" << endl;
            cout << "\t1. Add a security requirement " << endl;
            cout << "\t2. Delete a security requirement " << endl;
            cout << "\t3. Exit" << endl;
            cout << "\n\tSelect your choice: "; cin >> choose;

            switch(choose)
            {
                case 1:
                        upLoadSecurity_Req();
                        break;
                case 2:
                        deleteSecurity_Req();
                        break;
                case 3:
                        cout << "Exiting ...." << endl;
                        return;
                default:
                        cout << "Please choose a correct number" << endl;
            }
            cin.ignore();
            cin.get();
        }while(choose != 3);
    }

    void SecurityMngr::upLoadSecurity_Mech()
    {
        cout << "\n\tUpload Security Mechanisms into the Database" << endl << endl;
		cin.ignore(1, '\n');
		cout << "\tEnter Security Mechanism ID: "; getline(cin, M_ID);
		cout << "\tEnter Security Mechanism: "; getline(cin, mechanism);

		string insert_query = "insert into security_mechns (M_ID, mechanism) values('"+M_ID+"','"+mechanism+"')";

		const char* qu = insert_query.c_str();
		qstate = mysql_query(conn, qu);

		if(!qstate)
		{
			cout << endl << "\n\tSuccessfully added into the database." << endl;
		}
		else
		{
			cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
		}
    }

    void SecurityMngr::retrieveSecurity_Mech()
    {
        cout << "Enter the ID of security mechanism you want: "; cin >> M_ID;

		string findbyID_query = "select * from security_mechns where M_ID like '%"+M_ID+"%'";
		const char* qr = findbyID_query.c_str();
		qstate = mysql_query(conn, qr);

		cout << endl << "Showing Security mechanism ...." << endl << endl;
		if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
				cout << "Mechanism ID: " << row[0] << endl;
				cout << "Mechanism: " << row[1] << endl;
			}
		}
		else
		{
			cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
		}
    }

    void SecurityMngr::deleteSecurity_Mech()
    {
        cout << "\n\tEnter the ID of security mechanism you want to delete: "; cin >> M_ID;
        string delete_query = "delete from security_mechns where M_ID = '"+M_ID+"'";
        const char* qd = delete_query.c_str();
        qstate = mysql_query(conn, qd);

        if(!qstate)
        {
            cout << "\n\tSuccessfully Deleted from Database. " << endl;
        }
        else
        {
            cout << "\tFailed to Delete!" << mysql_errno(conn) << endl;
        }
    }

    void SecurityMngr::show_add_or_deleteSecurity_Mech()
    {
         qstate = mysql_query(conn, "select * from security_mechns");
         system("cls");
		cout << "\tShowing supported security mechanisms .... " << endl << endl;

		if(!qstate)
		{
			res = mysql_store_result(conn);
			cout << "|M_ID |mechanism |" << endl;
			cout << "------------------" << endl;
			while((row = mysql_fetch_row(res)))
			{
				cout << "|" << row[0] << "|" << row[1] << endl;
			}
		}
		else
		{
			cout << "Query error!" << mysql_errno(conn) << endl;
		}

         int choose;
      do{
            cout << "\n\n\tWhat do you want to do?" << endl;
            cout << "\t1. Add a security mechanism " << endl;
            cout << "\t2. Delete a security mechanism " << endl;
            cout << "\t3. Exit " << endl;
            cout << "\n\tSelect your choice: "; cin >> choose;

            switch(choose)
            {
                case 1:
                        upLoadSecurity_Mech();
                        break;
                case 2:
                        deleteSecurity_Mech();
                        break;
                case 3:
                        cout << "Exiting ...." << endl;
                        return;
                default:
                        cout << "Please choose a correct number" << endl;
            }
            cin.ignore();
            cin.get();
        }while(choose != 3);
    }

    void SecurityMngr::decisionMaker()
    {
           UserInput usrIp;
           Processing_and_Output po;
            string Request_ID;
            system("cls");
            std::cout << "\n***********************************************************************************************************\n";
            std::cout<<"\t\tREQUEST PROCESSING\n\n";
            cout << "\tPlease enter your Request ID: "; cin >> Request_ID;

            Preliminary pre;

            pre.convert_lowerC_to_upperC(Request_ID);

            int num_digits;
            int string_length;
            char first_letter;

            auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
            num_digits = collector.n1;
            string_length = collector.n2;
            first_letter = collector.c;

            while(num_digits !=4 || string_length != 5 || (first_letter != 'S' && first_letter != 'H'))
            {
                system("cls");
                std::cout << "\n***********************************************************************************************************\n";
                std::cout << "\n\t\t\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n";

                std::cout << "\n\t\t\t\tPlease enter a valid request ID: ";
                std::cin >> Request_ID;

                pre.convert_lowerC_to_upperC(Request_ID);

                auto collector = usrIp.countDigits_lengthOfString_firstCharacter(Request_ID);
                num_digits = collector.n1;
                string_length = collector.n2;
                first_letter = collector.c;
            }

            int implemtn_type = pre.determine_requestType(Request_ID);

            system("cls");
            switch(implemtn_type)
            {
                case 1:

                    {
                        string findbyID_query = "select * from users_requests_2 where Request_ID = " + ("'"+Request_ID+"'");
                        const char* qn = findbyID_query.c_str();
                        qstate = mysql_query(conn, qn);

                        if(!qstate)
                        {
                            string type, as, ps, energy, r1, ccta1, tp1, r2, ccta2, tp2, r3, ccta3, tp3, r4, ccta4, tp4, r5, ccta5, tp5, r6, ccta6, tp6;
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                type = row[1];
                                as = row[2];
                                ps = row[3];
                                energy = row[4];
                                r1 = row[5];
                                ccta1 = row[6];
                                tp1 = row[7];
                                r2 = row[8];
                                ccta2 = row[9];
                                tp2 = row[10];
                                r3 = row[11];
                                ccta3 = row[12];
                                tp3 = row[13];
                                r4 = row[14];
                                ccta4 = row[15];
                                tp4 = row[16];
                                r5 = row[17];
                                ccta5 = row[18];
                                tp5 = row[19];
                                r6 = row[20];
                                ccta6 = row[21];
                                tp6 = row[22];
                            }

                                double ccta1_doub = atof(ccta1.c_str());
                                double tp1_doub = atof(tp1.c_str());
                                double ccta2_doub = atof(ccta2.c_str());
                                double tp2_doub = atof(tp2.c_str());
                                double ccta3_doub = atof(ccta3.c_str());
                                double tp3_doub = atof(tp3.c_str());
                                double ccta4_doub = atof(ccta4.c_str());
                                double tp4_doub = atof(tp4.c_str());
                                double ccta5_doub = atof(ccta5.c_str());
                                double tp5_doub = atof(tp5.c_str());
                                double ccta6_doub = atof(ccta6.c_str());
                                double tp6_doub = atof(tp6.c_str());

                                system("cls");

                                string userReqmnts, Req1 = "CONF", Req2 = "INTG", Req3 = "AUTH", Req4 = "PRIV", Req5 = "NONR", Req6 = "COAU";

                                if(type == "FPGA")
                                {

                                         int flag1, flag2, flag3, flag4, flag5, flag6;

                                             auto searchingResult = po.mapping1b(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                             flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                             flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;


                                         int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                         auto result_Al2 = po.mapping2Hardware(flag1, flag2, flag3, flag4, flag5, flag6, ccta1_doub, tp1_doub, ccta2_doub, tp2_doub, ccta3_doub, tp3_doub, ccta4_doub, tp4_doub, ccta5_doub, tp5_doub, ccta6_doub, tp6_doub, as, ps, type);

                                         algo1 = result_Al2.int_1; ps1 = result_Al2.p1; algo2 = result_Al2.int_2; algo3 = result_Al2.int_3;
                                         algo4 = result_Al2.int_4; ps4 = result_Al2.p4; algo5 = result_Al2.int_5; algo6 = result_Al2.int_6;
                                         ps6 = result_Al2.p6;

                                         string alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name;
                                         auto result_algo_name_HW = po.display_Mech_Algo_mapping2(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6, energy);

                                         alg1_name = result_algo_name_HW.st1; alg2_name = result_algo_name_HW.st2; alg3_name = result_algo_name_HW.st3;
                                         alg4_name = result_algo_name_HW.st4; alg5_name = result_algo_name_HW.st5; alg6_name = result_algo_name_HW.st6;

                                         double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                         int warn1 = 0;

                                         po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name, totalAlgoWeight, warn1, Request_ID);

                                         double fms = 0, rs = 0, fms_ = 0, rs_ = 0;
                                         po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name, totalAlgoWeight, fms, rs, fms_, rs_, Request_ID);

                                }
                                else if(type == "ASIC")
                                {

                                          int flag1, flag2, flag3, flag4, flag5, flag6;

                                             auto searchingResult = po.mapping1b(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                             flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                             flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                        int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                         auto result_Al2 = po.mapping2Hardware(flag1, flag2, flag3, flag4, flag5, flag6, ccta1_doub, tp1_doub, ccta2_doub, tp2_doub, ccta3_doub, tp3_doub, ccta4_doub, tp4_doub, ccta5_doub, tp5_doub, ccta6_doub, tp6_doub, as, ps, type);

                                         algo1 = result_Al2.int_1; ps1 = result_Al2.p1; algo2 = result_Al2.int_2; algo3 = result_Al2.int_3;
                                         algo4 = result_Al2.int_4; ps4 = result_Al2.p4; algo5 = result_Al2.int_5; algo6 = result_Al2.int_6;
                                         ps6 = result_Al2.p6;

                                         string alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name;
                                         auto result_algo_name_HW = po.display_Mech_Algo_mapping2(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6, energy);

                                         alg1_name = result_algo_name_HW.st1; alg2_name = result_algo_name_HW.st2; alg3_name = result_algo_name_HW.st3;
                                         alg4_name = result_algo_name_HW.st4; alg5_name = result_algo_name_HW.st5; alg6_name = result_algo_name_HW.st6;

                                         double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                         int warn1 = 0;

                                         po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name, totalAlgoWeight, warn1, Request_ID);

                                         double fms = 0, rs = 0, fms_ = 0, rs_ = 0;
                                         po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, alg1_name, alg2_name, alg3_name, alg4_name, alg5_name, alg6_name, totalAlgoWeight, fms, rs, fms_, rs_, Request_ID);
                                }
                                else
                                {
                                    cout << "\n\n\n\n\n\n\n\t\t\tERROR! THIS REQUEST ID DOES NOT EXIST IN THE DATABASE." << endl;

                                      cout << "\n\n\n\n\n\n\n\t\t\tPress Enter to return to Main Menu and try again. " << endl;
                                }
                        }
                        else
                        {
                            cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                        }
                     }

                    break;
                case 2:
                    {
                                level_:
                                char ch;
                                system("cls");
                                std::cout<<"\n" "***********************************************************************************************************\n";
                                std::cout << "\n\tWhat is the development phase of the IoT system, or it is an existing system? \n";

                                std::cout<<"\n\t\t1. Conception, Planning, Analysis, Design";
                                std::cout<<"\n\t\t2. Existing System ";
                                std::cout<<"\n\n\tSelect Your Option (1-2): ";

                                std::cin>>ch;

                                switch(ch)
                                {
                                        case '1':
                                             {
                                                    system("cls");
                                                    std::cout << "\n" "***********************************************************************************************************\n";
                                                    std::cout<<"\n\t\tABOUT BE TO DESIGNED\n\n";
                                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                    std::cin.ignore();

                                                    if(cin.get() == '\n')
                                                    {
                                                                string findbyID_query = "select * from users_requests where Request_ID = " + ("'"+Request_ID+"'");
                                                                const char* qn = findbyID_query.c_str();
                                                                qstate = mysql_query(conn, qn);

                                                                if(!qstate)
                                                                {
                                                                     string type, cpu, fms, rs, cs, as, ps, r1, r2, r3, r4, r5, r6;
                                                                    res = mysql_store_result(conn);
                                                                    while((row = mysql_fetch_row(res)))
                                                                    {
                                                                        type = row[1];
                                                                        cpu = row[2];
                                                                        fms = row[3];
                                                                        rs = row[4];
                                                                        cs = row[5];
                                                                        as = row[6];
                                                                        ps = row[7];
                                                                        r1 = row[8];
                                                                        r2 = row[9];
                                                                        r3 = row[10];
                                                                        r4 = row[11];
                                                                        r5 = row[12];
                                                                        r6 = row[13];
                                                                    }
                                                                        stringstream Num(cpu);

                                                                        int cpu_int;
                                                                        Num >> cpu_int;
                                                                        double fms_doub = atof(fms.c_str());
                                                                        double rs_doub = atof(rs.c_str());
                                                                        double cs_doub = atof(cs.c_str());

                                                                        system("cls");

                                                                        string userReqmnts, Req1 = "CONF", Req2 = "INTG", Req3 = "AUTH", Req4 = "PRIV", Req5 = "NONR", Req6 = "COAU";

                                                                        if(type == "SBC")
                                                                        {
                                                                            int cpu = 32;
                                                                            double flash = 2000000.00, ram = 252000, clock = 400.00, flash_, ram_;
                                                                            flash_ = 0.05*flash + flash;
                                                                            bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                            if(!capable)
                                                                            {
                                                                                cout << "\n\n\n\n\n\n\t\tERROR! Hardware specifications not typical of SBCs.\n\n\n\n";

                                                                                cout << "\n\t Please, press Enter to return to Main Menu and make another request.";
                                                                            }
                                                                            else
                                                                            {
                                                                                 int flag1, flag2, flag3, flag4, flag5, flag6;
                                                                                 auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                 flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                 flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                 int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                 auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                 algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                 algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                 ps6 = result_Al.p6;

                                                                                string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                            }
                                                                        }
                                                                        else
                                                                        {
                                                                          if(type == "AVR")
                                                                            {
                                                                               int cpu = 8;
                                                                               double flash = 48.00, ram = 4.00, clock = 16.00, flash_, ram_;
                                                                               flash_ = 0.03*flash + flash;
                                                                               ram_ = 0.02*ram + ram;
                                                                               bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {

                                                                                    cout << "\n\n\n\n\n\n\n\tSORRY! Your MCU is too constrained for the cryptographic algorithms in the database.\n\n\n\n";

                                                                                    cout << "\n\t Please, press Enter to return to Main Menu and make another request, or exit.";
                                                                                }
                                                                                else
                                                                                {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                    string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                    auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                    algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                    algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                    double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                    int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                    po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                    pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                    po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                            }
                                                                            else if(type =="MSP")
                                                                            {
                                                                                int cpu = 16;
                                                                                double flash = 48.00, ram = 8.00, clock = 8.00, flash_, ram_;
                                                                                flash_ = 0.05*flash + flash;
                                                                                ram_ = 0.04*ram + ram;
                                                                               bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {
                                                                                    cout << "\n\n\n\n\n\n\n\tSORRY! Your MCU is too constrained for the cryptographic algorithms in the database.\n\n\n\n";

                                                                                    cout << "\n\t Please, press Enter to return to Main Menu and make another request, or exit.";
                                                                                }
                                                                                else
                                                                                {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                       string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                        auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                        algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                        algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                        double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                        int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                        pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                            }
                                                                            else if(type == "ARM")
                                                                            {
                                                                                int cpu = 32;
                                                                                double flash = 256.00, ram = 64.00, clock = 72.00, flash_, ram_;
                                                                                flash_ = 0.05*flash + flash;
                                                                                ram_ = 0.04*ram + ram;
                                                                               bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {
                                                                                    cout << "\n\n\n\n\n\n\n\tSORRY! Your MCU is too constrained for the cryptographic algorithms in the database.\n\n\n\n";

                                                                                    cout << "\n\t Please, press Enter to return to Main Menu and make another request, or exit.";
                                                                                }
                                                                                else
                                                                                {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;


                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                       string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                        auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                        algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                        algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                        double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                        int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                        pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                            }
                                                                            else if(type == "PIC")
                                                                            {
                                                                                int cpu = 8;
                                                                                double flash = 28.00, ram = 4.00, clock = 4.00, flash_, ram_;
                                                                                flash_ = 0.09*flash + flash;
                                                                                ram_ = 0.04*ram + ram;
                                                                               bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {
                                                                                    cout << "\n\n\n\n\n\n\n\tSORRY! Your MCU is too constrained for the cryptographic algorithms in the database.\n\n\n\n";

                                                                                    cout << "\n\t Please, press Enter to return to Main Menu and make another request, or exit.";
                                                                                }
                                                                                else
                                                                                {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;


                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                       string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                        auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                        algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                        algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                        double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                        int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                        pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                            }
                                                                            else if((type != "AVR" || type != "MSP" || type != "ARM" || type != "PIC") && !cpu.empty())
                                                                            {
                                                                                int cpu = 4;
                                                                                double flash = 38.00, ram = 4.00, clock = 10.00, flash_, ram_;
                                                                                flash_ = 0.05*flash + flash;
                                                                                ram_ = 0.04*ram + ram;
                                                                                bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {
                                                                                    cout << "\n\n\n\n\n\n\n\tSORRY! Your MCU is too constrained for the cryptographic algorithms in the database.\n\n\n\n";

                                                                                    cout << "\n\t Please, press Enter to return to Main Menu and make another request, or exit.";
                                                                                }
                                                                                else
                                                                                {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2(flag1, flag2, flag3, flag4, flag5, flag6, cpu_int, fms_doub, rs_doub, as, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                       string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                        auto result_algo_name_SW = po.display_Mech_Algo_mapping(algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                        algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                        algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                        double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);
                                                                                        int warn1 = pre.warning1(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.displayReq_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, warn1, Request_ID);

                                                                                        pre.warning2(totalAlgoWeight, fms_doub, rs_doub, flash_, ram_);

                                                                                        po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                            }
                                                                            else
                                                                            {
                                                                                int cpu = 4;
                                                                                double flash = 38.00, ram = 4.00, clock = 10.00, flash_, ram_;
                                                                                flash_ = 0.05*flash + flash;
                                                                                ram_ = 0.04*ram + ram;
                                                                                bool capable = po.isCapable(cpu_int, fms_doub, rs_doub, cs_doub, cpu, flash, ram, clock);
                                                                                if(!capable)
                                                                                {
                                                                                    cout << "\n\n\n\n\n\n\n\t\t\tERROR! THIS REQUEST ID DOES NOT EXIST IN THE DATABASE." << endl;

                                                                                    cout << "\n\n\n\n\n\n\n\t\t\tPress Enter to return to Main Menu and try again. " << endl;
                                                                                }
                                                                            }

                                                                        }
                                                                }
                                                                else
                                                                {
                                                                    cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                                                                }

                                                        }
                                                        else
                                                        {
                                                            goto level_;
                                                        }
                                                break;
                                                }
                                        case '2':
                                            {
                                                    system("cls");
                                                    std::cout << "\n" "***********************************************************************************************************\n";
                                                    std::cout<<"\n\t\tEXISTING SYSTEM\n";
                                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                    std::cin.ignore();

                                                    if(cin.get() == '\n')
                                                    {
                                                                string type, cpu, cs, ad, ps, r1, fm1, ram1, r2, fm2, ram2, r3, fm3, ram3, r4, fm4, ram4, r5, fm5, ram5, r6, fm6, ram6;
                                                                string findbyID_query = "select * from users_requests_ where Request_ID = " + ("'"+Request_ID+"'");
                                                                const char* qn = findbyID_query.c_str();
                                                                qstate = mysql_query(conn, qn);

                                                                if(!qstate)
                                                                {
                                                                        res = mysql_store_result(conn);
                                                                        while((row = mysql_fetch_row(res)))
                                                                        {
                                                                            type = row[1];
                                                                            cpu = row[2];
                                                                            cs = row[3];
                                                                            ad = row[4];
                                                                            ps = row[5];
                                                                            r1 = row[6];
                                                                            fm1 = row[7];
                                                                            ram1 = row[8];
                                                                            r2 = row[9];
                                                                            fm2 = row[10];
                                                                            ram2 = row[11];
                                                                            r3 = row[12];
                                                                            fm3 = row[13];
                                                                            ram3 = row[14];
                                                                            r4 = row[15];
                                                                            fm4 = row[16];
                                                                            ram4 = row[17];
                                                                            r5 = row[18];
                                                                            fm5 = row[19];
                                                                            ram5 = row[20];
                                                                            r6 = row[21];
                                                                            fm6 = row[22];
                                                                            ram6 = row[23];
                                                                        }

                                                                            stringstream Num(cpu);

                                                                            int cpu_int;
                                                                            Num >> cpu_int;

                                                                            double cs_doub = atof(cs.c_str());

                                                                            double fm1_doub = atof(fm1.c_str());
                                                                            double ram1_doub = atof(ram1.c_str());
                                                                            double fm2_doub = atof(fm2.c_str());
                                                                            double ram2_doub = atof(ram2.c_str());
                                                                            double fm3_doub = atof(fm3.c_str());
                                                                            double ram3_doub = atof(ram3.c_str());
                                                                            double fm4_doub = atof(fm4.c_str());
                                                                            double ram4_doub = atof(ram4.c_str());
                                                                            double fm5_doub = atof(fm5.c_str());
                                                                            double ram5_doub = atof(ram5.c_str());
                                                                            double fm6_doub = atof(fm6.c_str());
                                                                            double ram6_doub = atof(ram6.c_str());

                                                                            system("cls");

                                                                            string userReqmnts, Req1 = "CONF", Req2 = "INTG", Req3 = "AUTH", Req4 = "PRIV", Req5 = "NONR", Req6 = "COAU";

                                                                        if(type == "SBC")
                                                                        {

                                                                                 int flag1, flag2, flag3, flag4, flag5, flag6;
                                                                                 auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                 flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                 flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                 int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                 auto result_Al = po.mapping2_3(flag1, flag2, flag3, flag4, flag5, flag6, fm1_doub, ram1_doub, fm2_doub, ram2_doub, fm3_doub, ram3_doub, fm4_doub, ram4_doub, fm5_doub, ram5_doub, fm6_doub, ram6_doub, ad, ps);

                                                                                 algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                 algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                 ps6 = result_Al.p6;

                                                                                string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                auto result_algo_name_SW = po.display_Mech_Algo_mapping3(type, algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                double totalAlgoWeight = po.reqWeighting(flag1, flag2, flag3, flag4, flag5, flag6);

                                                                                po.displayReq_Mech_mapping3(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, Request_ID);

                                                                                double rs_doub = 0.0, fms_doub = 0.0, flash_ = 0.0, ram_ = 0.0;
                                                                               po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                        }
                                                                        else
                                                                        {
                                                                          if(type == "AVR")
                                                                            {
                                                                                      int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                      auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                       flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                       flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                       int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                       auto result_Al = po.mapping2_3(flag1, flag2, flag3, flag4, flag5, flag6, fm1_doub, ram1_doub, fm2_doub, ram2_doub, fm3_doub, ram3_doub, fm4_doub, ram4_doub, fm5_doub, ram5_doub, fm6_doub, ram6_doub, ad, ps);

                                                                                       algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                       algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                       ps6 = result_Al.p6;

                                                                                    string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                    auto result_algo_name_SW = po.display_Mech_Algo_mapping3(type, algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                    algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                    algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                     po.displayReq_Mech_mapping3(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, Request_ID);

                                                                                    double rs_doub = 0.0, fms_doub = 0.0, flash_ = 0.0, ram_ = 0.0, totalAlgoWeight = 0.0;
                                                                                     po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                }
                                                                                else if(type =="MSP")
                                                                                {
                                                                                              int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                              auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                               flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                               flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                               int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                              auto result_Al = po.mapping2_3(flag1, flag2, flag3, flag4, flag5, flag6, fm1_doub, ram1_doub, fm2_doub, ram2_doub, fm3_doub, ram3_doub, fm4_doub, ram4_doub, fm5_doub, ram5_doub, fm6_doub, ram6_doub, ad, ps);

                                                                                               algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                               algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                               ps6 = result_Al.p6;

                                                                                               string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                                auto result_algo_name_SW = po.display_Mech_Algo_mapping3(type, algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                                algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                                algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                               po.displayReq_Mech_mapping3(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, Request_ID);

                                                                                                double rs_doub = 0.0, fms_doub = 0.0, flash_ = 0.0, ram_ = 0.0, totalAlgoWeight = 0.0;
                                                                                                po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                    }
                                                                                    else if(type == "ARM")
                                                                                    {
                                                                                              int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                              auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                               flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                               flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;


                                                                                               int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                             auto result_Al = po.mapping2_3(flag1, flag2, flag3, flag4, flag5, flag6, fm1_doub, ram1_doub, fm2_doub, ram2_doub, fm3_doub, ram3_doub, fm4_doub, ram4_doub, fm5_doub, ram5_doub, fm6_doub, ram6_doub, ad, ps);

                                                                                               algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                               algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                               ps6 = result_Al.p6;

                                                                                               string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                               auto result_algo_name_SW = po.display_Mech_Algo_mapping3(type, algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                                algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                                algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;


                                                                                                po.displayReq_Mech_mapping3(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, Request_ID);

                                                                                                  double rs_doub = 0.0, fms_doub = 0.0, flash_ = 0.0, ram_ = 0.0, totalAlgoWeight = 0.0;
                                                                                                  po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                    }
                                                                                    else if((type != "AVR" || type != "MSP" || type != "ARM" || type != "PIC") && !cpu.empty())
                                                                                    {
                                                                                              int flag1, flag2, flag3, flag4, flag5, flag6;

                                                                                              auto searchingResult = po.mapping1(userReqmnts, r1, r2, r3, r4, r5, r6, Req1, Req2, Req3, Req4, Req5, Req6);

                                                                                               flag1 = searchingResult.int1;  flag2 = searchingResult.int2;  flag3 = searchingResult.int3;
                                                                                               flag4 = searchingResult.int4; flag5 = searchingResult.int5;  flag6 = searchingResult.int6;

                                                                                               int algo1, ps1, algo2, algo3, algo4, ps4, algo5, algo6, ps6;

                                                                                               auto result_Al = po.mapping2_3(flag1, flag2, flag3, flag4, flag5, flag6, fm1_doub, ram1_doub, fm2_doub, ram2_doub, fm3_doub, ram3_doub, fm4_doub, ram4_doub, fm5_doub, ram5_doub, fm6_doub, ram6_doub, ad, ps);

                                                                                               algo1 = result_Al.int_1; ps1 = result_Al.p1; algo2 = result_Al.int_2; algo3 = result_Al.int_3;
                                                                                               algo4 = result_Al.int_4; ps4 = result_Al.p4; algo5 = result_Al.int_5; algo6 = result_Al.int_6;
                                                                                               ps6 = result_Al.p6;

                                                                                               string algName1, algName2, algName3, algName4, algName5, algName6;
                                                                                               auto result_algo_name_SW = po.display_Mech_Algo_mapping3(type, algo1, algo2, algo3, algo4, algo5, algo6, ps1, ps4, ps6);

                                                                                                algName1 = result_algo_name_SW.st_1; algName2 = result_algo_name_SW.st_2; algName3 = result_algo_name_SW.st_3;
                                                                                                algName4 = result_algo_name_SW.st_4; algName5 = result_algo_name_SW.st_5; algName6 = result_algo_name_SW.st_6;

                                                                                                po.displayReq_Mech_mapping3(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, Request_ID);

                                                                                                 double rs_doub = 0.0, fms_doub = 0.0, flash_ = 0.0, ram_ = 0.0, totalAlgoWeight = 0.0;
                                                                                                 po.write_Req_Mech_mapping(flag1, flag2, flag3, flag4, flag5, flag6, algName1, algName2, algName3, algName4, algName5, algName6, totalAlgoWeight, fms_doub, rs_doub, flash_, ram_, Request_ID);
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                            cout << "\n\n\n\n\n\n\n\t\t\tERROR! THIS REQUEST ID DOES NOT EXIST IN THE DATABASE." << endl;

                                                                                            cout << "\n\n\n\n\n\n\n\t\t\tPress Enter to return to Main Menu and try again. " << endl;
                                                                                    }

                                                                                }
                                                                }
                                                                else
                                                                {
                                                                    cout << "Query Execution Problems!" << mysql_errno(conn) << endl;
                                                                }


                                                    }
                                                    else
                                                    {
                                                        goto level_;
                                                    }
                                                    break;
                                                }
                                        default:
                                            std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        goto level_;
                                }
                    }
                    break;
                default:
                    system("cls");
                     std::cout << "\n\n\n\n\n\n\n\n\n\t  ERROR! YOU HAVE ENTERED AN INVALID REQUEST ID.\n\n\n";
                     std::cout << "\n\tPress Enter to return to the Main Menu and try again.";
                break;
            }
    }

class LoginManager
{
	public:
	LoginManager();
	void setAuthorized_to_be_Admin();
	bool getAuthorized_to_be_Admin();
	string maskPassword();
	string check_password_Strength(string& password);
	string combine_mask_and_check();
	string maskPassword2();
	bool IsLoggedIn(bool admin);
	void registration(bool flag);
	int login(bool admin);
	void show_and_deleteUser_Registr();
	void add_one_more_Admin();
	int general_login();
};

    LoginManager::LoginManager()
	{

	}

	void LoginManager::setAuthorized_to_be_Admin()
	{
	    authorized_to_be_Admin = true;
	}

	bool LoginManager::getAuthorized_to_be_Admin()
	{
	    return authorized_to_be_Admin;
	}

    string LoginManager::maskPassword()
    {
        int ch;
        string password = "";

        cout << "\n\t""Enter your password: ";

        while(ch = getch())
        {
            if(ch == 13)
            {

                return password;
            }
            else if(ch == 8)
            {
                if(password.length() > 0)
                {
                    cout << "\b \b";
                    password.erase(password.length() - 1);
                }
            }
            else
            {
                cout << "*";
                password += ch;
            }
        }
    }

string LoginManager::check_password_Strength(string& password)
{
    int n = password.length();
    bool hasLower = false, hasUpper = false;
    bool hasDigit = false, specialChar = false;
    string normalChars = "abcdefghijklmnopqrstu"
        "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ";

    for (int i = 0; i < n; i++) {
        if (islower(password[i]))
            hasLower = true;
        if (isupper(password[i]))
            hasUpper = true;
        if (isdigit(password[i]))
            hasDigit = true;

        size_t special = password.find_first_not_of(normalChars);
        if (special != string::npos)
            specialChar = true;
    }

    system("cls");
    cout << "\n\tYour password is: ";
    if (hasLower && hasUpper && hasDigit && specialChar && (n >= 8))
    {
       cout << "Strong" << endl;
       strength = 3;
       return password;
    }
    else if ((hasLower || hasUpper) && specialChar && (n >= 6))
    {
        cout << "Moderate" << endl;
        strength = 2;
        return password;
    }
    else
    {
        cout << "Weak\n" << endl;
        cout << "\tA GOOD PASSWORD SHOULD CONTAIN AT LEAST 1 LOWERCASE, 1 UPPERCASE, AND 1 SPECIAL CHARACTER; "<< endl;
        cout << "\t \t\t\t  AND ITS LENGTH SHOULD BE AT LEAST 6.  " << endl;
        strength = 1;
    }
}

string LoginManager::combine_mask_and_check()
{
	string pw;

    do
    {
        string password = maskPassword();
        pw = check_password_Strength(password);

    }while(strength == 1);

	return pw;
}

    string LoginManager::maskPassword2()
    {
        int ch;
        string password = "";

        cout << "\n\tPlease re-enter your password: ";

        while(ch = getch())
        {
            if(ch == 13)
            {
                return password;
            }
            else if(ch == 8)
            {
                if(password.length() > 0)
                {
                    cout << "\b \b";
                    password.erase(password.length() - 1);
                }
            }
            else
            {
                cout << "*";
                password += ch;
            }
        }
    }

    bool LoginManager::IsLoggedIn(bool admin)
	{
		std::string username, password, usernameAd, passwordAd, un, pw, un_Ad, pw_Ad, st, st_Ad, AdminID, UserID;
		if(!admin)
        {
            system("cls");
            std::cout << "\n" "***********************************************************************************************************\n";
            std::cout << "\tUSER LOGIN \n" << endl;
            std::cout << "\t""Enter your username: "; std::cin >> username;
            password = maskPassword();
        }
        else
        {
            system("cls");
            std::cout << "\n" "***********************************************************************************************************\n";
            std::cout << "\tADMIN LOGIN \n" << endl;
            std::cout << "\t""Enter your username: "; std::cin >> usernameAd;
             passwordAd = maskPassword();
        }

        if(!admin)
        {
            string findbyname_query = "select * from users_hashedpassword where username like '%"+username+"%'";
            const char* qn = findbyname_query.c_str();
            qstate = mysql_query(conn, qn);
        }
        else
        {
            string findbyname_query = "select * from admin_hashedpassword2 where usernameAd like '%"+usernameAd+"%'";
            const char* qn = findbyname_query.c_str();
            qstate = mysql_query(conn, qn);
        }

        if(!qstate)
		{
			res = mysql_store_result(conn);
			while((row = mysql_fetch_row(res)))
			{
                if(!admin)
                {
                   UserID = row[0];
                   un = row[1];
                   pw = row[2];
                   st = row[3];
                }
                else
                {
                   AdminID = row[0];
                   un_Ad = row[1];
                   pw_Ad = row[2];
                   st_Ad = row[3];
                }
			}
		}
		else
		{
			cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
		}


        string output1;

        if(!admin)
        {
            const string input = password + st;//*
            output1 = sha256(input);//*
        }
        else
        {
            const string input = passwordAd + st_Ad;//*
            output1 = sha256(input);//*
        }


		if((un_Ad == usernameAd && pw_Ad == output1)||(un == username && pw == output1))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	void LoginManager::add_one_more_Admin()
	{
	     string AdminUser, usernameAd;
          ;
	     char result;
	     system("cls");
	     std::cout << "\n" "***********************************************************************************************************\n"
                      " \t\t\t\t\t   WARNING!" "\n" "\n"
                      "\n\tAre you sure you want to allow the creation of a second Admin account? (y/n): "; cin >> result;

	     if(result == 'y' || result == 'Y')
         {
                string findbyname_query = "select * from admin_hashedpassword2 where usernameAd like '%"+usernameAd+"%'";
                 const char* qn = findbyname_query.c_str();
                 qstate = mysql_query(conn, qn);

                if(!qstate)
                {
                    res = mysql_store_result(conn);
                    while((row = mysql_fetch_row(res)))
                    {
                        AdminUser = row[1];
                    }
                }
                else
                {
                    cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
                }

                if(AdminUser == "Admin1")
                {
                   system("cls");
                    std::cout << "\n" "***********************************************************************************************************\n"
                                " \t\t\t\t\tWARNING!" "\n" "\n"
                                "\n\t\tYou have just allowed the creation of a new Admin account! \n"
                                "\n\n\t\t\t Press Enter to return to the Admin Menu." << endl;
                   setAuthorized_to_be_Admin();
                }
                else
                {
                   system("cls");
                         std::cout << "\n" "***********************************************************************************************************\n"
                                      " \t\t\t\t\t\tWARNING!" "\n" "\n"
                                      "\n\t\t\tSORRY! A second Admin account has been created already.\n"
                                      "\n\n\t\t\t Press Enter to return to the Admin Menu." << endl;
                        return;
                }
         }
         else
         {
            std::cout << "\n\n\t\t\t Press Enter to return to the Admin Menu." << endl;
             return;
         }
	}

	void LoginManager::registration(bool flag)
	{
			std::string username, un, password, password2, usernameAd, passwordAd, passwordAd2, AdminID, AdminUser;

			if(flag)
            {
                system("cls");
                std::cout<<"\n" "***********************************************************************************************************\n";
                std::cout << "\n\tPlease enter a username: "; std::cin >> username;
            }
            else
            {
                    system("cls");

                     string findbyname_query = "select * from admin_hashedpassword2 where usernameAd like '%"+usernameAd+"%'";
                    const char* qn = findbyname_query.c_str();
                    qstate = mysql_query(conn, qn);

                     if(!qstate)
                        {
                            res = mysql_store_result(conn);
                            while((row = mysql_fetch_row(res)))
                            {
                                AdminUser = row[1];
                            }
                        }
                        else
                        {
                            cout << "\tQuery Execution Problems!" << mysql_errno(conn) << endl;
                        }

                     if(AdminUser.empty())
                     {
                         authorized_to_be_Admin = true;


                     }
                     if(AdminUser.empty() || authorized_to_be_Admin == true)
                     {
                         system("cls");
                         if(AdminUser.empty())
                         {
                             std::cout << "\n\tYOUR USERNAME IS Admin1: \n" << endl;
                             usernameAd = "Admin1";
                         }
                         else
                         {
                             do
                             {
                                 system("cls");
                                 std::cout << "\n\tPlease enter any Admin username except Admin1: "; std::cin >> usernameAd;
                             }while(usernameAd == "Admin1");

                         }
                     }
                     else
                     {
                         system("cls");
                         std::cout << "\n" "***********************************************************************************************************\n"
                                      " \t\t\t\t\t\tWARNING!" "\n"
                                      "\n\n\n\t\t\t  SORRY! YOU ARE NOT AUTHORIZE TO REGISTER AS ADMIN.\n"
                                      "\n\n\t\t\t  Press Enter to return to Registration/Login Menu." << endl;
                         return;
                     }
            }

             if(flag)
             {
                 password = combine_mask_and_check();
                 password2 = maskPassword2();

                while (password != password2)
                {
                    system("cls");
                    std::cout << "\n\tError! Passwords do not match." "\n";
                    password = combine_mask_and_check();
                    password2 = maskPassword2();
                }
             }
             else
              {
                passwordAd = combine_mask_and_check();
                passwordAd2 = maskPassword2();

                while (passwordAd != passwordAd2)
                {
                    system("cls");
                    std::cout << "\n\tError! Passwords do not match." "\n";
                    passwordAd = combine_mask_and_check();
                    passwordAd2 = maskPassword2();
                }
              }

            if(flag)
              {
                string salt = generateSalt();
                const string input = password + salt;
                string output1 = sha256(input);
                string hashedPassword = output1;
                string insert_query = "insert into users_hashedpassword (username, hashedPassword, salt) values('"+username+"', '"+hashedPassword+"', '"+salt+"')";
                const char* q = insert_query.c_str();
                qstate = mysql_query(conn, q);
              }
              else
              {
                string saltAd = generateSalt();//*
                std::cout << "\t" << saltAd << std::endl;//*

                const string input = passwordAd + saltAd;//*
                string output1 = sha256(input);//*
                string hashedPasswordAd = output1;

                string insert_query = "insert into 	admin_hashedpassword2 (AdminID, usernameAd, hashedPasswordAd, saltAd) values('"+AdminID+"', '"+usernameAd+"', '"+hashedPasswordAd+"', '"+saltAd+"')";
                const char* q = insert_query.c_str();
                qstate = mysql_query(conn, q);
              }

              if(flag)
              {
                    if(!qstate)
                    {
                        system("cls");
                        cout << "\n\n\n\n\n\n\n\tYou are successfully registered!" << std::endl;
                        cout << endl << "\tData successfully added in the database. \n\n" << endl;
                        cout << endl << "\tPress Enter to Continue. \n" << endl;
                    }
                    else
                    {
                        cout << "\n\tQuery Execution Problem! Error number: " << mysql_errno(conn) << endl;
                        cout << "\n\tDuplicate Username Entry! Please choose a unique username and try again." << endl;
                    }
              }
              else
              {
                    if(!qstate)
                    {
                        system("cls");
                        cout << "\n\n\n\n\n\n\n\tYou are successfully registered as Admin!" << std::endl;
                        cout << endl << "\tData successfully added in the database. \n\n" << endl;
                        authorized_to_be_Admin = false;
                        cout << endl << "\tPress Enter to Continue. \n" << endl;

                    }
                    else
                    {
                        cout << "\n\tQuery Execution Problem! Error number: " << mysql_errno(conn) << endl;
                        cout << "\n\tDuplicate Username Entry! Please choose a unique username and try again." << endl;
                    }
              }
			return;
	}

	int LoginManager::login(bool admin)
	{
			bool status = IsLoggedIn(admin);

			if(!status)
			{
				std::cout << "\n\tError! Username or password is wrong. "<< std::endl;
				return 2;
			}
			else
			{
				std::cout << "\n\tSuccefully logged in!"  << std::endl;
				return 1;

			}
	}

	void LoginManager::show_and_deleteUser_Registr()
	{
	    kaza:
	    qstate = mysql_query(conn, "select * from users_hashedpassword");
		system("cls");
		std::cout << "\n" "***********************************************************************************************************\n";
        std::cout<<"\t\tSHOW AND DELETE USERS REGISTRATION \n\n";



		cout << "         Showing all users .... " << endl << endl;

        res = mysql_use_result(conn);

                cout << left << setw(7) << setfill('-') << left << '+'
                << setw(12) << setfill('-') <<'+'
                << setw(65)<< setfill('-') << '+'
                << setw(21)<< setfill('-') << '+' << '+' << endl;

                cout << setfill(' ') << '|' << left << setw(6) << "UserID"
                << setfill(' ') << '|' << left << setw(11) << "User Names"
                << setfill(' ') << '|' << left << setw(64) << "Hashed Passwords"
                << setfill(' ') << '|' << left << setw(20) << "Salt" << '|' << endl; //The left can be changed to right

                 cout << left << setw(7) << setfill('-') << left<< '+'
                 << setw(12) << setfill('-') << '+'
                  << setw(65)<< setfill('-') << '+'
                 << setw(21) << setfill('-') << '+' << '+' << endl;

            if(!qstate)
            {
                 while((row = mysql_fetch_row(res)))
                 {
                     cout << setfill(' ') << '|' << left << setw(6) << row[0]
                     << setfill(' ') << '|' << left << setw(11) << row[1]
                     << setfill(' ') << '|' << left << setw(64) << row[2]
                    << setfill(' ') << '|' << left << setw(20) << row[3] << '|' << endl;//The left can be changed to right
                 }
            }
            else
            {
                cout << "Query error!" << mysql_errno(conn) << endl;
            }
                cout << left << setw(7) << setfill('-') << left << '+'
                << setw(12) << setfill('-') << '+'
                 << setw(65)<< setfill('-') << '+'
                << setw(21)<< setfill('-') << '+' << '+' << endl;
                mysql_free_result(res);

		string UserID; char ch;

		cout << "\n\tDo you want to delete any user? (y/n): ";cin >> ch;

		if(ch == 'y' || ch == 'Y')
		{
			cout << "\n\tEnter the user ID of the user you want to delete: "; cin >> UserID;

			string delete_query = "delete from users_hashedpassword where UserID = '"+UserID+"'";
			const char* qd = delete_query.c_str();
			qstate = mysql_query(conn, qd);

			if(!qstate)
			{
				system("cls");
				cout << "\n\n\n\t\tSuccessfully Deleted from Database!" << endl;
				cout << "\n\n\t\tPress Enter to return to Admin Menu ";
			}
			else
			{
				cout << "Failed to Delete!" << mysql_errno(conn) << endl;
			}
		}
		else if(ch == 'N' || ch == 'n')
        {
           system("cls");
            std::cout<<"\n***********************************************************************************************************\n\n";
            std::cout<<"\n\t\tPress Enter to return to Admin Menu ";
            return;
        }
		else
		{
			system("cls");
			cout << "\n\tERROR! You have entered an invalid input! " << endl;
			cout << "\n\n\tERROR! Please try again after this timeout " << endl;

            using namespace std::this_thread;
            using namespace std::chrono_literals;
            using std::chrono::system_clock;
            sleep_for(20ms);
            sleep_until(system_clock::now() + 1s);

			goto kaza;
		}
	}

	int LoginManager::general_login()
	{
		UserInput usip;
		LoginManager log;
		Cipher cph;

		char choice;

		do
        {
            system("cls");
       std::cout << "\n" "***********************************************************************************************************\n";
        std::cout<<"\t\t\t\t\tThe IoT-HarPSecA Tool \n";
		std::cout << "\n\tThis is version 1.1 of the IoT-HarPSecA Tool, a tool that provides an interface that allows "<< endl;
		std::cout << "\tusers to use the IoT-HarPSecA framework. The purpose of this framework is threefold."<< endl;
		std::cout << "\tFirstly, it can help non-security experts to design secure IoT devices and applications by"<< endl;
		std::cout << "\tproviding them with the necessary security requirements needed to develop secure IoT systems. "<< endl;
		std::cout << "\tSecondly, it can help non-security experts to generate security best practice guidelines for "<< endl;
		std::cout << "\tsecure IoT development. Thirdly, the tool is intended to help users with little or no security"<< endl;
        std::cout << "\texpertise to implement security in their IoT devices and applications by recommending to them   "<< endl;
        std::cout <<"\tthe most appropriate lightweight cryptographic algorithms for their software and hardware imp-" << endl;
        std::cout <<"\tlementations.\n" << endl << endl;
        std::cout << "\tIoT-HarPSecA is developed by Musa G. Samaila and Pedro R. M. Inacio from the Instituto de"<< endl;
        std::cout << "\tTelecomunicaçoes, and Department of Computer Science, Universidade da Beira Interior, "<< endl;
        std::cout << "\tCovilha, Portugal.\n"<< endl;
        std::cout << "\t\t\tCopyright 2019 Musa G. Samaila and Pedro R. M. Inacio\n"<< endl;
        std::cout << "\tSPDX-License-Identifier: Apache-2.0. The copy of the License may be obtained at "<< endl;
        std::cout << "\t\t\thttp://www.apache.org/licenses/LICENSE-2.0 \n\n"<< endl;
        std::cout << "\t\t\t\t\t\tDISCLAIMER "<< endl;
        std::cout << "\tThis Tool is provided \"AS IS\" BASIS, without any express or implied WARRANTY, UNDERTAKING, or"<< endl;
        std::cout << "\tINDEMNIFICATION of ANY KIND. Thus, no responsibility or liability to a user of this Tool will "<< endl;
        std::cout << "\tbe accepted by the developers or any institution in connection with this tool. Any such respo- "<< endl;
        std::cout << "\tnsibility or liability is hereby expressly disclaimed.\n\n"<< endl;
        std::cout << "\tThis work was supported in part by the Centre for Geodesy and Geodynamics, National Space"<< endl;
        std::cout << "\tResearch and Development Agency, Toro, Bauchi State, Nigeria. This work was performed under"<< endl;
        std::cout << "\tthe scope of Project SECURIoTESIGN with funding from FCT/COMPETE/FEDER (Projects with  " << endl;
        std::cout << "\treference numbers UID/EEA/50008/2019 and POCI-01-0145-FEDER-030657) and FCT research grant " << endl;
        std::cout << "\tBIM/no32/2018-B00582." << endl;
        cout << endl << "\t\t\t\t  Press Enter to use or explore the tool." << endl;

        }while(cin.get() != '\n');

		label:
		do
		{
			system("cls");
			std::cout << "\n" "***********************************************************************************************************\n";
			std::cout <<
               " \t\t\tLOGIN MENU" "\n" "\n"
				" \tHello! Would you like to register, or log in to IoT-HarPSecA?" "\n" "\n"
				"\t\t[1] Register" "\n"
				"\t\t[2] Log in" "\n"
				"\t\t[3] Log in as an Administrator" "\n"
			   "\t\t[4] Exit" "\n" "\t";

			std::cout << "\n\t""Select your option (1-4): ";
				std::cin >> choice;
				std:: cout << endl;

			switch (choice)
			{
			case '1':
                {
                        system("cls");
                        std::cout << "\n" "***********************************************************************************************************\n";
                        std::cout<<"\n\t\tREGISTER\n\n";
                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                        std::cin.ignore();


                        if(cin.get() == '\n')
                        {

                        }
                        else
                        {
                            goto label;
                        }
                        char choice;
                        lavel:
                        do
                        {
                            system("cls");
                            std::cout << "\n" "***********************************************************************************************************\n";
                            std::cout<<"\n\tREGISTRATION/LOGIN MENU\n";
                            std::cout<<"\n\t\t1. User Registration";
                            std::cout<<"\n\t\t2. Admin Registration";
                            std::cout<<"\n\t\t3. User Login";
                            std::cout<<"\n\t\t4. Admin Login";
                            std::cout<<"\n\t\t5. Return to Login Menu";
                            std::cout<<"\n\t\t6. Exit";
                            std::cout<<"\n\n\tSelect Your Option (1-6): ";
                            std::cin>>choice;

                            switch(choice)
                            {
                            case '1':
                                 {
                                        system("cls");
                                        std::cout << "\n" "***********************************************************************************************************\n";
                                        std::cout<<"\n\t\tUSER REGISTRATION\n\n";
                                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                        std::cin.ignore();

                                        if(cin.get() == '\n')
                                        {
                                            log.registration(true);
                                        }
                                        else
                                        {
                                            goto lavel;
                                        }
                                    break;
                                    }
                            case '2':
                                    {
                                            system("cls");
                                            std::cout << "\n" "***********************************************************************************************************\n";
                                            std::cout<<"\n\t\tADMIN REGISTRATION\n\n";
                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                            std::cin.ignore();

                                            if(cin.get() == '\n')
                                            {
                                                log.registration(false);
                                            }
                                            else
                                            {
                                                goto lavel;
                                            }
                                    break;
                                    }
                            case '3':
                                {
                                            system("cls");
                                            std::cout << "\n" "***********************************************************************************************************\n";
                                            std::cout<<"\n\t\tUSER LOGIN\n\n";
                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                            std::cin.ignore();

                                            if(cin.get() == '\n')
                                            {
                                                goto level;
                                            }
                                            else
                                            {
                                                goto lavel;
                                            }
                                        break;
                                    }
                            case '4':
                                {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tADMIN LOGIN\n\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                    {
                                        goto level2;
                                    }
                                    else
                                    {
                                        goto lavel;
                                    }
                                break;
                                }
                            case '5':
                                {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tRETURN TO LOGIN MENU\n\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                    {
                                        goto label;
                                    }
                                    else
                                    {
                                        goto lavel;
                                    }
                                break;
                                }
                            case '6':
                                {
                                    system("cls");
                                    std::cout << "\n" "***********************************************************************************************************\n";
                                    std::cout<<"\n\t\tEXIT\n\n";
                                    std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                    std::cin.ignore();

                                    if(cin.get() == '\n')
                                    {
                                        system("cls");
                                        std::cout << "\n" "***********************************************************************************************************\n";
                                        std::cout << "Thank you for using IoT-HarPSecA. " << std::endl;
                                        std::cout << "Exiting ........" << std::endl;
                                        return 0;
                                    }
                                    else
                                    {
                                        goto lavel;
                                    }
                                break;
                                }
                            default :
                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                            }
                            cin.ignore();
                            cin.get();
                        }while(choice !='6');
                        return 0;
                    break;
                  }
			case '2':
                 {
                        level:
                            system("cls");
                            std::cout << "\n" "***********************************************************************************************************\n";
                            std::cout<<"\n\t\tUSER LOGIN\n";
                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                            std::cin.ignore();

                            if(cin.get() == '\n')
                            {
                                    int flag1;
                                     flag1 = log.login(false);
                                     if(flag1 == 1)
                                     {
                                        int chowa;
                                       // int real_int;
                                        UserInput usip;
                                        SecurityMngr mngr;

                                        guga:
                                        do
                                        {
                                             system("cls");
                                            std::cout<<"\n***********************************************************************************************************\n";
                                            std::cout<<"\n\tWELCOME TO IoT-HarPSecA MAIN MENU\n";
                                            std::cout<<"\n\tWhat would you like to do?\n";
                                            std::cout<<"\n\t\t1.  Make A New Security Requirement Elicitation Request";
                                            std::cout<<"\n\t\t2.  Display/Modify Your Security Requirement Elicitation Request";
                                            std::cout<<"\n\t\t3.  Process Your Security Requirement Elicitation Request";
                                            std::cout<<"\n\t\t4.  Delete Your Security Requirement Elicitation Request";
                                            std::cout<<"\n\t\t5.  Request A New Security Best Practice Guidelines for Secure Development ";
                                            std::cout<<"\n\t\t6.  Display/Modify Your Security Best Practice Guidelines Request";
                                            std::cout<<"\n\t\t7.  Process Your Security Best Practice Guidelines Request";
                                            std::cout<<"\n\t\t8.  Delete Your Security Best Practice Guidelines Request";
                                            std::cout<<"\n\t\t9.  Make A New Lightweight Cryptographic Algorithms Recommendation Request";
                                            std::cout<<"\n\t\t10. Display/Modify Your Lightweight Cryptographic Algorithms Recommendation Request";
                                            std::cout<<"\n\t\t11. Process Your Lightweight Cryptographic Algorithms Recommendation Request";
                                            std::cout<<"\n\t\t12. Delete Your Lightweight Cryptographic Algorithms Recommendation Request";
                                            std::cout<<"\n\t\t13. Return to Login Menu";

                                                std::cout<<"\n\t\t14. Exit";

                                          std::cout<<"\n\n\tSelect Your Option (1-14): ";
                                           std::cin>>chowa;


                                         while(std::cin.fail())
                                         {
                                            std::cout << "\n\t\t\tERROR!";
                                            std::cin.clear();
                                            std::cin.ignore(256,'\n');
                                             std::cout <<"\tThis is not an integer. Please select Your Option (1-14): ";
                                            std::cin >> chowa;
                                         }
                                            switch(chowa)
                                            {
                                                case 1:
                                                    {
                                                        system("cls");
                                                        std::cout << "\n" "***********************************************************************************************************\n";
                                                        std::cout<<"\n\t\tMAKE A NEW SECURITY REQUIREMENT ELICITATION REQUEST\n\n";
                                                        std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                        std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.getUserInput_RE();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                    break;
                                                    }
                                                case 2:
                                                        {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY/MODIFY SECURITY REQUIREMENT ELICITATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.modifyUserRequirements_Elicitation_requests();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                         break;
                                                        }
                                                case 3:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tPROCESS SECURITY REQUIREMENT ELICITATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                               mngr.decisionMaker_RE();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                    break;
                                                      }
                                                case 4:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDELETE SECURITY REQUIREMENT ELICITATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                               usip.deleteRequest_RE();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                        break;
                                                    }
                                                case 5:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\t\tREQUEST A NEW BEST PRACTICE GUIDE FOR SECURE DEVELOPMENT \n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.getUserInput_BestPractGuide();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                      break;
                                                    }
                                                case 6:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY/MODIFY SECURE DEVELOPMENT BEST PRACTICE GUIDE REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.modifyBestPractGuide_requests();

                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 7:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tPROCESS SECURE DEVELOPMENT BEST PRACTICE GUIDE REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                mngr.decisionMaker_BP();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 8:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDELETE SECURE DEVELOPMENT BEST PRACTICE GUIDE REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.deleteBestPractGuide();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 9:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tMAKE A NEW LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.getUserInput();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 10:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY/MODIFY LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.showAndModifyUser_request();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 11:
                                                    {
                                                            int lu7 = 0;
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tPROCESS LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                mngr.decisionMaker();//decisionMaker()
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 12:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDELETE LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.deleteRequest();
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 13:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tRETURN TO LOGIN MENU\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 goto label;
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }
                                                case 14:
                                                    {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tEXIT\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 system("cls");
                                                                 std::cout << "\n\n\tThank you for using IoT-HarPSecA. " << std::endl;
                                                                 std::cout << "\n\n\tExiting ........" << std::endl;
                                                                return 0;
                                                            }
                                                            else
                                                            {
                                                                goto guga;
                                                            }
                                                       break;
                                                    }

                                               default :
                                                    system("cls");
                                                    std::cout << "\n\n\n\t\t\t\tSORRY! WRONG OPTION SELECTED." << std:: endl;
                                                    cout << endl << "\n\n\t\t\t\tPress Enter to return to the Main Menu and try again." << endl;
                                            }
                                            cin.ignore();
                                            cin.get();
                                       }while(chowa != 14);
                                     }
                                     else
                                     {
                                        goto label;
                                     }
                                }
                                else
                                {
                                    break;
                                }
                    break;

                }
			case '3':
                    {

                        level2:
                            system("cls");
                            std::cout << "\n" "***********************************************************************************************************\n";
                            std::cout<<"\n\t\tADMIN LOGIN\n";
                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                            std::cin.ignore();

                            if(cin.get() == '\n')
                            {
                                int flag2;
                                 flag2 = log.login(true);
                                if(flag2 == 1)
                                {
                                    char choice;
                                    //int ID;
                                    SecurityMngr mngr;

                                    do
                                    {
                                        lamua:
                                        system("cls");
                                        std::cout<<"\n" "***********************************************************************************************************\n";
                                        std::cout<<"\n      WELCOME TO IoT-HarPSecA ADMIN MENU\n";
                                        std::cout<<"\n      What would you like to do?\n";
                                        std::cout<<"\n\t 1. Display/Delete a User Registration";
                                        std::cout<<"\n\t 2. Delete a Security Requirements Elicitation Request";
                                        std::cout<<"\n\t 3. Delete a Security Best Practice Guidelines Request";
                                        std::cout<<"\n\t 4. Delete a Lightweight Cryptographic Algorithms Recommendation Request";
                                        std::cout<<"\n\t 5. Display, Add, Update, or Delete Lightweight Cryptographic Algorithms";
                                        std::cout<<"\n\t 6. Allow one more Admin user";
                                        std::cout<<"\n\t 7. Go to Registration/Login Menu and enter Main Menu as a user";
                                        std::cout<<"\n\t 8. Exit\n";
                                        std::cout<<"\n      Select Your Option (1-8): "; std::cin>>choice; cout << endl;

                                        switch(choice)
                                        {
                                            case '1':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY/DELETE USER REGISTRATIONS\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 log.show_and_deleteUser_Registr();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                             case '2':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY SECURITY REQUIREMENTS ELICITATION USER REQUEST IDS/DELETE A USER REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.showAndDeleteUser_Request_RE();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                             case '3':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\tDISPLAY BEST PRACTICE GUIDE FOR SECURE DEVELOPMENT USER REQUEST IDS/DELETE A USER REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                usip.showAndDeleteUser_BestPractGuide();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                            case '4':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY/DELETE LIGHTWEIGHT SECURITY ALGORITHM IMPLEMENTATION USER REQUEST\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 usip.showAndDeleteUser_Request();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                            case '5':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tDISPLAY, ADD, UPDATE, OR DELETE CRYPTOGRAPHIC ALGORITHMS\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 cph.show_add_update_or_deleteCipher();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                            case '6':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tALLOW ONE MORE ADMIN USER\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                 add_one_more_Admin();
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                             case '7':
                                                 {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tGO TO REGISTRATION/LOGIN MENU AND ENTER MAIN MENU AS A USER\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                goto lavel;
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                            case '8':
                                                {
                                                            system("cls");
                                                            std::cout << "\n" "***********************************************************************************************************\n";
                                                            std::cout<<"\n\t\tEXIT\n\n";
                                                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                                                            std::cin.ignore();

                                                            if(cin.get() == '\n')
                                                            {
                                                                system("cls");
                                                                std::cout << "\n" "***********************************************************************************************************\n";
                                                                std::cout << "Exiting ........\n" << std::endl;
                                                                return 0;
                                                            }
                                                            else
                                                            {
                                                                goto lamua;
                                                            }
                                                       break;
                                                    }
                                            default :
                                                std::cout << "\tSorry! Wrong option selected." << std:: endl;
                                        }
                                        cin.ignore();
                                        cin.get();
                                    }while(choice !='8');//9

                                }
                                else
                                {
                                    break;
                                }
                            }
                            else
                            {
                                goto label;
                            }

                     break;
                     }
			case '4':
                        {
                            system("cls");
                            std::cout << "\n" "***********************************************************************************************************\n";
                            std::cout<<"\n\t\tEXIT\n";
                            std::cout<<"\n\t\tPress Enter to Continue, or any other key to go back: ";
                            std::cin.ignore();

                            if(cin.get() == '\n')
                            {
                                system("cls");
                                std::cout << "\n" "***********************************************************************************************************\n";
                                std::cout << "\n\t\tThank you for using IoT-HarPSecA. " << std::endl;
                                std::cout << "\n\n\t\tExiting ........" << std::endl;
                                std::cout<<"\n\n\t\tKeep pressing Enter to close the application";

                            }
                            else
                            {
                                goto label;
                            }
                    break;
                    }
			default:

				  std::cout << "\tSorry! Wrong option selected." << std:: endl;
			}
			cin.ignore();
			cin.get();
		}while(choice != '4');
	}

int main()
{
    SetConsoleTitle("IoT-HarPSecA Tool");
    LoginManager log;
    log.general_login();

	return 0;
}


