import os
import sys

sys.path.append(os.getcwd())

import pipeline as pl

if __name__ == '__main__':
    # TODO some visible artifacts (to be specifically, noise) exists currently, need to be fixed some day
    pl.cvt.images2gif('../results/20210625_171732')
    pl.cvt.images2video('../results/20210625_171732', '../results/video.mp4')
    pl.cvt.video2gif('../results/video.mp4', '../results/vid2gif.gif')
