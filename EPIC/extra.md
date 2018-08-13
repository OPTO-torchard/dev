# Developing on _groov_ EPIC

<a name="Top"></a>

## Ignition EDGE

Software developed by Inductive Automation.<br>
Built-in drivers to other PLCs: Allen-Bradle, Seimens, Modbus, SNAP PAC, and groov EPIC compatibility.<br>
Cirus Link MQTT Sparkplug specification.<br>

### OPC-UA

>

### MQTT Sparkplug

Rather than having a tightly-coupled architecture, have a message-broker architecture with a bi-directional publish-subscribe model. Reduces reliance on IT.
* Simplicity: Build from the edge out, publish-subscribe model makes adding new elements straightforward.<br>
* Security: Everything is securely encrypted, a single centralized  place to manage security profiles; the broker.<br>
* Performance: Efficient payloads, minimal overhead, publish on change only, persistent connections.<br>
    With sparkplug you know the state of all tags in the system at all times.

Coming soon:

* Sparkplug - [Configuring the MQTT Broker, Edge Node, and Controller](https://training.opto22.com/sparkplug-configure-the-mqtt-broker-edge-node-and-controller/192670 "training.opto22")

* Sparkplug - [Sparkplug/MQTT and the Control Engine Status](https://training.opto22.com/sparkplug-status-view-for-sparkplug-and-the-control-engine/192716 "training.opto22")

[Top](#Top)

-----

## Node-RED

Ideal for quickly developing IoT applications, Node-RED is a browser-based flow programming environment originally developed by IBM Emerging Technology Services. It is now open-source and has incredible stock features, with the option to import external Node packages — including officially supported PAC and _groov_ nodes. You can use Node-RED on the EPIC processor itself, or access your PAC control tags and _groov_ view tags from another system running Node-RED, for example; a windows or linux computer, the _groov_ Edge Appliance, even from lightweight computers like the Raspberry Pi.<br>
It is both the runtime and editor, ultimately compiling to Javascript. Of particular interest to developers is the function node, which exposes a block of Javascript to the programmer to freely enter raw code that will run in the flow right there on the device.<br>

* Opto 22 Training: [Node-RED - Status, the Editor, Backup and Restore Projects](https://training.opto22.com/series/groov-epic-training-series/node-red-launch-the-editor-view-status-manage-project "training.opto22")

* OptoVideo: [Node-RED Tutorials](https://www.youtube.com/playlist?list=PLKYvTRORAnx6a9tETvF95o35mykuysuOw "YouTube.com/OptoVideo")

* [Node-RED](https://nodered.org/ "NodeRED.org")

    * [Node-Red Flows Library](https://flows.nodered.org/ "flows.NodeRED.org")

[Top](#Top)

-----

## REST API

>

[Top](#Top)

-----

## Python for REST API

To make RESTful requests with Python requests you need to:

1. `sudo apt-get update`

    Do **NOT** apt-get upgrade!
2. `sudo apt-get install python-pip`

    Do **NOT** upgrade pip individually either!
3. `sudo pip install requests`

4. `import requests`

    Import the library to your script once it is installed

* Forum: [EPIC data using RESTful Python](http://forums.opto22.com/t/epic-data-using-restful-python/2038 "OptoForums")

* Developer: [groov Manage REST API](http://developer.opto22.com/groov/manage/ "developer.opto22.com")

[Top](#Top)

## Python for OptoMMP

>

* Forum: [EPIC data using OptoMMP with Python](http://forums.opto22.com/t/epic-data-using-optommp-with-python/2041 "OptoForums")

* Developer: [Getting Started with OptoMMP for Python](http://developer.opto22.com/pythonmmp/ "developer.opto22.com")

* [OptoMMP Protocol Guide](https://www.opto22.com/support/resources-tools/documents/1465-optommp-protocol-guide) (form 1465)

[Top](#Top)

-----

## C++ for OptoMMP

1. Create a new development folder and navigate there.

    `mkdir OptoMMP_CPP`<br>
    `cd OptoMMP_CPP`
2. Download the [C++ SDK from Opto 22](https://www.opto22.com/products/pac-dev-optommp-cplus "PAC-DEV-OPTOMMP-CPLUS"). Right click zip download link, copy link location to clipboard, and then use `wget` to download.

    `wget http://downloads.opto22.com/PAC-DEV-OPTOMMP-CPLUS%20R4.0a-002.zip`
3. Unzip the archive. Use the `tab` key to autocomplete your filename, or make sure you type in the exact release you have.

    `unzip PAC-DEV-OPTOMMP-CPLUS%20R4.0a-002.zip`
4. Create a new master Makefile to compile your source code with the required libraries.<br>
    Detailed contents of this master Makefile are described below.

5. Navigate to the source folder.

    `cd Source`
6. Create a new project source folder and navigate there.

    `mkdir Project`<br>
    `cd Project`
7. Create a new project Makefile, edit it using `nano` or `vim`.<br>
    Detailed contents of this project Makefile are described below.

    `touch Makefile`
8. Create or import your C++ source code file. An example is provided below.

    `touch project.cpp`
9. Leave the project folder, then compile the libraries required and make the project executable in `/Output`

    `cd ..`<br>
    `make`
10. Navigate to and run the executable, provided there were no compiler errors.

    `cd Output`<br>
    `./project`

<details><summary>Details for step `4`, the master Makefile:</summary>

```
CXXFLAGS = -I$(SRC_DIR) -Wall -D_LINUX -g

LIB_SOURCES=$(wildcard Source/*.cpp)
LIB_OBJECTS=$(patsubst %.cpp,%.o,${LIB_SOURCES})

all: build Output/liboptommp.a pulse

build:
        @mkdir -p Output

Output/liboptommp.a: ${LIB_OBJECTS}
        ar rcs $@ ${LIB_OBJECTS}
        ranlib $@

clean:
        rm -rf Output ${LIB_OBJECTS}
        ${MAKE} -C Source/Examples/C++/pulse clean

pulse:
        ${MAKE} -C Source/Examples/C++/pulse

Source/O22SIOMM.o: Source/O22SIOMM.cpp Source/O22SIOMM.h Source/O22SIOUT.h Source/O22STRCT.h

Source/O22SIOST.o: Source/O22SIOST.cpp Source/O22SIOST.h Source/O22SIOUT.h Source/O22STRCT.h

Source/O22SIOUT.o: Source/O22SIOUT.cpp Source/O22SIOUT.h
```

</details>

<details><summary>Details for step `7`, the project Makefile:</summary>

```
CXXFLAGS = -I../../../../Source -Wall -D_LINUX -g
LDFLAGS = -pthread

SOURCES=pulse.cpp
OBJECTS=$(patsubst %.cpp,%.o,${SOURCES})

all: ../../../../Output/pulse

../../../../Output/pulse: ../../../../Output/liboptommp.a ${OBJECTS}
        $(CXX) $(LDFLAGS) -o $@ ${OBJECTS} ../../../../Output/liboptommp.a

clean:
        rm -f *.o ../../../../Output/pulse
```

</details>

<details><summary>Details for step `8`, example C++ source code:</summary>

~~~ C++
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string>
#ifndef _WINSOCK_DEPRECATED_NO_WARNINGS
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#endif
#include "O22SIOMM.h"
#include "O22STRCT.h"

int main(int nArgs, char *pcharyArgs[])
{
        O22SnapIoMemMap objEpic;
        char *address = "127.0.0.1";
        const int modN = 0;
        const int ptN = 8;
        int nResult;

        // open a TCP connection
        nResult = objEpic.OpenEnet2(address, 2001, 10000, 1, SIOMM_TCP);
        if (nResult != SIOMM_OK) {
                printf("OpenEnet2 reports result %d, exiting.\n", nResult);
                exit(0);
        }

        // wait for the TCP connect to complete, not necessary for UDP
        usleep(100000);

        //      pulse the point 22 times:
        for(int i = 0; i < 22; i++) {
                nResult = objEpic.SetHDDigitalPointState(modN, ptN, 1);
                if (nResult != SIOMM_OK) {      // turn the point on
                        printf("Set digital point ON reports %d. Exiting.\n", nResult);
                        exit(0);
                }
                usleep(250000);
                nResult = objEpic.SetHDDigitalPointState(modN,ptN, 0);
                if (nResult != SIOMM_OK) {      // turn the point off
                        printf("Set digital point OFF reports %d. Exiting.\n", nResult);
                        exit(0);
                }
                usleep(250000);
        }

        return 0;
}
~~~

</details>

<br>

 * [C++ for OptoMMP](/cpp/)

    * [SDK product page](https://www.opto22.com/products/pac-dev-optommp-cplus)

    * [SDK download page](https://www.opto22.com/support/resources-tools/downloads/pac-dev-optommp-cpp)

[Top](#Top)

-----

## Java

>

[Top](#Top)