#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
v1:
Der circle_driver_v1 soll in einem durch vorgegebene speed und steering
Kreis ewig weiter fahren, ohne sich zu stoppen.

v3:
Die Fahrgeschwindigkeit inkrementiert sich konstant, während die Fahrrichtung 
konstant bleibt.


@author: Yichi Chen
@version: 1.0
@date: 28.06.2019
"""

import rospy
import rospkg
from autominy_msgs.msg import NormalizedSteeringCommand, NormalizedSpeedCommand
import tf

# Parameter. Einstellbar!
steering = 1.0      # 1.0 entspricht voll nach links, -1.0 umgekehrt.
MAX_SPEED = 1.0
MIN_SPEED = -1.0
TOP_SPEED_TIME = 3       # Zeitdauer für die Top-Speed, sowohl für MAX_SPEED als auch für MIN_SPEED
# TOP_SPEED_TIME wird in der Nachfolge implementiert
inkrement = 0.01

def talker():
    speed = 0.0
    direc = 1

    pub = rospy.Publisher('/control/command/normalized_wanted_steering', NormalizedSteeringCommand, queue_size=1) #, tcp_nodeplay=True)
    pubSpeed = rospy.Publisher('/control/command/normalized_wanted_speed', NormalizedSpeedCommand, queue_size=1)

    rospy.init_node('test_steering', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if speed >= MAX_SPEED:
            direc = -1
        if speed <= MIN_SPEED:
            direc = 1
        steerMsg = NormalizedSteeringCommand()
        steerMsg.value = steering
        pub.publish(steerMsg)

        speedMsg = NormalizedSpeedCommand()
        speed += 0.01 * direc       # Inkrement der Fahrgeschwindigkeit
        speedMsg.value = speed
        pubSpeed.publish(speedMsg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

