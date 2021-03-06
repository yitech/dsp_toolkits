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
    url = 'https://youtu.be/zGbUxKdGAGE'
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
    for tp, start, end in filter(lambda entity: entity[0] in ['male', 'female'], res):
        fn = clip.clip_segment(wav, start, end, f"{wav_name}_{tp}_{str(count).zfill(2)}.wav")
        data['segment'].update({fn: {}})
        data['segment'][fn].update({'start_seconds': start,
                                    'end_seconds': end,
                                    'stt': {}})
        count += 1

    # STT
    st = stt.STT()
    print(data)
    for wav_clip in data['segment'].keys():
        print(f"wav_clip: {wav_clip}")
        sentence, align = st.to_text(wav_clip)
        data['segment'][wav_clip]['stt'].update({'sentence': sentence,
                                                 'word_align': []})
        for a in align:
            data['segment'][wav_clip]['stt']['word_align'].append(a)
            data['segment'][wav_clip]['stt']['word_align'][-1]['start_ts'] += data['segment'][wav_clip]['start_seconds']
            data['segment'][wav_clip]['stt']['word_align'][-1]['end_ts'] += data['segment'][wav_clip]['start_seconds']

    # save files
    with open(file='data/data.json', mode='w+') as jfile:
        json.dump(data, jfile, indent=4)





