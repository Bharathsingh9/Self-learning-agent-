python
from setuptools import find_packages, setup

setup(
    name='scientific-calc',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'mathquill==0.9.1',
        'flask_wtf',
        'wtforms'
    ],
    include_package_data=True,
    zip_safe=False
)
