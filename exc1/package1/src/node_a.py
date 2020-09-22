#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

"""Acts as the publisher only for the topic "tibbling"."""

def publisher():
    """Main function that runs the pubslisher. """
    pub = rospy.Publisher('tibbling', Int16, queue_size=1)
    rospy.init_node('publisher', anonymous = True)
    rate = rospy.Rate(20) #Sets rate at 20 Hz
    k = 0                 #Number to be sent
    n = 4                 #The increment for k with each loop

    while not rospy.is_shutdown():
        k += n            #After 20 ms, send k + n to topic
        rospy.loginfo(k)  #Used for troubleshooting
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
