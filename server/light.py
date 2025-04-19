import RPi.GPIO as GPIO
import time
import database

FUNCTIONS = ['green', 'orange', 'red']


class Light:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.state = database.get_light_state(name)
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self._set(self.state)

    def _set(self, state):
        if state == self.state:
            print('%s is equal %s' % (state, self.state,))

        print('setting %s state to: %s' % (self.name, state,))
        GPIO.output(self.pin, GPIO.LOW if state == GPIO.HIGH else GPIO.HIGH)
        self.state = state
        database.set_light_state(self.name, state)

    def on(self):
        self._set(GPIO.HIGH)

    def off(self):
        self._set(GPIO.LOW)

    def flash(self, count=2, interval=0.2):
        for _ in range(count):
            self.on()
            time.sleep(interval)
            self.off()
            time.sleep(interval)


class Tower:
    def __init__(self, pinList):
        self.pins = pinList
        self.setupLights()
        self.green: Light
        self.orange: Light
        self.red: Light

    def setupLights(self):
        if len(FUNCTIONS) != len(self.pins):
            raise ValueError("only %s pins provided, but %s available" %
                             (len(self.pins), len(FUNCTIONS)))

        for pin in self.pins:
            light = Light(pin['pin'], pin['name'])
            if light.name == 'green':
                self.green = light
            elif light.name == 'orange':
                self.orange = light
            elif light.name == 'red':
                self.red = light

    def on(self):
        self.green.on()
        self.orange.on()
        self.red.on()

    def off(self):
        self.green.off()
        self.orange.off()
        self.red.off()
