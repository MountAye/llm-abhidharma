import json
from pathlib import Path

def unpunctuated2json(file_in,file_ou):
    data = []
    with open(file_in,"r",encoding='utf-8') as f:
        content = f.read()
        content,_,chapter = content.rstrip("\n").rpartition("\n")
        entries = content.split("\n")
        for entry in entries:
            if not "问" in entry:
                continue
            QNAs = entry.split("。问")
            for qna in QNAs:
                qna = qna.rstrip("。")
                sep = "。答" if "。答" in qna else "。"
                question,_,answer = qna.partition(sep)
                data.append({
                    "instruction": f"{question}？",
                    "input": "",
                    "output": f"{answer}。（{chapter}）"
                })

    with open(file_ou,"w",encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    return None

if __name__ == "__main__":
    if not Path("data/JSON/大毘婆沙論").exists():
        Path("data/JSON/大毘婆沙論").mkdir()
    for path_in in Path("data/zh-CN/大毘婆沙論").glob("*[0-9].txt"):
        path_ou = Path("data/JSON/大毘婆沙論")/f"{path_in.stem}.json"
        unpunctuated2json(str(path_in),str(path_ou))
        print("finished reformat:",str(path_ou))
