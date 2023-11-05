from websocket import create_connection
from time import sleep as s
import json

allDevice =[]
allInfo =[]
allMessage =[]

def fixed_point_to_decimal(value):
    # Extract the integer and fractional parts
    integer_part = (value >> 8) & 0xFF
    fractional_part = value & 0xFF
    
    # Handle the sign bit
    if integer_part & 0x80:  # Check the most significant bit for the sign
        integer_part = -((integer_part ^ 0xFF) + 1)
    
    # Convert the fractional part to its equivalent decimal value
    decimal_fraction = fractional_part / 256.0
    
    # Combine the integer and fractional parts
    decimal_value = integer_part + decimal_fraction
    
    return decimal_value

class Device:
    def __init__(self, rawData):
        ### GET THE MAC ###
        # Minew's device id. All of minew's devices have the same vendor id
        vendor_id = "3F23AC"
        # Find the starting position of the vendor ID in the string (NOTE: You can also just use the location index of the MAC in the strinf ie. 46)
        start_position = rawData.find(vendor_id)
        # Make sure the start position is valid
        if start_position != -1:
            # Extract the MAC from the rawData
            mac_address = rawData[start_position - 6:start_position + 6]
            # Reverse and format the MAC address
            self.mac = ":".join(reversed([mac_address[i:i+2] for i in range(0, len(mac_address), 2)]))
        else:
            # Invalid MAC x_x (this is no good) (TODO: printing the error instead of "invalid" would be cool)
            self.mac = "invalid"

        ### GET BATTERY LEVEL ###
        # convert the battery level from hex to decimal (int)
        self.battery = int(rawData[26:28], 16)

        ### GET X, Y and Z accel ###
        # Convert the fixed point value to decimal
        self.x = round(fixed_point_to_decimal(int(rawData[28:32], 32)),2)   # (optional) Round to 2 decimal places
        self.y = round(fixed_point_to_decimal(int(rawData[32:36], 32)),2)   # (optional) Round to 2 decimal places
        self.z = round(fixed_point_to_decimal(int(rawData[36:40], 32)),2)   # (optional) Round to 2 decimal places

        ### GET VERSION NUMBER ###
        # convert the version number from hex to decimal (int)
        self.versionNumber = int(rawData[24:26], 16)

        ### GET FRAME TYPE ###
        self.frameType = rawData[22:24]

        ### GET SERVICE DATA UUID ###
        # Extract the little-endian value at the specified position
        little_endian_value = rawData[18:22]

        # Convert the little-endian hex value to big-endian
        self.serviceDataUUID = "".join(reversed([little_endian_value[i:i+2] for i in range(0, len(little_endian_value), 2)]))

        ### GET COMPLETE SERVICE UUID ###
        # Extract the little-endian value at the specified position
        little_endian_value = rawData[10:14]

        # Convert the little-endian hex value to big-endian
        self.completeServiceUUID = "".join(reversed([little_endian_value[i:i+2] for i in range(0, len(little_endian_value), 2)]))

"""
*   il reçoit de Node-red tout ces données
"""
def webseocketReciever(ws):
    result =  ws.recv()
    result = json.loads(result)
    return result


"""
*   il séparer les données des trame qu'il 
*   reçoit. deplus il identifie tout les 
*   appareils.
"""
def tags(message):
    info = 0
    if 'Unknown' in message['type']:
        d = Device(message['rawData'])
        if 'invalid' in d.mac:
            info = d
            d ='Other'
        else:
            info = d
            d = 'E8 plus'
    else:
        d = message['type']
    return d, info


"""
*   il disperse les travail a faire soit décoder les
*   trames, séparer les données des noms et les mettre
*   dans des variables pour que le programme API fasse
*   le reste. 
"""
def main():
    global allDevice
    global allMessage
    global allInfo
    i=0

    
    ws = create_connection("ws://localhost:1880/ws/labo4/")
    while(i != 3):
        i+=1
        allMessage.append(webseocketReciever(ws))
    ws.close()
        
    for x in range(len(allMessage)):
        if x == 0:
            device1, infoDevice1= tags(allMessage[x])
        
        if x == 1:
            device2, infoDevice2= tags(allMessage[x])

        if x == 2:
            device3, infoDevice3= tags(allMessage[x])

    allDevice = [device1,device2,device3]
    allInfo = [infoDevice1,infoDevice2,infoDevice3]
    
if __name__ == '__main__':
    main()