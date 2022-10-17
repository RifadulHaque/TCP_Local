import json
import os
import socket
import sys

from google.protobuf.json_format import MessageToJson

from request import continue_connection_establishment, client_data_request

import Protobuf.RRWorkload_pb2 as workloadpb2


path = sys.path[1]


# write the data inside the file
def write_in_file(data_id, data_type_store, information):
    with open(path + f"/Protobuf/Result/{data_id}/{data_type_store}_{rfw_id}.json", "w") as file:
        json.dump(MessageToJson(information), file)


if __name__ == '__main__':
    PORT = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # server socket

    s.connect((socket.gethostname(), PORT))
    print("Client is connected to the server\n")

    keep_connection_establishment = True
    while keep_connection_establishment:
        # store all the data here after making the request for them

        rfw_id, benchmark_type, workload_metric, batch_unit, batch_id, batch_size, data_type = client_data_request()

        # a directory is created to store the data
        os.makedirs(path + f"/Protobuf/Result/{rfw_id}")

        # Serialize the data
        rfw = workloadpb2.RFW(rfw_id=rfw_id, benchmark_type=benchmark_type, workload_metric=workload_metric,
                              batch_unit=batch_unit, batch_id=batch_id, batch_size=batch_size, batch_type=data_type)
        request = rfw.SerializeToString()

        write_in_file(rfw_id, "rfw", rfw)
        s.sendall(request)
        print(request)

        # receive data
        data = s.recv(1024)

        # deserialize
        response = workloadpb2.RFD()
        response.ParseFromString(data)
        print("Response : ")
        print(response)

        write_in_file(rfw_id, "rfd", response)

        # if user enters anything expect of yes then program is terminated
        keep_connection_establishment = continue_connection_establishment()
