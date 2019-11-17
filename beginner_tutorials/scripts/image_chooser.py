#!/usr/bin/env python
import rospy
import cv2
import random
from cv_bridge import CvBridge
import os
from sensor_msgs.msg import Image


def choose_send(pub, bridge, dir_path, here_dir):
    dir_path = here_dir if dir_path == '0' else dir_path
    file_names = ["g1", "g2", "r1", "r2", "y1", "y2"]
    file_name = random.choice(file_names)
    full_path = "{}/{}.png".format(dir_path, file_name)
    print("chosen file: {}".format(full_path))

    cv_image = cv2.imread(full_path)
    converted = bridge.cv2_to_imgmsg(cv_image, "bgr8")
    pub.publish(converted)
    print("published.")


def talker():
    bridge = CvBridge()
    pub = rospy.Publisher('image_topic', Image, queue_size=10)
    rospy.init_node('image_chooser', anonymous=True)

    here_dir = os.path.dirname(__file__)
    dir_path = raw_input("please enter the directory of the photos (or 0 if its here): ")

    while not rospy.is_shutdown():
        choose_send(pub, bridge, dir_path, here_dir)
        _ = raw_input("again? (any key to continue, or Ctrl+C to exit)")
        print("ok here we go again")


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
