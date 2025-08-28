from markdown import markdown
from xhtml2pdf import pisa
from src.handler.data_handler import  DataHandler

db = DataHandler()

class CMSMEModule:
    """
    [Summary]: Method responsible for processing information about SME module
    [Arguments]: No arguments
    [Return]: No return
    """

    def get_mechanisms(self):
        print("")
        print("  Processing information.....")
        print("")

        report = open("SECURITY_MECHANISMS.md", "w")
        report.write("# Final Security Mechanisms Report " + '\n')
        report.write("\n")

        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

        '''
        for i in range( 0,len(db.table_for_report) ):
            report.write("| " + db.table_for_report[i][0] + " | " + db.table_for_report[i][1] + " | \n" )
        '''
        for i in range(0, len(db.table_for_report)):
            report.write(
                "{:3}{:25}{:3}{:60}{:3}\n".format("|", db.table_for_report[i][0], "|", db.table_for_report[i][1], "|"))

        report.write("\n")

        # backup mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/backup_mechanism_guide.md", "r").read())

        # audit mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/audit_mechanisms_guide.md", "r").read())

        #  cryptographic algorithms mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/cryptographic_algorithms_mechanisms.md", "r").read())

        # biometric authentication mechanisms
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q4"].find("1") != -1:
            report.write(open("resources/data/security_mechanisms/biometric_authentication_mechanism.md", "r").read())

        # channel-based authentication mechanisms
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q4"].find("2") != -1:
            report.write(open("resources/data/security_mechanisms/channel_based_authentication_mechanism.md", "r").read())

        # factors-based authentication mechanisms
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q4"].find("3") != -1:
            report.write(open("resources/data/security_mechanisms/factors_based_authentication_mechanism.md", "r").read())

        # id-based authentication mechanisms
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q4"].find("4") != -1:
            report.write(open("resources/data/security_mechanisms/id_based_authentication_mechanism.md", "r").read())

        # cryptographic protocolos mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/cryptographic_protocols_mechanisms.md", "r").read())

        # access control mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_mechanisms/access_control_mechanisms.md", "r").read())

        # inspection and logging mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")
                report.write(open("resources/data/security_mechanisms/inspection_mechanisms.md", "r").read())

                report.write(open("resources/data/security_mechanisms/logging_mechanisms.md", "r").read())

        # device tamper detection mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1) and db.questions_and_answers["Q22"].find(
                "1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/device_detection_mechanisms.md", "r").read())

        # physical location mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1) and db.questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/physical_location_mechanism.md", "r").read())

        # confinement mechanisms
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q14"].find("1") != -1 or db.questions_and_answers["Q16"].find("1") != -1 or \
                    db.questions_and_answers["Q17"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_mechanisms/confinement_mechanisms.md", "r").read())

        # filtering mechanisms
        if db.questions_and_answers["Q14"].find("1") != -1 and db.questions_and_answers["Q16"].find("1") != -1 and \
                db.questions_and_answers["Q17"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/filtering_mechanism.md", "r").read())

        # iot and lora mechanisms
        if (db.questions_and_answers["Q1"].find("1") != -1 or db.questions_and_answers["Q1"].find("2") != -1 or
            db.questions_and_answers["Q1"].find("4") != -1) and db.questions_and_answers["Q1"].find("7") != -1 and (
                db.questions_and_answers["Q21"].find("11") != -1 or db.questions_and_answers["Q21"].find("12")):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_mechanisms/iot_lora_security_mechanisms.md", "r").read())

        report.close()
        self.mechanisms_convert_report()
        print("\n\n # Processing done! Check your security mechanisms in the SECURITY_MECHANISMS.pdf file")

    """
    [Summary]: Method to convert the markdown Security Mechanism Elicitation (SME) report to html and pdf format
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def mechanisms_convert_report(self):
        # input_filename = ("guides/example_report.md")
        # input_filename = "some_markdown.md")
        input_filename = ("SECURITY_MECHANISMS.md")

        output_filename = ("SECURITY_MECHANISMS.html")

        with open(input_filename, "r") as f:
            html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

        out = open(output_filename, "w")
        out.write(html_text)

        # writing in pdf file, the html content

        resultFile = open("SECURITY_MECHANISMS.pdf", "w+b")
        pisa.CreatePDF(html_text, dest=resultFile)
