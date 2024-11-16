from moviepy.editor import *

audio = VideoFileClip("Way Much Better.mp4").audio
audio.write_audiofile("Way Much Better.mp3")