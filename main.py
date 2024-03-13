def on_ir_button_right_pressed():
    global isRunning
    isRunning = not (isRunning)
    if isRunning == False:
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
makerbit.on_ir_button(IrButton.RIGHT,
    IrButtonAction.PRESSED,
    on_ir_button_right_pressed)

isRunning = False
maqueenPlusV2.i2c_init()
makerbit.connect_ir_receiver(DigitalPin.P16, IrProtocol.KEYESTUDIO)
basic.show_icon(IconNames.HEART)

def on_forever():
    if isRunning:
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_M) == 1:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
                maqueenPlusV2.MyEnumDir.FORWARD,
                30)
        else:
            if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 0 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 1:
                maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
                    maqueenPlusV2.MyEnumDir.FORWARD,
                    70)
                maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
                    maqueenPlusV2.MyEnumDir.FORWARD,
                    10)
            else:
                if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L1) == 1 and maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R1) == 0:
                    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
                        maqueenPlusV2.MyEnumDir.FORWARD,
                        70)
                    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
                        maqueenPlusV2.MyEnumDir.FORWARD,
                        10)
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_R2) == 1:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
                maqueenPlusV2.MyEnumDir.BACKWARD,
                25)
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
                maqueenPlusV2.MyEnumDir.FORWARD,
                25)
        if maqueenPlusV2.read_line_sensor_state(maqueenPlusV2.MyEnumLineSensor.SENSOR_L2) == 1:
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
                maqueenPlusV2.MyEnumDir.FORWARD,
                25)
            maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
                maqueenPlusV2.MyEnumDir.BACKWARD,
                25)
basic.forever(on_forever)
