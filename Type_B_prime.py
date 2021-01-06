from st25r3917 import St25r3917
nfc = St25r3917()

# Power-on sequence
# 1
nfc.write("00","00")
nfc.write("01","80") # sup 3V3
# 2
# Settings

# OSC on
nfc.write("02","80")

# Type B settings

nfc.write("03","14") # ISO B card
nfc.write("07","28") # No SOF (support of B'), 80 preable length
nfc.write("09","24") # f_c/32, 2 BPSK pulses
nfc.write("28","50") # 10% ASK

# Field on

nfc.write("02","D8")

# Communication

nfc.read("1A","01") # IRQ Status
nfc.clearFIFO() # clear fifo before writing
nfc.write("80","000B3F80") # apgen
nfc.write("23","20") # num of bytes = 4
nfc.transmit() # direct command
repgen = nfc.fifoRead("06") # response
nfc.read("1A","01") # IRQ Status
nfc.clearFIFO() # clear fifo for future use

uid = repgen[4:12]
print(f'UID of the card is {uid}')

nfc.direct("C0")
