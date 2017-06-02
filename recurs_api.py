#!/usr/bin/python3
"""
Query an api recursively and prints result in a given format
The idea is to call the querying function recursively, by passing the url, id
and and required whitespace.
"""
import requests
def recurs_query(url,idNum,tabs):
    req = requests.get("{:s}?id={}".format(url,idNum))
    res = req.json()
    if res:
        print("{:s}{:s} - {:s}".format(tabs,res.get('name'), res.get('title')))
        for i in res.get('reports'):
            recurs_query(url,i,"\t")
    else:
        return
