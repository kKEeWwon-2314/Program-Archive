import time

class Stopwatch:
    """
    Provides an abstraction for a basic stopwatch that allows us to
    measure elapsed time by pushing "buttons" (i.e. calling methods).
    """
    # 1. define a constructor
    def __init__(self):
        """
        Create a stopwatch object with elapsed time initially set to 0.
        """
        # "self" is a special reference to the object we're creating

        # 3. define and initialize instance variables
        self._start_time = 0.0
        self._accumulated_time = 0.0
        self._is_ticking = False


    # 2. define the methods we use to interace with our data type

    def start(self):
        """
        Starts our stopwatch timer running.
        Continues from previous readout time.
        """
        # if we're not already ticking, remember the start time
        # and set our state to ticking
        if not self._is_ticking:
            self._start_time = time.time()
            self._is_ticking = True


    def stop(self):
        """
        Stop our timer and report (return) the total accumulated time
        on our stopwatch.
        """
        # calculate how much time has elapsed since we last pushed start
        elapsed_seconds = time.time() - self._start_time

        # if we're ticking, stop the watch and add elapsed time
        if self._is_ticking:
            self._is_ticking = False
            # add elapsed time to our total accumulated time
            self._accumulated_time += elapsed_seconds
        
        return self._accumulated_time


    def reset(self):
        """
        Stop the watch and reset its state to 0.
        """
        self._start_time = 0.0
        self._accumulated_time = 0.0
        self._is_ticking = False


    def look_at_time(self):
        """
        Report (return) the time elapsed on our stopwatch timer.
        If the watch is ticking, this includes the accumulated time
        and the time elapsed since pushing start.
        """
        if self._is_ticking:
            # calculate how much time has elapsed since we pushed start
            elapsed_seconds = time.time() - self._start_time
            return self._accumulated_time + elapsed_seconds
        else:
            return self._accumulated_time
