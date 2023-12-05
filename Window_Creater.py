import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import random
import re


def window_creater(file_path='../data/full_set2.csv', window_size=0, non_peak_proportion=0):
    """
    :param file_path: default is 'full_set.csv'. It's the full dataset of merged readings from 3 satellites in the long format.
    :param window_size: default is 50. Integer How many Readings should sandwich the peak value (center)
    :param non_peak_proportion: default is 3. How many non-peaks should we have for every peak
    :return: A dataframe that is in the wide format with columns "time", [n amount of readings], "label"
    """
    print("Data retrieved.")
    source_data = pd.read_csv(file_path)
    source_data = source_data[["time", "xrsa_flux", "status"]]
    labels = []

    for status in source_data['status']:
        if status == 'EVENT_PEAK':
            event_label = 1
        else:
            event_label = 0
        labels.append(event_label)

    cleaned = source_data[["time", "xrsa_flux"]]
    cleaned['Label'] = labels

    # removing all the 2017 data
    cleaned['time'] = pd.to_datetime(cleaned['time'])

    start_time = pd.to_datetime('2018-01-01 00:00:00')
    cleaned = cleaned[(cleaned['time'] >= start_time)]

    cleaned = cleaned.dropna(subset=['xrsa_flux']).reset_index(drop=True)
    print("Data cleaned")

    peaks = []
    non_peaks = []

    for i in range(window_size, len(cleaned) - window_size):
        window = cleaned.iloc[i - window_size: i + window_size + 1]
        if window.Label[i] == 1:
            time = cleaned.iloc[i]['time']  # Capture the time of the peak
            row = [time] + list(window['xrsa_flux'].reset_index(drop=True))
            row.append(1)  # Label for peak
            peaks.append(row)
        if window.Label[i] == 0:
            time = cleaned.iloc[i]['time']  # Capture the time of the peak
            row = [time] + list(window['xrsa_flux'].reset_index(drop=True))
            row.append(0)
            non_peaks.append(row)

    mixed_peaks = peaks + non_peaks[: (len(peaks) * non_peak_proportion)]
    random.shuffle(mixed_peaks)
    print("Data Shuffled.")
    print("PEAKS:", len(peaks))
    print("NON PEAKS:", len(non_peaks))
    print()

    final_transposed_df = pd.DataFrame(mixed_peaks)
    final_transposed_df.columns = ['time'] + [str(i) for i in range((window_size * 2) + 1)] + ['Label']


    return final_transposed_df

