from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            requirements = file.read().splitlines()
            # Filter out '-e .' if it exists
            requirements = [req for req in requirements if req.strip() and req != HYPHEN_E_DOT]
            return requirements
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

setup(
    name='MLProject',
    version='0.0.1',
    author='Hiren Patel',
    author_email='hirenpatel4897@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)