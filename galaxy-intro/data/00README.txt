    bedtools intersect -a mm9_chrX_knownGenes.bed -b mm9_chrX_SNP128.bed -s -wo | cut -f 13- > mm9_chrX_SNP128_subset.bed 
    cat mm9_chrX_SNP128_subset.bed | head -10000 > mm9_chrX_SNP128_set.bed
    bedtools intersect -b mm9_chrX_knownGenes.bed -a mm9_chrX_SNP128.bed -s -v | head -10000 >> mm9_chrX_SNP128_set.bed 
