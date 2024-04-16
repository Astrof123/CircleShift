from setuptools import setup, find_packages

setup(
   name='CircleShift',
   version='1.0',
   description='My first library',
   license='MIT',
   author='Gleb Valeev',
   author_email='valeev_101@bk.ru',
   url='https://github.com/Astrof123/CircleShift',
   packages=find_packages(exclude=['tests']),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
