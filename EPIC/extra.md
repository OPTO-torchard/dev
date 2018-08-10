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
* Sparkplug - [Configuring the MQTT Broker, Edge Node, and Controller](https://training.opto22.com/sparkplug-configure-the-mqtt-broker-edge-node-and-controller/192670 "training.opto22")<br>
* Sparkplug - [Sparkplug/MQTT and the Control Engine Status](https://training.opto22.com/sparkplug-status-view-for-sparkplug-and-the-control-engine/192716 "training.opto22")<br>

[Top](#Top)

-----

## Node-RED

Ideal for quickly developing IoT applications, Node-RED is a browser-based flow programming environment originally developed by IBM Emerging Technology Services. It's now open-source and has incredible stock features, with the option to import external Node packages, including officially supported PAC and _groov_ nodes. You can use Node-RED on the EPIC processor itself, or access your PAC control tags and _groov_ view tags from another system running Node-RED like a windows or linux computer, the _groov_ Edge Appliance, even from lightweight computers like the Raspberry Pi.<br>
It is both the runtime and editor, ultimately compiling to Javascript. Of particular interest to developers is the function node, which exposes a block of Javascript to the programmer to freely enter raw code.<br>

* Opto 22 Training: [Node-RED - Status, the Editor, Backup and Restore Projects](https://training.opto22.com/series/groov-epic-training-series/node-red-launch-the-editor-view-status-manage-project "training.opto22")<br>
* [Node-RED](https://nodered.org/ "NodeRED.org")
    * [Node-Red Flows Library](https://flows.nodered.org/ "flows.NodeRED.org")

[Top](#Top)

## C++

>

[Top](#Top)

-----

## Python

### REST API

To make RESTful requests with Python requests you need to:

1. `sudo apt-get update`

    Do **NOT** apt-get upgrade!
2. `sudo apt-get install python-pip`

    Do **NOT** upgrade pip individually either!
3. `sudo pip install requests`

4. `import requests`

    Import the library to your script once it is installed

### OptoMMP


[Top](#Top)

-----

## Java

>

[Top](#Top)