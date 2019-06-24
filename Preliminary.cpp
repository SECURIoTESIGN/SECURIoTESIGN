Preliminary.h
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef PRELIMINARY_H
#define PRELIMINARY_H

#include <iostream>
#include <windows.h>



class Preliminary
{
    public:
        //Constructor that does nothing
        Preliminary();
        //Function that converts lowercase string to uppercase
    void convert_lowerC_to_upperC(std::string& s);
     //Function that returns 1 or -1 based on total user requirements weight, flash memory size and RAM of the hardware platform. The purpose of this function to make the "Press Enter to return to MAIN MENU" message to always appear at the bottom, not between the result table and the warning message.
    int warning1(double reqWeight, double fms, double rs, double fms_, double rs_);
    //Function that prints a warning based on user requirements weight, flash memory size and RAM of the hardware platform
    void warning2(double reqWeight, double fms, double rs, double fms_, double rs_);
    //Function that determines if Request ID is for Software implementation or Hardware implementation based on Request ID
    int determine_requestType(std::string s1);
};


#endif // PRELIMINARY_H

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Preliminary.cpp

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include "Preliminary.h"

 //Constructor that does nothing
        Preliminary::Preliminary()
        {

        }

    //Function that converts lowercase string to uppercase
    void Preliminary::convert_lowerC_to_upperC(std::string& s) //Function that converts lowercase string to uppercase
    {
            for(int i = 0; i < s.length(); i++)
            {
                s[i] = toupper(s[i]);
            }
    }

    //Function that returns 1 or -1 based on total user requirements weight, flash memory size and RAM of the hardware platform. The purpose of this function to make the "Press Enter to return to MAIN MENU" message to always appear at the bottom, not between the result table and the warning message.
    int Preliminary::warning1(double reqWeight, double fms, double rs, double fms_, double rs_)
    {
        if(reqWeight >= 5.0 && (fms < fms_ || rs < rs_)) // (reqWeight > 5.0) && (fms < fms_ )&& (rs < rs_)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    //Function that prints a warning based on user requirements weight, flash memory size and RAM of the hardware platform
    void Preliminary::warning2(double reqWeight, double fms, double rs, double fms_, double rs_)
    {
        if(reqWeight >= 5.0 && (fms < fms_ || rs < rs_)) // (reqWeight > 5.0) && (fms < fms_ )&& (rs < rs_)
        {
            std::cout << "\n\n\t\t\t\t WARNING! LIMITED RESOURCES!  " << std::endl;
            std::cout << "\t      Implementing all algorithms may have negative impact on performance." << std::endl;
            std::cout << "\n\n\t\t\t\tPress Enter to return to MAIN MENU \n";
        }
    }


    //Function that determines if Request ID is for Software implementation or Hardware implementation based on Request ID
    int Preliminary::determine_requestType(std::string s1)
    {
        std::string s11, s33, s22;
        s11=s1;
        s22 = "H";
        s33 = "S";
       // s44 = "E";
        //s55 = "P";
        if(strstr(s11.c_str(),s22.c_str()))//Check Request ID and if request type is hardware, return 1
        {
            return 1;
        }
        else if(strstr(s11.c_str(),s33.c_str()))//Check Request ID and if request type is software, return 2
        {
            return 2;
        }
        else// If Request ID does not march hardware or software type, return -1
        {
            return -1;
        }
    }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////