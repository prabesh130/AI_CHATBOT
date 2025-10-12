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
                                   streaming=True)

            data = []
            for i, item in enumerate(tqdm(dataset, total=num_samples)):
                if i >= num_samples:
                    break
                title=item.get('title','').strip()
                question_body=item.get("question_body",'').strip()
                answer_body=item.get("answer_body",'').strip()
                
                if not question_body or not answer_body:
                    continue
                question=f'{title}\n{question_body}'.strip()
                answer=answer_body
                if 20 < len(question) < 200 and 20 < len(answer) < 3000:
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

    def create_conversational_dataset(self):
        conversations = []
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
        self.create_conversational_dataset()


if __name__ == "__main__":
    collector = DataCollection()
    collector.run_entire_pipeline()
