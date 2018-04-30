class MyCalendar:
    def __init__(self):
        self.booked = []
        self.start = []
        self.end = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        self.start = start
        self.end = end
        # check on two ends
        add_sign = 1
        if len(self.booked) == 0:
            add_sign *= 1
        elif start >= self.booked[-1][1] or end <= self.booked[0][0]:
            add_sign *= 1
        else:
            for ind in range(0, len(self.booked)):
                if max(end, self.booked[ind][1]) - min(start, self.booked[ind][0]) >= (self.booked[ind][2] + end - start):
                    add_sign *= 1
                else:
                    add_sign *= 0
        if add_sign == 1:
            self.booked.append([start, end, end - start])
            self.booked.sort()
            print('True')
        else:
            print('False')

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
new1 = MyCalendar()
new1.book(47, 50)
new1.book(33, 41)
new1.book(39, 45)
new1.book(33, 42)
new1.book(25,32)
new1.book(26,35)
new1.book(19,25)
new1.book(3, 8)
new1.book(8, 13)
new1.book(18,27)

# new1.book(10, 20)
# new1.book(15, 25)
# new1.book(20, 30)


# new1.book(37, 50)
# new1.book(33, 50)
# new1.book(4, 17)