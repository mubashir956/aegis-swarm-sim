from setuptools import find_packages, setup

package_name = 'aegis_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mubbu',
    maintainer_email='mubbu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'heartbeat_monitor = aegis_core.heartbeat_monitor:main',
		'signal_analyzer = aegis_core.signal_analyzer:main',
        ],
    },
)
