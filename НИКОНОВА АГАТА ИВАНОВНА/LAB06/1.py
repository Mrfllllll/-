class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        print("Скорость:", self.speed)
        print("Вместимость:", self.capacity)


class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        Transport.__init__(self, speed, capacity)
        self.route_number = route_number

    def info(self):
        Transport.info(self)
        print("Номер маршрута:", self.route_number)


t = Transport(60, 4)
b = Bus(40, 50, 12)

print("Transport:")
t.info()

print("\nBus:")
b.info()