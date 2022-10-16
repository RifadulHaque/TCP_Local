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
import socket
from response import get_file_name, read_data_samples

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # server socket
    s.bind((socket.gethostname(), 5000))  # binding  server to the port and address
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
            request = json.loads(data.decode(Format))
            print(request)

            # Get File to Read
            file_name = get_file_name(request['benchmark_type'], request['data_type'])

            last_batch_id = request['batch_id'] + request['batch_size'] - 1

            data_samples = read_data_samples(file_name, request['workload_metric'], request['batch_unit'],
                                                       request['batch_id'], request['batch_size'])

            # Serialize which is encode
            rfd = {
                "rfw_id": request['rfw_id'],
                "last_batch_id": last_batch_id,
                "data_samples_requested": data_samples
            }

            response = json.dumps(rfd, indent=2)
            connection.sendall(response.encode(Format))

            print(response)
