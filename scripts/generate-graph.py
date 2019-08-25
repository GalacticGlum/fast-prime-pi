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
parser.add_argument('--title', type=str, help='The title of the graph.')
parser.add_argument('--label', type=str, help='The label of the plotted curve.')
parser.add_argument('--colour', type=str, help='The colour of the graph.', default='blue')
parser.add_argument('--xlabel', type=str, help='The label on the x-axis.', default='x')
parser.add_argument('--ylabel', type=str, help='The label on the y-axis.', default='y')
parser.add_argument('--xscale', type=str, help='The x-axis scale to apply.', default='linear')
parser.add_argument('--yscale', type=str, help='The y-axis scale to apply.', default='linear')
parser.add_argument('--axhline', type=float, help='The horizontal axis line.')
parser.add_argument('--axhline-style', type=str, help='The style of the horizontal axis line.', default='-')
parser.add_argument('--axhline-colour', type=str, help='The colour of the horizontal axis line.', default='red')
parser.add_argument('--legend', dest='legend', help='Enable the legend.', action='store_true')
parser.add_argument('--legend-loc', type=str, help='The location of the legend.', default='upper right')
parser.add_argument('--export-latex', dest='export_latex', help='Export the graph as a LaTeX file using PGF/TikZ.', action='store_true')
parser.add_argument('--latex-output', type=str, help='The name of the exported LaTeX file.')
parser.add_argument('--no-preview', dest='preview', help='Disable the graph preview window.', action='store_false')
parser.set_defaults(legend=False, export_latex=False, preview=True)
args = parser.parse_args()

input_filepath = Path(args.input)
if input_filepath.exists() and input_filepath.is_file():
    if args.axhline is not None:
        plt.axhline(y=args.axhline, color=args.axhline_colour, linestyle=args.axhline_style)
    
    x, y = np.loadtxt(input_filepath, delimiter=',', unpack=True)
    plt.plot(x, y, label=args.label, color=args.colour)
    if args.title is not None:
        plt.title(args.title)
    
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    plt.xscale(args.xscale)
    plt.yscale(args.yscale)

    if args.legend:
        plt.legend(loc=args.legend_loc)
    
    if args.preview:
        if not args.export_latex:
            plt.show()
        else:
            print('Warning: Graph preview was enabled but it could not be displayed since LaTeX export was also enabled.' +
            ' Previewing and LaTeX exporting cannot both be enabled.')

    if args.export_latex:
        import tikzplotlib
        if args.latex_output is None:
            parser.error('--export-latex requires --latex-output.')

        output_path = Path(args.latex_output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        tikzplotlib.save(args.latex_output)
else:
    print('Error: Could not read graph data - The provided CSV graph data file does not exist or is not a file.')
    