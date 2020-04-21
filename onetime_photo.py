import cv2
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#コマンドラインから認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#ログを取得 MODE: "log":ログ形式 "picture":写真名形式
def get_log(HEADNAME,MODE):
    nowtime = datetime.datetime.now()
    if(MODE == "log"):
        return nowtime.strftime("%Y/%m/%d %H:%M:%S " + HEADNAME)
    elif(MODE == "picture"):
        return nowtime.strftime(HEADNAME + "_%Y%m%d_%H%M%S")
    else:
        return "get_log_error"

#ログをローカルに記録
def up_log(PATH,LOG):
    file = open(PATH,"a")
    file.write("\n" + LOG)
    file.close()

#自身の圃場名をhojo_my.txtから取得
def get_hojo(PATH):
    file = open(PATH,"r")
    hojo_my = file.readline().strip()
    file.close()
    return hojo_my

#自身の圃場フォルダidをhojo_id.txtを更新して取得
def get_hojo_id(PATH,HEADNAME):
    file = open(PATH,"r")
    id_flag = False
    for id in file:
        print(id)
        if(id.strip() == HEADNAME):
            id_flag = True
        elif(id_flag == True):
            return id
        else:
            pass
    return "get_hojo_id_error"

"""
各種定数
"""
#カメラのID 1:内蔵 0:外部
CAM_ID = 0
#関連のpath
PICTURE_LOG_PATH = "hojo/photo_log.txt"
PICTURE_PATH = "picture/"
HOJO_MY_PATH = "hojo/hojo_my.txt"
HOJO_ID_PATH = "hojo/hojo_id.txt"
#圃場名
HOJO = get_hojo(HOJO_MY_PATH)
#圃場フォルダーID
HOJO_FOLDER_ID = get_hojo_id(HOJO_ID_PATH,HOJO)

#start
up_log(PICTURE_LOG_PATH,get_log("START","log"))
"""
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
            f = drive.CreateFile({"title": picture_name, "mimeType": "image/png","parents": [{"kind": "drive#fileLink", "id": HOJO_FOLDER_ID}]})
            f.SetContentFile(PICTURE_PATH + picture_name)
            if(f.Upload() == None):
                up_log(PICTURE_LOG_PATH,get_log("upload done","log"))
            else:
                up_log(PICTURE_LOG_PATH,get_log("upload error","log"))
            break

#カメラをクローズ
cam.release()
"""
#finish
up_log(PICTURE_LOG_PATH,get_log("FINISH","log"))