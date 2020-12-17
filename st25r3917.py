import serial as s
import time

class St25r3917:
  """Class for controling st25r3917 over serial line."""

  def __init__(self):
    """Constructor of nfc object with default values."""
    self.ser = s.Serial('/dev/ttyUSB0', 9600)
    self.addr = "50"

  def __del__(self):
    self.ser.close()

  def write(self,reg,data):
    """
    Writes data to register.
      Parameter:
        reg (string): addres in hex
        data(string): byte of data to register
    """
    self.send(reg + data)

  def send(self,command):
    """Sends data over UART to i2c translator with device address"""
    self.ser.write(bytearray.fromhex(self.addr + command))
    time.sleep(1)
