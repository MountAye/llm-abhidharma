import os
import json
from pathlib import Path
from datasets import Dataset
from transformers import AutoTokenizer

# Define data path
data_dir = "./data/JSON/"
save_dir = "./data/tokenized/"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("./models/Llama3-8B-hfl-instruct-v3")

"""Load text files and create a dataset."""
qa_data = {"question": [], "context": [], "answer": []}
for path_json in Path(data_dir).glob("*/*.json"):
    with open(str(path_json), "r", encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            question = entry.get("instruction", "")
            answer  = entry.get("output", "")
            if question and answer:
                qa_data["question"].append(question)
                qa_data["context"].append("")
                qa_data["answer"].append(answer)

dataset = Dataset.from_dict(qa_data)
tokenized = dataset.map(lambda x: tokenizer(), batched=True)


# Save processed dataset
dataset.save_to_disk("./data/tokenized")

print("Dataset saved successfully.")
