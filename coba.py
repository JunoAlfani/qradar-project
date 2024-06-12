import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x =b['SELLING PRICE']
y =b['KM DRIVEN']
slope, intercept, r, p, std_error = stats.linregress(x,y)