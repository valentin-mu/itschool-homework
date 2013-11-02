# Because of poor fantasy,
# let's generalize idea of kettle :)
# We have Heater class that implements work of heater device
# and some classes that inherit from Heater
# I will use python. Because of python doesn't know about 
# private, i separated public methods with comment

class Heater (object):
    power_consumption = 1000 # how powerful heater is
    max_heating_temperature = 100
    max_voltage = 240
    #power supply properties
    power_input  = 0 # did we plugged heater into socket
    power_voltage = 220 # what voltage is in circuit
    power_fuse =1 # do we have fuse or not
    heating_element = "unpowered" # is it powered or not
    current_temperature = 25 # here we store temperature
    
    def get_current_temperature(self):
        pass
    def is_on_power(self):
        """check if we are plugged in. return true or false"""
    def power_on(self):
        """start heating if everything is ok with power"""
        if self.is_power_correct():
            self.heat()
        else: print "problems with power"

    def power_off(self):
        self.heating_element = "unpowered"

    def is_power_correct(self):
        if self.is_on_power() and self.power_fuse:
            if self.power_voltage >= self.max_voltage:
                self.fuse_burn_out()
                return False
            return True
        else: return None

    def fuse_burn_out(self):
        self.power_fuse = "burnt"

    def heat(self,max_temp):
        self.heating_element = "powered"
        while self.current_temperature <= self.max_temperature:
            self.current_temperature += 5 # imitate heating :)
            self.get_current_temperature()
        self.power_off()
    
    # user-controlled methods
    def button_down(self):
        self.power_on()
    def plug_into_socket(self):
        pass

class Toaster(Heater):
    """
    let's suppose we have clever toaster
    that can measure temperature,
    """
    number_of_breads = 2
    number_of_breads_present = 0
    bread_evacuator = 1
    lever = "up"
    brownness_switch = 1 # "1 - light","2 - medium","3 - dark" brownness
    timer = 1 # timer is present as a part of toaster
    def bread_evacuate(self):
        self.lever = "up"

    def brownness_to_seconds(self,brownness_switch):
        if brownness_switch == 1: return 30
        elif brownness_switch == 2: return 45
        elif brownness_switch == 3: return 100

    def timer_start(self.interval):
        timer = Timer( interval , self.bread_evacuate() )
        timer.start()

    # user-controlled methods
    def put_breads(self, number):
        if number > self.number_of_breads:
            print "you cannot put more breads than i can heat"
        elif number == 1:
            print "ok, i can heat one bread, but maybe you'll put one more?"
            self.number_of_breads_present = number
        elif number == 2:
            print "ok, i'm ready to heat them both"
            self.number_of_breads_present = number
        else: print "something went wrong "

    def set_brownness(self.value):
        if value != 1 or value != 2 or value != 3: print "you entered incorrect brownness, be careful with switch"
        else: self.brownness_switch = switch

    def lever_down(self):
        if self.number_of_breads_present < 1:
            self.lever = "up"
            print "toaster is empty, put some bread please"
        self.lever = "down"
        self.heat(self.max_heating_temperature) # reached max temperature, assume there is no heat loss
        self.timer_start( self.brownness_to_seconds(self.brownness_switch) )

    def plug_into_socket(self):
        if self.lever == "up": print "all ok. i'm ready"
        if self.lever == "down" and self.number_of_breads_present == 0:
            print "put some bread, i have nothing to heat"
            self.bread_evacuate()

class Boiler(Heater):
    tank = 1
    tank_volume = 0
    heating_indicator = 0
    def indicator_on(self):
        pass
    def indicator_off(self):
        pass
    def heat(self,max_temp):
        while True:
            if self.fuse == "burnt":
                self.indicator_off()
                self.power_off()
                break

            while self.current_temperature <= self.max_temp:
                self.indicator_on()
                self.current_temperature += 5
                self.get_current_temperature()
            self.indicator_off()
