import math

class Statistics:
    def mean(values):
        """
        Calculate and return the average (mean) of a list of numbers provided
        in the values parameter.
        """
        N = len(values)
        average = sum(values) / N
        return average


    def median(values):
        """
        Find and return the middle value in the list of numbers if the list
        is odd length. Otherwise return the average of two middles values.
        """
        # first sort values to obtain ordered list
        values_in_order = sorted(values)

        # if list is odd length, pick middle
        N = len(values)
        if N % 2 == 1:
            middle_index = (N-1) // 2
            return values_in_order[middle_index]
        # otherwise average the two middle values
        else:
            m1_index = N // 2 - 1
            m2_index = N // 2
            return (values_in_order[m1_index] + values_in_order[m2_index]) / 2
        

    def mode(values):
        """
        Finds and returns a list of elements wich occur with the greatest
        frequency in the provided list of values.
        """
        # sort the list of values

        # run the algorithm from Quiz #6 on finding the largest number of adjacent, identical elements, and store the actual value(s)

        # implementation left as exercise to the reader
        pass


    def variance(values):
        """
        Calculates the statistical variance (using the formula from Assignment #3)
        of the list of numbers provided in values. There should be at least two
        elements in the values list.
        """
        # calculate the mean first
        x_bar = mean(values)

        # use variance formula
        N = len(values)
        total = 0
        for x_i in values:
            total += (x_i - x_bar) ** 2
        var = total / (N-1)
        return var


    def standard_deviation(values):
        """
        Calculate the standard deviation (square root of variance) of the provided
        list of values.
        """
        sigma = math.sqrt(variance(values))
        return sigma


    def z_score(values, observation):
        """
        Calcaulate the z-score of the given observation with respect to the
        statistical properties of the list of numbers provided in values.
        """
        x_bar = mean(values)
        sigma = standard_deviation(values)
        z = (observation - x_bar) / sigma
        return z