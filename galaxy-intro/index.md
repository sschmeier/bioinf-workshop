# Introduction to Galaxy
[![Galaxy](img/galaxyLogo.png)](http://galaxyproject.org/)
## 1. Overview
In this tutorial we will learn how to use the excellent tool [Galaxy](http://galaxyproject.org/) to analyze biological data [Galaxy](http://galaxyproject.org/) allows you to make use of a number of tools in a simple to use graphical interface (more on that in a moment). A user is thus not required to use any of the tools on the command-line (even though many of the integrated tools were developed for the command-line in the first place) but can fully use and control the integrated tools with the mouse pointer. On the flip side, it also allows developers of tools to easily integrate them into a graphical user interface system that is already known to many scientists and thus make the tools available for the research community. 

Another big advantage of [Galaxy](http://galaxyproject.org/) is that every step of the analysis is monitored and accessibly via a history. This makes reproducible research not only a possibility but also easy to facilitate. Steps from the history can be packaged into work-flows, which can be reused with  different data or shared with other scientists. [![GCC2015](img/gcc.png)](http://gcc2015.tsl.ac.uk/)
[Galaxy](http://galaxyproject.org/) enjoys a large and growing user and developer base, which is evident by its own yearly [conference](http://gcc2015.tsl.ac.uk/) and participation in [Google Summer of Code](https://wiki.galaxyproject.org/Develop/GSOC/2015). It is relatively easy to find help should one need it, e.g. through their [mailing list](http://wiki.galaxyproject.org/MailingLists) or [wiki](http://wiki.galaxyproject.org/). Also, many commercial companies that provide next-generation sequencing services, provide Galaxy instances to analyze your data (e.g.  we at [New Zealand Genomics Limited](http://nzgenomics.co.nz) have a full fledged installation on our infrastructure ready for scientist to be used).

### Important links
  * [__Wiki__](http://wiki.galaxyproject.org/)
  * [__Mailing lists__](http://wiki.galaxyproject.org/MailingLists)
  * [__Other learning material__](https://wiki.galaxyproject.org/Learn)

## 2. How to get access to Galaxy
There many option available to either give [Galaxy](http://galaxyproject.org/) a test run or do a full analysis with it. There is a ever growing list of public servers [available](https://wiki.galaxyproject.org/PublicGalaxyServers), some of which might have certain restrictions, e.g. maximum data-file size, etc. The standard server is accessible at: [https://usegalaxy.org/](https://usegalaxy.org/)

You can start your own [Galaxy](http://galaxyproject.org/) instances on [Cloud](https://wiki.galaxyproject.org/Cloud) infrastructure, e.g. [Amazon Cloud Services](http://aws.amazon.com/), should you have bigger analysis needs that you want to perform in the cloud.

You can [download](https://wiki.galaxyproject.org/Admin/GetGalaxy) and install [Galaxy](http://galaxyproject.org/) on you own machine or server, even integrating a computer cluster on the back-end.

You can install [BioLinux](http://environmentalomics.org/bio-linux/) on you own machine or run [BioLinux](http://environmentalomics.org/bio-linux/) as a virtual machine and you are set as well, as [Galaxy](http://galaxyproject.org/) comes pre-installed on [BioLinux 8](http://environmentalomics.org/bio-linux/).

## 3. The user interface

![](img/g_base1.png)

Hint! Click on the Galaxy screenshots to get a bigger version!

There are 3 areas of interest for now:

  1. The links to the tools that the Galaxy installation contains (this can very from Galaxy instance to instance).
  2. The working area, where we can change parameters of the tools that we want to use for some of our data.
  3. The history panel that contains all the data and steps we performed on the data.

![](img/g_base2.png)

## 4. A simple task
We want to know for upstream regions of human genes of a particular chromosome the transcription factor binding sites (TFBSs) that bind in those locations. We will do this through some ChiP-seq data. The tasks at hand are:

  1. Get the gene locations
  2. Get the upstream regions of the genes
  3. Get the ChIP-seq data we are interested in
  4. Overlap the TFBS sites with the upstream regions
  5. Visualize the results in a genome browser

## 5.  Uploading your own data
Download the following file to your computer: [mm9_chrX_SNP128_set.bed](data/mm9_chrX_SNP128_set.bed). The file is in [bed-format](http://genome.ucsc.edu/FAQ/FAQformat.html#format1), a simple tab-separated file containing 6 columns: **chromosome, start, stop, name, score, strand**. It can have more columns, though.

Hint! Data file: [mm9_chrX_SNP128_set.bed](data/mm9_chrX_SNP128_set.bed)

  1. On you Galaxy window go to the upper left in the tools area and click on **"Get data"**. A subsection of **"Get data"** will open and show available option for you to get data into the Galaxy system.
  2. Choose **"Upload File from your computer"**. 

![](img/g_loadFILE1.png)

 1. An additional window should open that allows you to select the your file.
 2. Here you can specify the species, given that we are looking at mouse data from mm9 set it to the same.

![](img/g_loadFILE2.png)

Once you hit the **Start** button, your data/analysis will be uploaded. In your history your data goes through three stages indicated by three different colors:

  1. Grey: Scheduled for uploading/running
  2. Yellow: Currently running
  3. Green: Dataset/analysis is ready

![](img/g_base_history1.png)

  1. Click on the filename and you get some information about the data.
  2. Here you will see information like how many regions (lines) are in the file, the format and genome
  3. Here you can download the data, get even more information about the data and run the job again (here it would reload the data)

![](img/g_base_history2.png)

Within the history panel and your data set there are several buttons of importance. The first one which looks like an eye will display you data in the working area.

![](img/g_base_history3.png)

  1. The second button will allow you to edit your data
  2. You can change the file-name
  3. Change the assignment of column numbers to particular properties
  4. and finally save your changes.

![](img/g_base_history4.png)

The last button can delete your data/analysis again from the history panel.

![](img/g_base_history5.png)

## 6. Loading data from web resources
Now we are focusing on getting some data from the [UCSC table browser](https://genome.ucsc.edu/cgi-bin/hgTables). Many people UCSC were quite busy integrating lots of data and there is plenty of data available especially for mammalian model systems.

  1. On you Galaxy window go to the upper left in the tools area and click on **"Get data"**. A subsection of **"Get data"** will open and show available option for you to get data into the Galaxy system.
  2. Click on **"UCSC Main table browser"**. This will open the  [UCSC table browser](https://genome.ucsc.edu/cgi-bin/hgTables) in your Galaxy working area.
  3. Here you can choose the genome that you want the data from, we will choose mm9
  4. Here you can choose the kind of data that you which to download from the particular genome, we will choose here the **"Genes and Gene Prediction group"** and the **"UCSC Genes"** as well as the **"knownGene"** table. The **"describe table schema"** button will get you to aanother webpage that describes the data within the **"knownGene"** table. Feel free to explore.
  5. Here you can chose if you which to download data from the whole genome or a subportion of it. We will choose here only data from **"chrX"** type thi in the field and hit **"lookup"**
 button which will complete the start and stop coordinates of the genome.
  6. Here we can specify the output-format. It is important here to make sure that the **"Send output to Galaxy"** choice is selected . Also, we want BED -format again.
  7. After we are finsihed we can hit the **"get output"** button, after which our requested data will be loaded into the Galaxy interface.
  
![](img/g_loadUCSC1.png)

Finally, your data should appear in the right hand side history panel.




## 7. Loading shared data


## 8. Another note on the history

You are able to create an account on the public Galaxy web-server. Once done, you will be able to save histories and fetch you old histories back. 
