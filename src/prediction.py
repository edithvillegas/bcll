import numpy as np
import pandas as pd

def predict(patient):

    # this is the risk class calculator

    cluster=-1

    if (patient['FISH_Del17'] >= 37):
            cluster = 7
    else:
        if patient['FISH_Del11'] >= 34:
            cluster = 6
        else:
            if patient['FISH_Tri12'] >= 20:
                cluster = 5
            else:
                if patient['IGHV_mutation'] >= 9:
                    cluster = 3
                else:
                    if patient['CD49d'] >= 51:
                        cluster = 4
                    else:
                        if patient['IGHV_mutation'] >= 3:
                            cluster = 2
                        else:
                            cluster = 1
    return cluster