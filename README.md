# OpenCV-Video-Experiment-Contour-Based-Object-Bounding

This project is a basic hands-on experiment done while learning OpenCV with Python. The goal of this code is not accurate object or face detection, but to understand how a video stream is processed frame by frame, how edges are detected, how contours are extracted, and how bounding boxes can be drawn around detected regions.

The code uses a webcam feed and applies classical computer vision techniques such as grayscale conversion, Gaussian blurring, Canny edge detection, contour detection, and bounding rectangles. All operations are intentionally simple and exploratory.

The program starts by importing OpenCV and opening the default webcam using cv2.VideoCapture(0). The video feed is read inside a while loop that runs as long as the camera is opened successfully. Each iteration of the loop processes one video frame.

For every frame read from the camera, the first step is to convert the color image (BGR format) into grayscale using cv2.cvtColor. This is done because most edge detection and thresholding algorithms work on intensity values rather than color information, and grayscale images reduce computational complexity.

Next, Gaussian blur is applied using cv2.GaussianBlur with a kernel size of (7, 7). This step smooths the image and reduces noise, which helps prevent false or fragmented edges during edge detection. Without blurring, small lighting variations or sensor noise can create unnecessary edges.

After blurring, Canny edge detection is applied using cv2.Canny with lower and upper threshold values of 50 and 150. This step detects strong intensity gradients in the image and produces a binary edge map. The output highlights boundaries of objects, facial features, shadows, and background structures.

A copy of the original color frame is created using frame.copy(). This is done to ensure that all drawing operations (rectangles) are performed on a separate image, leaving the original frame unmodified. This is a good practice during experimentation and debugging.

Contours are then extracted from the edge-detected image using cv2.findContours. The retrieval mode cv2.RETR_EXTERNAL is used to detect only the outermost contours, avoiding nested or internal contours. The approximation method cv2.CHAIN_APPROX_SIMPLE is chosen to reduce memory usage by storing only essential contour points.

Each detected contour is processed inside a loop. A small area threshold (cv2.contourArea(cnt) > 100) is applied to ignore very small contours caused by noise or minor edge fragments. This helps reduce the number of meaningless bounding boxes.

For contours that pass the area condition, a bounding rectangle is calculated using cv2.boundingRect. This function returns the top-left corner coordinates (x, y) and the width and height (w, h) of the rectangle that tightly encloses the contour. A green rectangle is then drawn on the copied frame using cv2.rectangle.

The processed frame with bounding boxes is displayed using cv2.imshow. The program continuously updates this window to show real-time processing of the video stream.

To control program termination, two exit conditions are used. The first allows the user to press the q key to exit the loop. The second checks whether the display window has been manually closed using cv2.getWindowProperty. Since OpenCV does not automatically stop execution when a window is closed, this check ensures the loop exits cleanly if the user clicks the close button.

Finally, once the loop ends, the webcam resource is released using vid.release(), and all OpenCV windows are closed using cv2.destroyAllWindows() to properly clean up resources.

Overall, this code is a learning exercise intended to understand how classical computer vision pipelines work on video data. The bounding boxes produced are based purely on edges and contours, which explains why they may appear around partial facial regions, shadows, or background objects instead of neatly around the face itself.
