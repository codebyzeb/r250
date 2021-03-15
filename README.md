# R250 Non-Standard NLP Project

This repository contains the report and scripts produced for my project as part of the R250 course on Non-Standard NLP, offered by Part III of the Computer Science Tripos at Cambridge University.

## Report

The report can be found at `report.pdf`.

## Language Model

The language model used for this report was too large to upload to github. It was produced with the [KenLM Langage Model Toolkit](https://kheafield.com/code/kenlm/)
using the Wiki_zh subsection of [ClueCorpusSmall](https://github.com/CLUEbenchmark/CLUECorpus2020). The corpus was pre-processed (combining all files) and tokenized using the [Stanford Chinese Segmenter](https://nlp.stanford.edu/software/segmenter.shtml) to produce a file `out.txt`. This file was then fed to kenlm to produce the language model:

  ./kenlm/build/bin/lmplz -o 5 -T /tmp <out.txt >out.arpa
  ./kenlm/build/bin/build_binary out.arpa out.klm

## Surprisal and Mutual Information Calculation

To add new surprisal and mutual information values to the code-switching dataset used for the project, I wrote a script that uses this language model to estimate probabilities `calculate_surprisal.py`. This requires checking out the code-switching dataset to append these features:

  git checkout https://github.com/lfang1/CodeSwitchingResearch.git
  python calculate_surprisal.py
  
Note that this also requires the `kenlm` python library to be installed. 

## Analysis

The `stat_analysis.R` file contains all the analysis run by this project. It is taken from the dataset's [repository](https://github.com/lfang1/CodeSwitchingResearch/), with additions to analyse the newly calculate features. 
