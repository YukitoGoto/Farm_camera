from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#コマンドラインから認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#指定されたメタ情報で.../フォルダー・ファイルを作成、作成したフォルダーIDを取得:BOOL = Ture/ローカルのファイルをアップロード:BOOL = False
def create_folder(META,BOOL,PATH = "initial_value"):
    f = drive.CreateFile(META)
    if(BOOL == False):
        f.SetContentFile(PATH)
    else:
        pass
    if(f.Upload() == None):
        #upload成功
        if(BOOL == True):
            #メタ情報を再取得（Upload後に実行しないとエラー）
            f.FetchMetadata()
            return f["id"]
        else:
            return True
    else:
        #upload失敗
        return False

#指定されたメタ情報でlist化
def get_list(META):
    file_list = drive.ListFile(META).GetList()
    return file_list

#指定されたlistをcheckしてファイルを作成
def check_list(LIST,META,PATH):
    #LISTの要素数が0であれば新規作成 そうでなければ上書き
    if(len(LIST) == 0):
        #新規アップロード
        create_folder(META,False,PATH)
    else:
        #フォルダーIDを前回時と同じものにして上書き
        META["id"] = LIST[0]["id"]
        create_folder(META,False,PATH)

"""
各種定数 "setting_XXX":setting.pyから置き換え
"""
#関連のpath
FOLDER_LOG_PATH = "honbu/folder_log.txt"
PICTURE_LOG_PATH = "hojo/photo_log.txt"
#各フォルダー・ファイル名
FOLDER_LOG_NAME = "folder_log.txt"
PICTURE_LOG_NAME = "photo_log.txt"
#各フォルダー・ファイルID
SETTING_FOLDER_ID = "setting_SETTING_FOLDER_ID"
#作成するフォルダー・ファイルのメタ情報
FOLDER_LOG_META = {"title": FOLDER_LOG_NAME, "mimeType": "text/plain","parents": [{"kind": "drive#fileLink", "id": SETTING_FOLDER_ID}]}
PICTURE_LOG_META = {"title": PICTURE_LOG_NAME, "mimeType": "text/plain","parents": [{"kind": "drive#fileLink", "id": SETTING_FOLDER_ID}]}
#list作成時のメタ情報
LIST_FOLDER_LOG_META = {"q": "title = \"" + FOLDER_LOG_NAME + "\" and \"" + SETTING_FOLDER_ID + "\" in parents"}
LIST_PICTURE_LOG_META = {"q": "title = \"" + PICTURE_LOG_NAME + "\" and \"" + SETTING_FOLDER_ID + "\" in parents"}

#各ログファイルをアップロード
check_list(get_list(LIST_FOLDER_LOG_META),FOLDER_LOG_META,FOLDER_LOG_PATH)
check_list(get_list(LIST_PICTURE_LOG_META),PICTURE_LOG_META,PICTURE_LOG_PATH)