# This is a sample Python script.
import socket
import os
import struct
import sys


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
        return int.from_bytes(os.urandom(4), sys.byteorder)

    @staticmethod
    def version():
        return 1


class Data:
    def __init__(self):
        self.user_id = CONFIG.rand_key()  # Size 4
        self.version = CONFIG.version()  # Size 1
        self.op = 0  # Size 1
        self.name_len = 0  # Size 2
        self.filename = 0  # Size filename Content Pointer
        self.size = 0  # Size 4
        self.payload = 0  # Size Payload Content Pointer

    def request_list_backup(self):
        self.op = 202
        s.connect((HOST, int(PORT)))
        s.sendall(self.pack_data_202())
        get_data = s.recv(1024)
        get_data = get_data.decode("utf-8")
        list_files = get_data.split("\n")
        del list_files[-1]
        print("BackUp List: ")
        for file_name in list_files:
            print(file_name)
        print(list_files)
        return list_files

    def request_save_file(self, filename):
        s.connect((HOST, int(PORT)))
        file_to_send = open("img.png", "rb")
        data = file_to_send.read(1024)
        while data:
            s.send(data)
            data = file_to_send.read(1024)
        file_to_send.close()

        print(s.recv(1024))
        s.shutdown(2)
        s.close()


    def pack_data_202(self):
        return struct.pack('<I', self.user_id) + struct.pack('<B', self.version) + struct.pack('<B', self.op)


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
