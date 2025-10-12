import os 
import json
import sys
from  pathlib import Path 
from datasets import load_dataset
from tqdm import tqdm 
import random 


BASE_DIR=
sys.path.append(str(BASE_DIR))

class DataCOlllection:
    def __init__(self):
        self.data_dir=BASE_DIR/'AI_Chatbot'/'data'/'training_data'
        self.raw_dir=self.data_dir/'raw'
        self.processed_dir=self.data_dir/'processed'
    def collect_stack_overflow(self,num_samples=10000):
        try:
            dataset=load_dataset('koutch/stackoverflow_python',
                                 split='train',
                                 streaming=True)
            data=[]
            for i ,item in enumerate(tqdm(dataset,total=num_samples)):
                if i>=num_samples:
                    break
                if 'question' in item and 'answer' in item:
                    question=item['question'].strip()
                    answer=item['answer'].strip()

                    if 20<len(question)<200 and 20 <len(answer)<3000:
                        data.appen({
                            'source':'stackoverflow',
                            'question':question,
                            'answer':answer,
                            'tags':item
                        })
            output_file=self.raw_dir/'stackoverflow.jsonl'
            with open(output_file,'w',encoding=utf-8) as f:
                for item in data:
                    f.write(json.dumps(item,ensure_ascii=False)+'\n')
            print(f'collected date length: {len(data)}')
            print(f'data is saved to {output_file}')
            return data
    def create_converstional_dataset(self):

        conversations=[]
        file=self.raw_dir/'stackoverflow.jsonl'
        if file.exist():
            print("stack over flow data processing")

            with open(file,'r',encoding='utf-8') as f:
                f.read()            