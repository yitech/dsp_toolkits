import torch


class STT:
    def __init__(self):
        self.device = torch.device('cpu')
        self.model, self.decoder, self.utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                              model='silero_stt',
                                                              language='en', # also available 'de', 'es'
                                                              device=self.device)

    def to_text(self, wav):
        (read_batch, split_into_batches,
         read_audio, prepare_model_input) = self.utils
        input = prepare_model_input(read_batch([wav]), device=self.device)
        output = self.model(input)
        for example in output:
            print(self.decoder(example.cpu()))
        return
