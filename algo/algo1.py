import pandas
import time


def conv_slang(sentences, slang_dict):
    newsentences = ""
    if len(sentences) > 0:
        for word in sentences.split():
            new_word = word
            for i in range(len(slang_dict)):
                if new_word == slang_dict[i][0]:
                    new_word = slang_dict[i][1]
                    break
            newsentences = newsentences + new_word
    return newsentences


def run():
    start = time.time()
    slang_dict = pandas.read_csv('./daftar-slang-bahasa-indonesia.csv', header=None).to_numpy()
    dataset_qa = pandas.read_csv('./qa.csv', usecols=['question', 'answer'])
    for index, row in dataset_qa.iterrows():
        _ = conv_slang(row['question'], slang_dict)
        _ = conv_slang(row['answer'], slang_dict)
    with open(f'algo1_time.txt', 'w') as f:
        f.write(f'{time.time() - start}')
