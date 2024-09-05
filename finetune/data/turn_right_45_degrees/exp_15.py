def turn_right_45_degree():
    duration = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = -math.pi/4 # 45 deg cw = -pi/4
    angular = radian / duration # angular velocity (rad/sec)
    linear = radius * angular # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop() # stops the robot if pedestrian observed
            stopping_time += time.time() - time_at # adds up the total time the robot was stopped
        else:
            velocity_publisher(linear, angular) # commands the robot to continue turning if no pedestrian is observed