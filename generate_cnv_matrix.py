import argparse
from os.path import dirname, isdir, basename
from os import mkdir, getcwd
import shutil
from SigProfilerMatrixGenerator.scripts import CNVMatrixGenerator as scna

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="maf", help="MAF file from which to extract matrix.", required=True)
    parser.add_argument("-f", "--file-type", dest="file_type", type=str, help="The file type (i.e., CNV caller).", required=True)
    parser.add_argument("-p", "--project", dest="project", default="PROJECT", help="Project name for output [PROJECT] .")    
    parser.add_argument("-o", "--output", dest="output", help="The output path (should be a directory).", required=True)
    
    return parser.parse_args()


if __name__ == "__main__":
    
    args = parse_args()
    
    # if args.directory is None:
    #     current = getcwd()
    #     args.directory = current + "/" + "sigprofiler_input"
    # try:
    #     if not isdir(args.directory):
    #         mkdir(args.directory)
    # except:
    #     print("ERROR: creation of directory", args.directory, "failed. Please use the -d option to create a valid directory.")

    # try:
    #     shutil.copyfile(args.maf, args.directory + "/" + basename(args.maf))
    # except:
    #     print("File copy failed.", args.maf, args.directory + basename(args.maf))
        
        
    scna.generateCNVMatrix(args.file_type, args.input, args.project, args.output)



# >>from SigProfilerMatrixGenerator.scripts import CNVMatrixGenerator as scna
# >>file_type = "BATTENBERG"
# >>input_file = "./SigProfilerMatrixGenerator/references/CNV/example_input/Battenberg_test.tsv" #example input file for testing
# >>output_path = "/Users/azhark/iCloud/dev/CNVMatrixGenerator/example_output/"
# >>project = "Battenberg_test"
# >>scna.generateCNVMatrix(file_type, input_file, project, output_path)