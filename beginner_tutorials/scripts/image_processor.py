#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from beginner_tutorials.srv import DoubleMessage, DoubleMessageResponse


def callback(data):
    print("got callback")
    rospy.wait_for_service('double_message')

    try:
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        color = get_color(cv_img=cv_image)
        print("image processing node found that the color is {}.".format(color))

        double_message_service = rospy.ServiceProxy('double_message', DoubleMessage)
        response = double_message_service(color)
        print(response.answer)

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def get_color(cv_img):
    h = cv_img.shape[0]
    w = cv_img.shape[1]

    for y in range(0, h):
        for x in range(0, w):
            b, g, r = cv_img[y, x]
            if b < 200 and g < 200 and r > 200:
                return "red"

            if b < 200 and g > 200 and r < 200:
                return "green"

            if b < 200 and g > 200 and r > 200:
                return "yellow"


def listener():
    rospy.init_node('image_processor', anonymous=True)
    rospy.Subscriber("image_topic", Image, callback)
    print("starting to listen on topic 'image_topic'")
    rospy.spin()


if __name__ == '__main__':
    listener()
