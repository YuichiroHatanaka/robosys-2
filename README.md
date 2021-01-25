## ROSを使用してタイマーを作成した
---

## 動作環境
* OS:ubuntu 20.04 server
* ROS:Noetic
---

## 実行手順
ROSインストール後に下記の手順を行ってください(端末1)
```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/YuichiroHatanaka/robosys-2.git
$ cd..
$ catkin_make
$ source ~/.bashrc
$ cd src/robosys-2/scripts
$ roscore
```
上記の手順が終わったら下記の手順を別の端末で行ってください(端末2)
```sh
$ cd ~/catkin_ws/src/robosys2/scripts
$ chmod +x timer_pub.py
$ rosrun Robot-system2 count_pub.py
```
次にさらに別の端末で下記の手順を実行してください(端末3)
```sh
$ cd ~/catkin_ws/src/Robot-system2/scripts
$ chmod +x timer_sub.py
$ rosrun reobosys-2 timer_sub.py
```
最後に新しい端末を開いてトピックから動作確認を行ってください(端末4)
```sh
$ cd ~/catkin_ws/src/robosys-2/scripts
$ rostopic list
$ rostopic echo /count_up
```
---

## 実行動画
動画URL：

---

## ライセンス

