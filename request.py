import random


# Continue Sending Requests by continuing the connection establishment


def continue_connection_establishment():
    connection_status = user_input_checker("Want to Request Another Workload (yes/no)? ", ["yes", "no"])

    # Return boolean true if user wants to continue the connection
    return connection_status.lower() in ["yes"]


def user_input_checker(message, correct_inputs):
    input_from_user = input(message).strip()

    while input_from_user not in correct_inputs:
        print('Please enter correct input')
        input_from_user = input(message).strip()

    return input_from_user


def client_data_request():
    rfw_id = int(random.randint(1, 18000))  # generate a random number from 1 to 18000 and make it string

    # input for benchmark
    benchmark_type = int(user_input_checker("1 for DVD store Or 2 for NDBench: ", ["1", "2"]))

    # input for Workload Metric
    workload_metric = int(user_input_checker("1 for CPU, 2 for Network In, 3 for Network Out Or 4 for Memory : ",
                                             ["1", "2", "3", "4"]))

    # user input for batch unit
    batch_unit = int(input("Enter Batch Unit : ").strip())

    # user input for batch id
    batch_id = int(input("Enter Batch ID : ").strip())

    # user input for batch size
    batch_size = int(input("Enter Batch Size : ").strip())

    # user input for data type
    data_type = int(user_input_checker("1 for Training Or 2 for Testing : ", ["1", "2"]))

    return rfw_id, benchmark_type, workload_metric, batch_unit, batch_id, batch_size, data_type
