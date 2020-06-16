# SN19yvq

This repository contains the software necessary to replicate (most of) the analysis presented in [The Spectacular Ultraviolet Flash From the Peculiar Type Ia Supernova 2019yvq](https://ui.adsabs.harvard.edu/abs/2020arXiv200505972M/abstract) by Miller, Magee, Polin, Maguire, et al.

The main purpose is to allow the user to recreate the figures presented in the above study. One important note - the TARDIS analysis and figure (see Section 5.1 and Figure 7 in the above study) were completed by @MarkMageeAstro and the tools to recreate that specific work is not included here. Additionally, the models presented in 6.4 were created as part of [The peculiar Type Ia supernova iPTF14atg: Chandrasekhar-mass explosion or violent merger?](https://ui.adsabs.harvard.edu/abs/2016MNRAS.459.4428K/abstract) by Kromer, Fremling, Pakmor, Taubenberger, et al. As such, this model is not included here, but it can be downloaded from the [Heidelberg Supernova Model Archive](https://hesma.h-its.org/doku.php).

Beyond that, the repository is organized as follows: 
  *  [data/](https://github.com/adamamiller/SN19yvq/tree/master/data) contains the observations of SN 2019yvq, as well as the SNe that are compared to SN 2019yvq, and the models of SN 2019yvq used in Section 6 of the analysis  
  *  [plots/](https://github.com/adamamiller/SN19yvq/tree/master/plots) contains Jupyter notebooks to recreate every figure, but Figure 7, in the study
  *  [playground/](https://github.com/adamamiller/SN19yvq/tree/master/playground) contains analysis of SN 2019yvq
  *  [paper/](https://github.com/adamamiller/SN19yvq/tree/master/paper) includes the source TeX files necessary to compile the paper