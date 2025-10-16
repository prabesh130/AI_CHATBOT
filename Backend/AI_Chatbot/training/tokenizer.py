import os 
import json 
from pathlib import Path 
from tokenizers import Tokenizer
from tqdm import tqdm 
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import ByteLevel,Whitespace
from tokenizers.processors import TemplateProcessing
BASE_DIR=Path('D:\Projects\AI_Chatbot\Backend').resolve()
class CodeTokenizer:
    def __init__(self):
        self.data_dir=BASE_DIR/'AI_Chatbot'/'data'/'training_data'
        self.processed_data=self.data_dir/'processed'
        self.tokenizer_data=BASE_DIR/'AI_Chatbot'/'data'/'tokenizer'
        self.tokenizer=None
    def preprare_tokenization_data(self):
        #creating a temporary file to store data 
        #that has tokenized
        total_lines=0
        text_file=self.tokenizer_data/'tokenizer_training.txt'
        with open(text_file,'w',encoding='utf-8') as f:
            with open(self.processed_data/'train.jsonl','r',encoding='utf-8') as inf:
                for line in tqdm(inf,desc='Processing'):
                    try:
                        data=json.loads(line)
                        f.write(data['prompt']+'\n')
                        f.write(data['response']+'\n')
                        total_lines+=2
                    except json.JSONDecodeError:
                     continue
        print(f'Extracted: {total_lines}')
        return str(text_file)
    def create_tokenizer(self,vocab_size=32000):
        self.tokenizer=Tokenizer(BPE(unk_token='<UNK>'))
        trainer=BpeTrainer(
            vocab_size=vocab_size,
            min_frequency=2,
            special_tokens=[
                "<PAD>",
                "<BOS>",
                "<EOS>",
                "<UNK>",
            ],show_progress=True)
        self.tokenizer.pre_tokenizer=ByteLevel()
        self.tokenizer.normalizer=None
        
        return trainer
    def train_tokenizer(self,training_file,trainer):
        self.tokenizer.train([training_file],trainer)
        self.tokenizer.post_process=TemplateProcessing(
            single="<BOS> $A <EOS>",
            special_tokens=[
                ('<BOS>',1),
                ('<EOS>',2),
            ],

        )
    def save_tokenizer(self):
        tokenizer_path=self.tokenizer_data/'code_tokenizer'
        self.tokenizer.save(str(tokenizer_path))
        return tokenizer_path
    def run_full_pipeline(self,vocab_size=32000):
        training_file=self.preprare_tokenization_data()
        trainer=self.create_tokenizer(vocab_size=vocab_size)
        self.train_tokenizer(training_file,trainer)
        tokenizer_path=self.save_tokenizer()
    def check_example(self,text_file):
        encoding=self.tokenizer.encode(text_file)
        print(encoding)
        print('\n')
        decoding=self.tokenizer.decode(encoding)
        print(decoding)
        print('\n')


        
if __name__=='__main__':
    trainer=CodeTokenizer()
    trainer.run_full_pipeline()
    text="hello i am prabesh"
    trainer.check_example(text)