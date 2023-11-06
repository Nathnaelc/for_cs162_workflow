class ClockIterator:
    def __init__(self):
        # Initialize the starting time at 00:00
        self.hours = 0
        self.minutes = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Format the current time as a string with zero-padded numbers
        current_time = f"{self.hours:02d}:{self.minutes:02d}"
        # Increment the minutes
        self.minutes += 1
        # Check if minutes have reached 60, which is the threshold to increment the hour
        if self.minutes == 60:
            # Reset minutes to 0 and increment the hour
            self.minutes = 0
            self.hours += 1
        # Check if hours have reached 24, which is the threshold to reset the clock
        if self.hours == 24:
            # Reset hours to 0
            self.hours = 0
        return current_time


# an example
# clock = ClockIterator()
# # Loop for one day (24*60 minutes = 1440 iterations)
# for _ in range(1440):
#     # Print the next minute on the clock
#     print(next(clock))
