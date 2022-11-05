import cv2

# capture frames from a video
cap = cv2.VideoCapture( 'carvedio3.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_tracker = cv2.CascadeClassifier( 'Cars.xml')

# loop runs if capturing has been initialized.
while True:

    # reads frames from a video
    read_Succesful, frame = cap.read()

    if read_Succesful:

        # convert to gray scale of each frames
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:
        break


    # Detects cars of different sizes in the input image
    cars = car_tracker.detectMultiScale( gray, 1.1, 1, 0, (110,110))

    # Print the cars
    print(f"Cars = {cars}")

    # To draw a rectangle on each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w-2,y+h-2),(0,0,255),2)
        # Display frames in a window
        cv2.imshow('Car Detection', frame)

    # Wait for Enter key to stop
    if cv2.waitKey(300) == 13:
        break

print("Code Completed")

cv2.destroyAllWindows()