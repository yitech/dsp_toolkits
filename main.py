import glob
import fetch
import convert
import clip
import json


if __name__ == '__main__':
    data = {}
    # Fetch from yt
    url = 'https://www.youtube.com/watch?v=R0Uq8Eg39R0'
    fn = fetch.download_mp4_from_youtube(url, 'data')
    data.update({'source_video': url, 'storage': fn})
    # Convert to wav
    mp4_files = glob.glob('data/*.mp4')
    wav = convert.convert_mp4_to_wav(mp4_files[-1])
    # Segment
    res = [('noise', 0.0, 2.18), ('music', 2.18, 12.88), ('male', 12.88, 106.78),
           ('noEnergy', 106.78, 107.3), ('male', 107.3, 132.58), ('noEnergy', 132.58, 133.44),
           ('male', 133.44, 176.58), ('noEnergy', 176.58, 176.98), ('male', 176.98, 179.5),
           ('noEnergy', 179.5, 179.96), ('male', 179.96, 205.74), ('noEnergy', 205.74, 206.20000000000002),
           ('male', 206.20000000000002, 217.98000000000002), ('noEnergy', 217.98000000000002, 218.5),
           ('male', 218.5, 252.08), ('noEnergy', 252.08, 253.0), ('male', 253.0, 256.46),
           ('noEnergy', 256.46, 257.28000000000003), ('male', 257.28000000000003, 274.98),
           ('music', 274.98, 277.8), ('male', 277.8, 299.98), ('music', 299.98, 309.52),
           ('female', 309.52, 320.88), ('music', 320.88, 323.68), ('male', 323.68, 338.28000000000003),
           ('music', 338.28000000000003, 340.18), ('female', 340.18, 342.46), ('noEnergy', 342.46, 342.86),
           ('female', 342.86, 344.5), ('noEnergy', 344.5, 346.08), ('male', 346.08, 353.40000000000003),
           ('noEnergy', 353.40000000000003, 354.16), ('male', 354.16, 370.62), ('noEnergy', 370.62, 371.08),
           ('music', 371.08, 382.22), ('female', 382.22, 388.28000000000003), ('music', 388.28000000000003, 389.56),
           ('female', 389.56, 397.16), ('noEnergy', 397.16, 397.76), ('male', 397.76, 445.04), ('noEnergy', 445.04, 445.74),
           ('music', 445.74, 449.5), ('male', 449.5, 457.12), ('noEnergy', 457.12, 458.62), ('female', 458.62, 467.2),
           ('noEnergy', 467.2, 468.78000000000003), ('male', 468.78000000000003, 471.78000000000003),
           ('noEnergy', 471.78000000000003, 472.22), ('male', 472.22, 476.04), ('noEnergy', 476.04, 477.16),
           ('male', 477.16, 482.86), ('noEnergy', 482.86, 483.96000000000004), ('female', 483.96000000000004, 491.82),
           ('noEnergy', 491.82, 493.24), ('male', 493.24, 532.44), ('noEnergy', 532.44, 534.44),
           ('music', 534.44, 539.34), ('male', 539.34, 567.64), ('noEnergy', 567.64, 568.16),
           ('male', 568.16, 599.02), ('noEnergy', 599.02, 600.08)]
    data.update({'segment': {}})
    # clip male and female
    count = 0
    wav_name = wav.split('.')[-1]
    for tp, start, end in filter(lambda entity: entity[0] == 'male', res):
        fn = clip.clip_segment(wav, start, end, f"{wav_name}_{tp}_{str(count).zfill(2)}.wav")
        data['segment'].update({fn: {}})
        data['segment'][fn].update({'start_seconds': start,
                                    'end_seconds': end})
        count += 1
    print(data)





