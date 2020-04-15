import cv2
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

"""
各種定数 "inital_value":プログラム中で取得
"""
#カメラのID 1:内蔵 0:外部
CAM_ID = 0
#関連のpath
PICTURE_LOG_PATH = "folder/photo_log.txt"
PICTURE_PATH = "picture/"
#圃場名
HOJO = "A"
#圃場フォルダーID
FOLDER_ID = "inital_value"

#ログを獲得 MODE: "log":ログ形式 "picture":写真名形式
def get_log(HEADNAME,MODE):
    nowtime = datetime.datetime.now()
    if(MODE == "log"):
        return nowtime.strftime(HEADNAME + " %Y/%m/%d %H:%M:%S")
    else if(MODE == "picture"):
        return nowtime.strftime(HEADNAME + "_%Y%m%d_%H%M%S")
    else:
        return "get_log_error"

#ログをローカルに記録
def up_log(PATH,LOG):
    file = open(PATH,'a')
    file.write("\n" + LOG)
    file.close()

#コマンドラインから認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#start
up_log(PICTURE_LOG_PATH,get_log("START","log"))

#カメラをオープン
cam = cv2.VideoCapture(CAM_ID)

if(cam.isOpened() == False):
    up_log(PICTURE_LOG_PATH,get_log("Couldn't open CAM " + str(CAM_ID),"log"))
else:
    up_log(PICTURE_LOG_PATH,get_log("Could open CAM " + str(CAM_ID),"log"))
    while True:
        read_check,frame_imfo = cam.read()
        if(read_check):
            picture_name = get_log(HOJO,"picture") + ".png"
            cv2.imwrite(PICTURE_PATH + picture_name,frame_imfo)
            f = drive.CreateFile({"title": picture_name, "mimeType": "image/png","parents": [{"kind": "drive#fileLink", "id": FOLDER_ID}]})
            f.SetContentFile(PICTURE_PATH + picture_name)
            if(f.Upload() == None):
                up_log(PICTURE_LOG_PATH,get_log("upload done","log"))
            else:
                up_log(PICTURE_LOG_PATH,get_log("upload error","log"))
            break

#カメラをクローズ
cam.release()

#finish
up_log(get_log("FINISH","log"))