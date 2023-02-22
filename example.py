from pyModbusTCP.client import ModbusClient
import requests
import time

Inverter_ip = "10.0.0.1" #Insert local-IP of your Inverter
Inverter_port = 502 #Standard port for SH10RT

#class for SH10RT
class Inverter:
    def init(self, ip, port):
        self.c = ModbusClient(host=ip, port=port, unit_id=1, auto_open=True)

    def get_grid_freq(self):
        regs = self.c.read_input_registers(5035, 1)
        return regs[0]/100

    def get_battery_power(self):
        regs = self.c.read_input_registers(13021, 1)
        return regs[0]
    def get_battery_level(self):
        regs = self.c.read_input_registers(13022, 1)
        return regs[0]/10

    def get_load_power(self):
        regs = self.c.read_input_registers(13007, 1)
        return regs[0]
    def get_dc_power(self):
        regs = self.c.read_input_registers(5016, 1)
        return regs[0]
    def get_total_active_power(self):
        regs = self.c.read_input_registers(13033, 1)
        return regs[0]

#decleration and init of Inverter object

my_Inverter = Inverter(Inverter_ip, Inverter_port)



grid_frequency = my_Inverter.get_grid_freq()
battery_power = my_Inverter.get_battery_power()
battery_level = my_Inverter.get_battery_level()
load_power = my_Inverter.get_load_power()
dc_power = my_Inverter.get_dc_power()
total_active_power = my_Inverter.get_total_active_power()

print("Frequency:"+ str(grid_frequency)+"\n"+"Battery_power:"+str(battery_power)+"\n"+"Battery_level:"+str(battery_level)+"\n"+"load_power:"+str(load_power)+"\n"+"dc_power:"+str(dc_power)+"\n"+"total_active_power:"+str(total_active_power)+"\n")