#!/usr/bin/env python3

import rospy
  4 from std_msgs.msg import Int32
  5
  6 def cb(message):
  7         rospy.loginfo(message.data*2)
  8
  9 if __name__ == '__main__':
 10         rospy.init_node('twice')
 11         sub = rospy.Subscriber('count_up', Int32, cb)
 12         rospy.spin()
 1
