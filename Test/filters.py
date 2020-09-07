class KalmanFixedFilter:
    def __init__(self, y, a, c, g, m, k):
        self.x_hat_pre = y / c
        self.a = a
        self.c = c
        self.m = m
        self.g = g
        self.k = k

    def calculate(self, y):
        x1 = self.a * self.x_hat_pre
        d = self.m * (y-self.c*x1)
        x2 = x1 + self.g * d
        x_hat = x2 + self.k * (y-self.c * x2)
        return [d, x_hat]
