import serial
import time
import csv


def envreadings(comport, baudrate, timestamp=False, iter=10):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    
    with open('/home/kantor-lab/Documents/i2grow_central_computer/sensor-readings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp','Temperature [in degrees C]','Relative Humidity [%]','CO2 [in ppm]'])
        dataline = []
        k = 0
        while k < iter:

            data = ser.readline().decode().strip()

            if data and timestamp:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f'{timestamp} > {data}')
                if data[0:11] == 'Temperature' and len(dataline) == 0:
                    dataline.append(timestamp)
                    temp = data[13:].replace(' degrees C','')
                    dataline.append(float(temp))
                elif data[0:17] == 'Relative Humidity' and len(dataline) == 2:
                    rh = data[19:].replace(' %','')
                    dataline.append(float(rh))
                elif data[0:3] == 'CO2' and len(dataline) == 3:
                    co2 = data[5:][:].replace(' ppm','')
                    dataline.append(float(co2))
                    if float(co2) != 0.000 and len(dataline) == 4:
                        writer.writerow(dataline)
                        k += 1
                    dataline = []
                
                if data[0:4] == 'TAKE':
                    return True
                else:
                    return False
                
            elif data:
                print(data)

    
        


if __name__ == '__main__':
    envreadings('/dev/ttyACM0', 115200, True) 