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
    tank_volume = 0 # bool is it filled with water or not.
    heating_indicator = 0 # disabled by default
    water_input = 1
    destination_temperature = self.current_temperature
    def is_water_input_present(self):
        return self.water_input
    def is_tank_filled(self):
        return self.tank_volume
    def fill_tank(self):
        self.tank_volume = 1
    def indicator_on(self):
        self.heating_indicator = 1
    def indicator_off(self):
        self.heating_indicator = 0

    # user-controlled methods
    def set_water_temperature(self,temp):
        if temp > self.max_heating_temperature: print "i cant make water hotter than %d" % self.max_heating_temperature
        elif temp <= self.current_temperature: print "i'm not a conditioner :) "
        else: self.destination_temperature = temp

    def get_hot_water_from_tank(self):
        self.tank_volume = 0

    def plug_into_socket(self):
        while True:
            if self.is_tank_filled() and self.is_water_input_present() and self.is_power_correct():
                if self.current_temperature >= self.destination_temperature:
                    print "we heated to destination temperature or hotter"
                    self.indicator_off()
                else:
                    self.indicator_on()
                    self.heat( self.destination_temperature )
            # disable everything if we cannot fill tank or having problem with power input
            elif not self.is_water_input_present() or not self.is_power_correct():
                self.indicator_off()
                print "water is absent or problems with power, call assistance"
                break
            elif not self.is_tank_filled():
                self.fill_tank()
                self.indicator_off()
