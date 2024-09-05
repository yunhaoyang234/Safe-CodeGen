def left_u_turn():
    duration = 10 # because a U-turn is 2 * 90 degrees, so it takes 2 * 5 seconds
    radius = 3 # turning radius (meters)
    radian = math.pi # 180 degrees = pi radian
    angular = radian / duration # angular velocity (rad/sec)
    linear = radius * angular # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()
    
    # Keep turning until the duration of the turn has passed
    # while accounting for any time spent stopped for pedestrians
    while (time.time() - start_time) < duration:
        if pedestrian_observed():
            stop() # stop if a pedestrian is observed
            stopping_time += time.time() - start_time
        else:
            # publish the calculated linear and angular velocities
            velocity_publisher(linear, angular)
