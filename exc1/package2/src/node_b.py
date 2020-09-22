#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Float32

pub = rospy.Publisher("/kthfs/result", Float32, queue_size=1)
q = 0.15

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    out_data = data.data/q   #Data to be sent to the topic "/kthfs/result"
    pub.publish(out_data)    #Publishinglogging for debugging
    rospy.loginfo(out_data)  #logging for debugging, optional

def bounce():
    rospy.init_node('buoncer', anonymous=True)
    rospy.Subscriber("tibbling", Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    bounce()
