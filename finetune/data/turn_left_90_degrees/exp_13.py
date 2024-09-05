def turn_left_90_degrees():
    duration = 5 # duration (seconds) of turn
    radius = 3 # radius (meters) of turn
    radian = math.pi/2 # 90 degrees in radians
    angular_velocity = radian / duration # angular velocity (radians/sec)
    linear_velocity = radius * angular_velocity # linear velocity (meters/sec)
    stop_time = 0 # time stopped for pedestrians
    start_time = time.time() # current timestamp in seconds since epoch

    while (time.time() - start_time) - stop_time < duration:
        if pedestrian_observed():
            stop()
            time_at_stop = time.time()
        else:
            velocity_publisher(linear_velocity, angular_velocity)
            if 'time_at_stop' in locals(): # if pedestrian was observed before
                stop_time += time.time() - time_at_stop # total time stopped
