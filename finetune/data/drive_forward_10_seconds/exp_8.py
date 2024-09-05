def drive_forward_10_seconds():
    linear_velocity = 1.0  # Assume a velocity of 1 m/s for driving forward
    angular_velocity = 0.0  # No angular change when driving forward
    end_time = time.time() + 10  # End time is 10 seconds from the current time
    total_stopped_time = 0.0  # Start with no stopped time
    while time.time() < end_time:
        if pedestrian_observed():
            stop()
            stopped_time_start = time.time()
            # Wait until the pedestrian is no longer observed
            while pedestrian_observed():
                pass
            total_stopped_time += time.time() - stopped_time_start
        else:
            velocity_publisher(linear_velocity, angular_velocity)
        # End time is pushed forward by the amount of time stopped
        end_time += total_stopped_time
