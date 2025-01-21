---
layout: archive
title: "Professional coding projects"
header-img: "images/default-site-banner-image_v4.png"
permalink: /professional-code-projects/
author_profile: true
redirect_from:
  - /projects
---

{% include base_path %}

I have worked on a number of professional coding projects (or relevant personal side projects).  Links to their respective web/GitHub pages and brief descriptions are provided here.


[<u>Hunter's tools</u>](https://github.com/Lindt8/Hunters-tools) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14266969.svg)](https://doi.org/10.5281/zenodo.14266969)
======
### Collection of my general-purpose Python functions
This is a simple Python module containing a collection of functions that I have written and curated over the years spanning a large variety of purposes.  Broadly, the functions fit into three categories: general use (somewhat of a catchall), science and engineering (nuclear in particular), and visualization and plotting.

[<font color="#709E4A">[Documentation]</font>](http://lindt8.github.io/Hunters-tools/)


[<u>PHITS Tools</u>](https://github.com/Lindt8/PHITS-Tools) [![status](https://joss.theoj.org/papers/ef67acccadb883867ba60dc9e018ff70/status.svg)](https://joss.theoj.org/papers/ef67acccadb883867ba60dc9e018ff70) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14262720.svg)](https://doi.org/10.5281/zenodo.14262720)
======
### PHITS universal output parser/processor
This is a Python module containing a collection of functions that serve to automatically process tally output from the [<font color="#709E4A">PHITS</font>](https://phits.jaea.go.jp/) general purpose Monte Carlo particle transport code, seeking to be a (nearly) universal tally output parser/processor for both PHITS standard tally output and its tally "dump" output files.  PHITS Tools can be interfaced with via its command line interface (CLI), graphical user interface (GUI), or as an imported module within a Python script.  The module's main function outputs results both as a "dense" NumPy array as well as in a Pandas DataFrame, along with a metadata dictionary, while dump file results are returned as a list of NamedTuples and/or a Pandas DataFrame; all output can be saved as [pickle](https://docs.python.org/3/library/pickle.html) (or [dill](https://pypi.org/project/dill/)) files for easy later use. (*under ongoing development*)

[<font color="#709E4A">[Documentation]</font>](https://lindt8.github.io/PHITS-Tools/)


[<u>DCHAIN Tools</u>](https://github.com/Lindt8/DCHAIN-Tools) [![status](https://joss.theoj.org/papers/ef67acccadb883867ba60dc9e018ff70/status.svg)](https://joss.theoj.org/papers/ef67acccadb883867ba60dc9e018ff70) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14267236.svg)](https://doi.org/10.5281/zenodo.14267236)
======
### DCHAIN-PHITS output parser/processor and toolkit
This is a simple Python module containing a collection of functions which serve to automatically process output from the DCHAIN-PHITS code, the nuclide activation, buildup, burnup, and decay code which is coupled to and distributed with the [<font color="#709E4A">PHITS</font>](https://phits.jaea.go.jp/) general purpose Monte Carlo particle transport code.  In addition to trivializing DCHAIN output parsing and processing, it has a handful of other useful tools related to DCHAIN.  <!--(*under ongoing development*)-->

[<font color="#709E4A">[Documentation]</font>](https://lindt8.github.io/DCHAIN-Tools/)


[<u>SHAEDIT</u>](https://github.com/Lindt8/SHAEDIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1287860.svg)](https://doi.org/10.5281/zenodo.1287860)
======
### Space Hadron Accelerator Experiment Data Investigation Tool
This is a Jupyter notebook for conveniently viewing and comparing the data collected from the measurements of double-differential secondary particle yields from intermediate-energy hadrons incident on thick-targets. These experimental measurements were made at the NASA Space Radiation Laboratory on the Brookhaven National Laboratory campus.  


[<u>GCR-SpecGen</u>](https://github.com/Lindt8/GCR_SpecGen) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2573359.svg)](https://doi.org/10.5281/zenodo.2573359)
======
### Galactic Cosmic Ray Spectra Generator
This is a Jupyter notebook for conveniently generating GCR spectra using the [<font color="#709E4A">GCR model developed by Dr. Daniel Matthiä</font>](https://www.sciencedirect.com/science/article/pii/S0273117712005947?via%3Dihub).  The notebook allows for selection of which source ions are of interest and the desired level of solar modulation, either set manually or calculated automatically from a date or range of dates.  It yields a brief summary of the GCR spectra, text files containing each ion's full spectrum (formatted in a "raw" tabular form and as source cards ready for use in MCNP and PHITS simulations), and a plot showing the selected spectra under the specified level of solar modulation.

[<u>CLSQ2</u>](https://github.com/Lindt8/CLSQ2)
======
### Cumming’s Least Squares (version 2)
This is a modernized version of the 1962 Cumming’s Least Squares (CLSQ) Brookhaven Decay Curve Analysis Program, written in FORTRAN IV.  The original paper on it can be read [<font color="#709E4A"><u>here</u></font>](https://books.google.com/books?id=DZQrAAAAYAAJ&lpg=PR1&pg=PA25#v=onepage&q&f=false). CLSQ analyzes multicomponent decay curves by a least-squares procedure to iteratively identify the half-lives and abundances of the individual isotopes of a measured sample.  Its use at Oak Ridge National Laboratory (ORNL) had been limited to a few very old computers due to its age and recompilation issues; only a 16-bit compiled version of the code was in use at ORNL.  To make this code more accessible, I translated the original code from FORTRAN IV into Python 3.  Additionally, I added improvements in the input and output functionalities of CLSQ, making it much more user-friendly.  The new CLSQ code is used today at ORNL and is featured in a graduate course on isotope production at the University of Tennessee.  



<!-- <embed src="http://lindt8.github.io/files/CV_Hunter_Ratliff.pdf" width="650" height="1800" type='application/pdf'> -->
