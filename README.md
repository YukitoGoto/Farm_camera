# 【概要】
[Legmin/Webcam-python](https://github.com/Legmin/Webcam-python.git)のデバックルームです。
opencvやpydriveを使って、カメラで撮った画像をGoogleDriveにアップロードします。

# 【チュートリアル】
サンプルプログラムを動かすまでの説明です。**git導入とgithubアカウント作成済み**として解説します。
## 1.作業ディレクトリにFarm_cameraをクローン
**ターミナル**または**コマンドプロンプト**を立ち上げます。

まず作業ディレクトリ（作業する場所）に移動します。
```
cd 作業ディレクトリのpath
```
以下はWindowsでデスクトップに移動する例です。
```
cd C:/Users/Username/Desktop
```
次にFarm_camera（このリポジトリ）をクローンします。
```
git clone https://github.com/YukitoGoto/Farm_camera.git
```
作業ディレクトリに**Farm_camera**というフォルダーが出来上がります。
## 2.Python3と必要ライブラリの導入
**工事中**
## 3.GoogleDriveAPIの認証
**工事中**
### 3-1.認証情報の取得
以下URLにアクセスしましょう。

https://console.developers.google.com/
### 3-2.client_secret.jsonとcredentials.jsonの書き換え
*工事中*
### 3-3.settings.yamlの書き換え
*工事中*
## 4.プログラムの書き換えと実行
**工事中**
# 【ソースコード・関連ファイル】
## imagesave.py
opencvのサンプルコードです。
## imageupload.py
pydriveのサンプルコードです。
## key_photo.py
`onetime_photo.py`のテストコードです。
## createfile.py
`createfile_date.py`のテストコードです。
## createfile_date.py
GoogleDrive上にフォルダーを自動生成するプログラムです。
## onetime_photo.py
写真を撮影、その後`createfile_date.py`で生成されたフォルダーにアップロードします。
## upload_log.py
`hojo/photo_log.txt`と`honbu/hojo_id.txt`をGoogleDrive上の`setting`というフォルダーにアップロードします。
## setting.py
**初回実行時のみ**GoogleDrive上に`setting`というフォルダーを作成、及び`createfile_date.py`・`onetime_photo.py`・`upload_log.py`を書き換えます。
## honbu/hojo_list.txt（本部ラズパイのみ設定）
```
HOJO_A
HOJO_B
HOJO_C
:
:
```
カメラを設置する全圃場名を**半角、改行区切り**で入力します。`createfile_date.py`はここを参照してGoogleDriveにフォルダーを作成します。**圃場を追加/消去**する場合、ここを書き換えます。書き換えを施すラズパイは、**本部ラズパイのみ**でOKです。
## hojo/hojo_my.txt（圃場ラズパイごとに設定）
```
HOJO_C

```
**honbu/hojo_list.txtの中**から、担当する圃場名を**半角**で入力します。`onetime_photo.py`はここを参照して、合致するGoogleDrive上のフォルダーに画像をアップロードします。例えば、`HOJO_C`を担当する場合、上記のように入力します。**圃場ラズパイごと**にここを書き換えます。
## picture/
```
HOJO_A_20xxxxxx_xxxxxx.png
HOJO_A_20xxxxxx_xxxxxx.png
:
:
```
撮影された写真はここに格納されます。
# 【GoogleDriveAPI認証関連ファイル】
## client_secret.json
認証情報が記されたファイルです。`settings.yaml`で`client_id`及び`client_secret`を設定している場合、**このファイルは不要**です。しかしながら導入を推奨している記事が多い為、一応入れておきます。
## credentials.json
`settings.yaml`で`save_credentials`を設定している場合、初回認証時に自動生成されます。認証情報のキャッシュが保存・更新されるファイルです。このファイルのお陰で、次回以降認証時はブラウザを起動することなく認証可能です。**GoogleDrive上のフォルダー及びファイルの管理者を変更する場合、このファイルを消去**します。その後、**以前と異なるOAuthクライアントIDを使って再認証を行う**ことで、新たに`credentials.json`が生成されます。
## settings.yaml
認証情報に関する設定ファイルです。**このファイルをpythonコマンドを立ち上げるディレクトリに置く**必要があります。
### client_config_backend
`settings`：認証情報を`settings.yaml`で設定することになります。

`file`：認証情報を`client_secret.json`から読み込むことになります。
### client_config
認証情報を`client_id`及び`client_secret`で設定します。
### save_credentials
`True`：認証情報のキャッシュを`credentials`で保存することになります。

`False`：保存しないことになります。
### save_credentials_backend
`File`：`credentials`をファイルとして保存することになります。
### save_credentials_file
`credentials.json`の保存先のpathを設定します。
### その他
`settings.yaml`：[pydrive公式](https://gsuitedevs.github.io/PyDrive/docs/build/html/oauth.html)  [pydrive参考サイト](https://note.nkmk.me/python-pydrive-download-upload-delete/)

`oauth_scope`：[GoogleDriveAPI公式](https://developers.google.com/drive/api/v3/about-auth)
### 設定例
デフォルトの内容にコメントを加えました。
```
#認証情報をsettings.yamlで設定する：settings
client_config_backend: settings

#認証情報を設定
client_config:
  #client_id: <your_client_id>
  client_id: http://138026631891-t8c7jfasleko7bg1ddj7vckk7ifuukh9.apps.googleusercontent.com
  #client_secret: <your_client_secret>
  client_secret: cbMKL-RWo6LLu2bKyvb6E-Xq

#認証情報のキャッシュをcredentialsで保存する：True
save_credentials: True
#credentialsをファイルで保存する：file
save_credentials_backend: file
#保存先のpathを設定（絶対パスが望ましい）
save_credentials_file: /home/pi/Webcam-python/credentials.json

#以下の設定は無くても良い

#refresh tokenを取得する：True
get_refresh_token: True

#スコープを設定してフォルダー及びファイルへの消去等のアクセスを制限する：デフォルト（未設定）ではフルアクセス可能
oauth_scope:
  #このプログラムで作成したフォルダー及びファイルのみ消去等可能：https://www.googleapis.com/auth/drive.file
  - https://www.googleapis.com/auth/drive.file
  #謎：ユーザーがアプリのインストールを承認するために使用される：https://www.googleapis.com/auth/drive.install
  - https://www.googleapis.com/auth/drive.install
```
## OAuthクライアントID
認証に使えるOAuthクライアントIDは、**他のプロジェクトで未使用のもの**である必要があります。新規プロジェクトを開始する度に、OAuthクライアントID及びシークレットを取得します。
# 資料
[pydrive参考サイト](https://note.nkmk.me/pydrive/)

[opencv参考サイト](https://note.nkmk.me/opencv/)

[pydrive公式](https://gsuitedevs.github.io/PyDrive/docs/build/html/quickstart.html#)

[GoogleDriveAPI公式](https://developers.google.com/drive/api/v3/about-sdk)