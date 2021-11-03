import os
import time


def clip_segment(wav_file, start_seconds, end_seconds, dst):
    cmd = 'ffmpeg -ss {start_time} -i """{input}""" -to {end_time} -c copy """{output}"""'
    start_ms = start_seconds - int(start_seconds)
    start_time = time.strftime('%H:%M:%S', time.gmtime(start_seconds)) + f".{str(start_ms).split('.')[-1]}"
    end_ms = end_seconds - int(end_seconds)
    end_time = time.strftime('%H:%M:%S', time.gmtime(end_seconds)) + f".{str(end_ms).split('.')[-1]}"
    os.system(cmd.format(start_time=start_time, input=wav_file, end_time=end_time, output=dst))
    return dst
