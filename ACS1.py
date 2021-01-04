from st25r3917 import St25r3917
nfc = St25r3917()
# Power-on sequence
# 1
nfc.write("00","00")
nfc.write("01","80") # sup 3V3
# 2
nfc.adjustRegulators()

# Settings

# OSC on
nfc.write("02","80")
# RX,TX,FIELD
nfc.write("02","CB")
nfc.write("05","01") # anticol ??
nfc.write("0C","6C") # mixer instead of peak

# Communication

nfc.read("1A","01") # IRQ Status
nfc.direct("C6") # send REQA
nfc.fifoRead("01")
nfc.read("1A","01") # IRQ Status
nfc.clearFIFO()
nfc.write("80","9320")
nfc.read("1A","01") # IRQ Status
nfc.write("23","10") # num of bytes = 3
nfc.read("1A","01") # IRQ Status
nfc.transmitNoCRC()
nfc.read("1A","01") # IRQ Status
nfc.fifoRead("04")
nfc.read("1A","01") # IRQ Status
# end of comm

nfc.direct("C0") # set defaut
