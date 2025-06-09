import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SMB_CONF_PATH = "/etc/samba/smb.conf"
NFS_EXPORTS_PATH = "/etc/exports"

STORAGE_USERS_GROUP = "storage_users"

SECRET_KEY = "*.bj'B.x/M%?y/7Xa^bB"  # Für Flask Sessions
