#!/usr/bin/env python
from beginner_tutorials.srv import DoubleMessage, DoubleMessageResponse
import rospy


def handle_double_message(req):
    d = {
        'red': 'stop',
        'yellow': 'wait',
        'green': 'go',
    }
    err_msg = 'call did not match somthing known :('
    print d.get(req.call, err_msg)
    return DoubleMessageResponse('done')


def double_message_server():
    rospy.init_node('double_message_server')
    s = rospy.Service('double_message', DoubleMessage, handle_double_message)
    print "Ready to handle double messages"
    rospy.spin()


if __name__ == "__main__":
    double_message_server()
