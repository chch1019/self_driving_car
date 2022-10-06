from setuptools import setup
import os
from glob import glob


package_name = 'self_driving_car'


config_module = "self_driving_car/config"
data_module ="self_driving_car/data"

detection_module ="self_driving_car/Detection"
gps_navigation = "self_driving_car/GPS_Navigation"

det_l_module ="self_driving_car/Detection/Lanes"
detec_l_a_module="self_driving_car/Detection/Lanes/a_Segmentation"
detec_l_b_module="self_driving_car/Detection/Lanes/b_Estimation"
detec_l_c_module="self_driving_car/Detection/Lanes/c_Cleaning"
detec_l_d_module="self_driving_car/Detection/Lanes/d_LaneInfo_Extraction"

det_s_module ="self_driving_car/Detection/Signs"
detec_s_a_module="self_driving_car/Detection/Signs/Classification"

detec_TL_module="self_driving_car/Detection/TrafficLights"


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,detec_l_d_module,detec_l_c_module,detec_l_b_module,detec_l_a_module,det_l_module,detec_s_a_module,det_s_module,detec_TL_module,detection_module,gps_navigation,config_module,data_module],

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('lib', package_name), glob('scripts/*')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
            ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'spawner_node = self_driving_car.sdf_spawner:main',
        'computer_vision_node = self_driving_car.computer_vision_node:main',
        'video_recording_node = self_driving_car.video_save:main',
        'upper_camera_recording = self_driving_car.upper_camera_video:main',
        'sdc_V2 = self_driving_car.sdc_V2:main',
        ],
    },
)
