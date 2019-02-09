import pandas as pd
import numpy as np
import json
import sys


filename = sys.argv[1]
print('input filename: {}'.format(filename))

with open(filename,'r') as f:
    columns = ['bc','apgrp','chn','lastMenuCode','sts','svct']
    lines = f.readlines()
    df = pd.DataFrame.from_records([json.loads(_) for _ in lines])
    df = df.groupby('glb').first().reset_index()
    print('total transactions: {}'.format(len(df)))
    df_suc = df.copy()
    df_suc['real'] = 0 + df_suc['bussc']
    df_suc.fillna(0,inplace=True)
    df_suc = df_suc.groupby(columns)['real'].sum().reset_index()
    df_suc = df_suc[columns + ['real']]
    print(df_suc)
    print('total success: {}'.format(np.sum(df_suc['real'])))
    df_suc.to_csv('{}_success.csv'.format(filename.split('.')[0]),index = None)

    df_ttl = df.copy()
    df_ttl['real'] = 1
    df_ttl.fillna(0,inplace=True)
    df_ttl = df_ttl.groupby(columns)['real'].sum().reset_index()
    df_ttl = df_ttl[columns + ['real']]
    print(df_ttl)
    print('total counts: {}'.format(np.sum(df_ttl['real'])))
    df_ttl.to_csv('{}_count.csv'.format(filename.split('.')[0]),index=None)


