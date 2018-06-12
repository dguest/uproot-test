#!/usr/bin/env python3

import uproot as up
from argparse import ArgumentParser
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigCanvas
from matplotlib.figure import Figure
from os import path, mkdir

def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('-o','--output-dir', default='plots')
    return parser.parse_args()

def run():
    args = get_args()
    roofile = up.open(args.input_file)
    outdir = args.output_dir
    if not path.isdir(outdir):
        mkdir(outdir)

    for name, hist in roofile.items():
        short_name = name.decode('utf-8').split(';')[0]
        print(f'drawing {short_name}')
        # set up canvas and figure
        fig = Figure(figsize=(5, 3))
        can = FigCanvas(fig)
        ax = fig.add_subplot(1,1,1)

        # add a plot
        vals, edges = hist.numpy
        centers = (edges[:-1] + edges[1:]) / 2
        ax.plot(centers, vals)
        ax.set_yscale('log')
        can.print_figure(f'{outdir}/{short_name}.pdf')

if __name__ == '__main__':
    run()
