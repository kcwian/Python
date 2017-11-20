# Python - instalacja niezbędnych pakietów

### Instalacja niezbędnych pakietów dla systemu ROS-Kinetic:
```
$ sudo apt-get install python-tk
$ sudo apt-get install python-pip
$ sudo apt-get install imagemagick
```


# Python - instalacja virtualenv & virtualenvwrapper

```
$ pip install virtualenv virtualenvwrapper
$ echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc
```

### Wysłanie wiadomości do topic'u

##### Włączenie momentu:
```
$ rostopic pub /servo_control_commands dynamixel_servos/CommandMessage "servo_id: 21
register_address: 64
bytes_number: 1
value: 1" 
```
##### Zadanie pozycji serwa:
```
$ rostopic pub /servo_control_commands dynamixel_servos/CommandMessage "servo_id: 21
register_address: 116
bytes_number: 4
value: 2000" 
```
gdzie:  
**servo_id** - ID serwa  
**register_address** - adres rejestru  
**bytes_number** - rozmiar rejestru  
**value** - wartość do wpisania

[Tabela zawierająca adresy oraz rozmiary rejestrów](http://support.robotis.com/en/product/actuator/dynamixel_x/xm_series/xm430-w210.htm#bookmark23) 

