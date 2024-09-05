def turn_left_90_degrees():
    duration = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = math.pi/2 # 90 deg = pi/2
    angular = radian / duration # angular velocity (rad/sec)
    linear = radius * angular # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - start_time
            start_time = time.time() #reset the start_time after continue the movement
        else:
            velocity_publisher(linear, angular)
