import serial as s
import time

class St25r3917:
  """Class for controling st25r3917 over serial line."""

  def __init__(self):
    """Constructor of nfc object with default values."""
    self.ser = s.Serial('/dev/ttyUSB0', 9600, timeout=3)

  def __del__(self):
    self.ser.close()

  def write(self, reg, data):
    """
    Writes data to register.
      Parameters:
        reg (string): addres in hex
        data (string): byte of data to register
    """
    self.rWrite(reg + data)
    print(f'Writing {data} to {reg}')

  def read(self, reg, size):
    """
    Writes data to register.
      Parameters:
        reg (string): addres in hex
        size (string): num of regs
    """
    self.rRead(reg, size)

  def direct(self, command):
    """
    Sends direct command.
      Parameter:
        command (string): direct command
    """
    self.rWrite(command)
    print(f'Direct Command {command}')


  def rWrite(self, command):
    """
    Sends write command.
      Parameters:
        reg (string): addres in hex
        data (string): byte of data to register
    """
    self.ser.write(bytearray.fromhex("F0" + command))
    time.sleep(0.5)

  def rRead(self,reg,size):
    """
    Sends read command.
      Parameters:
        reg (string): addres in hex
        size (string): num of regs in two digits
    """
    self.ser.write(bytearray.fromhex("F1" + reg + size))
    resp = self.ser.read(int(size))
    time.sleep(0.5)
    print(f'{int(size)} bytes with first adress {reg}: {resp.hex()}')
