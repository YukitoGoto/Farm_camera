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

#圃場名をhojo_listr.txtから文字列で取得
def get_hojo(PATH):
    file = open(PATH,"r")
    #改行文字を取り除いてリスト化
    hojo_list = [i.strip() for i in file.readlines()]
    file.close()
    return hojo_list

#指定されたメタ情報でフォルダーを作成 作成したフォルダーidを取得:Ture
def create_folder(META,BOOL):
    f = drive.CreateFile(META)
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

#関連のpath
FOLDER_LOG_PATH = "folder/folder_log.txt"
HOJO_LIST_PATH = "folder/hojo_list.txt"
#日付フォルダー名
TODAY_FOLDER_NAME = get_today()
HOJO_FOLDER_NAME = "initial_value"
#各フォルダーの親フォルダーID
PARENTS_TODAY_FOLDER_ID = "1UeneN_9RGHeLy2zKtxlgssyIDnXkG1dG"
PARENTS_HOJO_FOLDER_ID = "initial_value"
#作成するフォルダーのメタ情報
TODAY_FOLDER_META = {"title": TODAY_FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": PARENTS_TODAY_FOLDER_ID}]}
HOJO_FOLDER_META = {"title": "initial_value", "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": "initial_value"}]}
#日付フォルダーの親フォルダーのメタ情報
LIST_PARENTS_TODAY_FOLDER_META = {"q": "title = \"" + TODAY_FOLDER_NAME + "\" and \"" + PARENTS_TODAY_FOLDER_ID + "\" in parents"}

#親フォルダーIDがPARENTS_TODAY_FOLDER_IDでタイトルがTODAY_FOLDER_NAMEであるフォルダー及びファイルからlistを作成
file_list = drive.ListFile(LIST_PARENTS_TODAY_FOLDER_META).GetList()
#listの要素数が0であればTODAY_FOLDER_NAMEを作成
if(len(file_list) == 0):
    PARENTS_HOJO_FOLDER_ID = create_folder(TODAY_FOLDER_META,True)
    #取得したフォルダーIDを親フォルダーとしてメタ情報に反映
    HOJO_FOLDER_META["parents"][0]["id"] = PARENTS_HOJO_FOLDER_ID
    for name in get_hojo(HOJO_LIST_PATH):
        HOJO_FOLDER_NAME = name
        #取得した圃場名をメタ情報に反映
        HOJO_FOLDER_META["title"] = HOJO_FOLDER_NAME
        create_folder(HOJO_FOLDER_META,False)
else:
    print("already exist")