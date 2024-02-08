import argparse
import sys
from os.path import dirname, isdir
from os import mkdir, getcwd
import shutil
from SigProfilerExtractor import sigpro as sig

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--table", dest="table", help="Input mutational catalog table (see README.md for format description).", required=True)
    parser.add_argument("-d", "--directory", dest="directory", help="A directory name in which to run analysis.", required=False, default=None, type=str)
    parser.add_argument("-r", "--reference",dest="genome", default="GRCh37", type=str)
    parser.add_argument("-s", "--start-sig-number",dest="start", type=int, default=1)
    parser.add_argument("-e", "--end-sig-number",dest="end", type=int, default=10)
    parser.add_argument("--nmf-replicates", dest="nmf_replicates", type=int, default=100)
    parser.add_argument("--min-iters",dest="min_iters", type=int, default=1000)   
    parser.add_argument("--max-iters",dest="max_iters", type=int, default=10000)
    parser.add_argument("-c", "--cpu", dest="cpu", type=int, default=-1, )
    parser.add_argument("-m", "--mtype",dest="mtype", type=str, default="96")
    parser.add_argument("-G", "--gpu", dest="gpu", action="store_true", default=False, help="Use an available GPU for acceleration.")

    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    if args.directory is None:
        current = getcwd()
        args.directory = current + "/" + "sigprofiler_sigs"
    try:
        if not isdir(args.directory):
            mkdir(args.directory)
    except:
        print("ERROR: creation of directory", args.directory, "failed. Please use the -d option to create a valid directory.")
    try:
        shutil.copyfile(args.table, args.directory + "/" + args.table)
    except:
        print("File copy failed.", args.table, args.directory + "/" + args.table)


    sig.sigProfilerExtractor("table",
        args.directory,
        args.table,
        minimum_signatures=args.start,
        maximum_signatures=args.end,
        min_nmf_iterations=args.min_iters,
        max_nmf_iterations=args.max_iters,
        cpu=args.cpu,
        context_type=args.mtype,
        gpu=args.gpu)
