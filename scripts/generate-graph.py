"""
Constructs a graph via matplotlib from a CSV file.

"""

import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

parser = argparse.ArgumentParser(description='Constructs a graph via matplotlib from a CSV file.')
parser.add_argument('input', type=str, help='The filepath to the CSV file containing the graph data.')
parser.add_argument('--xscale', type=str, help='The x-axis scale to apply.', default='linear')
parser.add_argument('--yscale', type=str, help='The y-axis scale to apply.', default='linear')
args = parser.parse_args()

input_filepath = Path(args.input)
if input_filepath.exists() and input_filepath.is_file():
    x, y = np.loadtxt(input_filepath, delimiter=',', unpack=True)
    plt.plot(x, y, label='$\\frac{\pi(x)}{x/\ln(x)}$', color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xscale(args.xscale)
    plt.yscale(args.yscale)
    plt.legend(loc='upper right')
    plt.show()
else:
    print('Error: The provided CSV graph data file does not exist or is not a file.')
    