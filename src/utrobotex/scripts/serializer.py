#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String
from geometry_msgs.msg import Twist



cmd = ''

def callback(data):
    ser = serial.Serial('/dev/ttyACM0')
    leftwheelbuf = 0
    rightwheelbuf = 0
    backwheelbuf = 0
    rospy.loginfo(rospy.get_caller_id() + "I heard something: %s", data)
    if (data.linear.x!=0):
        leftwheelbuf=data.linear.x*278*-1
        rightwheelbuf=data.linear.x*278

    if (data.angular.z!=0):
        leftwheelbuf = data.angular.z * 43*-1
        rightwheelbuf = data.angular.z * 43*-1
        backwheelbuf = data.angular.z * 43*-1

    cmd = 'l' + str(int(leftwheelbuf)).zfill(4) + 'r' + str(int(rightwheelbuf)).zfill(4) + 'b' + str(int(backwheelbuf)).zfill(4) + '\n'
    rospy.loginfo(cmd)
    ser.write(cmd)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/cmd_vel_mux/input/teleop",Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
