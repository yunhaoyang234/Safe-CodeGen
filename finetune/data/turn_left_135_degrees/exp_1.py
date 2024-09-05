def turn_left_135_degrees():
    duration = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = (3*math.pi)/4 # 135 deg = (3*pi)/4
    angular_velocity = radian / duration # angular velocity (rad/s)
    linear_velocity = radius * angular_velocity # linear velocity (m/s)
    stopped_time = 0 # total time the car has stopped for pedestrians
    initial_time = time.time()

    while (time.time() - initial_time) - stopped_time < duration:
        current_time = time.time()
        if pedestrian_observed():
            stop()
            stopped_time += time.time() - current_time
        else:
            velocity_publisher(linear_velocity, angular_velocity)
