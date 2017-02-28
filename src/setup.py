#this is where I will write my setup.py
from setuptools import setup

setup(name="led_file",
      version="",
      description="",
      url="",
      author="Nikki Wong",
      author_email="nikki.wong@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['led_test=src.main:main']
      },
      install_requires=[
          'nose',
          'numpy',
          'argparse'
      ],
      )
