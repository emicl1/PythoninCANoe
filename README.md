## Python in CANoe


### Prerequisites
[Python version 3.9.2 32 bit](https://www.python.org/downloads/release/python-392/)

Vector CANoe 17

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
on or off.

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



