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
args = parser.parse_args()

input_filepath = Path(args.input)
if input_filepath.exists() and input_filepath.is_file():
    # with open(input_filepath) as input_csv:
    #     reader = csv.reader(input_csv)
        
    #     plt.ion()
    #     for row in reader:

    x, y = np.loadtxt(input_filepath, delimiter=',', unpack=True)
    plt.plot(x, y, label='$\\frac{\pi(x)}{x/\ln(x)}$', color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.show()
else:
    print('Error: The provided CSV graph data file does not exist or is not a file.')
    