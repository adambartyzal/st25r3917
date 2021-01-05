import serial as s
import time

class St25r3917:
  """Class for controling st25r3917 over serial line."""

  def __init__(self):
    """Constructor of nfc object with default values."""
    self.ser = s.Serial('/dev/ttyUSB0', 9600, timeout=2)

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

  def setDefault(self):
    """
    Sends set default
    """
    self.direct("DB")

  def fieldOn(self):
    """
    Turns on the field
    """
    self.direct("C8")

  def reqA(self):
    """
    Sends Request A
    """
    self.direct("C6")

  def clearRSSI(self):
    """
    clears RSSI
    """
    self.direct("DA")

  def clearFIFO(self):
    """
    Clears FIFO
    """
    self.direct("DB")

  def measureAmplitude(self):
    """
    Measures the amplitude of the signal present on RFI inputs and stores the result in the A/D converter output register
    """
    self.direct("D3")
    self.read("25","01")

  def adjustRegulators(self):
    """
    Adjusts regulators
    """
    self.direct("D6")

  def transmit(self):
    """
    Transmit data from FIFO
    """
    self.direct("C4")

  def transmitNoCRC(self):
    """
    Transmit data from FIFO
    """
    self.direct("C5")


  def rWrite(self, command):
    """
    Sends write command.
      Parameters:
        reg (string): addres in hex
        data (string): byte of data to register
    """
    self.ser.write(bytearray.fromhex("F0" + command))
    time.sleep(1)

  def rRead(self,reg,size):
    """
    Sends read command.
      Parameters:
        reg (string): addres in hex
        size (string): num of regs in two digits
    """
    self.ser.write(bytearray.fromhex("F1" + reg + size))
    resp = self.ser.read(int(size))
    time.sleep(1)
    print(f'{int(size)} bytes with first adress {reg}: {resp.hex()}')
    self.ser.flush()
    return resp.hex()

  def fifoRead(self,size):
    """
    Sends fifo read command.
      Parameters:
        size (string): num of regs in two digits
    """
    self.ser.write(bytearray.fromhex("F200" + size))
    resp = self.ser.read(int(size))
    time.sleep(1)
    print(f'{int(size)} bytes from FIFO: {resp.hex()}')
    self.ser.flush()
    return resp.hex()
