def turn_left_135_degrees():
    import time
    import math

    duration = 5    # turning time/duration (seconds)
    radius = 3      # turning radius (meters)

    # Calculating the necessary radians (135 degrees = 3/4 * pi)
    radians = 3/4 * math.pi

    # Calculating required linear and angular velocities
    angular_velocity = radians / duration   # angular velocity (radians/second)
    linear_velocity = radius * angular_velocity  # linear velocity (meters/second)

    total_stopping_time = 0    # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - total_stopping_time < duration:
        time_now = time.time()
        if pedestrian_observed():
            stop()
            # total stopping time (seconds) while pedestrians crossing
            total_stopping_time += time.time() - time_now
        else:
            # Start the movement with calculated linear and angular velocities.
            velocity_publisher(linear_velocity, angular_velocity)
