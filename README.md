# README

## OptoMMP: Python Scripts

The following Python scripts use OptoMMP thru the socket interface to communicate groov EPIC:

1. `getUptime_mmp` returns the uptime (ms) of the controller: one optional parameter for host.

`python getUptime_mmp.py` will default to localhost.

`python getUptime_mmp.py <hostname or IP address>` will get the given host's uptime.

2. `readModCh_mmp` returns the state of the given module and channel: two required parameters for module and channel number.

`python readModCh_mmp.py 0 1` will read the digital state of localhost module 1, channel 0, and output the result.

3. `writeModChVal_mmp` sets the state of the given module and channel: three required parameters for module number, channel number, and state 1 or 0

`python writeModCh_mmp.py 0 1 1` will write the digital state of localhost module 1, channel 0 to be = 1 (on/true) and attempt confirmation.


## REST API: Python Scripts

The remaining Python scripts use the REST API thru the requests interface to communicate groov EPIC.<br>
You will need the requests library before you can run these scripts on the groov EPIC over SSH:

1. run update (NOT upgrade): `sudo apt-get update`
2. then install pip: `sudo apt-get install python-pip`
3. and finally the requests library: `sudo pip install requests`

Their use is just like the mmp equivalents, they both require module and channel number, and write also requires the new state:

`python readModCh_rest.py 0 1` will read the digital state of localhost module 1, channel 0, and output the result.

`python writeModCh_rest.py 0 1 1` will write the digital state of localhost module 1, channel 0 to be = 1 (on/true) and attempt confirmation.


## OptoMMP: Executable file compiled from C++ code

1. `pluse` Flashes output 22 on module 0 twenty two times. Source code is pulse.cpp, uses the OptoMMP C++ SDK.

`sudo chmod +x pulse` to make the file executable,

`./pulse` to run the program.