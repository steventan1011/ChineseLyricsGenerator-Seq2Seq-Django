import torch
from data import Lyric
from config import fix_length, output_size
from utils import train


learning_rate = 5e-4
total_epoch = 100
batch_size = 32
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


if __name__ == "__main__":
    # singers = ["周杰伦", "张韶涵", "腾格尔", "邓紫棋", "张杰"]
    singers = ["邓紫棋"]
    for singer in singers:
        print("=" * 10)
        print("fine tune:" + singer)
        dataset = Lyric(batch_size=batch_size,
                        fix_length=fix_length,
                        singer=singer,
                        target_vocab_size=output_size,
                        device=device)
        train(dataset, learning_rate, total_epoch, device, save_epoch=10, log_step=50)
