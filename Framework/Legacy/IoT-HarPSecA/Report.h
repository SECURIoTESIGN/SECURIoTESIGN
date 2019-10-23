#ifndef REPORT_H
#define REPORT_H

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


class Report
{
    public:
        Report();
    void formatReport_for_Consle(std::string request_id, int flag, std::string algo_name1, std::string algo_name2, std::string algo_name3, std::string algo_name4, std::string algo_name5, std::string algo_name6, std::string Re_6, std::string Re_7, std::string Re_8, std::string Re_9, std::string Re_10, std::string Re_11, std::string Re_12, std::string Re_13, std::string Re_14, std::string Re_15);
    void formatReport_for_TextFile(std::string request_id, int flag, std::string algo_name1, std::string algo_name2, std::string algo_name3, std::string algo_name4, std::string algo_name5, std::string algo_name6, std::string Re_6, std::string Re_7, std::string Re_8, std::string Re_9, std::string Re_10, std::string Re_11, std::string Re_12, std::string Re_13, std::string Re_14, std::string Re_15);
    void cipher_Info1(std::string algo_name1);
    void cipher_Info1_text(std::string algo_name1);
    void cipher_Info2(std::string algo_name2);
    void cipher_Info2_text(std::string algo_name2);
    void cipher_Info3(std::string algo_name3);
    void cipher_Info3_text(std::string algo_name3);
    void cipher_Info6(std::string algo_name6);
    void cipher_Info6_text(std::string algo_name6);
    bool check_BP_condition(const char* path_to_file_x, std::ostream& combined_file);
    bool check_BP_condition2(const char* path_to_file_x, std::ostream& combined_file, std::string s);
    bool check_BP_condition3(const char* path_file, std::ostream& combined_file, std::string s1, std::string s2);
    bool mergeFiles(const char* path_to_file_x, std::ostream& combined_file);
};

#endif // REPORT_H
