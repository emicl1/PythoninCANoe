import clr
from System.Reflection import Assembly

Assembly.LoadFile('C:\Program Files\Vector CANoe 17\Exec64\Vector.CANoe.Interop.dll')  # load .NET DLL file
clr.AddReference('Vector.CANoe.Interop')  # add reference to .NET DLL file
import CANoe

function2 = None


class CanoeMeasurementEvents:
    @staticmethod
    def OnInit():
        print("OnInit")
        function2 = CANoe.CAPLFunction(mCANoeCAPL.GetFunction('square'))  # cast here is necessary


class CANoeclass:
    """
    This class is used to open CANoe and start measurement and call CAPL function
    CAPL function is called in OnInit event handler and then it's passed to a varibale
    so that it can be called in any other function.
    !!!!function must be defined in CANoe in Measurement Setup !!!!
    """

    def open_can(self):
        self.mCANoeApp = CANoe.Application()
        self.mCANoeMeasurement = self.mCANoeApp.Measurement
        self.mCANoeEnv = CANoe.Environment(self.mCANoeApp.Environment)
        self.mCANoeBus = CANoe.Bus(self.mCANoeApp.get_Bus("CAN"))
        self.mCANoeSys = CANoe.System(self.mCANoeApp.System)
        self.mCANoeNamespaces = CANoe.Namespaces(self.mCANoeSys.Namespaces)

        self.mCANoeMeasurement.OnInit += CANoe._IMeasurementEvents_OnInitEventHandler(self.OnInit)

        # accessing nodes through simulation setup
        self.mCANoeSimSetup = CANoe.SimulationSetup(self.mCANoeConfig.SimulationSetup)
        self.mCANoeNodes = CANoe.Nodes(self.mCANoeSimSetup.Nodes)
        # self.mCANoeNode = classmethod(self.mCANoeNodes.Item(0))    #should be used to access nodes, but it's not
        # working

        # trying to access devices through networks
        self.mCANoeNetwork = self.mCANoeApp.get_Networks
        # self.mCANoeNetwork.Item(1)                           #should be used to access networks, but it's not working

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
