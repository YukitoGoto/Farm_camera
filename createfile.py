from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

#フォルダー名
FOLDER_NAME = "Yugawa"
#親フォルダーID
PARENTS_FOLDER_ID = "1UeneN_9RGHeLy2zKtxlgssyIDnXkG1dG"
#作成するフォルダーのメタ情報
FOLDER_META = {"title": FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": PARENTS_FOLDER_ID}]}
#参照するフォルダーのメタ情報
"""
"q":検索
"title = 'name'":タイトルがnameである。
"= and not or":演算子
"'id' in parents":親フォルダーのfolder_idがidである。
"""
LIST_FOLDER_META = {"q": "title = \"" + FOLDER_NAME + "\" and \"" + PARENTS_FOLDER_ID + "\" in parents"}

#親フォルダーIDがPARENTS_FOLDER_IDでタイトルがFOLDER_NAMEであるフォルダー及びファイルからlistを作成
file_list = drive.ListFile(LIST_FOLDER_META).GetList()
#listの要素数が0であればフォルダーを作成
if(len(file_list) == 0):
    f = drive.CreateFile(FOLDER_META)
    f.Upload()
else:
    print(file_list[0]['id'])
    print("file_list len = " + str(len(file_list)),"already exist!")