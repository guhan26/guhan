import pyvisa
import time

rm = pyvisa.ResourceManager()
voa = rm.open_resource("GPIB0::20::INSTR")

bert = rm.open_resource("COM1")
bert.baud_rate = 115200

time.sleep(1)
voa.query("read att values")
