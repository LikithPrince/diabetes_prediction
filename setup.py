from setuptools import find_packages, setup
from typing import List


hypen_e_dot = '-e .'
def get_req_list(file_path:str) -> List[str]:
   """ This function is responsible for giving requirements list"""
   
   with open(file_path, 'r') as f:
      req_list = [line.strip() for line in f.readlines()]
      if hypen_e_dot in req_list:
         req_list.remove(hypen_e_dot)
   return req_list


setup(
   name='diabetes-prediction',
   version='0.1.0',
   description='A Python package for predicting diabetes risk using machine learning',
   author= 'Likith P',
   author_email='likithprasanna@gmail.com',
   packages= find_packages(),
   install_requires= get_req_list('requirements.txt')
)