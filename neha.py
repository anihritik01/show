from random import randrange


class LinkedList:
    class Node:
        def __init__(self, value):
            self.__value = value
            self.next = None

        def getValue(self):
            return self.__value

        def set_value(self, data):
            self.__value = data

    def __init__(self):
        self.__node = None

    def __str__(self):
        if self.__node is None:
            return 'Showroom: []'
        node = self.__node
        s = "Showroom: [" + str(node.getValue())
        if node.next is None:
            return s + "]"
        while node.next is not None:
            s += ", " + str(node.next.getValue())
            node = node.next
        return s + "]"

    def add(self, value):
        if self.__node is None:
            self.__node = self.Node(value)
            return
        node = self.__node
        while node.next is not None:
            node = node.next
        node.next = self.Node(value)

    def delete_it(self, key):
        temp = self.__node
        if temp is not None:
            if temp.getValue() == key:
                self.__node = temp.next
                temp = None
                return temp
        while temp is not None:
            if temp.getValue() == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return temp
        prev.next = temp.next
        temp = None

    def delete(self, value):

        if self.__node is None:
            return False  # or maybe raise

        node = self.__node
        if node.getValue() == value:
            if node.next is not None:
                self.__node = node.next
            else:
                self.__node = None
            return True

        while node.next is not None:
            if node.next.getValue() == value:
                newNext = node.next.next
                if newNext is not None:
                    node.next = newNext
                else:
                    node.next = None
                return True
        return False  # or maybe raise

    def __middle(self, start, last):
        if start is None:
            return None

        slow = start
        fast = start.next
        while fast is not last:
            fast = fast.next
            if fast is not last:
                slow = slow.next
                fast = fast.next
        return slow

    def sort_it(self):
        current = self.__node
        index = None
        if self.__node is None:
            return None
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.getValue() > index.getValue():
                        temp = current.getValue()
                        current.set_value(index.getValue())
                        index.set_value(temp)
                    index = index.next
                current = current.next

    def binary_search(self, key):
        self.sort_it()
        start = self.__node
        last = None
        while True:
            mid = self.__middle(start, last)
            if mid is None:
                return None
            if mid.getValue() == key:
                return mid
            elif mid.getValue() < key:   # less than symbol is not supporting
                start = mid.next
            else:
                last = mid

            if not (last is None or last != start):
                break
        return None


class Showroom:
    class Cars:
        wheels = 4

        def __lt__(self, other):
            return self.company_name < other.company_name

        def __eq__(self, other):
            return self.company_name.upper() == other.company_name.upper()

        def _generate_price(self):
            LUXURY_CARS = ["MERCEDES-BENZ", "BMW", "LEXUS", "JAGUAR", "CADILLAC", "INFINITE", "ROLLS-ROYCE", "FERRARI",
                           "LAMBORGHINI", "AUDI"]
            LATEST_MODELS = ["A", "E", "I", "O", "U"]
            FAV_COLOR = ["YELLOW", "RED", "BLACK"]
            price = 0
            if self.company_name.upper() in LUXURY_CARS:
                price = price + 5000000
            else:
                price = price + 600000
            model = self.model[0]
            if model.upper() in LATEST_MODELS:
                price = price + 3000000
            if self.autoDriving:
                price = price + 1500000
            if self.color.upper() in FAV_COLOR:
                price = price + 300000
            extra_charges = randrange(70000, 1200000)
            return price + extra_charges

        def __init__(self, name, color, model, auto_driver):
            try:
                self.company_name = name
                self.color = color
                self.model = model
                self.autoDriving = auto_driver
            except:
                self.company_name = str()
                self.color = str()
                self.model = str()
                self.autoDriving = bool()

            self.price = self._generate_price()

        def __str__(self):
            if self.autoDriving:
                driver = "YES"
            else:
                driver = "NO"
            result = "(\nCompany: " + str(self.company_name) \
                     + ", Color: " + str(self.color) \
                     + ", Model: " + str(self.model) \
                     + ", Auto Driving: " + str(driver) \
                     + ", Price: " + str(self.price) + ")\n"
            return str(result)

        def set_company_name(self, name):
            self.company_name = name

        def set_color(self, color):
            self.color = color

        def set_model(self, model):
            self.model = model

        def set_autoDriver(self, auto_driver):
            try:
                self.autoDriving = auto_driver
            except:
                self.autoDriving = False

    def __init__(self):
        self.room = LinkedList()

    def vehicles_entry(self, car):
        self.room.add(car)

    def show_all_vehicles(self):
        print(self.room)

    def buy_vehicles(self, car):
        self.room.delete_it(car)

    def search_vehicles(self, car_detail):
        if self.room.binary_search(car_detail):
            print("Car is available")
        else:
            print("Not available")


if __name__ == '__main__':
    car = Showroom.Cars("BMW", "red", "A11", True)
    car1 = Showroom.Cars("Audi", "black", "E88", True)
    car2 = Showroom.Cars("Tata", "green", "A", True)

    showroom = Showroom()
    showroom.vehicles_entry(car)
    showroom.vehicles_entry(car1)
    showroom.vehicles_entry(car2)
    showroom.show_all_vehicles()

    showroom.search_vehicles(car2)
    print()
    showroom.buy_vehicles(car2)
    showroom.show_all_vehicles()
    # print()

