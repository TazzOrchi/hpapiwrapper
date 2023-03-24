from hpapiwrapper import hpapiwrapper
import pytest
import requests
import pandas as pd
from pandas import json_normalize

key = 'f3a3447e46msha8e4483eae21e45p1a6e7ejsnb2339e337de7'
def test_houseplant_df():
    url = "https://house-plants2.p.rapidapi.com/"
    headers = {"X-RapidAPI-Key": key ,
                   "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers) 
    data = response.json()
    data_df = json_normalize(data)
    expected = data_df.iloc[0]['Categories'] 
    actual = hpapiwrapper.get_houseplant_df(key).iloc[0]['Categories']
    assert actual == expected 
    
    
def test_houseplant_ids():
    url = "https://house-plants2.p.rapidapi.com/"
    headers = {"X-RapidAPI-Key": key ,
                   "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers) 
    data = response.json()
    data_df = json_normalize(data)
    ids = data_df[['id', 'Categories']].copy()
    df_catid = ids.loc[ids['Categories'] == 'Palm']
    expected = df_catid.iloc[0]['id'] 
    actual = hpapiwrapper.get_houseplant_ids(key, 'Palm').iloc[0]['id']
    assert actual == expected 
    
    
def test_houseplant_byid():
    url = "https://house-plants2.p.rapidapi.com/" 
    url += '9b97aef1-20a4-5620-af90-7d64dadb414e'
    headers = {"X-RapidAPI-Key": key ,
           "X-RapidAPI-Host": "house-plants2.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers) 
    df = response.json() 
    data_df = json_normalize(df)
    expected = data_df.iloc[0]['Categories']
    actual = hpapiwrapper.get_houseplant_byid(key, '9b97aef1-20a4-5620-af90-7d64dadb414e').iloc[0]['Categories']
    assert actual == expected