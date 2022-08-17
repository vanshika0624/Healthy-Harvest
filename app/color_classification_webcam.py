import cv2
from .color_histogram_feature_extraction import *
from  .knn_classifier import *
import os
import os.path




def startwebcam():
    cap = cv2.VideoCapture(0)
    (ret, frame) = cap.read()
    prediction = 'n.a.'

    # checking whether the training data is ready
    PATH = './training.data'

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print ('training data is ready, classifier is loading...')
    while True:

        # Capture frame-by-frame
        (ret, frame) = cap.read()

        cv2.putText(
            frame,
            'Prediction: ' + prediction,
            (15, 45),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            200,
            )

        # Display the resulting frame
        cv2.imshow('color classifier', frame)

        color_histogram_of_test_image(frame)

        prediction = main('training.data', 'test.data')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
