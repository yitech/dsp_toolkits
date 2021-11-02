from pytube import YouTube


def download_mp4_from_youtube(url, dstination_folder=None):
    yt = YouTube(url)
    yt.streams.\
        filter(audio_codec="mp4a.40.2", file_extension='mp4').\
        first().\
        download()
    return
