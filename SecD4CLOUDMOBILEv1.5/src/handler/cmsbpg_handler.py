from markdown import markdown
from xhtml2pdf import pisa
from src.handler.data_handler import  DataHandler

db = DataHandler()

class CMSBPGModule:
    """
    [Summary]: Method responsible for processing information about CSBPG module
    [Arguments]: No arguments
    [Return]: No return
    """

    def get_security_best_practices(self):
        print("")
        print("  Processing information.....")
        print("")

        report = open("GOOD_PRACTICES.md", "w")
        report.write("# Final Security Good Practices " + '\n')
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

        # Injection security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                if (db.questions_and_answers["Q13"].find("1") != -1):
                    report.write("\n\n")

                    report.write(
                        open("resources/data/security_best_practices_guidelines/Injection_Prevention_Cheat_Sheet.md", "r").read())

        # SQL Injection Prevention security best practices guidelines
        if db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4"):
            if db.questions_and_answers["Q5"].find("1") != -1 and db.questions_and_answers["Q6"].find("1"):
                report.write("\n\n")

                report.write(
                    open("resources/data/security_best_practices_guidelines/SQL_Injection_Prevention_Cheat_Sheet.md", "r").read())

        # Authentication security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Authentication_Cheat_Sheet.md", "r").read())

            # Multifactor authentication security best practices guidelines
            if (db.questions_and_answers["Q4"].find("3") != -1):
                report.write("\n\n")

                report.write(
                    open("resources/data/security_best_practices_guidelines/Multifactor_Authentication_Cheat_Sheet.md", "r").read())

        # Authorization security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(open("resources/data/security_best_practices_guidelines/Authorization_Cheat_Sheet.md", "r").read())

            # Transaction Authorization security best practices guidelines
            if (db.questions_and_answers["Q2"].find("3") != -1 or db.questions_and_answers["Q2"].find("6") != -1):
                report.write("\n\n")

                report.write(
                    open("resources/data/security_best_practices_guidelines/Transaction_Authorization_Cheat_Sheet.md", "r").read())

        # Cross-Site-Scripting security best practices guidelines
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1):
            if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
                if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                        db.questions_and_answers["Q8"].find("3") != -1):
                    report.write("\n\n")

                    report.write(
                        open("resources/data/security_best_practices_guidelines/Cross_Site_Scripting_Prevention_Cheat_Sheet.md",
                             "r").read())

        # Cross Site Request Forgery security best practices guidelines
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1):
            if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
                if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                        db.questions_and_answers["Q8"].find("3") != -1):
                    report.write("\n\n")

                    report.write(
                        open("resources/data/security_best_practices_guidelines/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md",
                             "r").read())

        # Cryptographic Storage security best practices guidelines
        if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Cryptographic_Storage_Cheat_Sheet.md", "r").read())

        # Database security best practices guidelines
        if (db.questions_and_answers["Q5"].find("1") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Database_Security_Cheat_Sheet.md", "r").read())

        # Denial of Service security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Denial_of_Service_Cheat_Sheet.md", "r").read())

        # File uploading security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                if (db.questions_and_answers["Q14"].find("1") != -1):
                    report.write("\n\n")

                    report.write(open("resources/data/security_best_practices_guidelines/File_Upload_Cheat_Sheet.md", "r").read())

        # HTML5 security best practices guidelines
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1):
            if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
                if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                    if (db.questions_and_answers["Q12"].find("3") != -1):
                        report.write("\n\n")

                        report.write(
                            open("resources/data/security_best_practices_guidelines/HTML5_Security_Cheat_Sheet.md", "r").read())

        # Securing CSS security best practices guidelines
        if (db.questions_and_answers["Q12"].find("3") != -1):
            report.write("\n\n")

            report.write(
                open("resources/data/security_best_practices_guidelines/Securing_Cascading_Style_Sheets_Cheat_Sheet.md", "r").read())

        # Injection prevention in Java security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                if (db.questions_and_answers["Q12"].find("4") != -1):
                    report.write("\n\n")

                    report.write(open("resources/data/security_best_practices_guidelines/Injection_Prevention_in_Java_Cheat_Sheet.md",
                                      "r").read())

        # Secure Logging security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                if (db.questions_and_answers["Q15"].find("1") != -1):
                    report.write("\n\n")

                    report.write(open("resources/data/security_best_practices_guidelines/Logging_Cheat_Sheet.md", "r").read())

        # Logging Vocabulary security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                if (db.questions_and_answers["Q15"].find("1") != -1):
                    report.write("\n\n")

                    report.write(
                        open("resources/data/security_best_practices_guidelines/Logging_Vocabulary_Cheat_Sheet.md", "r").read())

        # Nodejs security best practices guidelines
        if (db.questions_and_answers["Q12"].find("5") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Nodejs_Security_Cheat_Sheet.md", "r").read())

        # NPM security best practices guidelines
        if (db.questions_and_answers["Q12"].find("5") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/NPM_Security_Cheat_Sheet.md", "r").read())

        # Third Party Javascript security best practices guidelines
        if (db.questions_and_answers["Q12"].find("5") != -1):
            if (db.questions_and_answers["Q17"].find("1") != -1):
                report.write("\n\n")

                report.write(open("resources/data/security_best_practices_guidelines/Third_Party_Javascript_Management_Cheat_Sheet.md",
                                  "r").read())

        # Password Storage security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(open("resources/data/security_best_practices_guidelines/Password_Storage_Cheat_Sheet.md", "r").read())

        # PHP Configuration security best practices guidelines
        if (db.questions_and_answers["Q12"].find("6") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/PHP_Configuration_Cheat_Sheet.md", "r").read())

            # Ruby on Rails security best practices guidelines
        if (db.questions_and_answers["Q12"].find("6") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Ruby_on_Rails_Cheat_Sheet.md", "r").read())

            # Server Side Request Forgery Prevention security best practices guidelines
        if (db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1):
            if (db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(
                    open("resources/data/security_best_practices_guidelines/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md",
                         "r").read())

        # Session Management security best practices guidelines
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(open("resources/data/security_best_practices_guidelines/Session_Management_Cheat_Sheet.md", "r").read())

        # Transport Layer Protection security best practices guidelines
        if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
            report.write("\n\n")

            report.write(
                open("resources/data/security_best_practices_guidelines/Transport_Layer_Protection_Cheat_Sheet.md", "r").read())

        # Input Validation security best practices guidelines
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                if db.questions_and_answers["Q13"].find("1") != -1:
                    report.write("\n\n")

                    report.write(open("resources/data/security_best_practices_guidelines/Input_Validation_Cheat_Sheet.md", "r").read())

        # User Privacy Protection security best practices guidelines
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if (db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n\n")

                report.write(
                    open("resources/data/security_best_practices_guidelines/User_Privacy_Protection_Cheat_Sheet.md", "r").read())

        # Cryptography security best practices guidelines
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/Cryptography_guide.md", "r").read())

        # Secure Sofware Update security best practices guidelines
        if db.questions_and_answers["Q16"].find("1") != -1:
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/App_Update_guide.md", "r").read())

        # Third-Party Application security best practices guidelines
        if db.questions_and_answers["Q17"].find("1") != -1:
            report.write("\n\n")

            report.write(open("resources/data/security_best_practices_guidelines/App_Third_Party_guide.md", "r").read())

        report.close()
        self.security_best_practices_convert_report()
        print("\n\n # Processing done! Check your security best practices guidelines in the GOOD_PRACTICES.pdf file")

    """
    [Summary]: Method to convert the markdown Security Best Practices Guidelines (SBPG) report to html and pdf format
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def security_best_practices_convert_report(self):
        # input_filename = ("guides/example_report.md")
        # input_filename = "some_markdown.md")
        input_filename = ("GOOD_PRACTICES.md")

        output_filename = ("GOOD_PRACTICES.html")

        with open(input_filename, "r") as f:
            html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

        out = open(output_filename, "w")
        out.write(html_text)

        # writing in pdf file, the html content

        resultFile = open("GOOD_PRACTICES.pdf", "w+b")
        pisa.CreatePDF(html_text, dest=resultFile)