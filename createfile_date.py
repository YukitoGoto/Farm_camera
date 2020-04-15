from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime

#コマンドラインから認証を行う
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#年月日を文字列で取得 xxxx/xx/xx
def get_today():
    nowtime = datetime.datetime.now()
    return nowtime.strftime("%Y/%m/%d")

#圃場名をhojo_list.txtから文字列で取得、list化
def get_hojo(PATH):
    file = open(PATH,"r")
    #改行文字を取り除いてlist作成
    hojo_list = [i.strip() for i in file.readlines()]
    file.close()
    return hojo_list

#指定されたメタ情報でlist化
def get_list(META):
    file_list = drive.ListFile(META).GetList()
    return file_list

#圃場名、圃場フォルダーIDの順でhojo_id.txtに書き込む
def write_hojo_id(PATH,HOJO,ID,MODE):
    file = open(PATH,MODE)
    file.write(HOJO + "\n")
    file.write(ID + "\n")
    file.close()
    return ID + "\n"

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
            return "upload done"
    else:
        #upload失敗
        return "upload error"

"""
各種定数 "inital_value":プログラム中で取得
"""
#関連のpath
FOLDER_LOG_PATH = "folder/folder_log.txt"
HOJO_LIST_PATH = "folder/hojo_list.txt"
HOJO_ID_PATH = "folder/hojo_id.txt"
#各フォルダー・ファイル名
TODAY_FOLDER_NAME = get_today()
HOJO_FOLDER_NAME = "initial_value"
HOJO_ID_NAME = "hojo_id.txt"
#各フォルダー・ファイルID
PARENTS_TODAY_FOLDER_ID = "1UeneN_9RGHeLy2zKtxlgssyIDnXkG1dG"
PARENTS_HOJO_FOLDER_ID = "initial_value"
HOJO_FOLDER_ID = "inital_value"
SETTING_FOLDER_ID = "1oN6nGBlrRfWevq5ebj8kKpzIfWv8GNuv"
#作成するフォルダー・ファイルのメタ情報
TODAY_FOLDER_META = {"title": TODAY_FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": PARENTS_TODAY_FOLDER_ID}]}
HOJO_FOLDER_META = {"title": "initial_value", "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": "initial_value"}]}
HOJO_ID_META = {"title": HOJO_ID_NAME, "mimeType": "text/plain","parents": [{"kind": "drive#fileLink", "id": SETTING_FOLDER_ID}]}
#list作成時のメタ情報
LIST_PARENTS_TODAY_FOLDER_META = {"q": "title = \"" + TODAY_FOLDER_NAME + "\" and \"" + PARENTS_TODAY_FOLDER_ID + "\" in parents"}
LIST_HOJO_ID_META = {"q": "title = \"" + HOJO_ID_NAME + "\" and \"" + SETTING_FOLDER_ID + "\" in parents"}

#親フォルダーIDがPARENTS_TODAY_FOLDER_IDでタイトルがTODAY_FOLDER_NAMEであるフォルダー及びファイルを検索、listを作成
today_list = get_list(LIST_PARENTS_TODAY_FOLDER_META)
#today_listの要素数が0であればTODAY_FOLDER_NAMEを作成
if(len(today_list) == 0):
    PARENTS_HOJO_FOLDER_ID = create_folder(TODAY_FOLDER_META,True)
    #取得したフォルダーIDを親フォルダーとしてメタ情報に反映
    HOJO_FOLDER_META["parents"][0]["id"] = PARENTS_HOJO_FOLDER_ID
    #圃場名をlistで取得 index:カウンタ（listの添え字）
    for index,name in enumerate(get_hojo(HOJO_LIST_PATH)):
        HOJO_FOLDER_NAME = name
        #取得した圃場名をメタ情報に反映
        HOJO_FOLDER_META["title"] = HOJO_FOLDER_NAME
        #HOJO_FOLDER_NAMEを作成 作成した圃場フォルダーのIDを取得
        HOJO_FOLDER_ID = create_folder(HOJO_FOLDER_META,True)
        #最初は上書きモード:"w" それ以降は追記モード:"a"
        mode = "w" if (index == 0) else "a"
        write_hojo_id(HOJO_ID_PATH,HOJO_FOLDER_NAME,HOJO_FOLDER_ID,mode)
    #親フォルダーIDがSETTING_FOLDER_IDでタイトルがHOJO_ID_NAMEであるフォルダー及びファイルを検索、listを作成
    id_list = get_list(LIST_HOJO_ID_META)
    #id_listの要素数が0であればHOJO_ID_NAMEを新規作成 そうでなければ上書き
    if(len(id_list) == 0):
        #hojo_id.txtをフォルダーIDがSETTING_FOLDER_IDであるフォルダーにアップロード
        create_folder(HOJO_ID_META,False,HOJO_ID_PATH)
    else:
        #フォルダーIDを前回時と同じものにして上書き
        HOJO_ID_META["id"] = id_list[0]["id"]
        create_folder(HOJO_ID_META,False,HOJO_ID_PATH)
else:
    print("already exist")