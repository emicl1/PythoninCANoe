import clr
from System.Reflection import Assembly
Assembly.LoadFile('C:\Program Files\Vector CANoe 17\Exec64\Vector.CANoe.Interop.dll')                # load .NET DLL file
clr.AddReference('Vector.CANoe.Interop')                      # add reference to .NET DLL file
import CANoe

function2 = None

class CANoeclass:
    """
    This class is used to open CANoe and start measurement and call CAPL function
    CAPL function is called in OnInit event handler and then it's passed to a varibale
    so that it can be called in any other function.
    !!!!function must be defined in CANoe in Measurement Setup !!!!
    """

    def open_can(self):
        self.mCANoeApp = CANoe.Application()
        self.mCANoeMeasurement = self.mCANoeApp.Measurement  # change here: no cast necessary
        self.mCANoeEnv = CANoe.Environment(self.mCANoeApp.Environment)
        self.mCANoeBus = CANoe.Bus(self.mCANoeApp.get_Bus("CAN"))
        self.mCANoeSys = CANoe.System(self.mCANoeApp.System)
        self.mCANoeNamespaces = CANoe.Namespaces(self.mCANoeSys.Namespaces)
        self.mCANoeCAPL = CANoe.CAPL(self.mCANoeApp.CAPL)
        self.mCANoeMeasurement.OnInit += CANoe._IMeasurementEvents_OnInitEventHandler(self.OnInit)

    def OnInit(self):
        global function2
        print("OnInit")
        function2 = CANoe.CAPLFunction(mCANoeCAPL.GetFunction('square'))  # cast here is necessary

    def callFunction(self):
        result = function2.Call()


    def start_measurement(self):
        self.mCANoeMeasurement.Start()




if __name__ == "__main__":
    can = CANoeclass()
    can.open_can()
    can.start_measurement()
    can.callFunction()
