# SBWA
`SBWA` is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. Based of the Burrows Wheelers Aligner Tool, which can be found here https://bio-bwa.sourceforge.net/

[Prerequisites](#prerequisites) | [Installation](#install) | [Basic Usage](#usage) |  [File formats](#formats)

<a name="prerequisites"></a>
## Prerequisites
`SBWA` requires the following python libraries to be installed:
- dnazip-bioinfo
- fastq
- minifasta

These packages can be installed with `pip`:
```
pip install dnazip-bioinfo fastq minifasta
```
Note: If you do not have root access, you can run the command above with additional options to install locally:
```
pip install --user dnazip-bioinfo fastq minifasta
```

<a name="install"></a>
## Installation
Once the required packages have been installed (please see [Prerequisites](#prerequisites)), install `SBWA` with the following commands:
```
git clone (https://github.com/Samgarci17/CSE-185)
cd Project
cd sbwa
python setup.py install
```
Note: if you do not have root access, you can run the command above with additional options to install locally:
```
python setup.py install --user
```

Note: If the SBWA command was not found, you may need to include the script installation path in your `$PATH` before calling spyglass. You can use `export PATH=$PATH:/home/<user>/.local/bin` to do so. 

<a name="usage"></a>
## Basic Usage 
The basic usage of `SBWA` is:
```
SBWA fasta.fa 
```

<a name="formats"></a>
## File Formats
### Input Files
#### `fasta.fa` 
A dna sequence in fasta format:

### Output Files

<a name="contributors"></a>
## Contributors 
This repository was generated by Samuel Garcia. I credit [`mypileup (CSE185 Project Demo)`](https://github.com/gymreklab/cse185-demo-project) for direction.
