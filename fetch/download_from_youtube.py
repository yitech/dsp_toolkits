import os
from pytube import YouTube


def download_mp4_from_youtube(url, destination_folder=''):
    yt = YouTube(url)
    yt.streams\
        .filter(audio_codec="mp4a.40.2", file_extension='mp4')\
        .first()\
        .download(destination_folder)
    return os.path.join(destination_folder, yt.title + '.mp4')
