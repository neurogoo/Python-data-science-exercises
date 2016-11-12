import matplotlib.pyplot as plt
import numpy as np

import sys, re, pdb
import logging
import argparse

import pandas as pd

import matplotlib, datetime

def read_data(file_name):
    #logger.info("Reading data from file " + file_name)
    df = pd.read_csv(file_name, parse_dates=['datetime'], sep = ';')
    df = df[df["municipalityId"].notnull()]
    df["municipalityId"] = df["municipalityId"].astype(int)
    df["userId"] = df["userId"].astype(int)
    #logger.info("N of rows: {:.0f}".format(len(df)))
    df = df.sort_values(['applicationId', 'datetime'])
    return df
usage_file_test = "../data/small/some-lupapiste-usage-pub-20161031.csv"
usage_file = "../data/all-lupapiste-usage-pub-20161031.csv"
operative_file = "../data/all-applications-operative-pub-20161031.csv"
df = read_data(usage_file)
df_operative = pd.read_csv(operative_file, sep = ';')
print('Amount of municipalites that have used the service is {}').format(df.municipalityId.unique().size)
print("Amount of application role users is {}").format(df[df['role'] == 'applicant'].userId.unique().size)
print("Amount of authority role users is {}").format(df[df['role'] == 'authority'].userId.unique().size)
