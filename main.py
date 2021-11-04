import glob
import os
import fetch
import convert
import seg
import clip
import stt
import json


if __name__ == '__main__':
    # empty files
    for root, dirs, files in os.walk('data'):
        for f in files:
            os.remove(os.path.join(root, f))
    data = {}
    # Fetch from yt
    url = 'https://www.youtube.com/watch?v=R0Uq8Eg39R0'
    fn = fetch.download_mp4_from_youtube(url, 'data')
    data.update({'source_video': url, 'storage': fn})
    # Convert to wav
    mp4_files = glob.glob('data/*.mp4')
    wav = convert.convert_mp4_to_wav(mp4_files[-1])
    # Segment
    segmenter = seg.Segmenter()
    res = segmenter(wav)
    data.update({'segment': {}})
    # clip male and female
    count = 0
    wav_name = wav.split('.')[0]
    for tp, start, end in filter(lambda entity: entity[0] == 'male', res):
        fn = clip.clip_segment(wav, start, end, f"{wav_name}_{tp}_{str(count).zfill(2)}.wav")
        data['segment'].update({fn: {}})
        data['segment'][fn].update({'start_seconds': start,
                                    'end_seconds': end})
        count += 1
    for tp, start, end in filter(lambda entity: entity[0] == 'female', res):
        fn = clip.clip_segment(wav, start, end, f"{wav_name}_{tp}_{str(count).zfill(2)}.wav")
        data['segment'].update({fn: {}})
        data['segment'][fn].update({'start_seconds': start,
                                    'end_seconds': end,
                                    'stt': {}})
        count += 1

    # STT
    st = stt.STT()
    for wav_clip in data['segment'].keys():
        sentence, align = st.to_text(wav_clip)
        data['segment'][fn]['stt'].update({'sentence': sentence})
        for a in align:
            data['segment'][fn]['stt'].update(a)
            data['segment'][fn]['stt']['start_ts'] += data['segment'][fn]['start_seconds']
            data['segment'][fn]['stt']['end_ts'] += data['segment'][fn]['start_seconds']


    # save files
    with open(file='data/data.json', mode='w+') as jfile:
        json.dump(data, jfile, indent=4)





