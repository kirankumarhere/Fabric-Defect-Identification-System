import os, sys

import tensorflow as tf
import cv2
import time
import serial, time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

time.sleep(1) #give the connection a second to settle
arduino.flush();
arduino.write('2') #stop motor
time.sleep(0.3)
camera_port = 1

ramp_frames = 50

camera = cv2.VideoCapture(camera_port)


def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
 
while(1): 
        
        print("Taking image...")
        # Take the actual image we want to keep
       
       # camera_capture = get_image()
        f = '/home/kiran/da.png'
        for i in xrange(ramp_frames):
                temp = get_image()

        camera_capture = get_image()
        time.sleep(1)
        cv2.imwrite(f, camera_capture) #write the file to ~/opencv/opencv-3.1.0/samples/python
        
        time.sleep(1)
        error_img = cv2.imread(f)
        time.sleep(1)
        
        image_path = f

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line 
                           in tf.gfile.GFile("retrained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            
            predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})
            
            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            
            
            l = [];    
             
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %f)' % (human_string, score))
                l.append(score)
                
            
            if l[0]>0.85:
                print 'no defect'
                print l
                arduino.write('1')
                #time.sleep(1.275)
                time.sleep(2)
                arduino.write('2')
            else:
                print 'error..'
                print l
                
                cv2.imshow('error_sample...',error_img)
                arduino.write('3')
                print 'Please Press Any Key to continue...'
                k=cv2.waitKey(0) 
                arduino.write('1')
                #time.sleep(1.275)
                time.sleep(2)
                arduino.write('2')
                
            l = []
                   


