#!/usr/bin/env python

"""Acts as the publisher"""

import rospy
from std_msgs.msg import Int16

def publisher():
    pub = rospy.Publisher('tibbling', Int16, queue_size=1)
    rospy.init_node('publisher', anonymous = True)
    rate = rospy.Rate(2) #Sets rate at 20 Hz
    k = 0                 #Number to be sent
    n = 4                 #The increment for k with each loop

    while not rospy.is_shutdown():
        k += n
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
