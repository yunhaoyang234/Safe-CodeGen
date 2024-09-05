def drive_forward_10_seconds():
    linear_velocity = 1 # units per second
    angular_velocity = 0 # the car is moving straight, not turning
    end_time = time.time() + 10 # calculate the end time
    stopping_time = 0 # total time stopped for pedestrians

    while time.time() < (end_time - stopping_time):
        if pedestrian_observed():
            stop() # stop if a pedestrian is observed
            stopping_time += time.time() - (end_time - 10)
        else:
            velocity_publisher(linear_velocity, angular_velocity) # drive forward

# Call the function:
drive_forward_10_seconds()
