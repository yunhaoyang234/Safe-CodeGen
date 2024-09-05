def left_u_turn():
    duration = 5  # turn duration in seconds
    radius = 3    # turn radius in meters
    radian = math.pi  # 180 degrees is pi in radian

    angular_velocity = radian / duration  # angular velocity in rad/sec
    linear_velocity = radius * angular_velocity  # linear velocity in m/s

    stop_time = 0  # to keep track of total stop time
    start_time = time.time()

    while (time.time() - start_time) - stop_time < duration:
        current_time = time.time()
        if pedestrian_observed():
            stop()  # stop the robot if a pedestrian is observed
            stop_time += time.time() - current_time  # incrementing the total stop time
        else:
            velocity_publisher(linear_velocity, angular_velocity)  # make the u turn 
