import socket

class NodeMCUController:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip_address, self.port))
        print("Connected to NodeMCU")

    def send_command(self, command):
        self.client_socket.send(command.encode())
        print("Sent command:", command)

        response = self.client_socket.recv(1024).decode()
        print("Received response:", response)

    def switch_led_on(self):
        self.send_command("LED ON")

    def switch_led_off(self):
        self.send_command("LED OFF")

    def disconnect(self):
        self.client_socket.close()
        print("Connection closed")

# Example usage:
# controller = NodeMCUController("192.168.1.102", 8081)
# controller.connect()
#
# controller.switch_led_on()
# controller.switch_led_off()
#
# controller.disconnect()
