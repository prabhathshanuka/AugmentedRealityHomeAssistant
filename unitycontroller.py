import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 8084


class unitycontroller:
    def __init__(self):
        a = 1

    def ConnectToUnity(self, value1, value2):
        # Connect to the Unity server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((TCP_IP, TCP_PORT))
        # Send the data to the client
        data = f"{value1},{value2}"  # Format the values as a string
        client.send(data.encode())  # Assuming data is a string, encode it to bytes before sending
        # Rest of the code
        print("HELLO FROM SENDING")

