Material for the paper entitled "TODO" and submitted to TODO
============================================================

This repository contains supplementary material for the reproducibiliy of computational studies performed in the article "TODO" written by:

* Etienne Rastoin
* Jordan Goetze
* Euan Harvey
* David Acuña-Marrero
* Pierre Fernique
* Pelayo Salinas de Leon

This article has been submitted to the "TODO" journal.
Here is the the citation formated as the bibtex standart.

.. code-block:: bibtex

  @article{RGHAFS20,
    author    = {TODO},
    title     = {TODO},
    journal   = {TODO},
    year      = {2020},
    url       = {TODO},
  }


You can install required packages on your computer to reproduce this study.
In order to ease the installation of these packages on multiple operating systems, the **Conda** `package and environment management system <https://conda.io/docs/>`_ is used.
Therefore is **Conda** is not installed on your computer, refers to this [page]() for more information.
Once **Conda** is installed, to install the required packages, proceed as as follows:

1. Clone this repository,

   .. code:: console
   
     git clone https://github.com/pfernique/RGHAFS20
     
2. Go to the repository directory

   .. code:: console

     cd RGHAFS20

2. Create a **Conda** environment :code:`RGHAFS20`,
      
   .. code:: console

     conda env create -f environment.yml

     
3. Activate the **Conda** environment as advised in your terminal.

   .. code:: console

     conda activate RGHAFS20

4. Launch the **Jupyter** notebook,

   .. code:: console
   
     jupyter notebook RGHAFS20.ipynb
     
     
6. Execute the code corresponding to this study.
   This study is formatted as a pre-executed **Jupyter** notebook, refers to this [page](https://jupyter.readthedocs.io/en/latest/index.html) for more information.