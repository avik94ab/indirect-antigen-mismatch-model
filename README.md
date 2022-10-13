# indirect-antigen-mismatch-model

This package is a wrapper function for NetMHCIIPan4.0 that considers just donor HLA Class I derived peptides being presented by recipient HLA Class II molecule.

## Pre-requisite Python packages

All code was developed in Python 3.x, and you will need a Python notebook viewer (such as Jupyter), the SciPy and NumPy libraries (which should be standard), the Pandas library, the iedbtools to make full use of the notebooks. You can install the latter two as pip packages "pandas" and "iedb".


## Modules

The entire package is split in to three major modules:

1. code

   Contains source code in ~/code/api.py

   ```
   NetMHCIIPan4: generates binders/non-binders prediction

   fetchSequence: gets sequences from input UniProt ID

   generatePeptides: generates theoretical peptides of user-defined size from an input sequence 

   ```


2. notebooks

   Contains notebooks to test code written in ~/code/

   ```
  import sys
  sys.path.append('../code')
  import pandas as pd
  import math
  import api

   ```
   Sample protein sequence
   ```
   seq = api.fetchSequence("P35329")
   ```
   Generate peptides
   ```
   peptides = api.generatePeptides(seq, 15, 5)

   ```
   Generate DataFrame

       Rows: Peptides
       Columns: Alleles
       Values: 0->Non-binder, 1->Binder
   ```
   display(api.NetMHCIIPan4(peptides, threshold = 0.5))
   ```


3. data

   Will populate when data is available, real or synthetic



## Reference(s)

1. ***Improved prediction of MHC II antigen presentation through integration and motif deconvolution of mass spectrometry MHC eluted ligand data.*** Reynisson B, Barra C, Kaabinejadian S, Hildebrand WH, Peters B, Nielsen M **J Proteome Res 2020 Apr 30.**, doi: 10.1021/acs.jproteome.9b00874. PubMed: [32308001](https://services.healthtech.dtu.dk/service.php?NetMHCIIpan-4.0)
