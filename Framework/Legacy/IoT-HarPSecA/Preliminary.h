#ifndef PRELIMINARY_H
#define PRELIMINARY_H

#include <iostream> 
#include <windows.h>



class Preliminary
{
    public:
        Preliminary();
    void convert_lowerC_to_upperC(std::string& s);
    int warning1(double reqWeight, double fms, double rs, double fms_, double rs_);
    void warning2(double reqWeight, double fms, double rs, double fms_, double rs_);
    int determine_requestType(std::string s1);
    bool validString(std::string& word);
};

#endif // PRELIMINARY_H
