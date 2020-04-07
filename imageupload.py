#samplecode
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'test.jpg', 'mimeType': 'image/jpeg'})
f.SetContentFile('picture/test.jpg')
f.Upload()