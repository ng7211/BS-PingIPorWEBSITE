#!/usr/bin/env python3
#Demy Abdulsalami, Ilja Winkler
#30.10.2025
import argparse
import os
import time

#Parseer-Objekt mit Deskription erstellen.
parser = argparse.ArgumentParser(description="This script pings websites or IP adresses in intervalls and shows status OK/FAILED.")
#Optionales Argument 
parser.add_argument('-s', '--seconds', type=float, default=3.0, help='This options sets the time in seconds between Pings.')
#Positinales Argument
parser.add_argument("website", help="The website or IP adress to ping.")
#Verarbeitet die Argument die über dir Befehlszeile übergeben wurden
args = parser.parse_args()



def pingIpOrWebsite(seconds, ipOrWebsite):
    while True:
        #Einen Ping senden und danach beenden
        response = os.popen(f"ping -c 1 {ipOrWebsite}").read()
        #Jede erfolgreiche Ping Nachricht hat in Linux ein ttl -> time to live, also Host ist erraichbar
        if "ttl=" in response.lower():
            print(f"{ipOrWebsite} OK")
        else:
            print(f"{ipOrWebsite} FAILED")
        #Das Zeitintervall
        time.sleep(seconds)

if __name__ == '__main__':
    pingIpOrWebsite(args.seconds, args.website)

