import csv
import sys

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
