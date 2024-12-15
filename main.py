
# Importing the required modules
import decrypt
import connectionClient
import logging
import nodeLogger
import time
import variables
from multiprocessing import Pool, Manager, cpu_count
import subprocess
import platform
import datetime


"""
    TODO:
    - add gpu support (if possible, this is not a priority and can be done later)
    """

# Main function
# Worker function for decrypting passwords
def decrypt_password(password, shared_data, _decrypt):
    
    if shared_data["found"]:
        return None  # Exit if another process has already found the password

    decryptedPassword = _decrypt.decrypt(password)
    if decryptedPassword:
        decryptedPassword, passwordFound = decryptedPassword
    
    with shared_data["lock"]:
            shared_data["last_checked_password"] = password
            shared_data["checkAmount"] += 1
            if decryptedPassword:
                shared_data["decryptedPassword"] = decryptedPassword
                shared_data["password"] = passwordFound
                shared_data["found"] = True
                
    return None

def taskGenerator(passwordsToCheck, shared_data, _decrypt):
    for password in passwordsToCheck:
        if shared_data["found"]:
            break
        yield (password, shared_data, _decrypt)

def restartNode(debug=False, found=False):
    if not debug and not found:
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/r", "/t", "0"], check=True) # /r is restart, /t is time in seconds, 0 is immediate restart
        elif platform.system() in ("Linux", "Darwin"):  # Darwin is macOS
            subprocess.run(["shutdown", "-r", "now"], check=True) # run chmod +s /sbin/shutdown to allow the user to run the command without sudo
        else:
            raise NotImplementedError("Unsupported operating system")
# Need to add server restarting functionality to make sure the node runs as best as possible

def shutdownNode(debug  = False):
    if not debug:
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "0"], check=True) # /s is shutdown, /t is time in seconds, 0 is immediate shutdown
        elif platform.system() in ("Linux", "Darwin"):  # Darwin is macOS
            subprocess.run(["shutdown", "-h", "now"], check=True) # run chmod +s /sbin/shutdown to allow the user to run the command without sudo
        else:
            raise NotImplementedError("Unsupported operating system")
    
def main():
    startime = time.time()
    _logger = nodeLogger
    _decrypt = decrypt.Decrypt(variables.settings["settings"]["encrypted_wif"])
    _connections = connectionClient.ConnectionClient()

    
    # Start up handling
    _logger.masterLogging()
    # Send the online packet - this will be sent to the master node this will loop until connection is established
    while True:
        try:
            _connections.nodeOnline()
            break
        except Exception as e:
            logging.error(f"Error connecting to the master node - {e}")
            time.sleep(5)
    
    # Main loop
    while True:
        checkecAmount = 0 # The amount of passwords that have been checked
        passwordsToCheck = [] # Makes sure that the passwords are not checked twice and also to store the passwords to be checked
        last_checked_password = None # The last password that was checked
        currentTime = time.time()

        # Master node restarts on the second of every month at 00:00
        # to prevent any issues with the node communicating with the master node the node will not send any requests to the master node between 23:55 and 00:05
        now = datetime.datetime.now()
        # Check if the current time is 23:55 on the 1st of the month
        if now.day == 1 and now.hour == 23 and now.minute >= 55:
            logging.info("It's 23:55 on the 1st. Waiting until 00:05 on the 2nd...")
            # Wait until 00:05 on the 2nd
            time.sleep(600)
            logging.info("It's 00:05 on the 2nd. Resuming execution.")
            

        # Check for needing to restart the node
        if currentTime - startime >= 604800: # 604800 seconds is 1 week
            logging.info("Node has been running for a week, restarting the node")
            break
        
        while True:
            data = _connections.getDecryptData()
            if data != None:
                break
            time.sleep(5)
        
        
        # load the data
        if not isinstance(data, dict):
            logging.error("Invalid data received")
            raise ValueError("Invalid data received")


        # Decrypting the passwords
        passwordsToCheck = data.get("passwords", [])

        #if passwordsToCheck.get("found") is True:
        #    logging.info("Password has been found by another node, stopping the node")
        #    break   

            

        with Manager() as manager:
            shared_data = manager.dict({
                "found": False,
                "decryptedPassword": None,
                "last_checked_password": None,
                "checkAmount": 0,
                "password": None,
                "lock": manager.Lock()
            })
            
            with Pool(cpu_count()) as pool:
                pool.starmap(decrypt_password, taskGenerator(passwordsToCheck, shared_data, _decrypt))


            # Check results after pool execution
            if shared_data["found"]:
                decryptedPassword = shared_data["decryptedPassword"]
                password = shared_data["password"]


                logging.info(f"Decrypted password - {decryptedPassword}")
                variables.returnPacket["packetInfo"]["successful"] = "True"
                variables.returnPacket["packetData"]["info"]["checkAmount"] = shared_data["checkAmount"]

                variables.returnPacket["packetData"]["info"]["lastCheckedPassword"] = password
                variables.returnPacket["packetData"]["data"]["success"] = "True"
                variables.returnPacket["packetData"]["data"]["password"] = decryptedPassword
                variables.found = True
                logging.info("Password has been found, stopping the node")
                logging.info(variables.returnPacket)
                break
            else:
                last_checked_password = shared_data["last_checked_password"]
                variables.returnPacket["packetInfo"]["successful"] = "False"
                variables.returnPacket["packetData"]["info"]["checkAmount"] = shared_data["checkAmount"]
                variables.returnPacket["packetData"]["info"]["lastCheckedPassword"] = last_checked_password
                variables.returnPacket["packetData"]["data"]["success"] = "False"
                variables.returnPacket["packetData"]["data"]["password"] = None

        _connections.sendReturnData()
    
    _connections.sendReturnData()
    if variables.found:
        # try to send the offline packet, retry 5 times before shutting down
        for _ in range(5):
            if _connections.nodeOffline():
                break
            time.sleep(5)
        else:
            logging.error("Failed to send offline packet to master node")
            shutdownNode(variables.debug)
        
        shutdownNode(variables.debug)
    
    # Shut down handling
    restartNode(variables.debug, variables.found)
    

    
    

if __name__ == "__main__":
    main()