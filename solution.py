class Carbase:
    def __init__(self, car_type, brand, photo_le_name,
                 carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name
        self.carrying = carrying

    def get_photo_le_ext(self):
        point = self.photo_le_name.rfind('.')
        return self.photo_le_name[point:len(self.photo_le_name)]

        pass


class Car(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl,
                 carrying, extra):
        super().__init__(car_type, brand, photo_le_name,
                         carrying)
        self.passenger_swats_count = passenger_seats_count


class Truck(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl,
                 carrying, extra):
        super().__init__(car_type, brand, photo_le_name,
                         carrying)
        self.body_whl = body_whl
        try:
            if self.body_whl != '':
              self.body_length = float(str(self.body_whl).split('x')[0])
              self.body_width = float(str(self.body_whl).split('x')[1])
              self.body_height = float(str(self.body_whl).split('x')[2])
            else:
              self.body_length = self.body_width = self.body_height = 0
        except ValueError:
            self.body_length = self.body_width = self.body_height = 0


    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width

    def __str__(self):
        return str(self.body_width)


class Specmachine(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl,
                 carrying, extra):
        super().__init__(car_type, brand, photo_le_name,
                         carrying)
        self.extra = extra


def get_car_list(filename):
    car_list = []

    with open(filename, 'r') as f:
        data = []
        for line in f.readlines():
            if line[len(line) - 1] == '\n':
                data.append(line[:len(line) - 2])
            else:
                data.append(line)

        for elem in data:
            m = elem.split(';')
            if len(m) < 7:
                m += ['']
                car_list.append(m)
            elif len(m) == 7:
                car_list.append(m)


    return car_list

def main():
    pass

if __name__ == '__main__':
    main()

