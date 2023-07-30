from setuptools import setup, find_packages

setup(
    name='pcdr',
    version='0.1.0',
    description='python-can-define-radio SDR class functionality.',
    packages=find_packages(),    
    install_requires=['numpy >= 1.0', 'matplotlib >= 1.0'],
)


# [project]
# name = "pcdr"
# version = "0.0.1"
# description = "python-can-define-radio SDR class functionality."
# requires-python = ">=3.7"
# classifiers = [
#     "Programming Language :: Python :: 3",
#     "Operating System :: OS Independent",
# ]

# [project.urls]
# "Homepage" = "https://github.com/python-can-define-radio/sdr-course"
# "Bug Tracker" = "https://github.com/python-can-define-radio/sdr-course/issues"
