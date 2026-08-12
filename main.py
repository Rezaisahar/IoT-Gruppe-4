import dht
import json
import time
from machine import Pin, ADC
from umqtt.simple import MQTTClient

# 1. Configuration
MQTT_BROKER = "broker.f4.htw-berlin.de"
MQTT_TOPIC = "f4/bis/gruppe4/temp"
CLIENT_ID = "esp32-gruppe4"

# Schwellenwert für Trockenheit (bitte testen und anpassen!)
DRY_THRESHOLD = 2000

# 3. Connect to MQTT
client = MQTTClient(CLIENT_ID, MQTT_BROKER)
client.connect()
print("MQTT ok")

# 4. Initialize Sensor & Actuators
soil_sensor = ADC(Pin(34))
soil_sensor.atten(ADC.ATTN_11DB)
pump = Pin(26, Pin.OUT)


soil_val = soil_sensor.read()
print("Soil Value test ", soil_val)



# 5. Main Loop
while True:
    try:
        
        #Bodenfeuchtigkeit lesen
        soil_val = soil_sensor.read()
        
        # --- LOGIK: Automatische Bewässerung ---
        pump_status = "OFF"
        if soil_val > DRY_THRESHOLD:
            pump.value(0)
            pump_status = "ON"
            print("On")
        else:
            pump.value(1)
            pump_status = "OFF"
            print("off")
        
        # Datenpaket erstellen
        data = {
            "soil_moisture": soil_val,
            "pump": pump_status
        }
        payload = json.dumps(data)
         
         
        #Senden
        client.publish(MQTT_TOPIC, payload)
        print(" Sent:", payload)
        
    except Exception as e:
        print(" Error:", e)
        try:
            cilent.connect()
        except:
            pass
    
    time.sleep(3)
        
         
        
         
         

