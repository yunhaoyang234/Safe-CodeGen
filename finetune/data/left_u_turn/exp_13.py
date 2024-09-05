def left_u_turn():
    duration = 5  # rotation time/duration (seconds)
    radius = 3  # rotation radius (meters)
    radian = math.pi  # 180 degrees in radian
    angular = radian / duration  # angular velocity (rad/second)
    linear = radius * angular  # linear velocity (m/second)
    stopping_time = 0  # total time stopped for pedestrians
    start_time = time.time()  # recording the start time for our maneuver 

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()  # recording the time at the start of each loop iteration
        if pedestrian_observed():
            stop()  # if there is a pedestrian we stop
            stopping_time += time.time() - time_at  # and increase the stopping time by the time we have been stopped
        else:
            velocity_publisher(linear, angular)  # if there isn't a pedestrian we can continue with our turn
