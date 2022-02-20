import pandas
import time


def conv_slang(sentences, slang_dict):
    newsentences = ""
    if len(sentences) > 0:
        for word in sentences.split():
            new_word = dynamic_switcher(slang_dict, word)
            if new_word:
                newsentences += new_word
                continue
            newsentences += word
    return newsentences


def dynamic_switcher(data, key):
    return data.get(key, None)


def run():
    slang_dict = {
        k: v

        for k, v in pandas.read_csv(
            "./daftar-slang-bahasa-indonesia.csv", header=None
        ).to_numpy()
    }
    dataset_qa = pandas.read_csv("./qa.csv", usecols=["question", "answer"])
    start = time.time()
    for _, row in dataset_qa.iterrows():
        _ = conv_slang(row["question"], slang_dict)
        _ = conv_slang(row["answer"], slang_dict)
    with open(f"algo2_time.txt", "w") as f:
        f.write(f"{time.time() - start}")
