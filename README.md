Material for the paper entitled "A diver operated stereo-video approach for characterizing reef fish spawning aggregations: the Galapagos Marine Reserve as case study" submitted to "Estuarine, Coastal and Shelf Science"
============================================================================================================================================================================================================================

This repository contains supplementary material for the reproducibiliy of computational studies performed in the article "A diver operated stereo-video approach for characterizing reef fish spawning aggregations: the Galapagos Marine Reserve as case study" written by:

* Etienne Rastoin
* Jordan Goetze
* Euan Harvey
* David Acuña-Marrero
* Pierre Fernique
* Pelayo Salinas de Leon

This article has been submitted to the "Estuarine, Coastal and Shelf Science" journal.
Here is the the citation formated as the bibtex standart.

```bibtex

  @article{RGHAFS20,
    author    = {Etienne Rastoin, Jordan Goetze, Euan Harvey, David Acuña-Marrero, Pierre Fernique, Pelayo Salinas de Leon},
    title     = {A diver operated stereo-video approach for characterizing reef fish spawning aggregations: the Galapagos Marine Reserve as case study},
    journal   = {Estuarine, Coastal and Shelf Scienc},
    year      = {2020},
    url       = {TODO},
  }
```

You can install required packages on your computer to reproduce this study.
In order to ease the installation of these packages on multiple operating systems, the **Conda** [package and environment management system](https://conda.io/docs/) is used.
Therefore if **Conda** is not installed on your computer, refers to this [page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) for more information (You have the choice between **Miniconda** and **Anaconda**, for this study we recommand to install the former one). You can look on this [page](https://www.datacamp.com/community/tutorials/installing-anaconda-windows) for a tutorial.
Once **Conda** is installed, to install the required packages, proceed as as follows:

1. Clone this repository,

   ```console
     git clone git://github.com/pfernique/wanda
   ```
2. Go to the repository directory

   ```console
     cd wanda
   ```

2. Create a **Conda** environment `RGHAFS20`,
      
   ```console
     conda activate
     conda install conda-build -y
     conda build recipe -c conda-forge -c defaults --override-channels --python=3.6
     conda env create -f environment.yml
   ```
     
3. Activate the **Conda** environment as advised in your terminal.

   ```console
     conda activate RGHAFS20
   ```
  
4. Launch the **Jupyter** notebook,

   ```console
     jupyter notebook RGHAFS20.ipynb
   ```
     
6. Execute the code corresponding to this study.
   This study is formatted as a **Jupyter** notebook, refers to this [page](https://jupyter.readthedocs.io/en/latest/index.html) for more information. You can look on this [page](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) for a tutorial.
