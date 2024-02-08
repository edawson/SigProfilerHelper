import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num-replicates", dest="num_replicates", type=int, default=100, help="The number of seeds to generate (1 per replicate) [100].")
    parser.add_argument("-s", "--seed", dest="seed", type=int, default=None, help="Fixed seed value. If not passed, a random seed is used for each iteration [random].")
    parser.add_argument("--random-range", dest="random_range", default="0:10000", help="The range to use for random seeds, in the format min:max [0:10000] .")
    parser.add_argument("-o", "--output", dest="output", required=True, type=str, help="Output file [required].")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    bottom_end, top_end = [int(i) for i in (args.random_range).split(":")]
    with open(args.output, "w") as ofi:
        for i in range(1, args.num_replicates+1):
            seed = args.seed if args.seed is not None else random.randint(bottom_end, top_end)
            ofi.write(f"{i}\t{seed}\n")