from st2reactor.sensor.base import PollingSensor

from base import get_environ

from lib.base import get_uuid_4


class FibonacciSensor(PollingSensor):

    def __init__(self, sensor_service, config,
                 poll_interval=5):
        super(FibonacciSensor, self).__init__(
            sensor_service=sensor_service,
            config=config,
            poll_interval=poll_interval
        )
        self.a = None
        self.b = None
        self.count = None

    def setup(self):
        self.a = 0
        self.b = 1
        self.count = 2

    def poll(self):
        fib = self.a + self.b
        self.sensor_service.get_logger('lib_test').info('UUID: %s', get_uuid_4())
        payload = {
            "count": self.count,
            "fibonacci": fib,
            "pythonpath": get_environ("PYTHONPATH"),
            "uuid": get_uuid_4()
        }

        self.sensor_service.dispatch(trigger="lib_test.fibonacci", payload=payload)
        self.a = self.b
        self.b = fib
        self.count = self.count + 1

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass
