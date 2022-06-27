mile_run_times = [15.0, 20.9, 18.5, 16.2, 17.0, 15.5, 9.1, 10.0, 7.0, 8.7]

novice_mile_run_times = filter(lambda run_times_x: run_times_x >= 9, mile_run_times)
print(list(novice_mile_run_times))




