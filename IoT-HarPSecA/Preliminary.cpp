#include "Preliminary.h"

        Preliminary::Preliminary()
        {

        }

    void Preliminary::convert_lowerC_to_upperC(std::string& s) 
    {
            for(int i = 0; i < s.length(); i++)
            {
                s[i] = toupper(s[i]);
            }
    }

    int Preliminary::warning1(double reqWeight, double fms, double rs, double fms_, double rs_)
    {
        if(reqWeight >= 5.0 && (fms < fms_ || rs < rs_)) 
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    void Preliminary::warning2(double reqWeight, double fms, double rs, double fms_, double rs_)
    {
        if(reqWeight >= 5.0 && (fms < fms_ || rs < rs_)) 
        {
            std::cout << "\n\t\t\t\t\t WARNING! LIMITED RESOURCES  " << std::endl;
            std::cout << "\t\t    Implementing all algorithms may have negative impact on performance." << std::endl;
            std::cout << "\n\t\t\t\t    Press Enter to return to MAIN MENU \n";
        }
    }

    int Preliminary::determine_requestType(std::string s1)
    {
        std::string s11, s33, s22;
        s11=s1;
        s22 = "H";
        s33 = "S";
     
        if(strstr(s11.c_str(),s22.c_str()))
        {
            return 1;
        }
        else if(strstr(s11.c_str(),s33.c_str()))
        {
            return 2;
        }
        else
        {
            return -1;
        }
    }

    bool Preliminary::validString(std::string& word)
    {
    if(word.length() == 0)
        return false; 

    for(int i = 0; i < word.length(); i++)
        if(word[i] >= '0' && word[i] <= '9')
            return false; 

    return true; 
}
