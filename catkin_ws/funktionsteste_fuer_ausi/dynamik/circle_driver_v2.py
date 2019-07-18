#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Wechselhafte Kreis-Fahrt. Also alle round_dist im Uhrzeigersinn bzw. gegen den Uhrzeigersinn

@author: Yichi Chen
@version: 1.0
@date: 28.06.2019
"""

import rospy
import rospkg
from autominy_msgs.msg import NormalizedSteeringCommand, NormalizedSpeedCommand
#import tf
import time

# Parameter. Einstellbar!
speed = 0.5
round_dist = 6       # Sekundenzahl für jede Runde


def talker():
    pub = rospy.Publisher('/control/command/normalized_wanted_steering', NormalizedSteeringCommand, queue_size=1) #, tcp_nodeplay=True)
    pubSpeed = rospy.Publisher('/control/command/normalized_wanted_speed', NormalizedSpeedCommand, queue_size=1)

    rospy.init_node('test_steering', anonymous=True)
    rate = rospy.Rate(10)
    old_time = time.time()
    steering = 1
    this_round = 0      # time for this round
    while not rospy.is_shutdown():
        new_time = time.time()
        this_round += new_time - old_time
        # Richtung wechseln
        if this_round >= round_dist:
            steering = -1 * steering
            this_round = 0
        old_time = new_time


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

