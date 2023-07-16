# demo
授業用デモ。
<img src="" width="50%" />

授業課題では、Amazon Rekognitionを用いて、送信した画像のラベルを検出し、じゃんけんを実装している。
岩の画像＝グー、ハサミの画像＝チョキ、紙の画像＝パーとみなしている。

<img src="https://github.com/SunaharaKana/demo/assets/103554924/76fc03e9-194e-4256-a92a-3a580ce455ed" width="30%" />

[一番上のフォーム]


<img src="https://github.com/SunaharaKana/demo/assets/103554924/0bbe2603-7106-476b-9bd4-8f5b9c840464" width="30%" />

[guu-iwa.png]


<img src="https://github.com/SunaharaKana/demo/assets/103554924/e87dffdb-3f2d-4a50-b34f-bd5fcc8667c1" width="50%" />

[結果]


本当は人間の手の形からラベルを検出させ、じゃんけんをさせたいところだが、デフォルトのラベル検出だとうまくいかない。
![image](https://github.com/SunaharaKana/demo/assets/103554924/bf042b08-6b20-44ba-ac4a-7843ad426fa5)
![image](https://github.com/SunaharaKana/demo/assets/103554924/66cdaaa0-7b8d-4ba8-b87a-5c804849637f)
![image](https://github.com/SunaharaKana/demo/assets/103554924/69e6d25e-d57a-4a61-92d5-16c49f78984c)



<img src="(https://github.com/SunaharaKana/demo/assets/103554924/bf042b08-6b20-44ba-ac4a-7843ad426fa5" width="80%" />
<img src="https://github.com/SunaharaKana/demo/assets/103554924/66cdaaa0-7b8d-4ba8-b87a-5c804849637fb" width="80%" />
<img src="https://github.com/SunaharaKana/demo/assets/103554924/69e6d25e-d57a-4a61-92d5-16c49f78984c" width="80%" />

背景のcomputerが検出されてしまったり、Body Partと検出されてしまったりしている。


# カスタムラベルを用いたじゃんけん

そこで、授業の発展形として、実際の人間の手でじゃんけんを行えるように改良し、デモとして授業内で見せた。

人間の手でじゃんけんの手を検出できるようにするには、カスタムラベルを用いる。

すると以下のようになる。

<img src="https://github.com/SunaharaKana/demo/assets/103554924/525f33f3-b5b2-4bf7-9dd9-3e7ef3beabbc" width="30%" />

[2番目のフォーム]


<img src="https://github.com/SunaharaKana/demo/assets/103554924/a9759e74-6f91-4796-b204-160a140be916" width="30%" />

[グー3.jpg]


![image](https://github.com/SunaharaKana/demo/assets/103554924/02094d67-0c3a-4b1a-a699-0e708441be0d)

[結果]

チョキ、パーに関しても、同様にうまく検出できている。

<img src="https://github.com/SunaharaKana/demo/assets/103554924/160471ee-44fb-424b-b553-5aff7778dd53" width="30%" />

![image](https://github.com/SunaharaKana/demo/assets/103554924/edb614f0-68e2-4c52-bf02-9e0df7174c63)

<img src="https://github.com/SunaharaKana/demo/assets/103554924/6b928b73-7887-4f99-8754-4a43fef74a37" width="30%" />

![image](https://github.com/SunaharaKana/demo/assets/103554924/b1d354a5-ca33-48e0-876b-454376358fd8)


