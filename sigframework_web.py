from flask import Flask, render_template, request, send_file, Response, url_for, send_from_directory
import test_gui_web as ts_gui
import attack_gui_web as Atty_gui
import os
import subprocess as sp

# UPLOAD_FOLDER = '/home/shiky/cp2/temp/testing'
# filename = ""
# ALLOWED_EXTENSIONS = {'txt', 'cve', 'list', 'lst', 'text', 'passwd'}
app = Flask(__name__)
app._static_folder = 'static'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template("Home.html")


@app.route('/index.html')
def index2():
    return render_template("Home.html")
@app.route('/Home.html')
def index3():
    return render_template("Home.html")

@app.route('/Attack_UpdateLocation.html')
def Attack_UpdateLocation():
    return render_template("Attack_UpdateLocation.html")

@app.route('/Attack_MTForwardSMSResp.html')
def Attack_MTForwardSMSResp():
    return render_template("Attack_MTForwardSMSResp.html")

@app.route('/Attack_SendIMSI.html')
def Attack_SendIMSI():
    return render_template("Attack_SendIMSI.html")

@app.route('/Attack_AnyTimeInterrogation.html')
def Attack_AnyTimeInterrogation():
    return render_template("Attack_AnyTimeInterrogation.html")

@app.route('/Attack_ProvideSubsriberInfo.html')
def Attack_ProvideSubscriberInfo():
    return render_template("Attack_ProvideSubsriberInfo.html")

@app.route('/Attack_SendRoutingInfo.html')
def Attack_SendRoutingInfo():
    return render_template("Attack_SendRoutingInfo.html")

@app.route('/Attack_SendRoutingInfoForGPRS.html')
def Attack_SendRoutingInfoForGPRS():
    return render_template("Attack_SendRoutingInfoForGPRS.html")

@app.route('/Attack_SendRoutingInfoForSM.html')
def Attack_SendRoutingInfoForSM():
    return render_template("Attack_SendRoutingInfoForSM.html")

@app.route('/Simulator_UpdateLocation.html')
def Simulator_UpdateLocation():
    return render_template("Simulator_UpdateLocation.html")

@app.route('/Simulator_MTForwardSMSResp.html')
def Simulator_MTForwardSMSResp():
    return render_template("Simulator_MTForwardSMSResp.html")

@app.route('/Simulator_SendIMSI.html')
def Simulator_SendIMSI():
    return render_template("Simulator_SendIMSI.html")

@app.route('/simulator_AnyTimeInterrogation.html')
def simulator_AnyTimeInterrogation():
    return render_template("simulator_AnyTimeInterrogation.html")

@app.route('/simulator_ProvideSubsriberInfo.html')
def simulator_ProvideSubscriberInfo():
    return render_template("simulator_ProvideSubsriberInfo.html")

@app.route('/simulator_SendRoutingInfo.html')
def simulator_SendRoutingInfo():
    return render_template("simulator_SendRoutingInfo.html")

@app.route('/simulator_SendRoutingInfoForGPRS.html')
def simulator_SendRoutingInfoForGPRS():
    return render_template("simulator_SendRoutingInfoForGPRS.html")

@app.route('/simulator_SendRoutingInfoForSM.html')
def simulator_SendRoutingInfoForSM():
    return render_template("simulator_SendRoutingInfoForSM.html")

@app.route('/simulator_SendRoutingInfoForSM.html', methods =["POST"])
def SendRoutingInfoForSM():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    Targer_HLR = str(request.form.get('Targer_HLR'))

    Targer_MSISDN  = str(request.form.get('Targer_MSISDN'))
    Targer_MSC = str(request.form.get('Targer_MSC'))
    Targer_SMSC = str(request.form.get('Targer_SMSC'))


    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    ts_gui.simulator_tracking_SendRoutingInfoForSM(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_MSISDN,Targer_MSC,Targer_SMSC)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("simulator_SendRoutingInfoForSM.html",deocded_massage_temp=str(output55))


@app.route('/simulator_SendRoutingInfoForGPRS.html', methods =["POST"])
def SendRoutingInfoForGPRS():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    Targer_HLR = str(request.form.get('Targer_HLR'))
    Targer_GGSN  = str(request.form.get('Targer_GGSN'))
    user_i_ggsn_ipv4 = str(request.form.get('user_i_ggsn_ipv4'))
    user_i_sgsn_ipv4 = str(request.form.get('user_i_sgsn_ipv4'))


    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    ts_gui.simulator_tracking_SendRoutingInfoForGPRS(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_GGSN,user_i_ggsn_ipv4,user_i_sgsn_ipv4)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("simulator_SendRoutingInfoForGPRS.html",deocded_massage_temp=str(output55))

@app.route('/simulator_SendRoutingInfo.html', methods =["POST"])
def SendRoutingInfo():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_MSC = str(request.form.get('locael_MSC'))
    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    

    user_i_mcc = str(request.form.get('user_i_mcc'))
    user_i_mnc = str(request.form.get('user_i_mnc'))
    user_i_LAC2 = str(request.form.get('user_i_LAC2'))
    user_i_CI  = str(request.form.get('user_i_CI'))
    user_i_Lat  = str(request.form.get('user_i_Lat'))
    user_i_Uncertain  = str(request.form.get('user_i_Uncertain'))
    user_i_Long2 = str(request.form.get('user_i_Long2'))

    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    ts_gui.simulator_tracking_SendRoutingInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_MSC,Targer_IMSI,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Long2)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("simulator_SendRoutingInfo.html",deocded_massage_temp=str(output55))



@app.route('/simulator_ProvideSubsriberInfo.html', methods =["POST"])
def ProvideSubsriberInfo():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    Targer_HLR = str(request.form.get('Targer_HLR'))
    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    

    user_i_mcc = str(request.form.get('user_i_mcc'))
    user_i_mnc = str(request.form.get('user_i_mnc'))
    user_i_LAC2 = str(request.form.get('user_i_LAC2'))
    user_i_CI  = str(request.form.get('user_i_CI'))
    user_i_Lat  = str(request.form.get('user_i_Lat'))
    user_i_Uncertain  = str(request.form.get('user_i_Uncertain'))
    user_i_Lat_ps = str(request.form.get('user_i_Lat_ps'))
    user_i_Long_ps = str(request.form.get('user_i_Long_ps'))
    user_i_Uncertain_ps  = str(request.form.get('user_i_Uncertain_ps'))
    user_i_Long2 = str(request.form.get('user_i_Long2'))

    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    ts_gui.simulator_tracking_ProvideSubscriberInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Targer_HLR,Targer_IMSI,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Lat_ps,user_i_Long_ps,user_i_Uncertain_ps,user_i_Long2)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("simulator_ProvideSubsriberInfo.html",deocded_massage_temp=str(output55))


@app.route('/simulator_AnyTimeInterrogation.html', methods =["POST"])
def AnyTimeInterrogation():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_GT = str(request.form.get('locael_GT'))

    

    user_i_mcc = str(request.form.get('user_i_mcc'))
    user_i_mnc = str(request.form.get('user_i_mnc'))
    user_i_LAC2 = str(request.form.get('user_i_LAC2'))
    user_i_CI  = str(request.form.get('user_i_CI'))
    user_i_Lat  = str(request.form.get('user_i_Lat'))
    user_i_Uncertain  = str(request.form.get('user_i_Uncertain'))
    user_i_Lat_ps = str(request.form.get('user_i_Lat_ps'))
    user_i_Long_ps = str(request.form.get('user_i_Long_ps'))
    user_i_Uncertain_ps  = str(request.form.get('user_i_Uncertain_ps'))
    user_i_Long2 = str(request.form.get('user_i_Long2'))

    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    ts_gui.simulator_tracking_AnyTimeInterrogation(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT,user_i_mcc,user_i_mnc,user_i_LAC2,user_i_CI,user_i_Lat,user_i_Uncertain,user_i_Lat_ps,user_i_Long_ps,user_i_Uncertain_ps,user_i_Long2)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("simulator_AnyTimeInterrogation.html",deocded_massage_temp=str(output55))

@app.route('/Simulator_MTForwardSMSResp.html', methods =["POST"])
def MTForwardSMSResp():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    SMSC_GT = str(request.form.get('SMSC_GT'))
    Sender_Name = str(request.form.get('Sender_Name'))
    SMS_Content = str(request.form.get('SMS_Content'))

    Target_MSC = str(request.form.get('Target_MSC'))
    locael_GT = str(request.form.get('locael_GT'))

    Target_IMSI = str(request.form.get('Target_IMSI'))
    if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+SMSC_GT+" "+locael_GT+" "+Target_IMSI+" "+Target_MSC+" "+Sender_Name+" " +SMS_Content)   
    ts_gui.simulator_MTForwardSMSResp(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_MSC,Target_IMSI,locael_GT,SMSC_GT,Sender_Name,SMS_Content)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Simulator_MTForwardSMSResp.html",deocded_massage_temp=str(output55))


@app.route('/Simulator_SendIMSI.html', methods =["POST"])
def SendIMSI():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_GT = str(request.form.get('locael_GT'))

    Target_IMSI = str(request.form.get('Target_IMSI'))
    if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_GT+" "+Target_IMSI)   
    ts_gui.simulator_SendIMSI(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Target_IMSI,locael_GT)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Simulator_SendIMSI.html",deocded_massage_temp=str(output55))


@app.route('/Simulator_UpdateLocation.html', methods =["POST"])
def UpdateLocation():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Target_IMSI = str(request.form.get('Target_IMSI'))
    Targer_IMSI_MGT = str(request.form.get('Targer_IMSI_MGT'))
    if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)
    locael_GT = str(request.form.get('locael_GT'))

    Targer_MSC = str(request.form.get('Targer_MSC'))
    SMS_Content = str(request.form.get('SMS_Content'))

    locael_vlr = str(request.form.get('locael_vlr'))

    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    ts_gui.simulator_UpdateLocation(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_IMSI,Targer_IMSI_MGT,Targer_MSC,SMS_Content,locael_GT,locael_vlr)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Simulator_UpdateLocation.html",deocded_massage_temp=str(output55))

#Attacker

@app.route('/Attack_SendRoutingInfoForSM.html', methods =["POST"])
def Att_SendRoutingInfoForSM():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

   
    Targer_HLR = str(request.form.get('Targer_HLR'))

    Targer_MSISDN  = str(request.form.get('Targer_MSISDN'))
    Targer_MSC = str(request.form.get('Targer_MSC'))
    Targer_SMSC = str(request.form.get('Targer_SMSC'))


    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    Atty_gui.attack_tracking_SendRoutingInfoForSM(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_HLR,Targer_MSISDN,Targer_MSC,Targer_SMSC)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_SendRoutingInfoForSM.html",deocded_massage_temp=str(output55))


@app.route('/Attack_SendRoutingInfoForGPRS.html', methods =["POST"])
def Att_SendRoutingInfoForGPRS():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    Targer_HLR = str(request.form.get('Targer_HLR'))
    Targer_GGSN  = str(request.form.get('Targer_GGSN'))
   
    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    Atty_gui.attack_tracking_SendRoutingInfoForGPRS(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_IMSI,Targer_HLR,Targer_GGSN)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_SendRoutingInfoForGPRS.html",deocded_massage_temp=str(output55))

@app.route('/Attack_SendRoutingInfo.html', methods =["POST"])
def Att_SendRoutingInfo():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_MSC = str(request.form.get('locael_MSC'))
    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    


    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    Atty_gui.attack_tracking_SendRoutingInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_MSC)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_SendRoutingInfo.html",deocded_massage_temp=str(output55))



@app.route('/Attack_ProvideSubsriberInfo.html', methods =["POST"])
def Att_ProvideSubsriberInfo():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    Targer_HLR = str(request.form.get('Targer_HLR'))
    Targer_IMSI = str(request.form.get('Targer_IMSI'))
    if(len(Targer_IMSI) < 15 or len(Targer_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    

   

    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    Atty_gui.attack_tracking_ProvideSubscriberInfo(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,Targer_HLR,Targer_IMSI)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_ProvideSubsriberInfo.html",deocded_massage_temp=str(output55))


@app.route('/Attack_AnyTimeInterrogation.html', methods =["POST"])
def Att_AnyTimeInterrogation():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_GT = str(request.form.get('locael_GT'))

    

   

    # print(client_ip+ client_port+ server_ip+ server_port+Targer_MSISDN+user_i_mcc+ user_i_mnc+ user_i_LAC2+ user_i_CI+ user_i_Lat +user_i_Uncertain +user_i_Lat_ps+ user_i_Long_ps+ user_i_Uncertain_ps+ user_i_Long2+locael_GT+Network_Indicator)


    Atty_gui.attack_tracking_AnyTimeInterrogation(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_AnyTimeInterrogation.html",deocded_massage_temp=str(output55))

@app.route('/Attack_MTForwardSMSResp.html', methods =["POST"])
def Att_MTForwardSMSResp():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    SMSC_GT = str(request.form.get('SMSC_GT'))
    Sender_Name = str(request.form.get('Sender_Name'))
    SMS_Content = str(request.form.get('SMS_Content'))

    Target_MSC = str(request.form.get('Target_MSC'))
    locael_GT = str(request.form.get('locael_GT'))

    Target_IMSI = str(request.form.get('Target_IMSI'))
    if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)

    print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+SMSC_GT+" "+locael_GT+" "+Target_IMSI+" "+Target_MSC+" "+Sender_Name+" " +SMS_Content)   
    Atty_gui.attack_MTForwardSMSResp(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_MSC,Target_IMSI,locael_GT,SMSC_GT,Sender_Name,SMS_Content)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_MTForwardSMSResp.html",deocded_massage_temp=str(output55))


@app.route('/Attack_SendIMSI.html', methods =["POST"])
def Att_SendIMSI():
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('text'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Targer_MSISDN = str(request.form.get('Targer_MSISDN'))
    locael_GT = str(request.form.get('locael_GT'))

    
    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Targer_MSISDN+" "+locael_GT+" "+Target_IMSI)   
    Atty_gui.attack_SendIMSI(client_ip,client_port,server_ip,server_port,Network_Indicator,Targer_MSISDN,locael_GT)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_SendIMSI.html",deocded_massage_temp=str(output55))


@app.route('/Attack_UpdateLocation.html', methods =["POST"])
def Att_UpdateLocation():
    # img_encode = request.files['img_tp_encode']
    # img_encode.save(secure_filename(img_encode.filename))
    client_ip = str(request.form.get("client_ip"))
    client_port = str(request.form.get("client_port"))
    server_ip  = str(request.form.get('nameserver_ip1'))
    server_port = str(request.form.get('server_port'))
    Network_Indicator = str(request.form.get('Network_Indicator'))

    Target_IMSI = str(request.form.get('Target_IMSI'))
    Targer_IMSI_MGT = str(request.form.get('Targer_IMSI_MGT'))
    if(len(Target_IMSI) < 15 or len(Target_IMSI) > 16):
        print("IMSI len should be 15 or 16")
        exit(0)
    locael_GT = str(request.form.get('locael_GT'))

    locael_vlr = str(request.form.get('locael_vlr'))

    # print(client_ip+" "+client_port+" "+server_ip+" "+server_port+" "+Network_Indicator+" "+Target_IMSI+" "+Targer_IMSI_MGT+" "+locael_GT+" "+Targer_MSC+" "+SMS_Content+" "+locael_vlr)
    Atty_gui.attack_UpdateLocation(client_ip,client_port,server_ip,server_port,Network_Indicator,Target_IMSI,Targer_IMSI_MGT,locael_GT,locael_vlr)
    output55 = open('outingss7.txt','r').read().replace('[0m',' \n ').replace('\x1b[31m',' \n ').replace('\x1b[32m',' \n ').replace('\x1b',' \n ').replace('[34m',' ')
    print(str(output55))
    # output55="shikyog"
    # print(0)
    # return output55
    return render_template("Attack_UpdateLocation.html",deocded_massage_temp=str(output55))



def mainW():
    app.run()

if __name__ == '__main__':
    mainW()
