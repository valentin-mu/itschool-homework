# Because of poor fantasy,
# let's generalize idea of kettle :)
# We have Heater class that implements work of heater device
# and some classes that inherit from Heater
# I will use python. Because of python doesn't know about 
# private, i separated public methods with comment


class Heater (object):
    power_consumption = 1000 #how powerful heater is
    max_heating_temperature = 100
    max_voltage = 240
    #power supply properties
    power_input  = 0#did we plugged heater into socket
    power_voltage = 220 #what voltage is in circuit
    power_fuse =1 # do we have fuse or not
    heating_element = "unpowered" #is it powered or not
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
            self.current_temperature += 5 #imitate heating :)
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
    not just starting timer when switched on
    """
    number_of_breads = 2
    number_of_breads_present = 0
    bread_evacuator = 1
    lever = "up"
    def bread_evacuate(self):
        self.lever = "up"
    def heat(self,max_temp):
            while self.current_temperature <= self.max_temp:
                self.current_temperature += 5
                self.get_current_temperature()
            self.bread.evacuate()
            self.power_off()
    
    # user-controlled methods
    def put_breads(self, number):
        pass
    def lever_down(self):
        self.lever = "down"

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
