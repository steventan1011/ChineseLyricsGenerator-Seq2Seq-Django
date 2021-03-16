# ChineseLyricsGenerator-Seq2Seq

This is an implement of Seq2Seq model for Chinese lyrics generating combined with website visualization (Django).

## Dependencies

- Python = 3.6.7
- Django = 2.1.8
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
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

## References

- [1] Hongru Liang , Qian Li , Haozheng Wang , Hang Li , Jin-Mao Wei ,  Zhenglu Yang, AttAE-RL²: Attention based Autoencoder for Rap Lyrics  Representation Learning, Companion Proceedings of the The Web Conference  2018, April 23-27, 2018, Lyon, France
- [2] Eric Malmi, Pyry Takala, Hannu Toivonen, Tapani Raiko, and  Aristides Gionis. 2016. DopeLearning: A Computational Approach to Rap  Lyrics Generation. In Proceedings of the 22nd ACM SIGKDD International  Conference on Knowledge Discovery and Data Mining (KDD '16). ACM, New  York, NY, USA, 195-204.
- [3] Potash, Peter , Romanov, Alexey , Rumshisky, and Anna. 2015.  GhostWriter: Using an LSTM for Automatic Rap Lyric Generation. In  Proceedings of the 2015 Conference on Empirical Methods in Natural  Language Processing. Association for Computational Linguistics. Lisbon,  Portugal, 1919-1924.
- [4] https://blog.csdn.net/quiet_girl/article/details/84768821
- [5] https://github.com/Nana0606/lyrics_generation