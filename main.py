import glob
import fetch
import convert

if __name__ == '__main__':
    urls = ['https://www.youtube.com/watch?v=R0Uq8Eg39R0']
    fetch.download_mp4_from_youtube(urls[0], 'data')
    files = glob.glob('data/*.wav')
    wav_file = convert.convert_mp4_to_wav(files[0])




