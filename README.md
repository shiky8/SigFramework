# SigFramework
SigFramework it's a modified version of SiGploit

SigFramework a signaling security testing framework dedicated to Telecom Security professionals and reasearchers to pentest and exploit vulnerabilites in the signaling protocols used in mobile operators regardless of the geneartion being in use. SiGploit aims to cover all used protocols used in the operators interconnects SS7, GTP (3G), Diameter (4G) or even SIP for IMS and VoLTE infrastructures used in the access layer and SS7 message encapsulation into SIP-T. Recommendations for each vulnerability will be provided to guide the tester and the operator the steps that should be done to enhance their security posture

SiGploit is developed on several versions

Note: In order to test SS7 attacks, you need to have an SS7 access or you can test in the virtual lab with the provided server sides of the attacks, the used values are provided.

  Version 1: SS7
  -------------
  SiGploit will initially start with SS7 vulnerabilities providing the messages used to test the below attacking scenarios
    A- Location Tracking
    B- Call and SMS Interception
    C- Fraud
    
## Installation and requirements
The requirements for this project are:

    1) Python 3
    2) Java version 1.7 +
    3) Linux machine (Windows doesnt support SCTP)

## To install use
     sudo python3 -m pip install -r requirements.txt

## To run use

    cd SigFramework
   ## CLI
      python3 sig_framwork_cli.py
   ## GUI
      python3 sigfremwork_gui_main.py
   ## Web Interface
     python3 sigframework_web.py
