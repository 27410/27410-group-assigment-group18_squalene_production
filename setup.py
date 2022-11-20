try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name="growth_coupling_suite",
      version="0.0.1",
      description="Computation and analysis of growth-coupled strain designs",
      author="Tobias Alter; Colton Lloyd",
      author_email="tobial@biosustain.dtu.dk",
      install_requires=[
          "pyparsing~=2.4",
          "cobra~=0.20.0",
          "openpyxl",
          "pandas",
          "optlang~=1.4.4",
          "requests",
          "equilibrator-api",
          "component-contribution",
          "numpy",
          "matplotlib",
        ],
      packages=find_packages(),
      python_requires=">=3.8",
      package_data={
          "": ["*.json", "*.pickle"]
          }   
      )