#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def callback(message):
    print(message.data)

if __name__ == "__main__":
    rospy.init_node('timer_sub')
    sub = rospy.Subscriber('timer_search', Float64, callback)
    rospy.spin()
© 2021 GitHub, Inc.
