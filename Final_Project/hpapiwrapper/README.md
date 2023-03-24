# hpapiwrapper

A Wrapper for the [House Plants API](https://rapidapi.com/mnai01/api/house-plants2) hosted on RapidAPI.

## Introduction 

This package provides a client for the House Plants API. Iw works with Python versions from 3.9+. 

The House Plants API provides users with access to data from over 300+ house plants along with some helpful information. 
***New Routes for the API to include additional GET options are in the works by the creator*** 

## Example Vignette 

You can find an example of how to use this client to analyze data and tell interesting stories in the [example.ipynb](https://github.com/QMSS-G5072-2022/Orchi_Tasnuva/blob/main/Final_Project/hpapiwrapper/docs/example.ipynb) file. 

## Installation

```bash
$ pip install hpapiwrapper
```

## Basic Tutorial

Below I provide a basic introduction to python code to query the House Plants API.
I suggest using the code in the order provided to get the best understanding of the data available. 

### Load Package and Package Dependencies
```python
import requests
import pandas as pd
import os
import json
from json import dumps, loads
from pandas import json_normalize
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

pip install hpapiwrapper

key = 'YOUR_KEY_HERE'

data = hpapiwrapper.get_houseplant_df(key)
```

### Get dataframe of all House Plant Data
```python
key = 'YOUR_KEY_HERE'

data = hpapiwrapper.get_houseplant_df(key)
```

### Get dataframe of all ids for a certain category of houseplants, such as 'Palm'
```python
data = hpapiwrapper.get_houseplant_ids(key, "Palm")
```

### Get dataframe of specific Houseplant using the API's search ByID option
You can find a list of all ids for a specific category using the get_houseplant_ids module
```python
hpapiwrapper.get_houseplant_byid(key,'9b97aef1-20a4-5620-af90-7d64dadb414e' )
```

### Get plot of potential Height vs potential Width of specific House Plants, such as for Palm plants
```python
hpapiwrapper.get_houseplant_byid(key,'Palm' )
```

### Get mean values of plant dimensions, temperature, and pot diameter. such as for Palm plants
```python
hpapiwrapper.get_houseplant_means(key, "Palm")
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`hpapiwrapper` was created by Tasnuva Orchi. It is licensed under the terms of the MIT license.

## Credits

`hpapiwrapper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
