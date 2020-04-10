"""
・Webカメラで画像保存
・GoogleDriveにアップロード
・GoogleDrive内でフォルダ作ってからその中に保存（日付→圃場の名前（一旦適当でOK）→画像ファイル（ファイル名は”圃場名_日付_時刻.png”　Yugawa_20200403_175720.png））
"""
import cv2
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#カメラのID 1:内蔵 0:外部
CAM_ID = 0
#カメラウィンドウの名前
CAM_WINDOW_NAME = "CAM " + str(CAM_ID)
#キー入力待機時間[ms]
KEY_DELAY = 1
#圃場名
HOJO = "Yugawa"
#写真のパス
PICTURE_PATH = "picture/"
#GoogleドライブフォルダのID
FOLDER_ID = "1UeneN_9RGHeLy2zKtxlgssyIDnXkG1dG"

def get_log(headname):
    nowtime = datetime.datetime.now()
    return nowtime.strftime(headname + "_%Y%m%d_%H%M%S")

print("start!")

#GoogleDrive準備
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#カメラをオープン
cam = cv2.VideoCapture(CAM_ID)

if(cam.isOpened() == False):
    print("Couldn't open CAM " + str(CAM_ID))
else:
    while True:
        read_check,frame_imfo = cam.read()
        if(read_check):
            cv2.imshow(CAM_WINDOW_NAME,frame_imfo)
            #キー入力処理（ASCIIに変換）
            key_check = cv2.waitKey(KEY_DELAY) & 0xff
            if(key_check == 0xff):
                pass
            elif(key_check == ord('s')):
                picture_name = get_log(HOJO) + ".png"
                cv2.imwrite(PICTURE_PATH + picture_name,frame_imfo)
                f = drive.CreateFile({"title": picture_name, "mimeType": "image/png","parents": [{"kind": "drive#fileLink", "id": FOLDER_ID}]})
                f.SetContentFile(PICTURE_PATH + picture_name)
                f.Upload()
            else:
                break

#カメラウィンドウをクローズ
cv2.destroyWindow(CAM_WINDOW_NAME)
#カメラをクローズ
cam.release()
print("fin!")