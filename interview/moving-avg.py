# Codility assessment question from Astranis
# Q2. time complexity & improvement, multiple methods?
# Q3. thread safety
# Q4. error handling

class MovingAvg:
    def __init__(self, window_size):
        if window_size < 0: raise Exception("Error") # TODO: can window size be 0? ret 0?
        self.k = window_size
        self.points = [0] * window_size # pad with 0s in case window_size < number of points
        self.avg = 0

    # add current point and subtract kth point before, weighted by 1 / window_size
    def add_point(self, point):
        self.avg += (1 / self.k) * (point - self.points[-self.k])
        self.points.append(point)

    # return current value of average in constant time
    def get_average(self):
        return self.avg

# test cases
if __name__ == "__main__":
    k = 1 # window_size
    A = [1, 2, 3]

    avg = MovingAvg(k)
    for point in A:
        avg.add_point(point)

    print(avg.get_average())