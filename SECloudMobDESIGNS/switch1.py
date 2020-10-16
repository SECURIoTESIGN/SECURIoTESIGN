from switch import Switch
from goto import with_goto

@with_goto
def simple_example_with_default():

    label .begin
    val = int(input("Inserte a value!"))
    with Switch(val) as case:
        if case(1):
            print("Bom dia Angola")

        if case(2):
            print("Olá Francisco!")

        if case.default:
            print("valores incorrectos")
            goto .begin
    

if __name__ == "__main__":
    
	print("---")
	print("")
	print("#  Welcome to ")
	print("")
	print("#  SECloudMobilEQUIREMENTS")
	print("")
	print("  The **SECloudMobilEQUIREMENTS** is a custom made program.") 
	print("  This program implements a questionnaire about the development")
	print("  of mobile cloud-based application and generate a report with secure development guides.")
	print("  It is part of the outputs of project PHD Thesis entitled Systematization of the ")
	print("  Security Engineering Process in the Cloud and Mobile Ecosystem ")
	print("")
	print("## License")
	print("")
	print("  Developed by Francisco T. Chimuco and Pedro R. M. Inácio")
	print("  Department of Computer Science")
	print("  Universidade da Beira Interior")
	print("")
	print("  Copyright 2019 Francisco T. Chimuco and Pedro R. M. Inácio")
	print("")
	print("  SPDX-License-Identifier: Apache-2.0")
	print("")

	simple_example_with_default()


	print("")
	print("#############################################################") # after this is for debugging xD

	print("")
	print("")
	print("")

	
	
	exit(0)
