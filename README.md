# WomoLIN MainUnit
Firmware for the WomoLIN main unit controller board.

## Getting started
* Structure of the repo
* Basic software architecture
* Further readings: [Wiki](https://github.com/muccc/WomoLIN-Sw-MainUnit/wiki/Home)

## Developing
Clone this repository: `git clone --recurse-submodules https://github.com/muccc/WomoLIN-Sw-MainUnit.git`.

* Available Docker images
* Simulation?
* Testing?
* IDE support?

## Building
We are using `cmake` to build the firmware binaries. You can use the docker scripts provided in [Docker](tree/develop/Docker) on a UNIX-based OS with the steps listed below. If you know what you are doing, you can also have a look at the `Dockerfile` for gcc9. You will find the list of dependencies there.

1. Make sure the docker engine is installed on your system, see https://docs.docker.com/engine/install/
1. Run the following commands in the root of you local working copy of this repository. Make sure your clone of the repo is inside your home folder to be able to access it from within the docker container.  
`$ cd Docker`  
`$ ./build_linux.sh`  
`$ ./build_gcc9.sh`

1. Now you can enter the docker container containing the build environment by executing the `start_gcc9.sh` script in the `Docker` directory. You should now be provided with a shell inside the container.
1. Start building within the container's shell by executing the following commands:  
`$ cd path/to/WomoLIN-SW-MainUnit/`  
`$ mkdir -p build`  
`$ cd build`  
`$ cmake -DCMAKE_TOOLCHAIN_FILE=../arm-gcc.cmake -DCMAKE_BUILD_TYPE=Debug ../`  
`$ make`

## Deploying on Hardware
TODO
