from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

#コマンドラインから認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#指定されたメタ情報でフォルダー・ファイルを作成、作成したフォルダーIDを取得
def create_folder(META):
    f = drive.CreateFile(META)
    if(f.Upload() == None):
        #upload成功
        #メタ情報を再取得（Upload後に実行しないとエラー）
        f.FetchMetadata()
        return f["id"]
    else:
        #upload失敗
        return False

#指定されたメタ情報でlist化
def get_list(META):
    file_list = drive.ListFile(META).GetList()
    return file_list

#指定されたlistをcheckしてファイルを作成
def check_list(LIST,META):
    #LISTの要素数が0であれば新規作成 そうでなければ上書き
    if(len(LIST) == 0):
        #新規アップロード フォルダーID取得
        return create_folder(META)
    else:
        #フォルダーIDのみを取得
        return LIST[0]["id"]

#親フォルダーIDを取得、有効な物か確認
def get_id():
    input_flag = False
    #list作成時のメタ情報（マイドライブ（root）にアクセスするのでスコープ設定に注意）
    LIST_PARENTS_SETTING_FOLDER_ID_META = {"q": "\"root\" in parents"}
    id_list = get_list(LIST_PARENTS_SETTING_FOLDER_ID_META)
    while (input_flag == False):
        print("親フォルダーIDは入力済みです。\n")
        ID = "1UeneN_9RGHeLy2zKtxlgssyIDnXkG1dG"
        #ID = input("親フォルダーIDを入力してください。\n")
        #指定されたIDが存在するか確認
        for f in (id_list):
            if(f["id"] == ID):
                input_flag = True
            else:
                pass
        if(input_flag == False):
            print("無効なIDです。\n")
        else:
            print("有効なIDです。\n")
            break
    return ID

#各プログラムを書き換え箇所を置換 str1:置き換え前の文字列 str2:置き換え後の文字列
def set_program(PATH,str1,str2):
    #書き換え後の情報を取得
    file_r = open(PATH,"r",encoding = "utf-8")
    filedate = file_r.read().replace(str1,str2)
    file_r.close()
    #上書き
    file_w = open(PATH,"w",encoding = "utf-8")
    file_w.write(filedate)
    file_w.close()

"""
各種定数 "inital_value":プログラム中で取得
"""
#関連のpath
ABSPATH = os.path.abspath("setting.py").strip("setting.py")
CREATEFILE_DATE_PATH = ABSPATH + "createfile_date.py"
ONETIME_PHOTO_PATH = ABSPATH + "onetime_photo.py"
UPLOAD_LOG_PATH = ABSPATH + "upload_log.py"
#各フォルダー・ファイル名
SETTING_FOLDER_NAME = "setting"
#各フォルダー・ファイルID
PARENTS_SETTING_FOLDER_ID = get_id()
SETTING_FOLDER_ID = "inital_value"
#作成するフォルダー・ファイルのメタ情報
SETTING_FOLDER_META = {"title": SETTING_FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": PARENTS_SETTING_FOLDER_ID}]}
#list作成時のメタ情報
LIST_PARENTS_SETTING_FOLDER_META = {"q": "title = \"" + SETTING_FOLDER_NAME + "\" and \"" + PARENTS_SETTING_FOLDER_ID + "\" in parents"}
#settingフォルダーをアップロード
SETTING_FOLDER_ID = check_list(get_list(LIST_PARENTS_SETTING_FOLDER_META),SETTING_FOLDER_META)

#各種プログラム書き換え
#createfiledate.py
set_program(CREATEFILE_DATE_PATH,"setting_PARENTS_TODAY_FOLDER_ID",PARENTS_SETTING_FOLDER_ID)
set_program(CREATEFILE_DATE_PATH,"setting_SETTING_FOLDER_ID",SETTING_FOLDER_ID)
#onetime_photo.py
set_program(ONETIME_PHOTO_PATH,"setting_SETTING_FOLDER_ID",SETTING_FOLDER_ID)
#upload_log.py
set_program(UPLOAD_LOG_PATH,"setting_SETTING_FOLDER_ID",SETTING_FOLDER_ID)