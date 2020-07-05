I install KineticROS on Ubuntu 16.04

- First write this command in Terminal:
sudo apt-get install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers

- Seond:
make a directory (I will make a directoy called TuretleBot3)

mkdir ~/TurtleBot3

- then i will make a directory inside Turtlebot folder

mkdir ~/TurtleBot3/src/

- then i will go to this directory

cd ~/TurtleBot3/src/

- Third:

git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/TurtleBot3 && catkin_make

-Fourth:

gedit ~/.bashrc

-the above command will open a file write this command inside it in last line and save the file without closing the file. (source $HOME/TurtleBot3/devel/setup.bash)

- then write this command in Terminal 
source ~/.bashrc

- add this command inside the file at last line and save the file (export TURTLEBOT3_MODEL=waffle_pi)

-after that write this command againg in Terminal 
source ~/.bashrc


-Fifth:

write this command in Terminal 
sudo apt-get install ros-kinetic-multirobot-map-merge

know you can run any simulation files

i will run a a TurtleBot3 World map with remote 

First i will write this command in terminal  
roslaunch turtlebot3_gazebo turtlebot3_world.launch
(before write the above command you can write this command to chose which robot do you want to use, export TURTLEBOT3_MODEL=${TB3_MODEL})

this command will open the simulation with a world map

Second i will open the new terminal and write this command inside it 
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

this command will let me to control the robot (Don't close the two terminal and inside the seond terminal you can use w-s-a-d to move the robot to all directions)



References:

http://wiki.ros.org/kinetic/Installation/Ubuntu
https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-nodes
https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#turtlebot3-simulation-using-fake-node
https://www.youtube.com/watch?v=M3QTWIqKtug
