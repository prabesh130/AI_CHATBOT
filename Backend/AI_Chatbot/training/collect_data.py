import os
import json
import sys
from pathlib import Path
from datasets import load_dataset
from tqdm import tqdm
import random

BASE_DIR = Path("D:/Projects/AI_Chatbot/Backend").resolve()
sys.path.append(str(BASE_DIR))


class DataCollection:
    def __init__(self):
        self.data_dir = BASE_DIR / 'AI_Chatbot' / 'data' / 'training_data'
        self.raw_dir = self.data_dir / 'raw'
        self.processed_dir = self.data_dir / 'processed'
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def collect_stack_overflow(self, num_samples):
        try:
            dataset = load_dataset('koutch/stackoverflow_python',
                                   split='train',
                                   )
            seen=set()
            data = []
            for i, item in enumerate(tqdm(dataset, total=num_samples)):
                if i >= num_samples:
                    break
                title=item.get('title','').strip()
                question_body=item.get("question_body",'').strip()
                answer_body=item.get("answer_body",'').strip()
                tags=item.get('tags',[])
                is_accepted=item.get('is_accepted_answer',False)
                score=item.get('score',0)

                if not question_body or not answer_body:
                    continue
                if not is_accepted and score<0:
                    continue
                key=hash(question_body+answer_body)
                if key in seen:
                    continue
                seen.add(key)
                question=f'{title}\n{question_body}'.strip()
                answer=answer_body
                if 20 < len(question) < 2000 and 20 < len(answer) < 3000:
                        data.append({
                            'source': 'stackoverflow',
                            'question': question,
                            'answer': answer,
                            'tags': item.get('tags', [])
                        })

            output_file = self.raw_dir / 'stackoverflow.jsonl'
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')

            print(f'Collected data length: {len(data)}')
            print(f'Data saved to {output_file}')
            return data
        except Exception as e:
            print(f"Error while collecting data: {e}")
    def collect_python_instruction_data(self,num_samples):
            try:
                dataset=load_dataset('iamtarun/python_code_instructions_18k_alpaca',split='train',streaming=True)
                data=[]
                for i ,item in enumerate(tqdm(dataset,total=num_samples)):
                    if i>=num_samples:
                        break
                    instruction=item.get('instruction', '').strip()
                    input_text=item.get('input','').strip()
                    output=item.get('output','').strip()
                    if not instruction or not  output:
                        continue
                    if len(instruction)>10 and len(output)>10:
                        data.append({
                            'source':'code_instuctions',
                            'instructions':instruction,
                            'input':input_text,
                            'output':output,
                            'type':'instruction',
                        })
                print(f"data downloading completed from code instruction{len(data)}")
                outputfile=self.raw_dir/'code_instructions.jsonl'
                with open(outputfile,'w',encoding='utf-8') as f:
                    for item in data:
                        f.write(json.dumps(item,ensure_ascii=False) + '\n')
                print(f"data collected from the python instructions")
                return data
            except Exception as e:
                print(f'error collecting code instruction: {e}')
                return []

    def create_conversational_dataset(self):
        conversations = []
        #process the stackoverflow data
        file = self.raw_dir / 'stackoverflow.jsonl'
        if file.exists():
            print("Processing Stack Overflow data...")

            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    data = json.loads(line)
                    conversations.append({
                        'prompt': data['question'],
                        'response': data['answer'],
                        'source': 'stackoverflow',
                        'metadata': {'tags': data.get('tags', [])}
                    })
        #process code instructions data
        file_c=self.raw_dir/ 'code_instructions.jsonl'
        if file_c.exists():
            print("processing the code instruction data")
        with open(file_c,'r',encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                instruction = data.get("instructions", "")
                input_text = data.get("input", "")
                output = data.get("output", "")

                prompt = instruction if not input_text else f"{instruction}\n\nInput:\n{input_text}"

                conversations.append({
                    'prompt': prompt,
                    'response': output,
                    'source': 'code_instructions',
                    'type': 'instruction'
                })

        import random
        random.shuffle(conversations)
        total = len(conversations)
        train_size = int(0.9 * total)
        val_size = int(0.05 * total)
        splits = {
            'train': conversations[:train_size],
            'val': conversations[train_size:train_size + val_size],
            'test': conversations[train_size + val_size:]
        }

        for split, split_data in splits.items():
            output_file = self.processed_dir / f'{split}.jsonl'
            with open(output_file, 'w', encoding='utf-8') as f:
                for item in split_data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')

        print("Dataset splits saved.")
        return splits

    def run_entire_pipeline(self):
        self.collect_stack_overflow(10000)
        self.collect_python_instruction_data(10000)
        self.create_conversational_dataset()


if __name__ == "__main__":
    collector = DataCollection()
    collector.run_entire_pipeline()
