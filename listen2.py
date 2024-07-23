from pymavlink import mavutil
import time
import board
import neopixel
# Start a connection listening on a UDP port

#the_connection = mavutil.mavlink_connection('/dev/ttyACM0,115200')
the_connection = mavutil.mavlink_connection('udpin:localhost:14550')


# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

pixels = neopixel.NeoPixel(board.D18, 1)
light_switch = True

# Once connected, use 'the_connection' to get and send messages
while 1:
    try:
        gps_msg = the_connection.messages['GLOBAL_POSITION_INT']
        print(f'lat: {gps_msg.lat}\t lon: {gps_msg.lon}\n')
    except:
        print('No GPS message')

    htbt = the_connection.recv_match(type='HEARTBEAT', blocking=True)
    #htbt = the_connection.messages['HEARTBEAT']
    if htbt.type != mavutil.mavlink.MAV_TYPE_GCS:
        armed = the_connection.motors_armed()
        if armed:
            pixels.fill((255*light_switch, 0, 0))
            if htbt.base_mode == 8:
                pixels.fill((0, 0, 255*light_switch))
        else:
            pixels.fill((0, 255*light_switch, 0))

    light_switch = not light_switch
    time.sleep(1)
