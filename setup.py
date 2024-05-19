from setuptools import find_packages, setup

setup(
    name='mabokahflib',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='Mohamed abokahf',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    install_requires=[]
)