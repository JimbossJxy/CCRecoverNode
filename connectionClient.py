
import requests 
import variables
import logging
import time
import json
import sys

class ConnectionClient:
    def __init__(self):
        self.url = str(variables.settings['settings']['url']) # Will be a domain name
        self.logging = logging.getLogger(__name__)
        self.passwordCheckLink = f"{self.url}password-check-list/"
        self.passwordReturn = f"{self.url}password-return/"
        self.headers = {'Content-Type': 'application/json'}

    def nodeOnline(self):
        """
        This function sends a ping to the master node to check if the node is online.
        Then it will send the online packet to the master node.
        
        :return: True if the node is online, False if the node is offline
        """
        _sendRoute = f"{self.url}online/"
        response = None
        for i in range(6):
            try:

                responseCode = requests.get(url=self.url)
                if responseCode.status_code == 200:
                    self.logging.info("Master Node is online")
                    response = True
                    break
                else:
                    return False
                
            except requests.exceptions.RequestException as e:
                self.logging.error(f"An error occurred while checking if the node is online: {e}- {self.url} - line: {sys.exc_info()[-1].tb_lineno}")
                time.sleep(i * 60)
        
        _minutes = 1

        for _ in range(6):
            if _minutes == 1:
                minutes = "1"
            elif _minutes == 2:
                minutes = "5"
            elif _minutes == 3:
                minutes = "10"
            elif _minutes == 4:
                minutes = "15"
            elif _minutes == 5:
                minutes = "30"
            else:
                minutes = "60"
            
            sendOnlinePacket = requests.post(_sendRoute, data=json.dumps(variables.onlinePacket), headers=self.headers)
            if sendOnlinePacket.status_code == 200:
                self.logging.info("Online packet sent to master node")
                return True
            else:
                self.logging.error("Failed to send online packet to master node")
                self.logging.error(f"Status code: {sendOnlinePacket.status_code}")
                self.logging.info(f"Retrying in {minutes} minute's")
                time.sleep(int(_minutes) * 60)
        
        self.logging.error(f"Failed to send online packet to master node - line: {sys.exc_info()[-1].tb_lineno}")
        return False
    
    def nodeOffline(self):
        """
        This function sends a ping to the master node to check if the node is online.
        Then it will send the online packet to the master node.
        
        :return: True if the node is online, False if the node is offline
        """
        _sendRoute = f"{self.url}offline/"
        response = None
        # Check if the master node is online, check 6 times with increasing intervals
        for i in range(6):
            try:

                responseCode = requests.get(url=self.url)
                if responseCode.status_code == 200:
                    self.logging.info("Master Node is online")
                    response = True
                    break
                else:
                    return False
                
            except requests.exceptions.RequestException as e:
                self.logging.error(f"An error occurred while checking if the node is online: {e}- {self.url} - line: {sys.exc_info()[-1].tb_lineno}")
                time.sleep(i * 60)
        

            
                

        
        
        _minutes = 1

        for _ in range(6):
            if _minutes == 1:
                minutes = "1"
            elif _minutes == 2:
                minutes = "5"
            elif _minutes == 3:
                minutes = "10"
            elif _minutes == 4:
                minutes = "15"
            elif _minutes == 5:
                minutes = "30"
            else:
                minutes = "60"
            
            sendOfflinePacket = requests.post(_sendRoute, data=json.dumps(variables.offlinePacket), headers=self.headers)
            if sendOfflinePacket.status_code == 200:
                self.logging.info("Offline packet sent to master node")
                return True
            else:
                self.logging.error("Failed to send offline packet to master node")
                self.logging.error(f"Status code: {sendOfflinePacket.status_code}")
                self.logging.info(f"Retrying in {minutes} minute's")
                time.sleep(int(_minutes) * 60)
        
        self.logging.error(f"Failed to send online packet to master node - line: {sys.exc_info()[-1].tb_lineno}")
        return False

    def getDecryptData(self):
        """
        Gets the data to be decrypted from the master node. 
        Format as a json file
        """
        response = None
        try:
            data = requests.get(url=(self.passwordCheckLink))
            if data.status_code == 200:
                self.logging.info("Data received from master node")
                response = data.json()
                return response
            else:
                self.logging.error("Failed to get data from master node")
                self.logging.error(f"Status code: {data.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            self.logging.error(f"An error occurred while getting data from the master node: {e} - line: {sys.exc_info()[-1].tb_lineno}")
            return None
    

    def sendReturnData(self):
        
        """
        Sends the data back to the master node after the data has been decrypted
        """
        response = None
        try:
            data = requests.post(url=(self.passwordReturn), data=json.dumps(variables.returnPacket), headers=self.headers)
            if data.status_code == 200:
                self.logging.info("Data sent to master node")
                response = data.json()
                return response
            else:
                self.logging.error("Failed to send data to master node")
                self.logging.error(f"Status code: {data.status_code}")
                return None
            
        except requests.exceptions.RequestException as e:
            self.logging.error(f"An error occurred while sending data to the master node: {e} - line: {sys.exc_info()[-1].tb_lineno}")
            return None

