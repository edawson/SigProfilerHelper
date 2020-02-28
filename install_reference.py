import argparse
from SigProfilerMatrixGenerator import install as genInstall

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reference", dest="ref", default="GRCh37", help="The name of the reference to install")

    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()
    try:
        genInstall.install(args.ref, rsync=False, bash=True)
    except:
        print("ERROR: reference installation failed")
        return 1
