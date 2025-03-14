from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

if __name__=="__main__":
    base_model_path = "/data/wangshixing/LLMs/llama3-abdm/models/Llama3-8B-hfl-instruct-v3"
    adaptor_path = "/data/wangshixing/LLMs/Chinese-LLaMA-Alpaca-3/models/abdm_sft"
    merged_path = "/data/wangshixing/LLMs/llama3-abdm/models/Llama3-abhidharma-zh_CN"

    model = AutoModelForCausalLM.from_pretrained(base_model_path)
    model = PeftModel.from_pretrained(model, adaptor_path)
    model = model.merge_and_unload()
    model.save_pretrained(merged_path)
