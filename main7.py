import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading

st.set_page_config(page_title="Streamlit WebRTC Demo", page_icon="🤖")

task_list = ["Video Stream"]
with st.sidebar:
    st.title('Task Selection')
    task_name = st.selectbox("Select your tasks:", task_list)
st.title(task_name)

if task_name == task_list[0]:
    style_list = ['color', 'black and white']
    st.sidebar.header('Style Selection')
    style_selection = st.sidebar.selectbox("Choose your style:", style_list)

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'
    def recv(self, frame):
        img = frame.to_image()
        
        # image processing code here
    
        return av.VideoFrame.from_image(img)
webrtc_streamer(key="vpf", video_processor_factory=VideoProcessor)

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'
def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # image processing code here
    
        return av.VideoFrame.from_ndarray(img, format="bgr24")
webrtc_streamer(key="vpf", video_processor_factory=VideoProcessor)

def recv(self, frame):
    img = frame.to_image()
        
    # image processing code here
    # using PIL to convert img to greyscale
    if self.style == style_list[1]:
        img = img.convert("L")
    return av.VideoFrame.from_image(img)

st.sidebar.header('Style Selection')
style_selection = st.sidebar.selectbox("Choose your style:", style_list)
...
ctx = webrtc_streamer(key="vpf", video_processor_factory=VideoProcessor)
if ctx.video_processor:
    ctx.video_processor.style = style_selection

st.sidebar.header('Style Selection')
style_selection = st.sidebar.selectbox("Choose your style:", style_list)
...
class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.model_lock = threading.Lock()
        self.style = style_list[0]
    def update_style(self, new_style):
        if self.style != new_style:
            with self.model_lock:
                self.style = new_style
...
ctx = webrtc_streamer(key="vpf", video_processor_factory=VideoProcessor)
if ctx.video_processor:
    ctx.video_transformer.update_style(style_selection)

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

ctx = webrtc_streamer(
        key="example",
        video_processor_factory=VideoProcessor,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )