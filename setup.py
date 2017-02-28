#this is where I will write my setup.py
from setuptools import setup

setup(name="ledtester",
      version="0.1",
      description="LED Testing for Assignment3 in Comp30670",
      url="",
      author="Nikki Wong",
      author_email="nikki.wong@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['led_tester=src.main:main']
      },
      install_requires=[
          'nose',
          'numpy',
          'argparse'
      ],
      )
 