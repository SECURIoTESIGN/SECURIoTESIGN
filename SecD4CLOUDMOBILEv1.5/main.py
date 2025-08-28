# !/usr/bin/python coding=utf-8
# !/bin/bash

"""
// ---------------------------------------------------------------------------
//
//	Security by Design for Cloud, Mobile and IoT Ecosystem (SecD4CLOUDMOBILE)
//
//  Copyright (C) 2020 Instituto de Telecomunicações (www.it.pt)
//  Copyright (C) 2020 Universidade da Beira Interior (www.ubi.pt)
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// This Work was developed under Doctoral Grant, supported by project
// CENTRO-01-0145-FEDER-000019 - C4 - Competence Center in Cloud Computing,
// Research Line 1: Cloud Systems, Work package WP 1.2 - Systems design and development
// processes and software for Cloud and Internet of Things ecosystems, cofinanced by the
// European Regional Development Fund (ERDF) through the Programa Operacional Regional do
// Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científica e
// Tecnológica - Programas Integrados de IC&DT.
// ---------------------------------------------------------------------------
"""

import os
from sys import exit
import webbrowser
from PyPDF2 import PdfMerger

from src.constants.constants import Constants

from src.handler.cmsbpg_handler import CMSBPGModule
from src.handler.cmsre_handler import CMSREModule
from src.handler.cmsme_handler import  CMSMEModule
from src.handler.cmame_handler import CMAMEModule
from src.handler.cm2st_handler import CM2STModule
from src.handler.data_handler import  DataHandler

################################# GLOBAL VARIABLES #################################
#db: DatabaseHandler
chosen_module: str
cmsre = CMSREModule()
cmsbpg = CMSBPGModule()
cmsme = CMSMEModule()
cmame = CMAMEModule()
cm2st = CM2STModule()
dataHandler = DataHandler()
global chosen_model

"""
[Summary]: Method responsible for creating, printing and outputting the complete processing report
[Arguments]: No arguments
[Return]: No return
"""
def fullReport():

    cmsre.get_requirements()
    cmsbpg.get_security_best_practices()
    cmsme.get_mechanisms()
    cmame.get_attack_models()
    cm2st.get_security_test_recommendation()

    pdfs = ['SECURITY_REQUIREMENTS.pdf', 'GOOD_PRACTICES.pdf', 'SECURITY_MECHANISMS.pdf', 'ATTACKS_MAPPING.pdf', 'TEST_SPECIFICATION.pdf']

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("FULL_REPORT.pdf")
    merger.close()
    print("\n\n *** Processing  done! See the full report requested in the FULL_REPORT.pdf file! ***\n\n")

######################################################################################################################################################################


# region menu_flow
def show_menu(menu_id):
    """
    handles the writing of the menu
    :param menu_id the menu to be drawn
    """
    print(''.ljust(80, '-'))
    print(menu_id)
    menu_options = Constants.MENU_OPTIONS[menu_id]
    for idx, option in enumerate(menu_options):
        print("{0} - {1}".format(idx, option))
    chosen_option = input("Enter option : ")
    handle_choice(menu_id, chosen_option)


def handle_choice(menu_id, chosen_option):
    """
    Handles the possible menu choices
    """
    # Main
    if menu_id == Constants.MENU_MAIN:
        if chosen_option == '0':  # Exit
            exit()
        elif chosen_option == '1':  # ANSWER THE QUESTIONNAIRE
            #dataHandler.switch1()
            show_menu(Constants.MENU_QUESTIONNAIRE)
        elif chosen_option == '2': # MODULES
            show_menu(Constants.MENU_MODULE)
        elif chosen_option == '3': # GET A FULL REPORT
            fullReport()
            show_menu(Constants.MENU_MAIN)
        else:
            show_menu(Constants.MENU_MAIN)

    # Questionnaire
    elif menu_id == Constants.MENU_QUESTIONNAIRE:
        if chosen_option == '0': # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1': # Answer the questions one by one
            dataHandler.answerQuestionnaire()
            show_menu(Constants.MENU_QUESTIONNAIRE)
        elif chosen_option == '2': # Use a text file with the answers already written
            dataHandler.openFile()
            show_menu(Constants.MENU_QUESTIONNAIRE)
        else:
            show_menu(Constants.MENU_MAIN)

    # Module
    elif menu_id == Constants.MENU_MODULE:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # CMSRE
            show_menu(Constants.MENU_MODULE_CMSRE)
        elif chosen_option == '2':  # CMSBPG
            show_menu(Constants.MENU_MODULE_CMSBPG)
        elif chosen_option == '3':  # CMSME
            show_menu(Constants.MENU_MODULE_CMSME)
        elif chosen_option == '4':  # CMAME
            show_menu(Constants.MENU_MODULE_CMAME)
        elif chosen_option == '5':  # CM2ST
            show_menu(Constants.MENU_MODULE_CM2ST)
        else:
            show_menu(Constants.MENU_MODULE)

    # CMSRE
    elif menu_id == Constants.MENU_MODULE_CMSRE:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # Generate CMSRE Report
            cmsre.get_requirements()
            show_menu(Constants.MENU_MODULE_CMSRE)
        else:
            show_menu(Constants.MENU_MODULE_CMSRE)

    # CMSBPG
    elif menu_id == Constants.MENU_MODULE_CMSBPG:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # Generate CMSBPG Report
            cmsbpg.get_security_best_practices()
            show_menu(Constants.MENU_MODULE_CMSBPG)
        else:
            show_menu(Constants.MENU_MODULE_CMSBPG)

    # CMSME
    elif menu_id == Constants.MENU_MODULE_CMSME:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # Generate CMSME Report
            cmsme.get_mechanisms()
            show_menu(Constants.MENU_MODULE_CMSME)
        else:
            show_menu(Constants.MENU_MODULE_CMSME)

    # CMAME
    elif menu_id == Constants.MENU_MODULE_CMAME:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # Generate CMAME Report
            cmame.get_attack_models()
            show_menu(Constants.MENU_MODULE_CMAME)
        else:
            show_menu(Constants.MENU_MODULE_CMAME)

        # CM2ST
    elif menu_id == Constants.MENU_MODULE_CM2ST:
        if chosen_option == '0':  # Return
            show_menu(Constants.MENU_MAIN)
        elif chosen_option == '1':  # Generate CM2ST Report
            cm2st.get_security_test_recommendation()
            show_menu(Constants.MENU_MODULE_CM2ST)
        else:
            show_menu(Constants.MENU_MODULE_CM2ST)

# endregion

def main():
    # global questions_and_answers
    global db
    db = DataHandler()
    show_menu(Constants.MENU_MAIN)


if __name__ == "__main__":

    print("#  Welcome to ")
    print("")
    print("#  SecD4CLOUDMOBILE ")
    print("")
    print("  The **SecD4CLOUDMOBILE** is a custom made program")
    print("  This program implements a questionnaire about the development")
    print("  of mobile cloud-based application and generate a report with secure development guides.")
    print("  It is part of the outputs of the doctoral thesis project entitled Systematization of the ")
    print("  Security Engineering Process in the Cloud and Mobile Ecosystem ")
    print("")
    print("## License")
    print("")
    print("  Developed by Francisco T. Chimuco and Pedro R. M. Inácio")
    print("  Department of Computer Science")
    print("  Universidade da Beira Interior")
    print("")
    print("  Copyright 2021 Francisco T. Chimuco and Pedro R. M. Inácio")
    print("")
    print("  SPDX-License-Identifier: Apache-2.0")
    print("")
    main()
