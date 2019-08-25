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
parser.add_argument('--label', type=str, help='The label of the graph.')
parser.add_argument('--colour', type=str, help='The colour of the graph.', default='blue')
parser.add_argument('--xscale', type=str, help='The x-axis scale to apply.', default='linear')
parser.add_argument('--yscale', type=str, help='The y-axis scale to apply.', default='linear')
parser.add_argument('--axhline', type=float, help='The horizontal axis line.')
parser.add_argument('--axhline-style', type=str, help='The style of the horizontal axis line.', default='-')
parser.add_argument('--axhline-colour', type=str, help='The colour of the horizontal axis line.', default='red')
args = parser.parse_args()

input_filepath = Path(args.input)
if input_filepath.exists() and input_filepath.is_file():
    if args.axhline is not None:
        plt.axhline(y=args.axhline, color=args.axhline_colour, linestyle=args.axhline_style)
    
    x, y = np.loadtxt(input_filepath, delimiter=',', unpack=True)
    plt.plot(x, y, label=args.label, color=args.colour)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.xscale(args.xscale)
    plt.yscale(args.yscale)

    plt.legend(loc='upper right')
    plt.show()
else:
    print('Error: The provided CSV graph data file does not exist or is not a file.')
    