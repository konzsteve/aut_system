#! /usr/bin/python3

import os
import sys

from .src.lsb_stegno import lsb_encode, lsb_decode
from .src.n_share import generate_shares, compress_shares

PATH = "media/image_otp/compress.png"
def _encode(txt, filename):
    generate_shares(lsb_encode(txt), filename)
    # this will therefore generate 2 shares where one will go to the user 
    # and and the other stored in the database.

def _decode(file_1, file_2):
    compress_shares(file_1, file_2)
    return lsb_decode("media/image_otp/compress.png")

