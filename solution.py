class Carbase:
    def __init__(self, list_atr):
        self.car_type = list_atr[0]
        self.brand = list_atr[1]
        self.photo_le_name = list_atr[3]
        try:
            self.carrying = float(list_atr[5])
        except ValueError:
            self.carrying = None


    def get_photo_le_ext(self):
        point = self.photo_le_name.rfind('.')
        return self.photo_le_name[point:len(self.photo_le_name)]

        pass


class Car(Carbase):
    def __init__(self, list_atr):
        super().__init__(list_atr)
        try:
            self.passenger_seats_count = int(list_atr[2])
        except ValueError:
            self.passenger_seats_count = None




class Truck(Carbase):
    def __init__(self, list_atr):
        super().__init__(list_atr)
        self.body_whl = list_atr[4]
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
    def __init__(self, list_atr):
        super().__init__(list_atr)
        self.extra = list_atr[6]


def get_car_list(filename):
    car_list = []
    list_atr = []
    try:

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

            for i in car_list:
                if 'car' in i:
                    list_atr.append(Car(i))
                elif 'truck' in i:
                    list_atr.append(Truck(i))
                elif 'spec_machine' in i:
                    list_atr.append(Specmachine(i))

        return list_atr
    except FileNotFoundError:
        return None


def main():
    pass

if __name__ == '__main__':
    main()

