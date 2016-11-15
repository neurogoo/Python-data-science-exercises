import Tkinter
import matplotlib.pyplot as plt
import numpy as np

import sys, re, pdb
import logging
import argparse

import pandas as pd

import datetime

def testi():
    return 3

def read_data(file_name):
    #logger.info("Reading data from file " + file_name)
    df = pd.read_csv(file_name, parse_dates=['datetime'], sep = ';')
    df = df[df["municipalityId"].notnull()]
    df["municipalityId"] = df["municipalityId"].astype(int)
    df["userId"] = df["userId"].astype(int)
    #logger.info("N of rows: {:.0f}".format(len(df)))
    df = df.sort_values(['applicationId', 'datetime'])
    return df
def print_week1a_result(df):
    print('Amount of municipalites that have used the service is {}').format(df.municipalityId.unique().size)
def print_week1b_results(df):
    print("Amount of application role users is {}").format(df[df['role'] == 'applicant'].userId.unique().size)
    print("Amount of authority role users is {}").format(df[df['role'] == 'authority'].userId.unique().size)
def print_week2h1a_results(df):
    print('Amount of comments on each application is:')
    print(df[(df['action'] == 'add-comment')].groupby('applicationId').count().userId)
#Create month column from createDate
def print_week2a1b_results(df_operative):
    df_operative['createdMonth'] = df_operative['createdDate'].map(lambda x: x.month)
    createdMonthPlot = df_operative[df_operative['state'] == 'submitted'].groupby('createdMonth').size().plot(kind='bar', title='Amount of application submitted each month')
    createdMonthPlot.set_xlabel('Month')

if __name__ == "__main__":
    usage_file = "/Users/toniok/Python/Python-data-science-exercises/data/all-lupapiste-usage-pub-20161031.csv"
    operative_file = "/Users/toniok/Python/Python-data-science-exercises/data/all-applications-operative-pub-20161031.csv"
    df = read_data(usage_file)
    df_operative = pd.read_csv(operative_file, parse_dates=['createdDate', 'submittedDate'], sep = ';')
    print_week1a_result(df)
    print_week1b_results(df)
    print_week2h1a_results(df)
    print_week2a1b_results(df_operative)
