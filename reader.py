#!/usr/bin/python

import zmq
import sys
import schema_pb2
import struct
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)
sock.setsockopt(zmq.SUBSCRIBE, '')


# Define subscription and messages with prefix to accept.
sock.connect("tcp://10.150.2.60:7779")


print "Recopilando datos del servidor..."
while True:
    print "waiting on msg"
    message= sock.recv_multipart()
    message2=message[1]
    p=schema_pb2.nb_event()

    p.ParseFromString(message2)
    print "Decoded",p