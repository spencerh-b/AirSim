import airsim
import cv2
import numpy as np
import os
import pprint
import setup_path 
import tempfile

# connect to the AirSim simulator
num_agents = 10

client = airsim.MultirotorClient()
client.confirmConnection()

for i in range(0,num_agents):
    client.enableApiControl(True, "Drone"+str(i))
    client.armDisarm(True, "Drone"+str(i))
    client.takeoffAsync(1,"Drone"+str(i))

airsim.wait_key('Press any key to continue')

for i in range(0,num_agents):
    print (i)
    print (client.simGetPositionWRTOrigin("Drone"+str(i)).x_val /100.0)
    print (client.simGetPositionWRTOrigin("Drone"+str(i)).y_val /100.0)
    print (client.simGetPositionWRTOrigin("Drone"+str(i)).z_val /100.0)

airsim.wait_key('Press any key to reset to original state')

client.armDisarm(False, "Drone1")
client.armDisarm(False, "Drone2")
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False, "Drone1")
client.enableApiControl(False, "Drone2")


