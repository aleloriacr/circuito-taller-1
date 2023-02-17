Set_PWM()

def on_forever():
    pass
    MotorCD(Pot())
    ServoMotor(Pot())    
    led.plot_bar_graph(Fotocelda(), 800)
basic.forever(on_forever)


def Set_PWM():
    pins.analog_write_pin(AnalogPin.P14, 512)
    pins.analog_set_period(AnalogPin.P14, 1000)

def Pot():
    return pins.analog_read_pin(AnalogPin.P0)

def Fotocelda():
    return pins.analog_read_pin(AnalogPin.P1)
    
def MotorCD(val):
    pins.analog_write_pin(AnalogPin.P14, val) 

def ServoMotor(val):
    pos = pins.map(val,0,1023,0,180)
    pins.servo_write_pin(AnalogPin.P5, pos)
    
def ServoMotor1(val):
    pos = pins.map(val,0,1023,0,180)
    pins.servo_write_pin(AnalogPin.P5, pos)
