#/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

while not rospy.is_shutdown():

	rospy.init_node('timer_pub')
	pub = rospy.Publisher('time_up', Float64, queue_size = 1)
	rate = rospy.Rate(10)

	print("計りたい秒数を設定してください")

	second = int(input())

	print("0を押してスタートしてください")

	figure = int(input())
	from time import sleep

	count = 0

	if figure == 0:

		while count < second:

			print(second - count)

			count += 1

			sleep(1)

		print("時間です!")

	rate.sleep()
