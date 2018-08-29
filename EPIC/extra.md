# Developing on _groov_ EPIC

<a name="Top"></a>

## Ignition EDGE

Software developed by Inductive Automation.<br>
Built-in drivers to other PLCs: Allen-Bradley, Siemens, Modbus, SNAP PAC, and _groov_ EPIC compatibility.<br>
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

## LINUX

The _groov_ EPIC processor runs a custom build of [Yocto](https://www.yoctoproject.org "Yocto Project") Linux as it's operating system, this is what you will be interacting with over SSH.<br>
Experience developing applications from a Unix system command line is extremely helpful here, since there is no traditional user interface (UI) to interact with the operating system, only the _groov_ Manage and _groov_ View interfaces.

Here are a few tasks and associated commands for working from the command line:

<details><summary>Useful Linux commands</summary>

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

</details>

* Editing files

    * `nano <file>` - **nano** is a simple command line editor, similar to Notepad it has basic features.

    * `vim <files>` - **vim** is "**vi** i**m**proved", where vi is a Unix text editor.<br>
    They both have a higher learning curve than nano, but may be worth using because they have syntax highlighting for most popular languages such as: C++, Python, Java, Javascript, and even Markdown.

* GitHub:<br>
    
    <p>On the topic of managing files and folder structures, many developers choose to manage their source code with GitHub repositories (repos).<br>
    GitHub is a web-based version control service primarily used for computer code, and is extremely popular due to the way it handles branching of features to develop code without damaging the 'master' release branch. Using GitHub, multiple people can be working on different branches —or contributing to the same branch— then compare their local versions, to the master, and safely merge all the features together, handling version discrepancies if and when they arise, all while being able to review and restore all previous versions and changes.<br>
    GitHub not only provides an easy way to share code and manage versions, it also provides a reliable way to have your data backed up in case anything happens to your device.</p>

<details><summary>Useful Git Commands</summary>

* `git` - **git** is the main command used to manage git repositories:

* `git init` - This command makes the current folder a GitHub repository.

* `git clone <repo>` - Creates a local repository in a new folder, cloned from `repo`.

* `git add <file>` - Tells GitHub to 'stage' this file in the repo, ready to be added.

* `git commit -m <message>` - Commits all staged changes to the local repository.

* `git push -u <source> <destination>` - Updates the `destination` repo with changes commited to the `source` repo.<br>
For example, to push local changes up to the master branch use `git push -u origin master`.

* `git pull` - Updates the local repo with any difference between it and the head of the current branch.<br>
This command is essentially two commands called in sequence, but they can be called separately as well:

    * `git fetch` - Gets updates for the local repo without applying them, useful to check differences.

    * `git merge` - Applies fetched differences to the local repo.

* `git branch` - Lists all branches of the current folder's associated repository.

* `git branch <name>` - Creates a new remote branch titled `name`, taking refs from the current repo.

* `git ls-remote` - Lists all remote branches, including those not on the device.

* `git checkout <branch>` - Makes `branch` the current working branch. By default, the main branch is `master`.

* `git checkout --track <remote>/<branch>` - Adds a new local branch at this `remote` to track the given `branch`.<br>
For example; `git checkout --track origin/distantBranch`

</details>
<br>

[Top](#Top)