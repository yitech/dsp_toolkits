import os


def convert_mp4_to_mp3(src, dst=None):
    if not dst:
        filename = src.split('.')[0]
        dst = filename + '.mp3'
    cmd = 'ffmpeg -i """{}""" -b:a 128K -vn """{}"""'
    os.system(cmd.format(src, dst))
    return


def convert_mp4_to_wav(src, dst=None):
    if not dst:
        filename = src.split('.')[0]
        dst = filename + '.wav'
    cmd = 'ffmpeg -i """{}""" -b:a 128K -vn """{}"""'
    os.system(cmd.format(src, dst))
    return
