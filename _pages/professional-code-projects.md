---
layout: archive
title: "Professional coding projects"
permalink: /professional-code-projects/
author_profile: true
redirect_from:
  - /projects
---

{% include base_path %}

I have worked on a number of professional coding projects (or relevant personal side projects).  Links to their respective web/GitHub pages and brief descriptions are provided here.

[<u>SHAEDIT</u>](https://github.com/Lindt8/SHAEDIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1287860.svg)](https://doi.org/10.5281/zenodo.1287860)
======
### Space Hadron Accelerator Experiment Data Investigation Tool
This is a Jupyter notebook for conveniently viewing and comparing the data collected from the measurements of double-differential secondary particle yields from intermediate-energy hadrons incident on thick-targets. These experimental measurements were made at the NASA Space Radiation Laboratory on the Brookhaven National Laboratory campus.  


[<u>GCR-SpecGen</u>](https://github.com/Lindt8/GCR_SpecGen) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2573359.svg)](https://doi.org/10.5281/zenodo.2573359)
======
### Galactic Cosmic Ray Spectra Generator
This is a Jupyter notebook for conveniently generating GCR spectra using the [GCR model developed by Dr. Daniel Matthiä](https://www.sciencedirect.com/science/article/pii/S0273117712005947?via%3Dihub).  The notebook allows for selection of which source ions are of interest and the desired level of solar modulation, either set manually or calculated automatically from a date or range of dates.  It yields a brief summary of the GCR spectra, text files containing each ion's full spectrum (formatted in a "raw" tabular form and as source cards ready for use in MCNP and PHITS simulations), and a plot showing the selected spectra under the specified level of solar modulation.

[<u>CLSQ2</u>](https://github.com/Lindt8/CLSQ2)
======
### Cumming’s Least Squares (version 2)
This is a modernized version of the 1962 Cumming’s Least Squares (CLSQ) Brookhaven Decay Curve Analysis Program, written in FORTRAN IV.  The original paper on it can be read [<u>here</u>](https://books.google.com/books?id=DZQrAAAAYAAJ&lpg=PR1&pg=PA25#v=onepage&q&f=false). CLSQ analyzes multicomponent decay curves by a least-squares procedure to iteratively identify the half-lives and abundances of the individual isotopes of a measured sample.  Its use at Oak Ridge National Laboratory (ORNL) had been limited to a few very old computers due to its age and recompilation issues; only a 16-bit compiled version of the code was in use at ORNL.  To make this code more accessible, I translated the original code from FORTRAN IV into Python 3.  Additionally, I added improvements in the input and output functionalities of CLSQ, making it much more user-friendly.  The new CLSQ code is used today at ORNL and is featured in a graduate course on isotope production at the University of Tennessee.  



<!-- <embed src="http://lindt8.github.io/files/CV_Hunter_Ratliff.pdf" width="650" height="1800" type='application/pdf'> -->
