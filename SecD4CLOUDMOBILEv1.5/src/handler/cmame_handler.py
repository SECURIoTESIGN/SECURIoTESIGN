from markdown import markdown
from xhtml2pdf import pisa
from src.handler.data_handler import  DataHandler

db = DataHandler()

class CMAMEModule:
    """
    [Summary]: Method responsible for processing information about CMAME module
    [Arguments]: No arguments
    [Return]: No return
    """

    def get_attack_models(self):
        print("")
        print("  Processing information.....")
        print("")

        report = open("ATTACKS_MAPPING.md", "w")
        report.write("# Final Attack Models Report  " + '\n')
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

        # MitM attack model
        if db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/mitm_attack_model.md", "r").read())

                # Write de scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/MiTM_Attack_Tree.JPG)")
                report.write("\n\n")

        # Brute Force attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write(open("resources/data/attack_models/brute_force_Attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Brute_Force_Attack_Tree.JPG)")
                report.write("\n\n")

        # Eavesdropping attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write(open("resources/data/attack_models/eavesdropping_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Eavesdropping_Attack_Tree.JPG)")
                report.write("\n\n")

        # XSS attack model
        if db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1 and (
                db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/xss_attack_model.md", "r").read())

                # Write de scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/XSS_Attack_Tree.JPG)")
                report.write("\n\n")

        # CSRF attack model
        if db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1 and (
                db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/csrf_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/CSRF_Attack_Tree.JPG)")
                report.write("\n\n")

        # Cookie Poisoning attack model
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1) and (
                db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/attack_models/cookie_poisoning_attack_model.md", "r").read())

            # Write de scheme in the report
            report.write("\n\n")
            report.write("![alt text](resources/data/attack_models/Cookie_Poisoning_Attack_Tree.JPG)")
            report.write("\n\n")

        # Cache Poisoning attack model
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1) and (
                db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/attack_models/cache_poisoning_attack_model.md", "r").read())

            # Write de scheme in the report
            report.write("\n\n")
            report.write("![alt text](resources/data/attack_models/Cache_Poisoning_Attack_Tree.JPG)")
            report.write("\n\n")

        # Malicious QR Code attack model
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1) and \
                db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/malicious_qr_code_attack_model.md", "r").read())

                # Write de scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Malicious_QR_Code_Attack_Tree.JPG)")
                report.write("\n\n")

        # SQLi attack model
        if (db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1) and \
                db.questions_and_answers["Q3"].find("1") != -1:
            if db.questions_and_answers["Q5"].find("1") != -1 and db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q7"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/sqli_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/SQL_Injection_Attack_Tree.JPG)")
                report.write("\n\n")

        # Flooding attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write(open("resources/data/attack_models/flooding_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Flooding_Attack_Tree.JPG)")
                report.write("\n\n")

        # Sniffing attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write(open("resources/data/attack_models/sniffing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Sniffing_Attack_Tree.JPG)")
                report.write("\n\n")

        # Phishing attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/phishing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Phishing_Attack_Tree.JPG)")
                report.write("\n\n")

        # Pharming attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/pharming_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Pharming_Attack_Tree.JPG)")
                report.write("\n\n")

        # Botnet attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1):
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/botnet_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Botnet_Attack_Tree.JPG)")
                report.write("\n\n")

        # Session Hijacking attack model
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("2") != -1 and db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/session_hijacking_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Session_Hijacking_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Buffer Overflow attack model
        if db.questions_and_answers["Q1"].find("2") != -1 or db.questions_and_answers["Q1"].find("6") != -1 or \
                db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q12"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/buffer_overflow_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Buffer_Overflow_Attack_Tree.JPG)")
                report.write("\n\n")

        # Spoofing attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/spoofing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Spoofing_Attack_Tree.JPG)")
                report.write("\n\n")

        # If the system was development for Android, iOS, Tizen and embedded platforms (Attack on VM at migration )
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/vm_migration_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/VM_Migration_Attack_Tree.JPG)")
                report.write("\n\n")

        # Malicious Insider attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q22"].find("1") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/malicious_insider_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Malicious_Insider_Attack_Tree.JPG)")
                    report.write("\n\n")

        # VM Escape attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/vm_escape_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/VM_Escape_Attack_Tree.JPG)")
                report.write("\n\n")

        # Side-Channel attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/side_channel_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Side_Channel_Attack_Tree.JPG)")
                report.write("\n\n")

            # Malware-as-a-Service attack model
            if (db.questions_and_answers["Q1"].find("1") != -1 or db.questions_and_answers["Q1"].find("2") != -1) or \
                    db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("5") != -1 or \
                    db.questions_and_answers["Q1"].find("6") != -1 or db.questions_and_answers["Q1"].find("7") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/malware_injection_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/MaaS_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Tampering attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q22"].find("1") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/tampering_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Tampering_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Bluejacking and Bluesnarfing attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("5") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/bluejacking_attack_model.md", "r").read())

                    report.write("\n\n")
                    report.write(open("resources/data/attack_models/bluesnarfing_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Bluetooth_Attack_Tree.JPG)")
                    report.write("\n\n")

        # GPS Jamming attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("7") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/gps_jamming_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/GPS_Jamming_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Code injection attack model
        if db.questions_and_answers["Q1"].find("3") != -1 and db.questions_and_answers["Q1"].find("4") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/code_injection_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Code_Injection_Attack_Tree.JPG)")
                    report.write("\n\n")

        # SSRF attack model
        if db.questions_and_answers["Q1"].find("3") != -1 and db.questions_and_answers["Q1"].find("4") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/ssrf_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/SSRF_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Command Injection attack model
        if db.questions_and_answers["Q1"].find("3") != -1 and db.questions_and_answers["Q1"].find("4") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/command_injection_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Command_Injection_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Cellular Jamming attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("1") != -1 or db.questions_and_answers["Q21"].find("2") != -1 or \
                        db.questions_and_answers["Q21"].find("3") != -1 or db.questions_and_answers["Q21"].find("4") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/cellular_jamming_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Cellular_Jamming_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Cryptanalysis attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/cryptanalysis_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Cryptanalysis_Attack_Tree.JPG)")
                report.write("\n\n")

        # Reverse Engineering attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/reverse_engineering_attack_model.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Reverse_Engineering_Attack_Tree.JPG)")
                report.write("\n\n")

        # Audit Log Manipulation attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q14"].find("1") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/audit_log_attack_model.md", "r").read())

                # Tampering Detection attack tree diagram
                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Audit_Log_Manipulation_Attack_Tree.JPG)")
                report.write("\n")
                report.write("\n")

        # Wi-Fi Jamming Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("6") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/wi_fi_jamming_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Wi_Fi_Jamming_Attack_Tree.JPG)")
                    report.write("\n\n")

        # Wi-Fi SSID Tracking attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("6") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/wi_fi_ssid_tracking_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("![alt text](resources/data/attack_models/Wi_Fi_SSID_Tracking_Attack_Tree.JPG)")
        # Byzantine Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q21"].find("6") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/byzantine_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Byzantine_Attack_Tree.JPG)")

            # On-Off Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/on_off_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/On_Off_Attack_Tree.JPG)")

        # Spectre Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/spectre_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Spectre_Attack_Tree.JPG)")

        # Meltdown Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/meltdown_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Meltdown_Attack_Tree.JPG)")

        # Hardware Integrity Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/hardware_integrity_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Hardware_Integrity_Attack_Tree.JPG)")

        # Rowhammer Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/attack_models/rowhammer_attack_model.md", "r").read())

            # Write the scheme in the report
            report.write("\n\n")
            report.write("![alt text](resources/data/attack_models/Rowhammer_Attack_Tree.JPG)")

        # RF Interference on RFIDs attack Model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/interference_on_rfid_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Interference_On_RFID_Attack_Tree.JPG)")

        # Node Tampering attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q22"].find("1") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/attack_models/node_tampering_attack_model.md", "r").read())

                    # Write the scheme in the report
                    report.write("\n\n")
                    report.write("![alt text](resources/data/attack_models/Node_Tampering_Attack_Tree.JPG)")

        # Node Jamming in WSNs attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/node_jamming_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Node_Jamming_Attack_Tree.JPG)")

        # Sybil attack Model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/sybil_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Sybil_Attack_Tree.JPG)")

        # Malicious Node Injection attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/malicious_node_injection_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Malicious_Node_Injection_Attack_Tree.JPG)")

        # RFID Spoofing attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/rfid_Spoofing_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/RFID_Spoofing_Attack_Tree.JPG)")

        # RFID Cloning attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/rfid_cloning_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/RFID_Cloning_Attack_Tree.JPG)")

        # RFID Unauthorized Access attack model
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/rfid_unauthorized_access_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/RFID_Unauthorized_Access_Attack_Tree.JPG)")

            # Orbital Jamming attack model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("1") != -1 or db.questions_and_answers["Q21"].find("2") != -1 or \
                    db.questions_and_answers["Q21"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/orbital_jamming_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/Orbital_Jamming_Attack_Tree.JPG)")

            # NFC Payment Replay Attack Model
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("9") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/attack_models/nfc_payment_replay_attack_model.md", "r").read())

                # Write the scheme in the report
                report.write("\n\n")
                report.write("![alt text](resources/data/attack_models/NFC_Payment_Replay_Attack_Tree.JPG)")

        report.close()
        self.attack_models_convert_report()
        print("\n\n # Processing done! Check your attack models in the ATTACKS_MAPPING.pdf file")

    """
    [Summary]: Method to convert the markdown Attack Models Elicitation (AME) report to html and pdf format
    [Arguments]: 
        - $version$: An integer constant equal to unity
    [Returns]: No return
    """

    def attack_models_convert_report(self):
        # input_filename = ("guides/example_report.md")
        # input_filename = "some_markdown.md")
        input_filename = ("ATTACKS_MAPPING.md")

        output_filename = ("ATTACKS_MAPPING.html")

        with open(input_filename, "r") as f:
            html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

        out = open(output_filename, "w")
        out.write(html_text)

        # writing in pdf file, the html content

        resultFile = open("ATTACKS_MAPPING.pdf", "w+b")
        pisa.CreatePDF(html_text, dest=resultFile)
