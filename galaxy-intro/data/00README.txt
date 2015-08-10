#### Thu Apr 30 16:03:04 2015 ####
    bedtools intersect -a mm9_chrX_SNP128.bed.gz -b mm9_chrX_knownGenes_5000up.bed.gz | head -1000 > snps
    bedtools intersect -a mm9_chrX_SNP128.bed.gz -b mm9_chrX_knownGenes_5000up.bed.gz -v | awk -F '\t' '{if ($2>3200000 && $3 < 7458535) print $0}' >> snps 
    less snps | sort -k 2,2n > mm9_chrX_SNP128_set.bed
    rm snps 
