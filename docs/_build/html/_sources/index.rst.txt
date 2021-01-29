.. SphinxDemo documentation master file, created by
   sphinx-quickstart on Fri Jan 29 17:29:16 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SphinxDemo's documentation!
======================================

This is one try to understand how things work in Sphinx and document 
structure.

minimalisitic python documentation approach

steps 
#####
1. Install Sphinx

      pip install Sphinx

2. Either make a project dir

      mkdir SphinxDemo

   or go to project dir 

      cd SphinxDemo

3. Create a doc dir 

      mkdir docs

   and enter the dir 

      cd docs

4. Run command to quickstart sphinx

      sphinx-quickstart
   
   It will generate a basic structure of docs and 
   will create index.rst,conf.py etc. files. These are very
   important as from this point we will be updating in these file to provide next 
   configurations. for starters give all default values.
   

5. Go to conf.py and update 
   
   * for sphinx to understand the module path in which code is residing
         
         | import os
         | import sys 
         | sys.path.insert(0, os.path.abspath('..')) 

      ".." will tell sphinx to look for parent dir.

   * update extention to be used.
   
         extensions = [
            'sphinx.ext.napoleon',
            'sphinx_rtd_theme',
            'sphinx.ext.viewcode',
         ]

      we will be using napoleon to document python docstring and "rtd" read the docs 
      theme to document it.
   
   * install rtd theme

         pip install sphinx_rtd_theme

      and update this in conf.py
      
         html_theme = 'sphinx_rtd_theme'

   * and update this info in conf.py

         source_suffix = '.rst'

         master_doc = 'index'

6. Now go to project dir and write your python code and modules.
   use google docstring method to document classes and functions.

7. Go to docs and Run this command to generate rst pages.

         sphinx-apidoc -o . ../

   for all the modules.

8. Update index.rst by looking at this page's raw text to understand the 
   requirement.

9. go to docs and run this command to generate html pages.

         make html
   
Note
****
If you want to host it on github-pages use an empty ".nojekyll" file and add it to the docs dir.
This will tell github that we are not using jekyll to host our pages.


Contents
========
.. toctree::
   :maxdepth: 2

   modules
   main 
   dataload

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
