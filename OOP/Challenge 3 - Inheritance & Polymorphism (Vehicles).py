class Vehichles:
    name=''
    with_engine=''

    def __init__(self, name, with_engine):
        self.name = name
        self.with_engine = with_engine
    
    def identify_myself(self):
        print( "Hi I'm Parent of All Vehicles, My Name is {}, My Engine Status is '{}'".format(self.name, self.with_engine))

class Bikes(Vehichles):
    wheel_count = 0
    def __init__(self, name, with_engine, wheel_count):
        super().__init__(name, with_engine)
        self.wheel_count = wheel_count

    def identify_myself(self):
        print( "Hi I'm Bike, My Name is {}, My Engine Status is '{}', I Have {} wheel(s)".format(self.name, self.with_engine, self.wheel_count))

class Cars(Vehichles):
    wheel_count = 0
    engine_type = ''
    def __init__(self, name, with_engine, wheel_count, engine_type):
        super().__init__(name, with_engine)
        self.wheel_count = wheel_count
        self.engine_type = engine_type

    def identify_myself(self):
        print( "Hi I'm Car, My Name is {}, My Engine Status is '{}', I Have {} wheel(s), My Engine Type = {}".format(self.name, self.with_engine, self.wheel_count, self.engine_type))


class Buses(Vehichles):
    wheel_count = 0
    private_bus = ''
    def __init__(self, name, with_engine, wheel_count, private_bus):
        super().__init__(name, with_engine)
        self.wheel_count = wheel_count
        self.private_bus = private_bus

    def identify_myself(self):
        print( "Hi I'm Bus[{}], My Name is {}, My Engine Status is '{}', I Have {} wheel(s)".format(self.private_bus, self.name, self.with_engine, self.wheel_count))

print('')
gerobak=Vehichles('Gerobak', 'no engine')
gerobak.identify_myself()

print('')
pedal_bikes=Bikes("Pedal Bikes","no engine", 2)
pedal_bikes.identify_myself()
motor_bikes=Bikes("Motor Bikes","with engine", 2)
pedal_bikes.identify_myself()

print('')
sport_cars=Cars('Sport Cars', 'with engine',4,'V8')
sport_cars.identify_myself()
pickup_cars=Cars('Pickup Cars', 'with engine',4,'Solar')
sport_cars.identify_myself()

print('')
trans=Buses('Trans Jakarta', 'with engine',4,'Public Bus')
trans.identify_myself()
school=Buses('School Bus', 'with engine',4,'Private Bus')
school.identify_myself()
print('')