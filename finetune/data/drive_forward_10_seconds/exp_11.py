def drive_forward_10_seconds():
    duration = 10  # drive time/duration (seconds)
    linear = 1 # assuming 1 meter per second. Adjust this value as needed.
    angular = 0 # no deviation angularly as the car is moving forward straight
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time() # taking the time when the function starts

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time() # taking the current time
        if pedestrian_observed():
            stop() # if a pedestrian is observed, stop the car
            stopping_time += time.time() - time_at # incrementing the total stopping time
        else:
            velocity_publisher(linear, angular) # if no pedestrian is observed, move car forward
