"""
    Created at 16:00:00 on 10/11/2024
    File name: variables.py
    Description:
        This file is responsible for storing all the necessary variables.
        This file will be responsible for the following:
            - Storing all the necessary variables
"""


import hashlib

from pathlib import Path


# Default settings for the node
settings = {
    "settings": {
        "url": "http://127.0.0.1:80",    # URL of the node - modify this to the URL of the Master node
        "use_ssl": False,          # Enable SSL for communication
        "ssl_certfile": "/path/to/cert.pem",  # Path to SSL certificate
        "ssl_keyfile": "/path/to/key.pem",    # Path to SSL private key
        "encrypted_wif": "6PnXQfXefRSvJPDkZfQQ1TfvidRQ1esNJLEdojsCE9uBiA1Em4zuWMhnjS", # Encrypted WIF to be decrypted - This is a placeholder wif key, it has no value, the password is g and you can use this to test the node
        "ip": "127.0.0.1"  # IP address of the node - this will be used to identify the node - edit this to the IP address of the node
    }
}
ip = settings["settings"]["ip"]
nodeId = str(hashlib.sha256(ip.encode()).hexdigest())
# Online data Packet
onlinePacket = {
    "packet": {
        "node_id": nodeId,  # Unique ID of the node - based on the IP address
        "status": "online",
        "ip": ip # Status of the node
    }
}
offlinePacket = {
    "packet": {
        "node_id": nodeId,  # Unique ID of the node - based on the IP address
        "status": "offline",
        "ip": ip # Status of the node
    }
}

requestPacket = {
    "packetInfo": {
        "node_id": nodeId,
        "status": "online",
        "ip": ip,
        "requestData": "True"
    }
}

# Return Packet for the master node
returnPacket = {
    "packetInfo": {
        "node_id": nodeId,
        "status": "online",
        "ip": ip,
        "successful" : False
    },
    "packetData": {
        "info":
            {
                "checkAmount": 0,
                "lastCheckedPassword": "a",
            },
        "data": 
            {
                "success": "False", # True if the password was found, False if the password was not found
                "password": "a" # if the password was found, this will be the password otherwise it will be ignored
            }
        }
}

# Make true if you dont want it to restart or shut down the computer - only if you are testing or debugging
debug = False

# Found variable
found = False
password = ""
# Paths for configuration and data files
defaultPath = str(Path.home() / "node")
certPath = str(Path.home() / "node" / "certs")
keyPath = str(Path.home() / "node" / "keys")
logPath = str(Path.home() / "node" / "logs")

# Ensure directories exist
for path in [defaultPath, certPath, keyPath, logPath]:
    Path(path).mkdir(parents=True, exist_ok=True)

 
   