# https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
# cd C:/Users/lzmi1/PycharmProjects/PDF_TO_SFTP
import pysftp as sftp
import json
def load_settings():
   global FTP_HOST
   global FTP_USER
   global FTP_PASS
   # Opening JSON file
   f = open('test_cred.json')

   # returns JSON object as
   # a dictionary
   data = json.load(f)

   # Iterating through the json
   # list
   FTP_HOST = data['sftp2_data']['FTP_HOST']
   FTP_USER = data['sftp2_data']['FTP_USER']
   FTP_PASS = data['sftp2_data']['FTP_PASS']

   # Closing file
   f.close()

load_settings()

cnopts = sftp.CnOpts()
cnopts.hostkeys = None

with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
   print("Connection succesfully stablished ... ")
   directory_structure = sftp.listdir_attr() # Obtain structure of the remote directory

for attr in directory_structure:
   print(attr.filename, attr)