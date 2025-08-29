from markdown import markdown
from xhtml2pdf import pisa
from src.handler.data_handler import DataHandler

db = DataHandler()

class CMSREModule:

    """
    [Summary]: Method responsible for processing information about CSRE
    [Arguments]: No arguments
    [Return]: No return
    """

    def get_requirements(self):
        print("")
        print("  Processing information.....")
        print("")

        print_data()

        report = open("SECURITY_REQUIREMENTS.md", "w")
        report.write("# Final Security Requirements Report " + '\n')
        report.write("\n")

        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", "", "|", "", "|"))
        report.write("{:3}{:25}{:3}{:60}{:3}\n".format("|", ":--------", "|", ":---------", "|"))

        '''
        for i in range( 0,len(table_for_report) ):
            report.write("| " + table_for_report[i][0] + " | " + table_for_report[i][1] + " | \n" )
        '''
        for i in range(0, len(db.table_for_report)):
            report.write(
                "{:3}{:25}{:3}{:60}{:3}\n".format("|", db.table_for_report[i][0], "|",db.table_for_report[i][1], "|"))

        report.write("\n")

        # confidentiality requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/confidentiality.md", "r").read())

        # integrity requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/integrity.md", "r").read())

        # availability requirement
        report.write("\n")
        report.write("\n")

        report.write(open("resources/data/security_requirements/availability.md", "r").read())

        # authentication requirement
        if db.questions_and_answers["Q3"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/authentication.md", "r").read())

        # authorization requirement
        if db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_requirements/authorization.md", "r").read())

        # nonRepudiaton and accountability requirements
        if db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_requirements/nonRepudiation.md", "r").read())
                report.write("\n")
                report.write(open("resources/data/security_requirements/accountability.md", "r").read())

        # reliability requirement
        report.write("\n")
        report.write("\n")
        report.write(open("resources/data/security_requirements/reliability.md", "r").read())

        # # privacy resources/data/security_requirements
        # if db.questions_and_answers["Q5"].find("1") != -1 and (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
        #     report.write("\n")
        #     report.write("\n")
        #     report.write(open("resources/data/security_requirements/privacy.md", "r").read())

        # physical security requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1) and \
                db.questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/physicalSecurity.md", "r").read())

        # forgery resistance requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1) and \
                db.questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/forgeryResistance.md", "r").read())

        # tampering detection requirement
        if db.questions_and_answers["Q22"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/tamperDetection.md", "r").read())

        # data freshness requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/dataFreshness.md", "r").read())

        # confinement requirement
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q14"].find("1") != -1 or db.questions_and_answers["Q16"].find("1") != -1 or \
                    db.questions_and_answers["Q17"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_requirements/confinement.md", "r").read())

        # Interoperability requirement
        if db.questions_and_answers["Q14"].find("1") != -1 and db.questions_and_answers["Q16"].find("1") != -1 and \
                db.questions_and_answers["Q17"].find("1") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_requirements/interoperability.md", "r").read())

        # data origin authentication
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q5"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_requirements/dataOriginAuthentication.md", "r").read())

        report.close()
        self.requirements_convert_report()
        print("\n\n # Processing done! Check your requirements in the SECURITY_REQUIREMENTS.pdf file")
           """
    [Summary]: Method responsible for processing information about CSRE
    [Arguments]: No arguments
    [Return]: No return
    """
    def requirements_convert_report(self):
        # input_filename = ("guides/example_report.md")
        # input_filename = "some_markdown.md")
        input_filename = ("SECURITY_REQUIREMENTS.md")

        output_filename = ("SECURITY_REQUIREMENTS.html")

        with open(input_filename, "r") as f:
            html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

        out = open(output_filename, "w")
        out.write(html_text)

        # writing in pdf file, the html content

        resultFile = open("SECURITY_REQUIREMENTS.pdf", "w+b")
        pisa.CreatePDF(html_text, dest=resultFile)
