from setuptools import find_packages, setup

package_name = 'damin_robot1'

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
    maintainer_email='jongo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "logitech1 = damin_robot1.modbusRTU:main",
            "jongo_node1 = damin_robot1.node1:main",
            "jongo_node2 = damin_robot1.node2:main",
            "jongo_drawshape = damin_robot1.drawshape:main",
            "jongo_posesubs = damin_robot1.pose_subscriber:main",
            "jongo_sudong= damin_robot1.pose_subscriber:main"

        ],
    },
)
