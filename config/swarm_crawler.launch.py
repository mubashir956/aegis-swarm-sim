from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    	urdf_path = os.path.expanduser(
        	'~/aegis-swarm-sim/robots/crawler.urdf.xacro'
    	)

    	return LaunchDescription
	([
        	# Start Gazebo
        	ExecuteProcess(
            	cmd=['gazebo', '--verbose', '-s',
                 	'libgazebo_ros_init.so',
                 	'-s', 'libgazebo_ros_factory.so'],
            	output='screen'
        	),
        # Spawn robot
        	Node(
            		package='gazebo_ros',
            		executable='spawn_entity.py',
            		arguments=['-file', urdf_path, '-entity', 'crawler'],
            		output='screen'
        	),
    	])
