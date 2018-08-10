# Developing on _groov_ EPIC

<a name="Top"></a>

## Documentation

Your most powerful tool as a developer is documentation. You will need to regularly consult specifications, descriptions, and other reference material while developing custom applications, even if you have experience. Both official documentation and google results can be extremely helpful.

Some of your best Opto resources are:

* [Developer Site](http://developer.opto22.com/ "developer.opto22")
* [Training Site](https://training.opto22.com/ "training.opto22")
    * [Workshops](http://workshops.opto22.com/ "workshops.opto22")
* [YouTube Channel](https://www.youtube.com/user/OptoVideo "OptoVideo")
* [Opto22 Support](https://www.opto22.com/support "opto22 support")
    * [Resources & Tools](https://www.opto22.com/support/resources-tools "resources & tools")<br>
        Here you can find and filter by documents, downloads, videos, case studies, data sheets, drawings, firmware, images, knowledge base, manuals, pressroom, release notes, software, SKDs and integration kits, white papers, compliance, samples and utilities, and finally demos.
        There are lot of resources available!

Some good outside sources:

* <b>[google](https://google.com/ "google.com")</b>
* [Node-RED](https://nodered.org/ "NodeRED.org")
    * [Node-Red Flows Library](https://flows.nodered.org/ "flows.NodeRED.org")
* [w3Schools](https://www.w3schools.com/ "w3schools.com")


[Top](#Top)

## General Use of groov EPIC

[groov EPIC Training Series](https://training.opto22.com/series/groov-epic-training-series, "training.opto22")

* [Initializing groov EPIC](https://training.opto22.com/series/groov-epic-training-series/maintenance-course "training.opto22.com")
* [Maintenance - Backup, Restore, Update](https://training.opto22.com/series/groov-epic-training-series/maintenance-backup-restore-update-1, "training.opto22")
* [System - Display (calibration, external monitor, mouse & keyboard)](https://training.opto22.com/series/groov-epic-training-series/system-display, "training.opto22")
* [Reset to Factory Defaults (video)](https://training.opto22.com/hardware-resetting-to-factory-defaults/211962, "training.opto22")



[Top](#Top)

## Shell access / SSH

* Opto 22 Training: [Downloading and Running Custom Programs](https://training.opto22.com/series/groov-epic-training-series/downloading-and-running-custom-programs/196374 "training.opto22")<br>

* A shell license is required to use SSH.



[Top](#Top)

## Linux

The _groov_ EPIC processor runs a custom build of [Yocto](https://www.yoctoproject.org, "Yocto Project") Linux as it's operating system, it is what you will be interacting with over SSH.<br>
Experience developing applications from a Unix system command line is extremely helpful here, since there is no traditional user interface (UI) to interact with the operating system, only the _groov_ Manage and _groov_ View interfaces (both are described below). 



[Top](#Top)

## _groov_ Manage

* Opto 22 Training: [groov Manage - Introduction](https://training.opto22.com/groov-manage-introduction/ "training.opto22")<br>



[Top](#Top)

## REST API
You can make rest requests on the device (localhost) or from elsewhere in the network to access data on the device (via IP or hostname).

If you want to execute RESTful programs to make requests from the EPIC processor itself you will need a shell license -- but you do not need one to RESTfully access the data from elsewhere in the network.

To make RESTful requests with Python requests you need to:

1. `sudo apt-get update`

    Do **NOT** apt-get upgrade!
2. `sudo apt-get install python-pip`

    Do **NOT** upgrade pip individually either!
3. `sudo pip install requests`

4. `import requests`

    Import the library to your script once it is installed



[Top](#Top)

## OptoMMP

OptoMMP is a memory-mapped protocol based on the [IEEE 1394 standard](https://standards.ieee.org/findstds/standard/1394-2008.html "IEEE Standards Association") that is used to create custom software applications for remote monitoring, industrial control, and data acquisition. For full details, see the [OptoMMP Protocol Guide](https://www.opto22.com/support/resources-tools/documents/1465-optommp-protocol-guide) (form 1465).

* [C++ for OptoMMP](http://developer.opto22.com/cpp "developer.opto22")
* [Getting Started with OptoMMP for Python](http://developer.opto22.com/pythonmmp/ "developer.opto22")


[Top](#Top)

## Node-RED

* Opto 22 Training: [Node-RED - Status, the Editor, Backup and Restore Projects](https://training.opto22.com/series/groov-epic-training-series/node-red-launch-the-editor-view-status-manage-project "training.opto22")<br>
* [Node-RED](https://nodered.org/ "NodeRED.org")
    * [Node-Red Flows Library](https://flows.nodered.org/ "flows.NodeRED.org")



[Top](#Top)