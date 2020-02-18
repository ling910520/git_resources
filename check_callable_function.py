class TelNexxHost():
    def __init__(self, A, B, C):
        self._device_status_A = A
        self._device_status_B = B
        self._device_status_C = C

    def __call__(self):
        return "call function"

    @property
    def device_status_A(self):
        return self._device_status_A

    @device_status_A.setter
    def device_status_A(self, value):
        self._device_status_A = value

    @property
    def device_status_B(self):
        return self._device_status_B

    @device_status_B.setter
    def device_status_B(self, value):
        self._device_status_B = value

    @property
    def device_status_C(self):
        return self._device_status_C

    @device_status_C.setter
    def device_status_C(self, value):
        self._device_status_C = value

    def __repr__(self):
        return str(self.__dict__)

    def get(self):
        return [self._device_status_A, self._device_status_B, self._device_status_C]


spt20 = TelNexxHost(12, 2, 2)
returned_from_tools = [22, 22, 22]
if spt20.get() == returned_from_tools:
    pass
else:
    diff = [x for index, x in enumerate(
        zip(spt20.get(), returned_from_tools)) if len(set(x)) != 1]
    setting = {0: "device_status_A", 1: "device_status_B", 2: "device_status_C"}
    print(diff)
    # for val in diff:
    #     setattr(spt20,setting[val],returned_from_tools[val]) 
    #     diff
spt20
