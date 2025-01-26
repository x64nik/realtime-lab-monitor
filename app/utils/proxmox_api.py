import time
import os
import configparser
from proxmoxer import ProxmoxAPI
from proxmoxer.tools import Tasks
from urllib import parse as urlparse
import urllib3

from dotenv import load_dotenv
load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()
config.read('config.ini')

proxmox_host = os.getenv('proxmox_host')
proxmox_user = os.getenv('proxmox_user')
proxmox_token_name = os.getenv('proxmox_token_name')
proxmox_token = os.getenv('proxmox_token')
node_name = os.getenv('node_name')


proxmoxClient = ProxmoxAPI(
    proxmox_host, user=proxmox_user, token_name=proxmox_token_name, token_value=proxmox_token, verify_ssl=False
)