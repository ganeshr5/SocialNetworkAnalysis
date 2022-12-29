
"""
Create a Social Network

References:
1] Mahdi Sadjadi (2017). arxivscraper: Zenodo. http://doi.org/10.5281/zenodo.889853
2] Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008
    
"""


# import the required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import arxivscraper
import collections


# Part 1: Data Collection
# Create scraper, scrape arxiv database, store output as Pandas data frame

scraper = arxivscraper.Scraper(category='physics:astro-ph', date_from='2017-04-24',date_until='2017-05-05')
output = scraper.scrape()
# create a pandas data frame
cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
df = pd.DataFrame(output, columns = cols)

