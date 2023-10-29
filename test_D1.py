class Count_points:
    def __init__(self, uchastniki):
        self.coin = uchastniki
        self.median = 0

    def get_median(self):
        self.coin.sort()
        if len(self.coin) % 2 == 0:
            self.median = ((self.coin[(len(self.coin) - 1) // 2]) + self.coin[len(self.coin) // 2]) / 2
        else:
            self.median = (self.coin[(len(self.coin)) // 2])
        print(self.median)

uchastniki = [10]
num = int(input())
while num != 10:
    uchastniki += [num]
    num = int(input())

Count_points(uchastniki).get_median()
