def search():
    while True:
        if target_observed():
            signal()
            stop()
            return
        elif person_observed():
            stop()
        else:
            navigate()
