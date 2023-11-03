# AI-grades-register

## 目的
在台灣，國、高中時期的科目小老師總是要負責幫助老師登記考卷分數，但登記分數是一件重複勞動且費時的事情，
我希望能透過運用AI(影像辨識、語音辨識)來幫助我自動化這些瑣碎且浪費人生的事情。

## 目前專案MVP介紹
透過AI即時辨識語音，登記考卷成績，並且自動寫入google sheet。

## DEMO
[![載入DEMO影片中](https://img.youtube.com/vi/ICIQxyWSBdY/0.jpg)](https://youtu.be/ICIQxyWSBdY)


## 實作方法
通過speech_recognition這個庫串接google的免費STT服務(https://www.google.com/intl/en/chrome/demos/speech.html)
隨後通過 Google sheet api將成績直接登記在雲端


## 為何不先開發影像辨識自動登記成績的功能
由於我們班平常做的英文練習卷有兩面且需將兩面成績相加除以2，
很多同學會將兩次成績登記在一面並進行直式計算得出分數，故較難通過影像辨識從三個分數(第一面成績、第二面成績、加總平均成績)中辨識出
需要登記的那一個。
由於開發此程式主要目的還是為了讓我自己登記成績更加方便，故目前就暫時只開發語音辨識自動登記成績功能。


## 未來計畫
1. 加入影像辨識功能，可供使用者自行選擇模式
2. 自己訓練影像辨識與語音辨識的模型，提高辨識精確度
3. 將程式利用django框架、websocket技術等部屬成一個簡易工具網站，讓不會寫程式的小老師們也能來使用


## Dependencies
```
SpeechRecognition==3.10.0
PyAudio==0.2.13
google-api-python-client==2.101.0
google-auth-httplib2==0.1.1
google-auth-oauthlib==0.4.6
python-dotenv==0.21.0
```

## References
- 進程與線程的概念整理
https://pjchender.dev/computer-science/cs-process-thread/

- Speech_recognition listen in BG
https://www.youtube.com/watch?v=p2vx-JliElY

- Google Web speech API
https://wicg.github.io/speech-api/#speechreco-events

- Speech Recognition repo
https://github.com/Uberi/speech_recognition/tree/master

- pretrained model
https://github.com/kpu/kenlm

- the method to train your own STT model
https://www.youtube.com/watch?v=YereI6Gn3bM

- How to Use Google Sheets With Python (2023)
https://www.youtube.com/watch?v=bu5wXjz2KvU