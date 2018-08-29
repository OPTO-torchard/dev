# Opto Memory-Mapped Protocol


<a name="Top"></a>

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

all: build Output/liboptommp.a test

build:
        @mkdir -p Output

Output/liboptommp.a: ${LIB_OBJECTS}
        ar rcs $@ ${LIB_OBJECTS}
        ranlib $@

clean:
        rm -rf Output ${LIB_OBJECTS}
        ${MAKE} -C Source/Examples/C++/test clean

test:
        ${MAKE} -C Source/Examples/C++/test

Source/O22SIOMM.o: Source/O22SIOMM.cpp Source/O22SIOMM.h Source/O22SIOUT.h Source/O22STRCT.h

Source/O22SIOST.o: Source/O22SIOST.cpp Source/O22SIOST.h Source/O22SIOUT.h Source/O22STRCT.h

Source/O22SIOUT.o: Source/O22SIOUT.cpp Source/O22SIOUT.h
```

</details>

<details><summary>Details for step `7`, the project Makefile:</summary>

```
TOP_DIR=../../../..
SOURCE_DIR=$(TOP_DIR)/Source
OUTPUT_DIR=$(TOP_DIR)/Output

CXXFLAGS = -I$(SOURCE_DIR) -Wall -D_LINUX -g
LDFLAGS = -pthread

SOURCES=test.cpp
OBJECTS=$(patsubst %.cpp,%.o,${SOURCES})

all: $(OUTPUT_DIR)/test

$(OUTPUT_DIR)/test: $(OUTPUT_DIR)/liboptommp.a ${OBJECTS}
        $(CXX) $(LDFLAGS) -o $@ ${OBJECTS} $(OUTPUT_DIR)/liboptommp.a

clean:
        rm -f *.o $(OUTPUT_DIR)/test

```

</details>

<details><summary>Details for step `8`, example C++ source code:</summary>

~~~ C++
#include "O22SIOMM.h"
#include "O22STRCT.h"
int main() {
        char *address = "127.0.0.1";
        const int module = 0;
        const int point = 8;

        O22SnapIoMemMap dev_EPIC;
        dev_EPIC.OpenEnet2(address, 2001, 10000, 1, SIOMM_TCP);
        for(int i = 0; i < 22; i++) {
                dev_EPIC.SetHDDigitalPointState(module, point, 1);
                usleep(250000);
                dev_EPIC.SetHDDigitalPointState(module, point, 0);
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