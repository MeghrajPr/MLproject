# Setup.py file is required to ack
from setuptools import find_packages, setup
from typing import List


# This functions returns the list of requiremetns from given input the requirements.txt file
def get_requirements(file_path:str) -> List[str]:

    requirements =[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]


        if "-e ." in requirements:
            requirements.remove("-e .")

    print("################################################")
    return requirements



setup(
name= "mlproject",
version= "0.0.1",
author = "Meghraj",
author_contact="1111111111",
packages= find_packages(),
install_requires=get_requirements("requirements.txt")
)