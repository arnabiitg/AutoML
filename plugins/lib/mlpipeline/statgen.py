import pandas as pd
import logging
from configuration import 
from statsmodels.stats.diagnostic import acorr_ljungbox as ljungbox
class stats:
    df = pd.read_csv("model_data_input.csv", columns = ["temperature",])
    def ljung_box():
        boxtest = ljungbox(df["relativehumidity_2m"], lags = 24)
        for pval in boxtest["lb_pvalue"]:
            if  pval >0.05:
                lag = lag +1