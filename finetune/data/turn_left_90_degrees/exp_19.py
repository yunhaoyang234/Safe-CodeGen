def turn_left_90_degrees():
    duration = 5  # turning time/duration in seconds
    radius = 3  # turning radius in meters
    radian = math.pi / 2  # 90 deg in rads
    angular = radian / duration  # angular velocity (rad/sec)
    linear = radius * angular  # linear velocity (m/s)
    stopping_time = 0 

    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)  # For moving left, angular is positive
