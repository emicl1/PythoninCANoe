import vector.canoe
import vector.canoe.measurement

@vector.canoe.measurement_script        #required decorator
class CANoe:
    def __init__(self):
        pass

    @vector.canoe.on_key("a")
    def key_a_pressed(self, char: str):
        vector.canoe.write('key a pressed')

    @vector.canoe.on_key("b")
    def key_b_pressed(self, char: str):
        vector.canoe.write(vector.canoe.measurement.get_current_time_in_ns())

