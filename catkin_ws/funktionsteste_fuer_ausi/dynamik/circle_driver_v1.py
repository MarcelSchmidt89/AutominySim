#!/usr/bin/env python2

"""
Der circle_driver_v1 soll in einem durch vorgegebene speed und steering
Kreis ewig weiter fahren, ohne sich zu stoppen.

@author: Yichi Chen
@version: 1.0
@date: 28.06.2019
"""

import rospy
import rospkg
from autominy_msgs.msg import NormalizedSteeringCommand, NormalizedSpeedCommand
import tf

# Parameter. Einstellbar!
speed = 0.5
steering = 1.0      # 1.0 entspricht voll nach links, -1.0 umgekehrt.


def talker():
    pub = rospy.Publisher('/control/command/normalized_wanted_steering', NormalizedSteeringCommand, queue_size=1) #, tcp_nodeplay=True)
    pubSpeed = rospy.Publisher('/control/command/normalized_wanted_speed', NormalizedSpeedCommand, queue_size=1)

    rospy.init_node('test_steering', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        steerMsg = NormalizedSteeringCommand()
        steerMsg.value = steering
        pub.publish(steerMsg)

        speedMsg = NormalizedSpeedCommand()
        speedMsg.value = speed
        pubSpeed.publish(speedMsg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

