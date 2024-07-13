from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function returns the list of the libraries from the requirements.txt
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPEN_E_DOT]
    return requirements

setup(
    name='ML PROJECT',
    version='0.0.1',
    author='Manideep',
    author_email='manideepannarapu@my.unt.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
