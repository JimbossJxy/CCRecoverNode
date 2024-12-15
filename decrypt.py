"""
    Created at 1:02:00 on 11/11/2024
    File name: decrypt.py
    Description:
        This file is responsible for decrypting the encrypted message.
        This file will be responsible for the following:
            - Decrypting the encrypted message
"""

from bip38 import BIP38
from bip38.exceptions import PassphraseError
from bip38.cryptocurrencies import Bitcoin
import logging
import variables


class Decrypt:
    def __init__(self, encrypted_wif: str):
        """
        This function is responsible for initializing the class.
        :param encrypted_wif: The encrypted message
        :param passphrase: The passphrase
        """
        self.encrypted_wif = encrypted_wif
        self.logging = logging.getLogger(__name__)


    def decrypt(self, passphrase: str):
        """
        This function is responsible for decrypting the encrypted message.
        :param encrypted_wif: The encrypted message
        :param passphrase: The passphrase
        :return: The decrypted message
        """
        #bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network='mainnet')
        #return bip38.decrypt(encrypted_wif=encrypted_wif, passphrase=passphrase)
        try:
            bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network='mainnet') 
            passkey = bip38.decrypt(encrypted_wif=self.encrypted_wif, passphrase=passphrase)
            variables.password = passkey
            self.logging.info(f"Decrypted message: {passkey} - password: {passphrase}")
            return passkey, passphrase
        except PassphraseError:
            print(f"The passphrase is incorrect - password: {passphrase}")
            return False
        except Exception as e:
            self.logging.error(f"An error occurred while decrypting the message: {e} - password: {passphrase}")
            return False
    
    def parseJsonToList(self, json):
        """
        This function is responsible for parsing the JSON data to a list.
        :param json: The JSON data
        :return: The list
        """
        return json["passphrases"]



