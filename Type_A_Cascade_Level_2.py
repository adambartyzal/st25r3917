from st25r3917 import St25r3917
nfc = St25r3917()

# Power-on sequence
# 1
nfc.write("00","00")
nfc.write("01","80") # sup 3V3
# 2
#nfc.adjustRegulators() # TODO check if it affects distance or consumption

# Settings

# OSC on
nfc.write("02","80")
# RX,TX,FIELD
nfc.write("02","CB")
# anticol
#nfc.write("05","01")
# mixer instead of peak # TODO check if it affects distance or consumption
#nfc.write("0C","6C") 

# Communication

nfc.direct("C6") # send REQA
atqa = nfc.fifoRead("01")
if (atqa[0] == "0"):
  print("Cascade level 1!")
  # Cascade Level 1
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo before writing
  nfc.write("80","9320") # bytes to write
  nfc.write("23","10") # num of bytes = 2
  nfc.transmitNoCRC() # direct command
  uidcl1 = nfc.fifoRead("05") # response
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo for future use
  uid = uidcl1[0:8]
elif (atqa[0] == "4"):
  print("Cascade level 2!")
  # Cascade Level 1
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo before writing
  nfc.write("80","9320") # bytes to write
  nfc.write("23","10") # num of bytes = 2
  nfc.transmitNoCRC() # direct command
  uidcl1 = nfc.fifoRead("05") # CT + UID0-UID2
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo for future use
  # Cascade Level 2
  nfc.write("80","9370" + uidcl1) # bytes to write
  nfc.write("23","38") # num of bytes = 7
  nfc.transmit() # direct command
  sak = nfc.fifoRead("01") # response
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo for future use
  nfc.write("80","9520") # bytes to write
  nfc.write("23","10") # num of bytes = 2
  nfc.transmitNoCRC() # direct command
  uidcl2 = nfc.fifoRead("05") # response
  nfc.read("1A","01") # IRQ Status
  nfc.clearFIFO() # clear fifo for future use
  uid = uidcl1[2:8] + uidcl2[0:8]
else:
  print("Somethings's fishy!")

print(f'UID of the card is {uid}')

# end of comm

# set defaut
nfc.direct("C0")
