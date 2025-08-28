from markdown import markdown
from xhtml2pdf import pisa
from src.handler.data_handler import  DataHandler

db = DataHandler()

class CM2STModule:
    """
    [Summary]: Method responsible for processing information about STSAT module
    [Arguments]: No arguments
    [Return]: No return
    """

    def get_security_test_recommendation(self):
        print("")
        print("  Processing information.....")
        print("")

        report = open("TEST_SPECIFICATION.md", "w")
        report.write("# Final Security Test Specification and Tools Report  " + '\n')
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

        # Testing DoS Jamming attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("1") != -1 or db.questions_and_answers["Q21"].find("2") != -1 or \
                    db.questions_and_answers["Q21"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/cellular_jamming_testing_guide.md", "r").read())

        # Testing Wi-Fi Jamming attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/wi_fi_jamming_testing_guide.md", "r").read())

        # Testing NFC Payment Replay attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("9") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/nfc_payment_replay_testing_guide.md", "r").read())

        # Testing Orbital Jamming attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("1") != -1 or db.questions_and_answers["Q21"].find("2") != -1 or \
                    db.questions_and_answers["Q21"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/orbital_jamming_testing_guide.md", "r").read())

        # Testing GPS Jamming attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("7") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/gps_jamming_testing_guide.md", "r").read())

        # Testing Bluesnarfing attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("5") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/bluesnarfing_testing_guide.md", "r").read())

        # Testing Bluejacking attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("5") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/bluejacking_testing_guide.md", "r").read())

        # Testing Wi-Fi SSID Tracking attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/wi_fi_ssid_tracking_testing_guide.md", "r").read())

        # Testing Byzantine attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/byzantine_testing_guide.md", "r").read())

        # Testing On-Off attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/on_off_testing_guide.md", "r").read())

        # Testing Malicious Insider attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/malicious_insider_testing_guide.md", "r").read())

        # Testing Sniffing attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/sniffing_testing_guide.md", "r").read())

        # Testing MitM attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/mitm_testing_guide.md", "r").read())

        # Testing Eavesdropping attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q18"].find("4") != -1 or db.questions_and_answers["Q18"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/eavesdropping_testing_guide.md", "r").read())

        # Testing CSRF attack
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/csrf_testing_guide.md", "r").read())

        # Testing SQLi attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/sqli_testing_guide.md", "r").read())

        # Testing XSS attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/xss_testing_guide.md", "r").read())

        # Testing SSRF attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/ssrf_testing_guide.md", "r").read())

        # Testing Command Injection attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/command_injection_testing_guide.md", "r").read())

        # Testing Command Injection attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/code_injection_testing_guide.md", "r").read())

        # Testing Phishing attacks
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/phishing_testing_guide.md", "r").read())

        # Testing Pharming attack
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/pharming_testing_guide.md", "r").read())

        # Testing Spoofing attack
        if db.questions_and_answers["Q1"].find("4") != -1 or db.questions_and_answers["Q1"].find("3") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and \
                    db.questions_and_answers["Q6"].find("1") != -1 and (
                    db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                    db.questions_and_answers["Q8"].find("3") != -1):
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/spoofing_testing_guide.md", "r").read())

        # Testing Session Fixation attack
        if db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 and db.questions_and_answers["Q8"].find("2") != -1 and \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    if db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1:
                        report.write("\n")
                        report.write("\n")

                        report.write(open("resources/data/security_test_recommendation/session_fixation_testing_guide.md", "r").read())

        # Testing Session Hijacking attacks
        if db.questions_and_answers["Q1"].find("3") != -1 or db.questions_and_answers["Q1"].find("4") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 and db.questions_and_answers["Q8"].find("2") != -1 and \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    if db.questions_and_answers["Q18"].find("2") != -1 or db.questions_and_answers["Q18"].find("4") != -1:
                        report.write("\n")
                        report.write("\n")

                        report.write(
                            open("resources/data/security_test_recommendation/session_hijacking_testing_guide.md", "r").read())

        # Testing Access Point Hijacking attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("6") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/access_point_hijacking_testing_guide.md", "r").read())

        # Testing Cellular Rogue Base Station attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q21"].find("1") != -1 or db.questions_and_answers["Q21"].find("2") != -1 or \
                    db.questions_and_answers["Q21"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(
                    open("resources/data/security_test_recommendation/cellular_rogue_base_station_testing_guide.md", "r").read())

        # Testing GPS Spoofing attack
        if db.questions_and_answers["Q21"].find("7") != -1:
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_test_recommendation/gps_spoofing_testing_guide.md", "r").read())

        # Testing RF Interference on RFIDs attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/interference_on_rfid_testing_guide.md", "r").read())

        # Testing Node Tampering attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q8"].find("2") != -1 or db.questions_and_answers["Q8"].find("3") != -1:
                if db.questions_and_answers["Q22"].find("1") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/security_test_recommendation/node_tampering_testing_guide.md", "r").read())

        # Testing Node Jamming in WSNs attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/node_jamming_testing_guide.md", "r").read())

            # Testing Sybil attack
            if db.questions_and_answers["Q1"].find("7") != -1:
                if db.questions_and_answers["Q21"].find("10") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/security_test_recommendation/sybil_testing_guide.md", "r").read())

        # Testing Malicious Node Injection attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("10") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/malicious_node_injection_testing_guide.md", "r").read())

        # Testing RFID Spoofing attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/rfid_Spoofing_testing_guide.md", "r").read())

        # Testing RFID Cloning attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/rfid_cloning_testing_guide.md", "r").read())

        # Testing RFID Unauthorized Access attack
        if db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q21"].find("8") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/rfid_unauthorized_access_testing_guide.md", "r").read())

        # Testing Botnet attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/botnet_testing_guide.md", "r").read())

        # Testing Malware-as-a-Service attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/maas_testing_guide.md", "r").read())

        # Testing Buffer Overflow attacks
        if db.questions_and_answers["Q1"].find("2") != -1 or db.questions_and_answers["Q1"].find("6") != -1 or \
                db.questions_and_answers["Q1"].find("7") != -1:
            if db.questions_and_answers["Q12"].find("2") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/buffer_overflow_testing_guide.md", "r").read())

        # Testing Bypassing Physical Security attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/bps_testing_guide.md", "r").read())

        # Testing Physical theft attack
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
            if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                    db.questions_and_answers["Q8"].find("3") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/physical_theft_testing_guide.md", "r").read())

            # Testing VM Migration attacks
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/security_test_recommendation/vm_migration_testing_guide.md", "r").read())

        # Testing Side-Channel attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/side_channel_testing_guide.md", "r").read())

        # Testing Spectre attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/spectre_testing_guide.md", "r").read())

        # Testing Meltdown attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/meltdown_testing_guide.md", "r").read())

        # Testing Hardware Integrity attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            if db.questions_and_answers["Q22"].find("1") != -1:
                report.write("\n")
                report.write("\n")

                report.write(open("resources/data/security_test_recommendation/hardware_integrity_testing_guide.md", "r").read())

        # Testing Rowhammer attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_test_recommendation/rowhammer_testing_guide.md", "r").read())

        # Testing Reverse Engineering attacks
        if db.questions_and_answers["Q1"].find("1") != -1 and db.questions_and_answers["Q5"].find("2") != -1:
            if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1:
                if db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or \
                        db.questions_and_answers["Q8"].find("3") != -1:
                    report.write("\n")
                    report.write("\n")

                    report.write(open("resources/data/security_test_recommendation/rea_testing_guide.md", "r").read())

        # Testing VM Escape attacks
        if db.questions_and_answers["Q3"].find("1") != -1 and db.questions_and_answers["Q5"].find("1") != -1 and (
                db.questions_and_answers["Q8"].find("1") != -1 or db.questions_and_answers["Q8"].find("2") != -1 or
                db.questions_and_answers["Q8"].find("3") != -1):
            report.write("\n")
            report.write("\n")

            report.write(open("resources/data/security_test_recommendation/vm_escape_testing_guide.md", "r").read())

        report.close()
        self.security_test_recommendation_convert_report()
        print("\n\n # Processing done! Check your security test specification and automation tools in the TEST_SPECIFICATION.pdf file")

    """
    [Summary]: Method to convert the markdown Security Test Specification and Automation Tools (STSAT) report to html and pdf format
    [Arguments]: No arguments
    [Returns]: No return
    """

    def security_test_recommendation_convert_report(self):
        # input_filename = ("guides/example_report.md")
        # input_filename = "some_markdown.md")
        input_filename = ("TEST_SPECIFICATION.md")

        output_filename = ("TEST_SPECIFICATION.html")

        with open(input_filename, "r") as f:
            html_text = markdown(f.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.sane_lists'])

        out = open(output_filename, "w")
        out.write(html_text)

        # writing in pdf file, the html content

        resultFile = open("TEST_SPECIFICATION.pdf", "w+b")
        pisa.CreatePDF(html_text, dest=resultFile)
