from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads the 'requirements.txt' file and returns
    a list of package requirements as strings.
    """
    requirement_list: List[str] = []
    
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                cleaned = line.strip()
                if cleaned and not cleaned.startswith('#'):  # skip comments and empty lines
                    requirement_list.append(cleaned)
    except FileNotFoundError:
        print("requirements.txt not found.")
    
    return requirement_list

setup(
    name = "PRODUCT_REIVIEW",
    version= "0.0.1",
    author="Mithlesh Singla",
    author_email="mithleshsingla123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)