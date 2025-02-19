#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

def image_callback(ros_image):
    print 'got an image'
    global bridge
    #Convert ros_image into an opencv-compatible image
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)
    # Work in opencv-compatible
    (rows,cols,channels) = cv_image.shape
    if cols > 200 and rows > 200 :
         cv2.circle(cv_image, (100,100), 90, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.imshow("image window", cv_image)
    cv2.waitKey(3)

def main(args):
    rospy.init_node('image_converter', anonymous=False)
    image_sub = rospy.Subscriber("/carsim/camera1/image_raw1",Image,image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
