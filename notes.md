# Notes
- Anticolision frame transmission in RFAL is on line 2805 in file rfal_rfst25r3916.c
- wu 2nd bit in Operation control register 02h puts the device in wake up mode
- After OSC is stable IRQ on pin 7 is generated it goes to log 1 and stays until IRQ register is read
## algorithm

- 0A = (1 << 7) disable CRC
- ST25R3916_CMD_STOP - C2
- ST25R3916_CMD_RESET_RXGAIN - D5 
- ST25R3916_IRQ_MASK_COL ? 
- ST25R3916_REG_NUM_TX_BYTES2 - 23h = 0
- C6
- 

# Antenna matching
- Cp + 22p - antiresonance
## Reviecer
- on when rx_en [6] in Operation Controll Register [02h]
### Preparation and execution of a transceive sequence:
- Stop all activities
- Reset RX gain