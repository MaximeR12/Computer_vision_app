############################
#   Importation du modèle  #
############################
from ultralytics import YOLO

model = YOLO("bestS.pt")

############################
#      Streamlit app       #
############################
import streamlit as st
from PIL import Image 
import tempfile
import cv2




def _display_detected_frames(conf, model, st_frame, image):
    """
    Display the detected objects on a video frame using the YOLOv8 model.
    :param conf (float): Confidence threshold for object detection.
    :param model (YOLOv8): An instance of the `YOLOv8` class containing the YOLOv8 model.
    :param st_frame (Streamlit object): A Streamlit object to display the detected video.
    :param image (numpy array): A numpy array representing the video frame.
    :return: None
    """
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Predict the objects in the image using YOLOv8 model
    res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )
source_video = st.sidebar.file_uploader(
        label="Choose a video..."
    )
if source_video:
        st.video(source_video)

if source_video:
    if st.button("Execution"):
        with st.spinner("Running..."):
            try:
                tfile = tempfile.NamedTemporaryFile()
                tfile.write(source_video.read())
                vid_cap = cv2.VideoCapture(
                    tfile.name)
                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        _display_detected_frames(0.2,
                                                model,
                                                st_frame,
                                                image
                                                )
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.error(f"Error loading video: {e}")