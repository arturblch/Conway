import socket
import struct
import json
import logging
from model.Objects import Objects
from model.Map import Map

# create logger
logger = logging.getLogger('RemouteClient')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('RemouteClient.log')
fh.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


class RemoteProcessClient:
    BYTE_ORDER_FORMAT_STRING = "<"

    BYTE_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "b"
    UNSIGNED_INT_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "I"

    SIGNED_BYTE_SIZE_BYTES = 1
    UNSIGNED_INTEGER_SIZE_BYTES = 4

    ACTION = {"LOGIN": 1, "LOGOUT": 2, "MOVE": 3, "TURN": 5, "MAP": 10}

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logger.info("Create socket")
        self.socket.connect((host, port))
        logger.info("Connection done")
        self.socket.settimeout(5)

    def login(self, name):
        return self.write_message('LOGIN', {"name": name})

    def logout(self):
        return self.write_message('LOGOUT')

    def move(self, move):
        return self.write_message('MOVE', {"line_idx": move.line_idx, "speed": move.speed, "train_idx": move.train_idx})

    def turn(self):
        return self.write_message('TURN')

    def map(self, layer=1):
        return self.write_message('MAP', {"layer": layer})

    def write_message(self, action, data=None):
        if action in RemoteProcessClient.ACTION:
            self.write_uint(RemoteProcessClient.ACTION[action])
            logger.info("Action: %s", action)
        else:
            logger.error("write_message received wrong action=%s", action)
            raise ValueError("Received wrong action=%s" % action)
        if data is None:
            data = {}
        self.write_string(json.dumps(data))
        logger.info("Loging message: %s", data)
        return self.read_response()

    def read_response(self):
        result = self.read_uint()
        data = self.read_string()
        logger.info("Result code: %d", result)
        if data:
            logger.info("Data: %s", data)
            return [result, json.loads(data)]
        return [result]

    def close(self):
        self.socket.close()
        logger.info("Close socket")

    def read_string(self):
        length = self.read_uint()
        if length == -1:
            return None
        byte_array = self.read_bytes(length)
        return byte_array.decode()

    def write_string(self, value):
        if value is None:
            return
        byte_array = value.encode()
        self.write_uint(len(byte_array))
        self.write_bytes(byte_array)

    def read_uint(self):
        byte_array = self.read_bytes(
            RemoteProcessClient.UNSIGNED_INTEGER_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.UNSIGNED_INT_FORMAT_STRING,
                             byte_array)[0]

    def write_uint(self, value):
        self.write_bytes(
            struct.pack(RemoteProcessClient.UNSIGNED_INT_FORMAT_STRING, value))

    def read_bytes(self, byte_count):
        byte_array = b''
        while len(byte_array) < byte_count:
            byte_array += self.socket.recv(byte_count - len(byte_array))
        if len(byte_array) != byte_count:
            raise IOError(
                "Error read %s bytes from input stream." % str(byte_count))
        return byte_array

    def write_bytes(self, byte_array):
        self.socket.sendall(byte_array)

    def read_objects(self):
        layer = self.write_message('MAP', {"layer": 1})[1]
        return Objects(layer)

    def update_objects(self, objects):
        layer = self.write_message('MAP', {"layer": 1})[1]
        objects.update(layer)

    def read_map(self):
        layer = self.write_message('MAP', {"layer": 0})[1]
        return Map(layer)
