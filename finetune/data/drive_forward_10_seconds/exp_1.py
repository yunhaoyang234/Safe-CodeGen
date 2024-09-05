def drive_forward_10_seconds():
    linear_velocity = 1.0   # This is just a placeholder. You'd typically get this from your car's specifics
    angular_velocity = 0.0  # We don't want to turn while driving forward  

    start_time = time.time()
    while time.time() - start_time < 10:  # Drive for 10 seconds
        if pedestrian_observed():
            stop()   # Stop if a pedestrian is observed
            time.sleep(0.1)  # add a delay to avoid frequently polling the pedestrian check.
        else:
            velocity_publisher(linear_velocity, angular_velocity)   # Drive straight
