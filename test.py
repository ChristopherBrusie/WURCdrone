# LED status and GPS coordinates

import board
import neopixel
from pymavlink import mavutil
import time


connection_string = 'udp:127.0.0.1:14550'
conn = mavutil.mavlink_connection(connection_string)

pixels = neopixel.NeoPixel(board.D18, 1)

switch = True

while True:
        msg = conn.recv_msg()
        if msg is not None:
                mtype = msg.get_type()
                if mtype == 'HEARTBEAT' and msg.type != mavutil.mavlink.MAV_TYPE_GCS:
                        armed = conn.motors_armed()
                        if armed:
                            pixels.fill((255, 0, 0))
                        else:
                            pixels.fill((0, 0, 255))
                if mtype == 'GLOBAL_POSITION_INT':
                        print(f'lat: {msg.lat}\t lon: {msg.lon}\n')