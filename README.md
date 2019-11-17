# cse-571-Group-1
Maze Solving algorithm

IF YOU ARE ON BRANCH robot_setup, start the project with:
execute catkin_make from catkin folder
roslaunch cse-571-Group-1 maze.launch 

Maze Plugin: Gzmaze (https://github.com/athenian-programming/gzmaze)
Requirements

cmake 2.8 Gazebo 6+ (currently using 8)
Building

Goto cse-571-Group-1 directory
$ mkdir build
$ cd build
$ cmake .. 
$ make

Running

Add the following to your ~/.gazebo/gui.ini file:

[overlay_plugins]
filenames=libregenerate_widget.so

Run Gazebo with:

$ #this will setup the environment variables you need and run gazebo
$ cd ~/catkin_ws/src/cse-571-Group-1
$ ./setup.sh 

The input files

Look at sample_maze.mz for an example.
