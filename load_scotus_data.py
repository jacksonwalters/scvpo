#JACKSON WALTERS
#US SUPREME COURT v. THE COURT OF PUBLIC OPINION
#this project is for The Data Incubator, Summer 2018.
#analyzing relationship between public opinion and supreme court decisions

import pandas as pd
import csv, os
from example_issues import civil_rights

SCDB_PATH = ".\\data\\scdb\\"
SCOTUS_OPINIONS_PATH = ".\\data\\scotus_opinions\\"

OPINION_PATH = os.path.join(SCOTUS_OPINIONS_PATH,'scotus_opinions.csv') #input filename
#path for scotus case data from SCDB, 1946 - present
CASE_DATA_PATH = os.path.join(SCDB_PATH,'scdb_case_data.csv')
#path for scotus legacy case data from SCDB, 1789 - 1946
LEGACY_CASE_DATA_PATH = os.path.join(SCDB_PATH,'scdb_legacy_case_data.csv')
#path for justice data, 1946 - present
JUSTICE_DATA_PATH = os.path.join(SCDB_PATH,'scdb_justice_data.csv')
#path for legacy justice data, 1789 - 1946
LEGACY_JUSTICE_DATA_PATH = os.path.join(SCDB_PATH,'scdb_legacy_justice_data.csv')

#load SCOTUS opinion data from CourtListener json->.csv conversion
def scotus_opinion_data():
    return pd.read_csv(OPINION_PATH)

#load csv files with pandas. not utf-8, must use alternate encoding
#case centered data stored in dataframe
def legacy_scdb_case_data():
    return pd.read_csv(LEGACY_CASE_DATA_PATH,encoding='windows-1252')

#load csv files with pandas. not utf-8, must use alternate encoding
#case centered data stored in dataframe
def scdb_case_data():
    return pd.read_csv(CASE_DATA_PATH,encoding='windows-1252')

#merge legacy and up-to-present case data and return as pandas dataframe
#ensure numeric index is unique!
def all_scdb_case_data():
    return pd.concat([legacy_scdb_case_data(),scdb_case_data()],ignore_index=True)

#only return relevant cases given their indices
def rel_scdb_case_data(case_ind,all_scdb_case_data):
    return all_scdb_case_data.iloc[case_ind]

#return scdb justice data
def scdb_justice_data():
    return pd.read_csv(JUSTICE_DATA_PATH,encoding='windows-1252')

#get legacy scdb justice data
def legacy_scdb_justice_data():
    return pd.read_csv(LEGACY_JUSTICE_DATA_PATH,encoding='windows-1252')

#merge legacy and up-to-present justice data and return as pandas dataframe
def all_scdb_justice_data():
    return pd.concat([scdb_justice_data(),legacy_scdb_justice_data()])

#get justice data only for relevant cases specified by indices
def rel_scdb_justice_data(case_ind,all_scdb_justice_data):
    return all_scdb_justice_data.iloc[case_ind]

#load supreme court data
if __name__ == "__main__":
    print(rel_scdb_case_data(civil_rights().case_ind))
