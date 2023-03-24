import requests
import pandas as pd
import os
import json
from json import dumps, loads
from pandas import json_normalize
import seaborn as sns
import matplotlib.pyplot as plt
import pytest


#Function 1
#Function for getting houseplant data in the form of a dataframe  
def get_houseplant_df(key):
    """
    This function will provide data gathered from the House Plant API
    in the form of a dataframe. Users can use this dataframe for further analysis.

    Parameters
    ----------
    key: API Key

    Returns
    -------
    Returns a dataframe. 

    Examples
    --------
    >>> from hpapiwrapper import hpapiwrapper
    >>> hpapiwrapper.get_houseplant_df(key)
    Output: A Dataframe with 355 rows and 47 columns.
    """    
    def get_df1(key):
        url = "https://house-plants2.p.rapidapi.com/"
        headers = {"X-RapidAPI-Key": key ,
           "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
        response = requests.request("GET", url, headers=headers) 
        data = response.json() 
        return data 
    
    data_df = json_normalize(get_df1(key))
    return data_df  

#Function 2
#Function to get all id values for specific plant cateogries if you want to use the id search aspect of the api instead 
def get_houseplant_ids(key, category):
    """
    This function will allows users to get the information they need in order to
    utilize the other search option for this API. 
    Since the API allows you to search by plant id,
    this function can be used to get a dataframe with all plant id's for 
    a specific category of plants. 

    Parameters
    ----------
    key: API Key
    category: Select from the following options: ['Dracaena', 'Palm',
    'Anthurium', 'Other', 'Aglaonema', 'Hanging',
    'Bromeliad', 'Spathiphyllum', 'Flower', 'Aralia', 'Ficus',
    'Sansevieria', 'Foliage plant', 'Dieffenbachia', 'Philodendron',
    'Cactus & Succulent', 'Schefflera', 'Topiairy', 'Fern', 'Grass',
     'Ground Cover']

    Returns
    -------
    Returns a dataframe with all id's of plants from a certain category.  

    Examples
    --------
    >>> from hpapiwrapper import hpapiwrapper
    >>> hpapiwrapper.get_houseplant_ids(key, 'Palm')
    Output: A Dataframe with all id's for only Palm plants.
    """  
    def get_houseplant_df2(key):

            def get_df2(key):
                url = "https://house-plants2.p.rapidapi.com/"
                headers = {"X-RapidAPI-Key": key ,
                   "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
                response = requests.request("GET", url, headers=headers) 
                data = response.json() 
                return data 

            data_df = json_normalize(get_df2(key))
            return data_df

    data_df = get_houseplant_df2(key)
    ids = data_df[['id', 'Categories']].copy()
    df_catid = ids.loc[ids['Categories'] == category]
    return df_catid

#Function 3
#Using the results of the earlier function you can then more easily use the version of the API that searches using id values 
def get_houseplant_byid(key, ID):
    """
    This function will allows users to look up specific house plant samples
    using their associated id's. 

    Parameters
    ----------
    key: API Key
    ID: The associated id for a plant, this can be found using the 
    get_houseplant_ids() function

    Returns
    -------
    Returns a dataframe with all data associated with the specified plant id.  

    Examples
    --------
    >>> from hpapiwrapper import hpapiwrapper
    >>> hpapiwrapper.get_houseplant_byid(key,'9b97aef1-20a4-5620-af90-7d64dadb414e' )
    Output: A Dataframe with all data for the Palm plant associated with this id.
    """      
    def get_df3(key, ID):
        url = "https://house-plants2.p.rapidapi.com/" 
        url += ID
        headers = {"X-RapidAPI-Key": key ,
           "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
        response = requests.request("GET", url, headers=headers) 
        df = response.json() 
        return df 

    id_df = json_normalize(get_df3(key, ID))
    return id_df   

#Function 4
#Function to make scatterplot of plant category height distribution 
def get_houseplant_plot(key, category):
    """
    This function will allows users to create a scatterlpot of the Height vs. Width of 
    plants of a particular category. This plot also includes a regression line and confidence
    interval. 

    Parameters
    ----------
    key: API Key
    category: Select from the following options: ['Dracaena', 'Palm',
    'Anthurium', 'Other', 'Aglaonema', 'Hanging',
    'Bromeliad', 'Spathiphyllum', 'Flower', 'Aralia', 'Ficus',
    'Sansevieria', 'Foliage plant', 'Dieffenbachia', 'Philodendron',
    'Cactus & Succulent', 'Schefflera', 'Topiairy', 'Fern', 'Grass',
     'Ground Cover']

    Returns
    -------
    A scatterplot with the correct labels, points, and regression line.  

    Examples
    --------
    >>> from hpapiwrapper import hpapiwrapper
    >>> hpapiwrapper.get_houseplant_plot(key, 'Palm')
    Output: A plot showing the relationship between the Height and Width of 
    a certain category of plants.
    """     
    def get_houseplant_df3(key, category):

        def get_df4(key):
            url = "https://house-plants2.p.rapidapi.com/"
            headers = {"X-RapidAPI-Key": key ,
               "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
            response = requests.request("GET", url, headers=headers) 
            data = response.json() 
            return data 

        data_df = json_normalize(get_df4(key))
        df_cat = data_df.loc[data_df['Categories'] == category]
        return df_cat  
    

    df_cat = get_houseplant_df3(key,category)
    plot = sns.regplot(x=df_cat['Height potential.cm'], y=df_cat['Width potential.cm'], line_kws={"color":"r","alpha":0.7,"lw":2})
    plt.xlabel(f"{category} Plant Width Potential (cm)")
    plt.ylabel(f"{category} Plant Height Potential (cm)")
    plt.title(f"{category} Plant Height vs Width")
    return plt.show(plot) 

#Function 5
#Function for getting average stats for a given plant category 
def get_houseplant_means(key, category):
    """
    This function will allows users to get some insight into relevant 
    statistics for a plant category of interest. This function will output
    all the relevant mean values for a plant category.

    Parameters
    ----------
    key: API Key
    category: Select from the following options: ['Dracaena', 'Palm',
    'Anthurium', 'Other', 'Aglaonema', 'Hanging',
    'Bromeliad', 'Spathiphyllum', 'Flower', 'Aralia', 'Ficus',
    'Sansevieria', 'Foliage plant', 'Dieffenbachia', 'Philodendron',
    'Cactus & Succulent', 'Schefflera', 'Topiairy', 'Fern', 'Grass',
     'Ground Cover']

    Returns
    -------
    Prints our the average height, width, temperature, and pot diameter values.  

    Examples
    --------
    >>> from hpapiwrapper import hpapiwrapper
    >>> hpapiwrapper.get_houseplant_means(key, 'Dracaena')
    Output:
    Average Potential Height in cm: 374 cm
    Average Potential Width in cm: 168 cm
    Average Height at Purchase in cm: 113 cm
    Average Width at Purchase in cm: 82 cm
    Average Maximum Temperature in F: 86 F
    Average Minimum Temperature in F: 51 F
    Average pot diameter in cm: 27 cm
    """     
    def get_houseplant_df4(key, category):

        def get_df5(key):
            url = "https://house-plants2.p.rapidapi.com/"
            headers = {"X-RapidAPI-Key": key ,
               "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
            response = requests.request("GET", url, headers=headers) 
            data = response.json() 
            return data 

        data_df = json_normalize(get_df5(key))
        df_cat = data_df.loc[data_df['Categories'] == category]
        return df_cat  
    
    df_cat = get_houseplant_df4(key, category)
    print(f"Average Potential Height in cm: {round(df_cat['Height potential.cm'].mean())} cm")
    print(f"Average Potential Width in cm: {round(df_cat['Width potential.cm'].mean())} cm")
    print(f"Average Height at Purchase in cm: {round(df_cat['Height at purchase.cm'].mean())} cm")
    print(f"Average Width at Purchase in cm: {round(df_cat['Width at purchase.cm'].mean())} cm")
    print(f"Average Maximum Temperature in F: {round(df_cat['Temperature max.F'].mean())} F")
    print(f"Average Minimum Temperature in F: {round(df_cat['Temperature min.F'].mean())} F")
    print(f"Average pot diameter in cm: {round(df_cat['Pot diameter (cm).cm'].mean())} cm")