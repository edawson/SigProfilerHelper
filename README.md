SigProfilerHelper
-----------------
Eric T. Dawson  
February 2020

## Introduction
SigProfilerHelper provides a set of python command line interface implementations
to the SigProfiler suite of tools (i.e., SigProfilerMatrixGenerator, SigProfilerExtractor, etc).

## Installation

```bash
pip install -r requirements.txt
```

## Basic usage

If you have not already installed a reference, you'll need to install one of the available references from SigProfiler
using the `install_reference.py` script. Here's how to install GRCh38 (GRCh37 is available in the same manner):

### Installing a reference genome:
```bash
python install_reference.py --ref GRCh38

```

### Generating SigProfiler Matrices
To generate the SBS / ID / DNP matrices using SigProfilerMatrixGenerator and place them in a directory called "sigprof\_input":
```
python generate_matrix.py -m <input.maf> -d sigprof_input
```

### Running SigProfilerExtractor
To run SBS96 analysis for 1 to 7 signatures (1000 iterations each) on 16 threads:
```
time python scripts/run_sigprofiler.py -c 16 -i 1000 -s 1 -e 7 -t sigprof_input/output/SBS/PROJECT.SBS96.all -d <output_dir>
```

### Full working example with public data:

```bash

## Install your reference
python install_reference.py --ref GRCh37

## Generate the matrix
python generate_matrix.py --maf data_mutations.maf --ref GRCh37 -d data_mutations_output --project Example

## Run sigprofiler
python run_sigprofiler.py -i data_mutations_output/output/SBS/Example.SBS96.all -d signatures -s 1 -e 3 -i 10
```
