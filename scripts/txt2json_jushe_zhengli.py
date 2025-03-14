import json
from pathlib import Path

def punctuated2json(file_in,file_ou,book):
    data = []
    with open(file_in,"r",encoding='utf-8') as f:
        content = f.read()
        chapter,_,content = content.partition("三藏法师玄奘奉诏译\n")[2].partition("\n")
        preface,_,content = content.partition("颂曰：\n")
        content,_,_ = content.rpartition("\n")[0].rpartition("\n")
        data.append({
            "instruction": f"《{book}》的《{chapter}》这一章讲了什么？",
            "input": "",
            "output":      f"原文对这一章的总结为：{preface.replace('\n','')}"
        })
        entries = content.split("颂曰：\n")
        for entry in entries:
            instruction,_,output = entry.partition("论曰：")
            data.append({
                "instruction": f"“{instruction.replace('\n','')}”应该如何理解？", 
                "input": "",
                "output":      f"这几句是《{book}·{chapter}》中的颂，原文对此的解读是：“{output.replace('\n','')}”"
            })
        oneline = content.replace("\n","")
        QnAs = oneline.split("。")
        for qna in QnAs:
            if not "？" in qna:
                continue
            question,_,answer = qna.rpartition("？")
            if question == "所以者何":
                data[-1]["output"] = data[-1]["output"].replace(f'（{book}·',f'所以者何？{answer}。（{book}·')
                continue
            if question == "云何":
                data[-1]["output"] = f"{data[-1]["output"]}云何？{answer}。"
                continue
            data.append({
                "instruction": f"{question}？", 
                "input": "",
                "output":      f"{answer}。（{book}·{chapter}）"
            })

    with open(file_ou,"w",encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    return None

if __name__ == "__main__":
    if not Path("data/JSON/俱舍论").exists():
        Path("data/JSON/俱舍论").mkdir()
    for path_in in Path("data/zh-CN/俱舍论").glob("*[0-9].txt"):
        path_ou = Path("data/JSON/俱舍论")/f"{path_in.stem}.json"
        punctuated2json(str(path_in),str(path_ou),"俱舍论")
        print("finished reformat:",str(path_ou))

    if not Path("data/JSON/顺正理论").exists():
        Path("data/JSON/顺正理论").mkdir()
    for path_in in Path("data/zh-CN/顺正理论").glob("*[0-9].txt"):
        path_ou = Path("data/JSON/顺正理论")/f"{path_in.stem}.json"
        punctuated2json(str(path_in),str(path_ou),"顺正理论")
        print("finished reformat:",str(path_ou))