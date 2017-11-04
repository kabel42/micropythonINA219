# micropythonINA219
simple micropython driver for INA219

# Example session

ina219 connections:  
+3v3<->3v3  
gnd<->gnd  
scl<->Pin5(D1 on D1 mini, pullup onboard)  
sda<->Pin4(D2, pullup onboard)  
Vin+<->+5V(USB)  
Vin-<->LED+400R  

```
MicroPython v1.9.2-8-gbf8f45cf on 2017-08-23; ESP module with ESP8266
Type "help()" for more information.
>>> import ina219
>>> ina = ina219.INA219()
>>> ina.read()
(4.2, 4864.0)
>>> ina.read()
(4.3, 4864.0)
>>> ina.read()
(4.3, 4868.0)
```
