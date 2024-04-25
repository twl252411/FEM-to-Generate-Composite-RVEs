#
import numpy as np
import string
import random
import openpyxl
import xlrd
import pandas as pd
#
#------------------------------------------------------------------------------------
#
fad = './Local_Volume_Fraction_circle_6_20.xlsx'
#
ccol = pd.read_excel(io=fad, sheet_name=1)


