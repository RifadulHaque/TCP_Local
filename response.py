import csv
import sys
import pandas as pd

path = sys.path[1]


def get_file_name(benchmark, data):
    if benchmark == "DVD":
        benchmark_type = "DVD"
    else:
        benchmark_type = "NDBench"

    if data == "testing":
        data_type = "testing"
    else:
        data_type = "training"

    # location of the file to be read
    return path + f"/Resources/{benchmark_type}-{data_type}.csv"


def read_data_samples(file_name, workload_metric, batch_unit, batch_id, batch_size):
    data_samples_requested = []

    # Read file line by line using file_name
    with open(file_name, 'r') as file:
        # using csv reader to read the file
        csv_reader = csv.reader(file)

        # convert the csv to list for allowing it to be used as rows and columns
        list_of_rows = list(csv_reader)

        # Start and End of record
        first_data = batch_id * batch_unit
        last_data = first_data + batch_size * batch_unit - 1

        # add the record in the list of data samples that are requested to be returned
        for index in range(first_data, last_data):
            data_samples_requested.append(float(list_of_rows[index][workload_metric - 1]))

    return data_samples_requested


# https://medium.com/@kasiarachuta/basic-statistics-in-pandas-dataframe-594208074f85

def read_data_analytics(file_name, workload_metric, data_analytics):
    with open(file_name, 'r') as file:
        reader_csv = pd.read_csv(file)

        if workload_metric == 1:
            column_name = 'CPUUtilization_Average'
        elif workload_metric == 2:
            column_name = 'NetworkIn_Average'
        elif workload_metric == 3:
            column_name = 'NetworkOut_Average'
        else:
            column_name = 'MemoryUtilization_Average'

        if data_analytics == "50":
            analytics = reader_csv[column_name].mean()
        elif data_analytics == "min":
            analytics = reader_csv[column_name].min()
        elif data_analytics == "max":
            analytics = reader_csv[column_name].max()
        elif data_analytics == "std":
            analytics = reader_csv[column_name].std()
        else:
            analytics = reader_csv[column_name].describe(percentiles=[int(data_analytics) / 100])

    return str(analytics)
