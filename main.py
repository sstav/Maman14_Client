# This is a sample Python script.
import socket
import os


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
        return open("server.info", "r").readlines()

    @staticmethod
    def rand_key():
        return os.urandom(4)

    @staticmethod
    def version():
        return 1


class Data:
    def __init__(self):
        self.user_id = bytearray(4)  # Size 4
        self.version = bytearray(1)  # Size 1
        self.op = bytearray(1)  # Size 1
        self.name_len = bytearray(2)  # Size 2
        self.filename = bytearray()  # Size filename Content Pointer
        self.size = bytearray(4)  # Size 4
        self.payload = bytearray()  # Size Payload Content Pointer
        # Init data constructor:
        self.version.append(CONFIG.version())
        self.user_id.extend(CONFIG.rand_key())

    def request_list_backup(self):
        self.op = bytearray(0)
        self.op.append(202)
        me_byte = bytearray()
        me_byte.extend(self.pack_data())

        s.connect((HOST, int(PORT)))
        s.sendall(me_byte)
        get_data = s.recv(1024)
        print("Data Res: " + get_data)

    def pack_data(self):
        temp_buffer = bytearray(0)
        self.user_id.reverse()
        self.version.reverse()
        self.op.reverse()
        self.name_len.reverse()
        self.filename.reverse()
        self.size.reverse()
        self.payload.reverse()
        temp_buffer.extend(self.user_id)
        temp_buffer.extend(self.version)
        temp_buffer.extend(self.op)
        temp_buffer.extend(self.name_len)
        temp_buffer.extend(self.filename)
        temp_buffer.extend(self.size)
        temp_buffer.extend(self.payload)
        return temp_buffer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HOST = CONFIG.ip()  # The server's hostname or IP address
    PORT = CONFIG.port()  # The port used by the server
    KEY = CONFIG.rand_key()
    client = Data()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        client.request_list_backup()

    # print('Received', repr(data))
    print("Bye")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
