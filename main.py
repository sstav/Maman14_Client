# This is a sample Python script.
import socket


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class CONFIG:
    @staticmethod
    def port():
        f = open("server.info", "r")
        f = f.read().split(":")
        return f[1]

    @staticmethod
    def ip():
        f = open("server.info", "r")
        f = f.read().split(":")
        return f[0]

    @staticmethod
    def backup_list():
        return open("server.info", "r").readlines();


class Data:
    user_id = bytearray(4)
    version = bytearray(1)
    op = bytearray(1)
    name_len = bytearray(2)
    filename = bytearray()
    size = bytearray(4)
    Payload = bytearray()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HOST = CONFIG.ip()  # The server's hostname or IP address
    PORT = CONFIG.port()  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
