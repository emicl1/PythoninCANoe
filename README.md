## Python in CANoe


### Prerequisites
[Python version 3.9.2 32 bit](https://www.python.org/downloads/release/python-392/)

Vector CANoe 17 --> configuration file is provided in the repository

### Using a Python editor 
You can edit Python scripts by using VS Code or PyCharm. However, you need to open CANoe and 
select File->Options->External Programs->Tools->Python file editor and select the editor you want by 
selecting Edit_Python_Source_With_VisualStudioCode.vbs for VS Code 
or Edit_Python_Source_With_PyCharm.vbs for PyCharm.
The files should be located in Vector CANoe 17 -> Exec64 -> Scripts

### How to use Python in CANoe

There are two main ways to use Python in CANoe. The first one is to use the 
[CANoe Python API](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/Shared/PythonAPI.htm?TocPath=Technical%2520References%257CPython%2520API%257C_____0).
The second one is to use the [COM interface](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/COMInterface/COMInterface.htm?TocPath=Technical%2520References%257C_____1). 

### Using the CANoe Python API

To access the CANoe Python API, you need to open the Communication Setup and click on Add Application Model where 
you can select your Python script. After selecting the script, you can right-click on it and select the State, either 
on or off. CANoe Python programming and API is described in [CANoe help file](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/Shared/PythonAPI.htm?TocPath=Technical%2520References%257CPython%2520API%257C_____0).

##### Usage of the API
The CANoe Python API is a set of functions that can be used to access the CANoe environment. There are four main modules 
that can be used: vector.canoe, vector.canoe.tfs, vector.canoe.measurement, and vector.canoe.threading.

**vector.canoe** contains general parts of the Python API

**vector.canoe.tfs** contains methods for accessing the Test Feature Set

**vector.canoe.measurement** contains methods for getting the current time of simulation and stopping the simulation.

**vector.canoe.threading** contains methods for creating threads and accessing the CANoe environment from these threads.

**!!WARNING!!**
after importing desired modules, the script must contain exactly one class that has the **vector.canoe.measurement_script** decorator and 
the class must have a default constructor.

Example is provided in the PythonAPI.py file. 

### Using the COM interface                                                                                                                                                                                                                                                                                                                                                       

Unlike the CANoe Python API, the COM interface has no need to be established in the Communication Setup. You just need to 
run the Python script in your editor. There are two ways to establish the COM interface. The first one is to use the
win32com.client module. The second one is to use the dll files provided by Vector.
All the documentation about the COM interface can be found in the [CANoe help file](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/COMInterface/COMInterface.htm?TocPath=Technical%2520References%257C_____1).

##### Usage of the win32com.client module

To use the win32com.client module, you need to import it in your script. Then you need to create a CANoe application object
and connect it to the CANoe application. After that, you can use the CANoe application object to access the CANoe environment.

Example is provided by the [py_canoe module](https://github.com/chaitu-ycr/py_canoe), which even has already
implemented some functions for starting measurement, sending signals to CAN network and so on.

##### Usage of the dll files provided by Vector

To use the dll files provided by Vector, you need to download the Pythonnet module by running the following command in the command line:
```pip install pythonnet```
and also downloading all the [requirements](https://github.com/pythonnet/pythonnet/blob/master/requirements.txt)

After that, you need to import the clr module, load the file, add the reference to the CANoe dll file and import CANoe.

**Example is provided in the COMInterface.py file.**

#### Issues with the COM interface

First issue is with the [COM interface documentation](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/COMInterface/COMInterface.htm?TocPath=Technical%2520References%257C_____1)
which is sometimes not clear enough or incomplete. For example, the documentation for the [CANoe networks is wrong](file:///C:/Program%20Files/Vector%20CANoe%2017/Help01/CANoeCANalyzerHTML5/CANoeCANalyzer.htm#Topics/COMInterface/Objects/COMObjectNetworks.htm).
The object should be easily accessible by using the following code:
```self.networks = CANoe.Network(self.CANoeApp.Networks)```, but rather than that, you need to use the following code:
```self.networks = self.CANoeApp.get_Networks```.

Second issue also comes down to the documentation. In this case some methods and attributes are described in the documentation, but they cannot be used.
For example, the ```objects.Item(index)``` method is described in the documentation, but it cannot be used or there might be a way
to use it, but it is not described in the documentation.

























