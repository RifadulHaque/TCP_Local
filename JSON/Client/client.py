# References:
# https://realpython.com/python-sockets/
# https://www.geeksforgeeks.org/socket-programming-python/
# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# https://www.geeksforgeeks.org/json-dumps-in-python/
# https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
# https://json-schema.org/understanding-json-schema/reference/array.html
# https://www.geeksforgeeks.org/json-loads-in-python/#:~:text=loads()%20method%20can%20be,JSON%20data%20into%20Python%20Dictionary.
# https://www.w3schools.com/python/python_json.asp
# https://www.programiz.com/python-programming/json

import json
import os
import socket
import sys

from request import continue_connection_establishment, client_data_request

path = sys.path[1]


# write the data inside the file
def write_in_file(data_id, data_type_store, information):
    with open(path + f"/JSON/Result/{data_id}/{data_type_store}_{rfw_id}.json", "w") as file:
        json.dump(information, file)


if __name__ == '__main__':
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # server socket

    s.connect((socket.gethostname(), PORT))
    print("Client is connected to the server\n")

    keep_connection_establishment = True
    while keep_connection_establishment:
        # store all the data here after making the request for them

        rfw_id, benchmark_type, workload_metric, batch_unit, batch_id, batch_size, data_type = client_data_request()

        # a directory is created to store the data
        os.makedirs(path + f"/JSON/Result/{rfw_id}")

        # Serialize the data in JSON Data format
        rfw = {"rfw_id": rfw_id, "benchmark_type": benchmark_type, "workload_metric": workload_metric,
               "batch_unit": batch_unit, "batch_id": batch_id, "batch_size": batch_size, "data_type": data_type}
        request = json.dumps(rfw)
        write_in_file(rfw_id, "rfw", rfw)
        s.sendall(request.encode("utf-8"))
        print(request)

        # receive data
        data = s.recv(1024)

        # after receiving deserialize the data
        response = json.loads(data.decode("utf-8"))
        print("Response : ")
        print(response)

        # storing the response data into the file
        write_in_file(rfw_id, "rfd", response)

        # if user enters anything expect of yes then program is terminated
        keep_connection_establishment = continue_connection_establishment()
