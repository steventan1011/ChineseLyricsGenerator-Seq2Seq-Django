from django.shortcuts import render
from django.http import JsonResponse
import re
import random
import urllib.parse

from backend.data import Lyric
from backend.utils import model, attention_visualization
print("123456789")

dataset = Lyric(batch_size=128, fix_length=32, target_vocab_size=10000)
net_zhoujielun = [model(dataset, model_name="周杰伦_"+str(i)+"0.pkl", train=False) for i in range(1, 6)]
net_tengeer = [model(dataset, model_name="腾格尔_"+str(i)+"0.pkl", train=False) for i in range(1, 6)]
net_zhangshaohan = [model(dataset, model_name="张韶涵_"+str(i)+"0.pkl", train=False) for i in range(1, 6)]
net_dengziqi = [model(dataset, model_name="邓紫棋_"+str(i)+"0.pkl", train=False) for i in range(1, 6)]
net_zhangjie = [model(dataset, model_name="张杰_"+str(i)+"0.pkl", train=False) for i in range(1, 6)]
net = {'zhoujielun': net_zhoujielun, 'tenggeer': net_tengeer, 'zhangshaohan': net_zhangshaohan, 'zhangjie': net_zhangjie, 'dengziqi': net_dengziqi}


def generator(title, total_sentence=16, singer='zhoujielun', likely_extent='无偏好'):
    encoder_input = dataset.process(title)
    likely_dict = {'最不相似': 0, '很不相似': 1, '推荐': 2, '很相似': 3, '最相似': 4}
    likely = likely_dict[likely_extent]
    song = []
    for i in range(total_sentence):
        s = []
        output = net[singer][likely].predict(encoder_input)
        word = dataset.logist2word(output)[0]
        if word in dataset.itos[:50] + [s[0] for s in song[-3:]]:
            word = dataset.logist2word(output, topn=3)
            word = random.choice(word)
        next_input = dataset.stoi[word]
        s.append(word)
        while word != "<eos>":
            output = net[singer][likely].next(next_input)
            word = dataset.logist2word(output)[0]
            next_input = dataset.stoi[word]
            s.append(word)
        song.append(s[:-1])
        encoder_input = dataset.process("".join(s[:-1]))
    song = ["".join(s) for s in song]
    return song


# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):
    global net
    keywords = request.GET.get('keywords')
    keywords_list = re.split("、", keywords)
    if len(keywords_list) > 5:
        keywords_list = keywords_list[:5]
    singer = request.GET.get('singer')
    generate_length = int(request.GET.get('generate_length'))
    likely_extent = request.GET.get('likely_extent')
    model = generator(title="".join(keywords), total_sentence=generate_length, singer=singer, likely_extent=likely_extent)
    result = {"keywords": keywords_list, "singer": singer,
              "generate_length": generate_length, 'likely_extent': likely_extent, "content": model}

    return JsonResponse(result)
    # return render(request, 'response_lyrics.html', {"result":model})

def timeline(request):
    return render(request, 'timeline.html')

def lyrics(request):
    return render(request, 'lyrics_response.html')
# if __name__ == "__main__":
#     model = search(1)
#     print(model)

