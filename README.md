# indirect-antigen-mismatch-model

This package is a wrapper function for NetMHCIIPan4.0 that considers just donor HLA Class I derived peptides being presented by recipient HLA Class II molecule.

## Pre-requisite Python packages

All code was developed in Python 3.x, and you will need a Python notebook viewer (such as Jupyter), the SciPy and NumPy libraries (which should be standard), the Pandas library, the iedbtools to make full use of the notebooks. You can install the latter two as pip packages "pandas" and "iedb".


## Step-by-step instructions for how to install NetMHCIIpan

The installation for NetMHCIIpan is quite similar to netMHCpan.  There are only few differences like the name of the
folders to download and the name of the test files.

1. First, uncompress and untar the package
    1. Double click on the netMHCIIpan-4.0.linux.tar.gz or netMHCIIpan-4.0.darwin.tar.gz in your Downloads folder
        1. On Mac this will produce a directory ‘netMHCIIpan-4.0’.
        2. In Linux, the archive will open and you will see a folder inside called netMHCIIpan-4.0. Drag the folder out
        into your downloads directory.
2. Then, you need to download another file to complete the installation.
    1. Download the file
        1. Type `https://services.healthtech.dtu.dk/services/NetMHCIIpan-4.0/data.tar.gz` in your browser and hit enter
        2. This will start the download. If prompted, choose a location to save it (e.g. Downloads).
        3. Copy this file into the directory NetMHCIIpan-4.0 from step 1.
        4. Then, untar it as in step 1.
3. Now you’re good, you have all the required files for NetMHCIIpan4.0. Now you need to make some changes in the
netMHCIIpan program (or script) to indicate where your files will be stored.
4. To do this, you need to open the program script with a text editor (e.g. TextEdit).
    1. Go to Downloads/netMHCIIpan4.0/netMHCIIpan. Right-click it and choose "Open with" and open it with TextEdit
    or Text Editor or something similar.
5. Once the file opened, go under the section GENERAL SETTINGS: CUSTOMIZE TO YOUR SITE. There are 2 lines of code
to change to indicate where your files will go:
    1. Under the line `# full path to the NetMHCIIpan 4.0 directory (mandatory)`, indicate where the directory of
    netMHCpan-4.0 is located. Here is an example:
    2. setenv  NMHOME   <b>/Users/isasirois/Downloads/</b>netMHCIIpan-4.0
        1. You just need to change what is in bold, i.e. your personal location
        2. Save your change (cmd+S or ctrl+s)
    3. Then, under the line `# you need to determine where to store temporary files`, you will indicate where the files
    will be stored
    4. You need to make the following change
        1. setenv  TMPDIR  /scratch
into this: setenv  TMPDIR  $NMHOME/tmp
        2. Save your change (cmd+S or ctrl+s)
    5. Make sure the tmp folder exists, because the programs aren't smart enough to make it for you if it doesn't.
    So for the above example, you would create a folder called "tmp" inside your NetMHCIIpan directory.
        2. For example, go to ~/Downloads/netMHCpan-4.0 and create a folder there named tmp
6. You can now close the netMHCIIpan file. Now you need to copy it in the bin.
    1. Go to Finder and click on Go to.  In the black space, type: /usr/local/bin (hit enter).
    Copy your netMHCIIpan file that you just modified right there.  

###### Testing NetMHCIIpan

1. To be sure that the netMHCIIPan4.0 is well installed, you need to do a test. This is also indicated in the netMHCpan4.0.readme file under the third section called: ‘ In the ‘netMHCIIpan-4.0/test’ directory test the software:’
2. Open your Terminal (Go to Finder/Applications/Utilities/Terminal or via your Launchpad)
    1. You need to indicate to the terminal which directory it should open.  Type:
        1. `cd ~/Downloads/NetMHCIIpan-4.0/test` and hit enter.
            - Be sure to replace the path with the path to the NetMHCIIpan-4.0 test folder on YOUR computer.
            - Note there is a space between "cd" and "/"
3. Then type or copy-paste:
    1. `../netMHCIIpan -f example.fsa -a DRB1_0101 > example.fsa.myout` and hit enter.
    1. `../netMHCIIpan -f example.pep -inptype 1 -a DRB1_0101 > example.pep.myout` and hit enter.
    1. `../netMHCIIpan -f example.fsa -a H-2-IAb -s -u > example.fsa.sorted.myout` and hit enter.
    1. `../netMHCIIpan -f example.fsa -hlaseq DRB10101.fsa > example.fsa_hlaseq.myout` and hit enter.
    1. `../netMHCIIpan -f example.fsa -hlaseqA alpha.dat -hlaseq beta.dat > example.fsa_hlaseq_A+B.myout` and hit enter.
4. Go into the Test directory via your Finder and open the files with the .out and .myout extensions. At the top of each
file will be a lengthy header with all the parameters and settings which were used. Under that there will be a table. For
each pair of files (your test file and the one provided as a comparison, e.g. example.fsa.out and example.fsa.myout), the
values in the tables should be identical or nearly identical.

Congratulations!  NetMHCIIpan is installed and functional!

Adapted from: https://raw.githubusercontent.com/wiki/CaronLab/MhcVizPipe/Installation-of-third-party-software.md


## Reference(s)

1. ***Improved prediction of MHC II antigen presentation through integration and motif deconvolution of mass spectrometry MHC eluted ligand data.*** Reynisson B, Barra C, Kaabinejadian S, Hildebrand WH, Peters B, Nielsen M **J Proteome Res 2020 Apr 30.**, doi: 10.1021/acs.jproteome.9b00874. PubMed: [32308001](https://services.healthtech.dtu.dk/service.php?NetMHCIIpan-4.0)
