# Developing on _groov_ EPIC

<a name="Top"></a>

From PAC control and _groov_ View to the REST API and OptoMMP, there's no shortage of ways to access the data on your Edge Programmable Industrial Controller, it's just a matter of which method to get what data, and how to apply that method.<br>
Your specific application and experience level will largely determine your development method, where most applications are best handled using PAC control flows for control and groov view pages for monitoring. If you are adding to existing architecture or already have experience in another language, however, you may find that the Opto Memory-Mapped protocol or RESTful API is more appropriate for you, although working with them often requires accessing the device command line through secure shell or SSH.

## Secure Shell (SSH)

A shell license is required to use SSH, you can get one from [Opto 22](https://www.opto22.com/ "opto22.com")

* Opto 22 Training: [Downloading and Running Custom Programs](https://training.opto22.com/series/groov-epic-training-series/downloading-and-running-custom-programs/196374 "training.opto22")<br>

>

[Top](#Top)

## Representational State Transfer (REST)

See more details about the [REST API with groov EPIC](/EPIC/epic-rest/).

The RESTful application program interface (API) uses HTTP requests to get, put, and post data to and from the _groov_ EPIC. Because it simply uses URLs, the interface is straightforward and easy to use with chrome, curl, programming languages like Java, Python, and C, as well as desktop applications like Postman.<br>
Both [_groov_ View](/groov/view/) and [_groov_ Manage](/groov/manage/) have REST API implementations, so you can use RESTful requests to access both _groov_ data store tags and data and control for all installed I/O modules.

[Top](#Top)

## Opto Memory-Mapped Protocol (OptoMMP)

See more details about [OptoMMP with groov EPIC](/EPIC/epic-mmp/).

OptoMMP is a memory-mapped protocol based on the [IEEE 1394 standard](https://standards.ieee.org/findstds/standard/1394-2008.html "IEEE Standards Association") that is used to create custom software applications for remote monitoring, industrial control, and data acquisition. For full details, see the [OptoMMP Protocol Guide](https://www.opto22.com/support/resources-tools/documents/1465-optommp-protocol-guide) (form 1465).

[Top](#Top)

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

## General Use of _groov_ EPIC

[groov EPIC Training Series](https://training.opto22.com/series/groov-epic-training-series, "training.opto22")
* [Initializing groov EPIC](https://training.opto22.com/series/groov-epic-training-series/maintenance-course "training.opto22.com")

* [Maintenance - Backup, Restore, Update](https://training.opto22.com/series/groov-epic-training-series/maintenance-backup-restore-update-1, "training.opto22")

* [System - Display (calibration, external monitor, mouse & keyboard)](https://training.opto22.com/series/groov-epic-training-series/system-display, "training.opto22")

* [Reset to Factory Defaults (video)](https://training.opto22.com/hardware-resetting-to-factory-defaults/211962, "training.opto22")


[Top](#Top)