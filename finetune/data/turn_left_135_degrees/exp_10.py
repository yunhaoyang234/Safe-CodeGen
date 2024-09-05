def turn_left_135_degrees():
    duration = 5 # turning time/duration in seconds
    radius = 3 # turning radius in meters
    radian = 3*math.pi/4 # 135 degrees in radians
    angular = radian / duration # angular velocity in rad/sec
    linear = radius * angular # linear velocity in m/s
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time() 

    while (time.time() - start_time) - stopping_time < duration:
        time_at_observation = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at_observation
        else:
            velocity_publisher(linear, angular) # turn left
