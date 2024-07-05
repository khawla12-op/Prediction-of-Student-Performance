from setuptools import find_packages, setup
from typing import List

HYPHENE_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHENE_E_DOT in requirements:
            requirements.remove(HYPHENE_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.1",
    author="khaoula",
    author_email='khawlaallak@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
