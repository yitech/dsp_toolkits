import inaSpeechSegmenter


class Segmenter(inaSpeechSegmenter.segmenter):
    def __init__(self):
        super(Segmenter, self).__init__()

    def segment(self, wav_file):
        return super(Segmenter, self).__call__(wav_file)
