# ChineseLyricsGenerator-Seq2Seq

This is an implement of Seq2Seq model for Chinese lyrics generating combined with website visualization (Django).

- Algorithm: Using Seq2Seq to generate lyrics by a given sentence. The code is in ./backend, which is forked and edited from https://github.com/dengxiuqi/Lyricist-torch.

  <img src="https://i.loli.net/2021/03/17/zsRJXTFKjmWevYk.png" alt="image-20210317015320194" style="zoom:50%;" />

- Web development: Using Django to develop the webpage. We can change the number of output sentences and the similarity index.

  <img src="https://i.loli.net/2021/03/17/vxiLpRWPISmYaMs.png" alt="image-20210317015648875" style="zoom: 67%;" />

## Dependencies

- Python == 3.6.7
- Django == 2.1.8
- torch==1.3.1
- torchtext==0.4.0
- jieba==0.39
- numpy==1.16.4
- seaborn==0.9.0
- matplotlib==3.1.1

## Usage

- Windows: Windows Terminal, cmd, PowerShell
- Linux

```
cd ChineseLyricsGenerator-Seq2Seq/
# you can also create a virtual environment here
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

- Open http://localhost:8000

## Result

- The training and validation accuracy is as below.

  <img src="https://i.loli.net/2021/03/17/aonTbH8QxvFJqMm.png" alt="image-20210317020142306" style="zoom: 67%;" />

- We can also analyze some examples:

  - <img src="https://i.loli.net/2021/03/17/jdLUzoyMhePIYaw.png" alt="image-20210317020413356" style="zoom:67%;" />
    - “我的机场把你留”一句，出自《新走西口》的“我在机场把你留”一句；
    - “可爱的英格鸟”出自《达那巴拉》中对于“可爱的英格鸟呀它在哪里落脚歌唱”、“可爱的英格鸟呀可在山顶放声歌唱”等句；
    - “我的天堂”、“你的天堂”几句，出自腾格尔经典歌曲《天堂》；
    - “这世界不会再有痛苦”出自《有你有我》中“明天不会有痛苦”、“世界的未来属于你我”两句的组合。
  - <img src="https://i.loli.net/2021/03/17/3AjV7UGL9YFONfq.png" alt="image-20210317020503555" style="zoom: 67%;" />
    - “我搅拌害羞的笑”一句，出自《甜甜的》中“加一个奶球我搅拌害羞”一句；
    - “将甜度调高后再牵手”、“你的爱太多” 两句，出自《甜甜的》中“将甜度调高后再牵手”、“你的爱太多”原句；
    - “像这样的生活”、“我爱你”两句，出自《简单爱》中“像这样的生活”、“我爱你”原句；
    - “没办法逃离你的魔法”一句，出自《手语》中“没办法逃离你的魔法”原句。

## References

- [1] Hongru Liang , Qian Li , Haozheng Wang , Hang Li , Jin-Mao Wei ,  Zhenglu Yang, AttAE-RL²: Attention based Autoencoder for Rap Lyrics  Representation Learning, Companion Proceedings of the The Web Conference  2018, April 23-27, 2018, Lyon, France
- [2] Eric Malmi, Pyry Takala, Hannu Toivonen, Tapani Raiko, and  Aristides Gionis. 2016. DopeLearning: A Computational Approach to Rap  Lyrics Generation. In Proceedings of the 22nd ACM SIGKDD International  Conference on Knowledge Discovery and Data Mining (KDD '16). ACM, New  York, NY, USA, 195-204.
- [3] Potash, Peter , Romanov, Alexey , Rumshisky, and Anna. 2015.  GhostWriter: Using an LSTM for Automatic Rap Lyric Generation. In  Proceedings of the 2015 Conference on Empirical Methods in Natural  Language Processing. Association for Computational Linguistics. Lisbon,  Portugal, 1919-1924.
- [4] https://blog.csdn.net/quiet_girl/article/details/84768821
- [5] https://github.com/Nana0606/lyrics_generation