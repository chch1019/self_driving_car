# ROS2 Prius Self Driving Car  using AI/Deeplearning and Computer Vision


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Repository-Tree">Repository Tree</a></li>
    <li><a href="#Link-to-the-Course">Link to the Course</a></li>
    <li><a href="#Instructors">Instructors</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
A tesla Like Car in ROS2 will follow lane , Use AI to classify Sign Boards and perform Object tracking to act on the sign boards and set speed respectively

[![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/thumbnail_1.png)](https://youtu.be/D5BkqDcfw2U "Click to Watch Intro Video on Youtube")
----
## Using this Repository
* Clone the repository in you Home folder
```
git clone https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV.git
```
* Get into the downloaded repository
 ```
 cd path/to/ROS2-Self-Driving-Car-AI-using-OpenCV/
##e.g cd ~/ROS2-Self-Driving-Car-AI-using-OpenCV/
  ```

* Bring all models into your **.gazebo/models** ( requires gazebo to be installed )
 ```
 cp /models/* ~/.gazebo/models
 ```
 or manually copy->paste them into ~/.gazebo/models/ ( if not avaible press ctrl + H  , a hidden foler )

* Perform Colcon Build ( if not installed refer to Repo_resources/How_to_run_the_project.txt )
```
colcon build
```
* Source your Workspace in any terminal you open to Run files from this workspace ( Basic thing of ROS )
```
source /path/to/ROS2-Self-Driving-Car-AI-using-OpenCV/install/setup.bash
```
* (Optional for Power USERs ) Add source to this workspace into bash file
 ```
  echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
 ```

 * To Run the pathplanning world and saving Video
 ```
 ros2 launch  self_driving_car_pkg maze_solving_world.launch.py
 ```
   * Next terminal
 ```
 ros2 run self_driving_car_pkg  upper_camera_recording

 ```

  **NOTE:** This upper command is going to add the source file path into your ~/.bashrc file ( Only perform it once and you know what you are doing).This will save your time when running things from the Workspace
* If the repository is not working for you. Watch the free preview video on our course page
 Where full explaination is given on setting up this repository.
  * **[[How to Run the Project]](https://www.udemy.com/course/ros2-self-driving-car-with-deep-learning-and-computer-vision/learn/lecture/30013318#overview)**
----
## Course Workflow
#### **Ros Package**
* World Models Creation
* Prius OSRF gazebo Model Editing
* Nodes , Launch Files
* SDF through Gazebo
* Textures and Plugins in SDF

#### **Computer Vision**
* Perception Pipeline setup
* Lane Detection with Computer Vision Techniques
* Traffic Light Detection Using Haar Cascades
* Sign and Traffic Light Tracking using Optical Flow
* Rule-Based Control Algorithms

#### **DeepLearning**
* Sign Classification using (custom-built) CNN
---
## Features
* **Prius Hybrid Car**
  -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/the_car.gif)

* **Satellite Navigation (NEW!)**
    * **Stage 1: Localiation**

      -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/Sat_Nav/1_localization.gif)

    * **Stage 2: Mapping**

      -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/Sat_Nav/2_mapping.gif)

    * **Stage 3: Path-Planning**

      -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/Sat_Nav/3_pathplanning.gif)

    * **Stage 4: Motion-Planning**

      -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/Sat_Nav/4_motionplanning.gif)
  
* **Lane Following**
  -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/lane_detection.gif)
* **Sign Board Detection**
  - ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/traffic_signs_boards.gif)
* **Traffic Signal Recognition**
  - ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/traffic_signal.gif)

* **T-Junction Navigation**
  - ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/j_turning.gif)

* **The World**
  -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/world.gif)

* **Custom Models**
  -  ![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/custom_models.gif)

----
## Pre-Course Requirments

**Software Based**
* Ubuntu 20.04 (LTS)
* ROS2 - Foxy Fitzroy
* Python 3.6
* Opencv 4.2
* Tensorflow 2.14

**Skill Based**
* Basic ROS2 Nodes Communication
* Launch Files
* Gazebo Model Creation
* Basic OpenCV Usage
* Motivated mind :)
---

## Repository Tree
> Explaining repository structure (i.e important files and their functions).

![alt text](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV/blob/main/Images_videos/ROS2_SDC_Tree.png)

----

## Link to the Course

**[[Discounted Link]](https://www.udemy.com/course/ros2-self-driving-car-with-deep-learning-and-computer-vision/?couponCode=SAT_NAV)**

----

## Instructors

Haider Najeeb   (Computer Vision)    -  [Profile Link](https://www.linkedin.com/in/haider-najeeb-68812516a/)
Muhammad Luqman (ROS Simulation and Control Systems) - [Profile Link](https://www.linkedin.com/in/muhammad-luqman-9b227a11b/)

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
