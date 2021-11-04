import os
import time


def clip_segment(wav_file, start_seconds, end_seconds, dst):
    cmd = 'ffmpeg -ss {start_time} -i """{input}""" -to {duration} -c copy """{output}"""'
    start_ms = start_seconds - int(start_seconds)
    start_time = time.strftime('%H:%M:%S', time.gmtime(start_seconds)) + f".{str(start_ms).split('.')[-1]}"
    duration_seconds = end_seconds - start_seconds
    duration_ms = duration_seconds - int(duration_seconds)
    duration_time = time.strftime('%H:%M:%S', time.gmtime(duration_seconds)) + f".{str(duration_ms).split('.')[-1]}"
    os.system(cmd.format(start_time=start_time, input=wav_file, duration=duration_time, output=dst))
    return dst
