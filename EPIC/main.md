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

## General Use of _groov_ EPIC

[groov EPIC Training Series](https://training.opto22.com/series/groov-epic-training-series, "training.opto22")

* [Initializing groov EPIC](https://training.opto22.com/series/groov-epic-training-series/maintenance-course "training.opto22.com")
* [Maintenance - Backup, Restore, Update](https://training.opto22.com/series/groov-epic-training-series/maintenance-backup-restore-update-1, "training.opto22")
* [System - Display (calibration, external monitor, mouse & keyboard)](https://training.opto22.com/series/groov-epic-training-series/system-display, "training.opto22")
* [Reset to Factory Defaults (video)](https://training.opto22.com/hardware-resetting-to-factory-defaults/211962, "training.opto22")



[Top](#Top)

## Shell access / SSH

A shell license is required to use SSH, you can get one from [Opto 22](https://www.opto22.com/ "opto22.com")

* Opto 22 Training: [Downloading and Running Custom Programs](https://training.opto22.com/series/groov-epic-training-series/downloading-and-running-custom-programs/196374 "training.opto22")<br>

The _groov_ EPIC processor runs a custom build of [Yocto](https://www.yoctoproject.org "Yocto Project") Linux as it's operating system, this is what you will be interacting with over SSH.<br>
Experience developing applications from a Unix system command line is extremely helpful here, since there is no traditional user interface (UI) to interact with the operating system, only the _groov_ Manage and _groov_ View interfaces.

Here are a few tasks and associated commands for working from the command line:

* Navigating

    * `pwd` - **print** working directory; Output the full path to the current folder.

    * `ls` - **list**; Output a list of all files in the current folder.

        * `ls -a` - **list all**; Output list will also include hidden files.

        * `ls -l` - **list long**; Output full details of the files.

        * `ls -la` - Use multiple flags to combine their functionality. For example; to display all files and their details.

    * `cd <dir>` - **change directory**; Jump from the current directory to `dir`.<br>
    You can give partial and full paths here, so you don't have to jump every single folder individually.<br>
    Use `..` to go up on folder, `../..` to go up two, and so on.

* Managing files

    * `touch <file>` - **touch**; Creates `file` if it does not exist, and updates the modification time if it does.

    * `mv <file> <dest>` - **move**; Moves `file` to `dest`, where `dest` can be a single folder or full path.<br>
        Use this to rename files by putting just the name and no path in `dest`.

    * `cp <file> <dest>` - **copy**; Copies `file` to `dest`, where the destination can be used to rename the copy.

    * `rm <file>` - **remove**; Deletes `file` from the current directory, or you can include a full path.

        * `rm -rf <dir>` - **remove folder**; The addition of the `-rf` flag allows for the removal of entire folders.

    * `*` - **wildcard**; matches all files in the current directory, or if used mid-file, for example; `rm o*.txt` will delete all text files that begin with the letter 'o'.

* Editing files

    * `nano <file>` - **nano** is a simple command line editor, similar to Notepad it has basic features.

    * `vim <files>` - **vim** is "**vi** i**m**proved", where vi is a Unix text editor.<br>
    They both have a higher learning curve than nano, but may be worth using because they have syntax highlighting for most popular languages such as: C++, Python, Java, Javascript, and even Markdown.

* GitHub:<br>
    <p>On the topic of managing files and folder structures, many developers choose to manage their source code with GitHub repositories.<br>
    GitHub is a web-based version control service primarily used for computer code, and is extremely popular due to the way it handles branching of features to develop code without damaging the 'master' release branch. Using GitHub, multiple people can be working on different branches —or contributing to the same branch— then compare their local versions, to the master, and safely merge all the features together, handling conflicts if and when they arse, all while being able to review and restore all previous versions and changes.</p>
    GitHub not only handles version control but also is a way to have your data backed up in case anything happens to your device. It is recommended to have major programs backed up in three places: an on-site backup, an off-site backup, and a secure (physically isolated or password protected) backup.

[Top](#Top)

-----

## _groov_ Manage, _groov_ View, and PAC Control

> ...

[Top](#Top)

-----

## REST API

Representational State Transfer (REST)

You can make RESTful requests either on the device (localhost) or from elsewhere on the network, all you need is a request interface (a web browser or cUrl work too), the IP or hostname of your device, and of course the request URL and authentication key. The [_groov_ View REST API](http://developer.opto22.com/groov/view/ "Getting Started (developer.opto22.com)") and [_groov_ Manage REST API](http://developer.opto22.com/groov/manage/ "Getting Started (developer.opto22.com)") both support get and put/post requests, so it's possible to both read tags and I/O as well as write over tags and control outputs, depending on your application. The details of the request URL to access _groov_ View tags are in the [_groov_ View REST API Reference](http://developer.opto22.com/static/generated/groov-rest-api/swagger-ui/index.html?url=/static/generated/groov-rest-api/swagger.yaml "Swagger UI"), and _groov_ EPIC I/O requests are detailed in the  [_groov_ Manage REST API Reference](http://developer.opto22.com/static/generated/manage-rest-api/swagger-ui/index.html "Swagger UI")

If you want to execute RESTful programs to make requests from the EPIC processor itself you will need a shell license -- but you do not need one to RESTfully access the data from another device.


[Top](#Top)

## OptoMMP

OptoMMP is a memory-mapped protocol based on the [IEEE 1394 standard](https://standards.ieee.org/findstds/standard/1394-2008.html "IEEE Standards Association") that is used to create custom software applications for remote monitoring, industrial control, and data acquisition. For full details, see the [OptoMMP Protocol Guide](https://www.opto22.com/support/resources-tools/documents/1465-optommp-protocol-guide) (form 1465).

* [C++ for OptoMMP](http://developer.opto22.com/cpp "developer.opto22")

* [Getting Started with OptoMMP for Python](http://developer.opto22.com/pythonmmp/ "developer.opto22")

* [.NET OptoMMP SDK](https://www.opto22.com/support/resources-tools/downloads/pac-dev-optommp-dotnet "opto22.com/downloads")

[Top](#Top)