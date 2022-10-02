import serial

def read_response(ser):
    reading = False
    resp = bytearray()
    while True:
        arr = ser.read(1)
        if len(arr) < 1:
            return None
        if reading == False:
            if arr[0] == 0x40:
                reading = True
        else:
            if arr[0] == 0x0d:
                return resp
            resp.append(arr[0])


if __name__ == "__main__":
    print("Hello, world!")
    ser = serial.Serial(
        '/dev/ttyUSB1',
        baudrate=1200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        timeout=1.6
    )

    req = bytearray()
    req.append(0x80)
    req.append(0x3f)
    req.append(0x01)
    req.append(0x05)
    req.append(0x8a)
    req.append(0x0d)
    print(req.hex(sep=' '))
    ser.write(req)

    resp = read_response(ser)
    print(resp.hex(sep=' '))