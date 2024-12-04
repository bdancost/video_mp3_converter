from moviepy.editor import *
import os

video_path = "Roar.mp4"

if not os.path.exists(video_path):
    print(f"Erro: O arquivo '{video_path}' não foi encontrado.")
else:
    with VideoFileClip(video_path) as video:
        audio = video.audio
        audio.write_audiofile("KatyPerry-Roar.mp3")

