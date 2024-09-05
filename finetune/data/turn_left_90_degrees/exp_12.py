def turn_left_90_degrees():
    duration = 5 # turning time/duration in seconds
    radius = 3  # turning radius in meters
    radian = math.pi/2 # 90 degrees = pi/2 radians
    angular = radian / duration # angular velocity in rad/sec
    linear = radius * angular # linear velocity in m/s
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time() # returns the current time in seconds since the epoch

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time() 
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)