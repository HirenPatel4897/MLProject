from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Hiren Patel',
    author_email='hirenpatel4897@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)