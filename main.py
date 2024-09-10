import cv2

frameTracker = {0: (940, 818, 156, 90), 242:(1647, 436, 119, 65)}
def get_video_frames(name):
    video = cv2.VideoCapture(name)  # Replace with your video file
    cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)

    # cv2.resizeWindow("Tracking", width, height)
    frame_id = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame_id += 1

        # if frame_id < 200:
        #     continue
        yield frame

    video.release()
    cv2.destroyAllWindows()

def track_object(frames):

    roiFrames = list(frameTracker.keys())
    for i, frame in enumerate(frames):
        if i in roiFrames :
            # bbox = (1647, 436, 119, 65)
            # bbox = cv2.selectROI("Tracking", frame, False)
            tracker = cv2.legacy.TrackerCSRT_create()
            bbox = frameTracker[i]
            print(bbox)
            tracker.init(frame, bbox)
        else:
            # Update tracker
            success, bbox = tracker.update(frame)

            if success:
                # Draw bounding box
                x, y, w, h = [int(i) for i in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        frame_id = i + 1
        # print('video frame id = ', frame_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    frames = get_video_frames('C:/Users/robor/Downloads/PXL_20240724_183502779.mp4')
    track_object(frames)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
