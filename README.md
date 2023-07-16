# demo
授業用デモ。

大学4年の時に作成した。

<img src="" width="50%" />

授業課題では、Amazon Rekognitionを用いて、送信した画像のラベルを検出し、じゃんけんを実装している。
岩の画像＝グー、ハサミの画像＝チョキ、紙の画像＝パーとみなしている。

<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16.png" width="30%" />

[一番上のフォーム]


<img src="https://github.com/SunaharaKana/demo/blob/master/guu-iwa.png" width="30%" />

[guu-iwa.png]


<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(1).png" width="50%" />

[結果]


本当は人間の手の形からラベルを検出させ、じゃんけんをさせたいところだが、デフォルトのラベル検出だとうまくいかない。

<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(4).png" width="80%" />
<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(2).png" width="80%" />
<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(3).png" width="80%" />

背景のcomputerが検出されてしまったり、Body Partと検出されてしまったりしている。


# カスタムラベルを用いたじゃんけん

そこで、授業の発展形として、実際の人間の手でじゃんけんを行えるように改良し、デモとして授業内で見せた。

人間の手でじゃんけんの手を検出できるようにするには、カスタムラベルを用いる。

すると以下のようになる。

<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(5).png" />

<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(6).png"/>

<img src="https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(7).png" />

使用した画像は上で示したものである。それぞれうまく検出できている。

# おまけ
おまけ用のデモとして、簡単な顔認証を実装した。

やり方は以下の通りである。

・S3バケットに顔写真をいれる

・Rekognitionの顔の比較を用い、S3バケットにある顔写真と、送信した顔写真が一致しているかどうかを見る

・一致していた場合はsuccess、失敗した場合はfailureを返す

![image](https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(8).png)

![image](https://github.com/SunaharaKana/demo/blob/master/2023-07-16%20(9).png)



