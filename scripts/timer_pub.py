#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

while not rospy.is_shutdown():

    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Float64, queue_size = 1)
    rate = rospy.Rate(10)

    print("1:start")
    print("2:stop")

    figure = int(input())

    if figure == 1:
        timer_time = 180
        start_time = rospy.get_time()
        print("180s timer start")
        finish_time = start_time + timertime
        
        for(;;)
        if rospy.get_time == finishtime:
        break
        
        printf("時間です！")
        
    rate.sleep()
