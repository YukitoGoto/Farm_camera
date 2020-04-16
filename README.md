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
作業ディレクトリに**Farm_camera**というフォルダが出来上がります。
## 2.Python3と必要ライブラリの導入
**工事中**
## 3.認証ファイルの設定
**client_secret.json**・**credentials.json**・**settings.yaml**が認証に使われるファイルです。デフォルトでは僕の情報になっていますから、設定し直します。
### 3-1.認証情報の取得
以下URLにアクセスしましょう。

https://console.developers.google.com/
### 3-2.client_secret.jsonとcredentials.jsonの書き換え
[alt](https://github.com/YukitoGoto/Farm_camera/blob/master/picture/test.jpg)
*工事中*
### 3-3.settings.yamlの書き換え
*工事中*
## 4.プログラムの書き換えと実行
**工事中**
# 【説明】
## imagesave.py
opencvのサンプルコードです。
## imageupload.py
pydriveのサンプルコードです。
## folder/hojo_list.txt
```
HOJO_A
HOJO_B
HOJO_C
:
:
```
カメラを設置する圃場名を**半角、改行区切り**で入力します。
**圃場を追加/消去**する場合、ここを書き換えます。
## picture/
```
HOJO_A_20xxxxxx_xxxxxx.png
HOJO_A_20xxxxxx_xxxxxx.png
:
:
```
撮影された写真はここに格納されます。
# 【注意】
**工事中**