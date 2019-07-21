# week2

・どんな実装をしたか

　　実行をし、カメラを起動すると、1フレーム（1/30秒）ごとに、輝度の平均値を求め、配列に追加していく。qを押し、終了した後にグラフを表示する。


・使い方

    1.calc_brightness_camera(1, 'camera_capture_cycle', 1)を実行する。
    
    (ちなみに、最初の1はカメラのデバイス（外カメラ)を表し、次はベースネーム（保存時に用いるため残した）、最後の1はサイクル（処理の速度）)
    
    2.カメラを動かしたりなどして、撮影する。
    
    3."q"を押し終了する。
    
    4.輝度値の平均のフレームごとを表すグラフが表示される。


・依存ライブラリ

　　cv2
    os
    datetime
    numpy as np
    matplotlib.pyplot as plt
    
    
・バージョン情報　python3.6.0


・参考にしたサイト

　　https://ensekitt.hatenablog.com/entry/2017/12/19/200000
 
  （処理が重くならないためにフレームサイズを小さかったので、
  
  　frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4))
   
   　を引用した)
    
    https://note.nkmk.me/python-opencv-camera-to-still-image/
    
    （このURLでは画像の保存を主としているが、最もわかりやすかったので、ベースの文章として引用させていただいた。)


・gifアニメーション

  ![ex](https://github.com/hu-mitu/week2/blob/master/exweek2.gif.gif)
