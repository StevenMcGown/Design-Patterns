import datetime
from time import sleep
import cv2
import sys
import logging

class monitor:
    movement_threshold = 0
    movement_sensitivity = 10
    max_movement = 300
    fps_cap = 10
    contour_sensitivity = 10
    motion = False
    recording = False

    def __init__(self, val):
        self.val = val

    def monitor_camera(self):
        print('Monitor starting at: ' + datetime.datetime.now().strftime
            ("%A %d %B %Y %I:%M:%S%p"))
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        out = cv2.VideoWriter(datetime.datetime.now().strftime
            ("%A %d %B %Y %I:%M:%S%p") + '.avi', fourcc, self.fps_cap, (640, 480))
        cap = cv2.VideoCapture(0)


        # Frame 1
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        #sleep(2)
        while cap.isOpened():

            if(self.motion==True and self.recording==False):
                print('Recording started at: ' + datetime.datetime.now().strftime
                ("%A %d %B %Y %I:%M:%S%p"))
                self.recording = True

            if self.movement_threshold >= self.movement_sensitivity and self.recording==True:
                out.write(frame1)
            # Difference between two frames
            diff = cv2.absdiff(frame1, frame2)

            # Convert to grayscale image
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

            # Blur with gausian blur
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # Finds threshold. https://docs.opencv.org/4.5.2/threshold.jpg
            _, thresh = cv2.threshold(blur, self.contour_sensitivity, 255, cv2.THRESH_BINARY)

            # Dilate image to fill in holes
            dilated = cv2.dilate(thresh, None, iterations=3)

            # Find the contour
            contours, _ = cv2.findContours(
                dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.putText(frame1, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p" + 
            "     Movement threshold: " + str(self.movement_threshold)),
            (10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            for contour in contours:

                # Save all coordinates of found contours and apply rect around contour
                (x, y, w, h) = cv2.boundingRect(contour)

                # Find area of contour. If area is less than certain value, ignore it
                if cv2.contourArea(contour) < 3000:
                    continue

                if self.movement_threshold > self.movement_sensitivity:
                    self.motion = True
                    
                self.movement_threshold+=10
                time = datetime.datetime.now()

                # draw rectangle on image
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                #cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2)
                cv2.putText(frame1, "Motion detected", (10, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            if self.movement_threshold <= 0 and self.recording == True :
                self.recording = False
                self.motion = False
                out.release()
                print('Recording stopped at: ' + datetime.datetime.now().strftime
                ("%A %d %B %Y %I:%M:%S%p"))

            elif self.movement_threshold > self.max_movement:
                self.movement_threshold = self.max_movement

            elif self.movement_threshold > 0 :
                self.movement_threshold -= 1

            elif self.movement_threshold < self.movement_sensitivity:
                self.motion = False


            
            # Show frame 1
            cv2.imshow("Security feed", frame1)
            frame1 = frame2

            # Inside frame 2, read a new value
            ret, frame2 = cap.read()

            if cv2.waitKey(40) & 0xFF == ord('q'):
                self.recording = False
                out.release()
                cv2.destroyAllWindows()
                cap.release()
                sys.exit("User issued quit command 'q'")

        cv2.destroyAllWindows()
        cap.release()