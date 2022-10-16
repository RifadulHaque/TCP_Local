# https://www.youtube.com/watch?v=46O73On0gyI&ab_channel=HusseinNasser
# https://developers.google.com/protocol-buffers/docs/pythontutorial
# https://developers.google.com/protocol-buffers/docs/proto
# https://www.youtube.com/watch?v=psYAhc9JUyo&t=653s&ab_channel=Jbang


import socket

import Protobuf.RRWorkload_pb2 as workloadpb2

from response import get_file_name, read_data_samples

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # server socket
    s.bind((socket.gethostname(), 4000))  # binding  server to the port and address
    s.listen()

    print("server is listening to receive signals from clients\n")
    Format = 'utf-8'

    # Accept Client Connection
    connection, ip_address = s.accept()
    print("Server is Connected\n")

    connection_established = True

    with connection:
        while connection_established:
            # as long a connection is established keep on receiving data
            data = connection.recv(1024)

            # Break when done receiving the data
            if not data:
                break

            print("Data request has been received\n")

            # Deserialize which is decode to the format utf-8
            request = workloadpb2.RFW()
            # deserializing the binary protobuf message back into the message object
            request.ParseFromString(data)  # fills the request with the parsed data
            print(request)

            # Get File to Read
            file_name = get_file_name(request.benchmark_type, request.data_type)

            last_batch_id = request.batch_id + request.batch_size - 1

            data_samples = read_data_samples(file_name, request.workload_metric, request.batch_unit,
                                             request.batch_id, request.batch_size)

            # Serialize the data
            rfd = workloadpb2.RFD(rfw_id=request.rfw_id, last_batch_id=last_batch_id,
                                  data_samples_requested=data_samples)

            response = rfd.SerializeToString()

            connection.sendall(response)
            print(response)
