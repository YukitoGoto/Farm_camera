from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

FOLDER_NAME = "GAKUDAN"
FOLDER_META = {"title": FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder"}

f = drive.CreateFile(FOLDER_META)
f.Upload()