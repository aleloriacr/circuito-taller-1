Set_PWM()
basic.forever(function on_forever() {
    
    MotorCD(Pot())
    ServoMotor(Pot())
    led.plotBarGraph(Fotocelda(), 800)
})
function Set_PWM() {
    pins.analogWritePin(AnalogPin.P14, 512)
    pins.analogSetPeriod(AnalogPin.P14, 1000)
}

function Pot(): number {
    return pins.analogReadPin(AnalogPin.P0)
}

function Fotocelda(): number {
    return pins.analogReadPin(AnalogPin.P1)
}

function MotorCD(val: number) {
    pins.analogWritePin(AnalogPin.P14, val)
}

function ServoMotor(val: number) {
    let pos = pins.map(val, 0, 1023, 0, 180)
    pins.servoWritePin(AnalogPin.P5, pos)
}

