#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('publisher', anonymous = True)
    rate = rospy.Rate(20) #Sets rate at 20 Hz
    k = 0                 #Number to be sent
    n = 4                 #The increment for k with each loop

    while not rospy.is_shutdown():
        k += n
        k_string = " " + str(k)
        #hello_str = "Hello there %s" % rospy.get_time()
        rospy.loginfo(k_string)
        pub.publish(k_string)
        rate.sleep()
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
