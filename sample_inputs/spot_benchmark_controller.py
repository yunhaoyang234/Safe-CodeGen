def search():
    while not target_observed():
        if person_observed():
            stop()
        else:
            navigate()
    signal()
