SigProfilerHelper
-----------------
Eric T. Dawson  
February 2020

## Introduction
SigProfilerHelper provides a set of python command line interface implementations
to the SigProfiler suite of tools (i.e., SigProfilerMatrixGenerator, SigProfilerExtractor, etc).

## Basic usage

To generate the SBS / ID / DNP matrices using SigProfilerMatrixGenerator and place them in a directory called "sigprof\§_input":
```
python generate_matrix.py -m <input.maf> -d sigprof_input
```

To run SBS96 analysis for 1 to 7 sigantures (1000 iterations each) on 16 threads:
```
time python scripts/run_sigprofiler.py -c 16 -i 1000 -s 1 -e 7 -t sigprof_input/output/SBS/PROJECT.SBS96.all -d <output_dir>
```

