#samplecode
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#コマンドラインから認証
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#Googleドライブオブジェクト生成
f = drive.CreateFile({'title': 'test.jpg', 'mimeType': 'image/jpeg'})
#ローカルファイルをセット
f.SetContentFile('picture/test.jpg')
#アップロード
f.Upload()