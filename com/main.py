import serial.tools.list_ports
import serial


def main():
    print("Start programm")

    com_list()



if __name__ == '__main__':
    main()


def com_list():
    ports = serial.tools.list_ports.comports()

    for port in ports:
        print(port.device)


def com_init():
    port = "COM1"  # Replace with the appropriate COM port name
    baudrate = 9600  # Replace with the desired baud rate

    ser = serial.Serial(port, baudrate=baudrate)

    # Perform operations on the COM port


def com_close():
    ser.close()  # Remember to close the connection when done