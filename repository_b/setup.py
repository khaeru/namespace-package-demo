from setuptools import find_namespace_packages, setup

setup(
    name='message_data_demo-transport',
    packages=find_namespace_packages(include=['message_data_demo.model.*'])
)
