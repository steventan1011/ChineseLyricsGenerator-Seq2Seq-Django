import sys
import random
import urllib.parse
sys.path.append("..")
from data import Lyric
from utils import model, attention_visualization

dataset = Lyric(batch_size=128, fix_length=32, target_vocab_size=10000)
net = model(dataset, model_name="pre_trained_50.pkl", train=False)

def generator(title, total_sentence=16):
    encoder_input = dataset.process(title)
    song = []
    for i in range(total_sentence):
        s = []
        output = net.predict(encoder_input)
        word = dataset.logist2word(output)[0]
        if word in dataset.itos[:50] + [s[0] for s in song[-3:]]:
            word = dataset.logist2word(output, topn=3)
            word = random.choice(word)
        next_input = dataset.stoi[word]
        s.append(word)
        while word != "<eos>":
            output = net.next(next_input)
            word = dataset.logist2word(output)[0]
            next_input = dataset.stoi[word]
            s.append(word)
        song.append(s[:-1])
        encoder_input = dataset.process("".join(s[:-1]))
    song = ["".join(s) for s in song]
    return song

if __name__ == '__main__':
    print({'abc':'qwe'})
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    input = urllib.parse.unquote(sys.argv[1])   # 输入语句
    num = sys.argv[2]   # 输出句子数目

    print({input: num})

    # result = generator(input, total_sentence=num)
    # print('输入：', input)
    # print('输出：')
    # n = 0
    # for i in result:
    #     n += 1
    #     if not n == num:
    #         print(i+'，\n')
    #     else:
    #         print(i+'。')

    # attention_visualization(dataset, net, "董明睿", "你的爱我的", file_name="1")

