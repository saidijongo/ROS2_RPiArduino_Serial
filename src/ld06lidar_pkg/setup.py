from setuptools import find_packages, setup

package_name = 'ld06lidar_pkg'

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
    maintainer='jongo',
    maintainer_email='saidijongo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "lidar_pub_node = ld06lidar_pkg.lidar_publisher_node:main",
            "lidar_subs_node= ld06lidar_pkg.lidar_subscriber_node:main"
        ],
    },
)
