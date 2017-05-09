#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String
from geometry_msgs.msg import Twist



cmd = ''

def callback(data):
    ser = serial.Serial('/dev/ttyACM0')
    rospy.loginfo(rospy.get_caller_id() + "I heard something: %s", data)

    leftwheelbuf=data.linear.x*278*-1
    rightwheelbuf=data.linear.x*278

    backwheelbuf = data.angular.z * 128*-1

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
