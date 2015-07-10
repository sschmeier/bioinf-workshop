# Genome assembly tutorial
![Shell](images/shell_out0.png)

## 0. Learning outcomes
1. Being able to compute, investigate and evaluate the quality of sequence data from a sequencing experiment.
2. Being able to compute, interpret and evaluate a whole genome assembly.
3. Being able to judge the quality of a genome assembly.

## 1. Get the data
You can download the data-file [here](data/eli.low10paired.fastq.gz). I will also bring the data on a USB drive, please copy it onto your system should the download not work.

The data is a down-sampled (randomly selected) small portion of the original sequencing data-set. This has been done because the amount of data produced was too high for this exercises today. Also, the original data was paired-end data, thus we had two files, one for each end. The paired-data here was already combined into one file.

## 1.1 Investigate the data
Make use of your newly developed skills on the command-line to investigate the files in two folders.

**To-do:**
1. Unzip the data using `gzip`.
2. What kind of files are we dealing with?
3. How many sequence reads are in the file?

## 2. Quality assessment sequencing reads
To assess the sequence read quality of the Illumina run we make use of a program called [SolexaQA](http://solexaqa.sourceforge.net/). This was originally developed to work with Solexa data (since bought by Illumina), but long since working with Illumina data. It produces nice graphics that intuitively show the quality of the sequences. it is alos able to dynamically trim the bad quality ends off the reads.

From the webpage:

> SolexaQA calculates sequence quality statistics and creates visual representations of data quality for second-generation sequencing data. Originally developed for the Illumina system (historically known as "Solexa"), SolexaQA now also supports Ion Torrent and 454 data.

## 2.1 Download/install SolexaQA++ (hopefully not necessary)
Download [SolexaQA](http://solexaqa.sourceforge.net/) from the developer webpage [here](http://downloads.sourceforge.net/project/solexaqa/src/SolexaQA%2B%2B_v3.0.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsolexaqa%2Ffiles%2Fsrc%2F&ts=1410759802&use_mirror=iweb).

Note! Emergency link [here](apps/SolexaQA++_v3.0.zip).

```bash
unzip SolexaQA++_v3.0.zip
chmod a+x SolexaQA++_v3.0/Linux_x64/SolexaQA++
./SolexaQA++_v3.0/Linux_x64/SolexaQA++
# should now run the program
```

## 2.2 Understand SolexaQA++
SolexaQA++ has three modes that can be run. Type:

```bash
SolexaQA++
```

This results in:

![SolexaQA++](images/shell_out1.png)

The three modes are: `analysis`, `dynamictrim`, and `lengthsort`

`analysis` - the primary quality analysis and visualization tool. Designed to run on unmodified FASTQ files obtained directly from Illumina, Ion Torrent or 454 sequencers.

`dynamictrim` - a read trimmer that individually crops each read to its longest contiguous segment for which quality scores are greater than a user-supplied quality cutoff.

`lengthsort` - a program to separate high quality reads from low quality reads. LengthSort assigns trimmed reads to paired-end, singleton and discard files based on a user-defined length cutoff.

## 2.2 Run SolexaQA++ on untrimmed data
**To-do:**
1. Create a directory for the result-files --> `qa_untrimmed/`
2. Run SolexaQA++ with the untrimmed data, and submit result-directory `qa_untrimmed/`.
3. Investigate the result-files in `qa_untrimmed/`.

Hint! Should you not get 1 and/or 2 it right, try these commands [here](code/solexaqa1.txt).

Compare your results to these examples of a particularly bad run (taken from [http://solexaqa.sourceforge.net/](http://solexaqa.sourceforge.net/)). **What can we say about our data?**

![SolexaQA++ heatmap](images/solexaqa_quality_bad.png) ![SolexaQA++ heatmap](images/solexaqa_hist_bad.png) ![SolexaQA++ cumulative](images/solexaqa_cumulative_bad.png)

![SolexaQA++ heatmap](images/solexaqa_heatmap_bad.png)

## 2.3 Dynamic trim the data
Despite what you may have found out about the untrimmed data, it is a good idea to trim the data before further analyses.

**To-do:**
1. Create a directory for the result-files --> `qa_toTrimmed/`
2. Use SolexaQA++ to trim the reads based on quality and a probability cutoff of 0.01.

Hint! Should you not get 1 and/or 2 it right, try these commands [here](code/solexaqa2.txt).

## 2.4 Run SolexaQA++ on trimmed data
**To-do:**
1. Create a directory for the result-files --> `qa_trimmed/`.
2. Do the quality assessment again with the trimmed data-set.
3. Compare the results in `qa_trimmed/` to the untrimmed results in `qa_untrimmed/`.

Hint! Should you not get 1 and/or 2 it right, try these commands [here](code/solexaqa3.txt).

## 2.5 Download/install FastQC (hopefully not necessary)
Download [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) from the developer webpage [here](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.2.zip).

Note! Emergency link [here](apps/fastqc_v0.11.2.zip).

```bash
# Download file on the command-line
wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.2.zip
unzip fastqc_v0.11.2.zip
./FastQC/fastqc --help
# should now run the program
```

## 2.6 Understand FastQC
FastQC is a very simple program to run that provides similar and additional information to SolexaQA++.

From the webpage:

> FastQC aims to provide a simple way to do some quality control checks on raw sequence data coming from high throughput sequencing pipelines. It provides a modular set of analyses which you can use to give a quick impression of whether your data has any problems of which you should be aware before doing any further analysis.

The basic command looks like:

```bash
fastqc -o result-dir/ input-file.[txt/fa/fq] ...
```

- `-o result-dir/` is the directory where the result files will be written
- `input-file.[txt/fa/fq]` is the sequence file to analyze, can be more than one file.

The result will be a HTML page per input file that can be opened in a web-browser.

## 2.7 Run FastQC on the untrimmed and trimmed data
**To-do**
1. Create a directory for the results --> `fastqc/`
2. Run FastQC with both files
3. Compare the two result-files in a browser

Hint! Should you not get it right, try these commands [here](code/fastqc.txt).

Compare your results to these examples of a particularly bad run (taken from [http://www.bioinformatics.babraham.ac.uk/projects/fastqc/](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/).

![FastQC1](images/fastqc_bad1.png) ![FastQC2](images/fastqc_bad2.png) ![FastQC3](images/fastqc_bad3.png)

## 3. Whole genome assembly
![Assembly](images/assembly.png)

[Velvet](https://www.ebi.ac.uk/~zerbino/velvet/) is a de Bruijn graph‐based assembly program. It is developed with the aim of assembling very short reads like in our case.

From the webpage:

> Velvet is a de novo genomic assembler specially designed for short read sequencing technologies, such as Solexa or 454. Velvet currently takes in short read sequences, removes errors then produces high quality unique contigs. It then uses paired-end read and long read information, when available, to retrieve the repeated areas between contigs.

## 3.1 Download/install Velvet (hopefully not necessary)
Download [Velvet](https://www.ebi.ac.uk/~zerbino/velvet/) from the developer website [here](https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz).

Note! Emergency download-link [here](apps/velvet_1.2.10.tgz).

```bash
# unzip
gunzip velvet_1.2.10.tgz
# extract the archive
tar xvf velvet_1.2.10.tar
# change directory
cd velvet_1.2.10/
# compile program
make 'MAXKMERLENGTH=63'
# this will take a few seconds
# we have now two programs: velveth and velvetg
```

## 3.2 Understanding Velvet
Velvet uses two different programs sequentially to achieve the assembly. You have to use them one at a time. You should familiarize yourself with the structure of the program calls. Once you understand this it is very easy to change things around.

**`velveth`**

This program is a hashing program. It basically prepares your data for the assembler `velvetg`. An example program call looks like:

```bash
# Running velveth without parameters gives you a help page
./velveth
# Here a complete example call
./velveth results_directory/ 63 -fastq -shortPaired input_seqs.fastq
```

- `./velveth` the program inlcuding the full path where the program is located
- `result_directory/` the directory where you want the results to be saved
- `63` the kmer value
- `-fastq` specifies the input sequence-file type
- `-shortPaired` the type of the reads (here short paired reads)
- `input_seqs.fastq` the file-name of the input data

**`velvetg`** This program is the core  of velvet and the actual assembler. An example program call looks like this:

```bash
./velvetg result_directory/ -cov_cutoff 10 -exp_cov 30 -min_contig_lgth 500 -ins_length 300
```

- `./velvetg` the program including the full path where the program is located
- `result_directory/` the directory where you want the results to be saved
- `-cov_cutoff 10` removal of low coverage nodes AFTER tour bus or allow the system to infer it [do not worry about this]
- `-exp_cov 30` the expected coverage of unique regions or allow the system to infer it [do not worry about this]
- `-min_contig_lgth 500` the minimum size of contig to report back (to exclude tiny ones we only look at contigs >500bp)
- `-ins_length 300` expected distance between two paired-end reads in the respective short-read dataset

## 3.3 Run Velvet with untrimmed data
**To-do:**
1. Make sure you have the untrimmed data and you know where it is.
2. Create a directory for the results --> `velvet_untrimmed/`
3. Run velveth with the data `eli.low10paired.fastq`
4. Run velvetg

Hint! Should you not get it right, try these commands [here](code/velvet1.txt).

## 3.4 Run Velvet with trimmed data
**To-do:**
1. Make sure you have the trimmed data and you know where it is.
2. Create a directory for the results --> `velvet_trimmed/`
3. Run velveth with the data `qa_toTrimmed/eli.low10paired.fastq.trimmed`
4. Run velvetg

Hint! Should you not get it right, try these commands [here](code/velvet2.txt).

## 4 Evaluate assemblies
**To-do:**
1. Look at the Log files from trimmed and untrimmed assemblies.
2. Look at the stat.txt files from trimmed and untrimmed assemblies.
3. Look at the contigs.fa files of the trimmed and untrimmed assemblies.
4. What can we say about the the assemblies?
5. How does untrimmed and trimmed compare?
6. What can you say about the trimming procedure in light of assembling sequences?

## 4.1 Visualize assemblies
[Bandage](https://rrwick.github.io/Bandage/)

## 4.2 Assembly quality assessment
[Quast](http://quast.bioinf.spbau.ru/)

## 5 Genome annotation
Genome annotation pipeline [RAST](http://rast.nmpdr.org/)

Phage-specific annotation pipeline [PHAST](http://phast.wishartlab.com/)

## 5. What's next?
Next steps could include:
- map all reads to the "new" genome
- look at the aligned reads in a genome viewer
- predict genes in the "new" genome
- overlay gene information with aligned reads in the genome viewer
- etc.

**_File: index.md - Sebastian Schmeier - Last update: 2015-07-10_**
