def velocity_publisher(linear, angular):
    pass

def stop():
    pass

def pedestrian_observed():
    pass

def turn_left_135_degrees():
    duration = 5 # turning time/duration (seconds)
    radius = 3  # turning radius (meters)
    radian = math.pi * 3/4  # 135 degrees equates to pie * 3/4 in radians
    angular = radian / duration # angular velocity (rad/sec)
    linear = radius * angular # linear velocity (m/s)
    stopping_time = 0  # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)  # for a left turn, angular velocity should be positive
