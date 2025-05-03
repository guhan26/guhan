import pyvisa

rm = pyvisa.ResourceManager()

voa = rm.open_resource("g")

voa.query("read att values")
