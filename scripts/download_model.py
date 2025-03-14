from huggingface_hub import snapshot_download
import os

# Define the path to store models
save_path = "./models/Llama3-8B-hfl-instruct-v3"
os.makedirs(save_path, exist_ok=True)

# Download model from Hugging Face Hub
snapshot_download(
    repo_id="hfl/llama-3-chinese-8b-instruct-v3",  # Replace with your model
    local_dir=save_path
)

print(f"Model downloaded to {save_path}")
