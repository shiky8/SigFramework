import os
import subprocess as sp


def simulator_MTForwardSMSResp(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_MSC,Target_IMSI,locael_GT,SMSC_GT,Sender_Name,SMS_Content):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")


    p=os.system("java -jar ./mtsms/test/MTForwardSMSResp.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+ Target_MSC+" &  java -jar ./mtsms/MTForwardSMS.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Target_MSC+" "+locael_GT+" "+SMSC_GT+" "+Sender_Name+" "+SMS_Content)
    p2 = os.system("pkill java")

def simulator_SendIMSI(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Target_IMSI,locael_GT):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    print("hi")
    # ipinng: str = str(sp.getoutput('ip address'))


    # if(client_ip not in ipinng):
    #     os.system("ip address add "+client_ip+" dev lo")
    # if(server_ip not in ipinng):
    #     os.system("ip address add "+server_ip+" dev lo")
    
    p=os.system("java -jar ./simsi/test/SendIMSI.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_MSISDN+"  &  java -jar ./simsi/SendIMSI.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+locael_GT+" "+Targer_MSISDN)
    print("hi2")
    p2 = os.system("pkill java")
    print("hi3")

def simulator_UpdateLocation(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_IMSI,Targer_IMSI_MGT,Targer_MSC,SMS_Content,locael_GT,locael_vlr):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
    


    p=os.system("java -jar ./UpdateLocation/test/UpdateLocation.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" not_tcp &  java -jar ./UpdateLocation/UpdateLocation.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+locael_vlr+" n")
    p2 = os.system("pkill java")

def simulator_tracking_AnyTimeInterrogation(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Lat_ps,user_i_Long_ps,user_i_Uncertain_ps,user_i_Long2):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
      

    p=os.system("java -jar ./tracking/ati/test/AnyTimeInterrogation.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Targer_MSISDN+" "+user_i_mcc+" "+ user_i_mnc+" "+ user_i_LAC2+" "+ user_i_CI+" "+ user_i_Lat +" "+user_i_Uncertain +" "+user_i_Lat_ps+" "+ user_i_Long_ps+" "+ user_i_Uncertain_ps+" "+ user_i_Long2+" &  java -jar ./tracking/ati/AnyTimeInterrogation.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_GT)
    p2 = os.system("pkill java")

def simulator_tracking_ProvideSubscriberInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Targer_HLR,Targer_IMSI,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Lat_ps,user_i_Long_ps,user_i_Uncertain_ps,user_i_Long2):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
     

    p=os.system("java -jar ./tracking/psi/test/ProvideSubscriberInfo.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Targer_MSISDN+" "+user_i_mcc+" "+ user_i_mnc+" "+ user_i_LAC2+" "+ user_i_CI+" "+ user_i_Lat +" "+user_i_Uncertain +" "+user_i_Lat_ps+" "+ user_i_Long_ps+" "+ user_i_Uncertain_ps+" "+ user_i_Long2+" no_tcp & java -jar ./tracking/psi/ProvideSubscriberInfo.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+Targer_IMSI+" "+Targer_HLR)
    p2 = os.system("pkill java")

def simulator_tracking_SendRoutingInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_MSC,Targer_IMSI,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Long2):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
      

    p=os.system("java -jar ./tracking/sri/test/SendRoutingInfo.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Targer_MSISDN+" "+ Targer_IMSI+" "+user_i_mcc+" "+ user_i_mnc+" "+ user_i_LAC2+" "+ user_i_CI+" "+ user_i_Lat +" "+user_i_Uncertain +" "+user_i_Long2+" & java -jar ./tracking/sri/SendRoutingInfo.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_MSC)
    p2 = os.system("pkill java")

def simulator_tracking_SendRoutingInfoForGPRS(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_GGSN,user_i_ggsn_ipv4,user_i_sgsn_ipv4):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")
     

    p=os.system("java -jar ./tracking/srigprs/test/SendRoutingInfoForGPRS.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Targer_HLR+" "+user_i_ggsn_ipv4+" "+user_i_sgsn_ipv4+"  & java -jar ./tracking/srigprs/SendRoutingInfoForGPRS.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_IMSI+" "+Targer_HLR+" "+Targer_GGSN)
    p2 = os.system("pkill java")

def simulator_tracking_SendRoutingInfoForSM(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_MSISDN,Targer_MSC,Targer_SMSC):
    p0 = os.system("rm *.xml")
    p0 = os.system("rm outingss7.txt")
    ipinng: str = str(sp.getoutput('ip address'))


    
    if(client_ip not in ipinng):
        os.system("ip address add "+client_ip+" dev lo")
    if(server_ip not in ipinng):
        os.system("ip address add "+server_ip+" dev lo")


    p=os.system("java -jar ./tracking/srism/test/SendRoutingInfoForSM.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Targer_MSISDN+" "+Targer_IMSI+" "+Targer_HLR+"  & java -jar ./tracking/srism/SendRoutingInfoForSM.jar 1 2 "+client_ip+" "+ client_port+" "+ server_ip+" "+ server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+Targer_HLR+" "+Targer_MSC+" "+Targer_SMSC)
    p2 = os.system("pkill java")