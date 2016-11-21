#!/usr/bin/env python3

import random
import string
import argparse
import numpy as np

from numpy.linalg import svd
from scipy.ndimage import imread

parser = argparse.ArgumentParser(description = "Convert an image into ascii art (Uses random ascii letters).")
parser.add_argument('image', help='Image to convert to ascii.')
parser.add_argument('-n',   nargs=1, default=[10],  type=int,   help='Number of ascii letters to use.')
parser.add_argument('--kx', nargs=1, default=[10],  type=int,   help='Window size (row dimension).')
parser.add_argument('--ky', nargs=1, default=[5],   type=int,   help='Window size (column dimension).')
parser.add_argument('--sx', nargs=1, default=[1],   type=int,   help='Repeat print sx times in the row dimension.')
parser.add_argument('--sy', nargs=1, default=[2],   type=int,   help='Repeat print sy times in the column dimension.')

args = vars(parser.parse_args())

image_path = args['image']
n  = args['n'].pop(0)
kx = args['kx'].pop(0)
ky = args['ky'].pop(0)
sx = args['sx'].pop(0)
sy = args['sy'].pop(0)

ascii_idx = np.array(random.sample(range(0, len(string.ascii_letters)), n))
ascii_lst = np.array(list(string.ascii_letters))[ascii_idx];

im = imread(image_path, flatten = True);
x = im.shape[0]
y = im.shape[1]

A = np.zeros(((x - kx + 1) * (y - ky + 1), kx * ky))

adx = 0;
for xdx in range(0, x - kx + 1):
  for ydx in range(0, y - ky + 1):
    vec = im[xdx:xdx+kx, ydx:ydx+ky].flatten()
    A[adx, :] = vec
    adx = adx + 1

u = np.mean(A, axis = 0);
for adx in range(A.shape[0]):
  A[adx, :] = A[adx, :] - u;

U, S, VH = svd(A, full_matrices=False)
VH = VH[0:n, :]

cor = VH.dot(A.T)

adx = 0;
for xdx in range(0, x - kx + 1):
  for ydx in range(0, y - ky + 1):
    vec = cor[:, adx]
    adx = adx + 1
    for idx in range(0, sx):
      print(ascii_lst[np.argmax(vec)] * sy, end="")
  print("\n", end="")
