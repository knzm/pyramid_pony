from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = [
    "pyramid",
    ]

entry_points = """
"""

setup(name='pyramid_pony',
      version='0.1',
      description="Pony for Pyramid",
      long_description=README,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        ],
      keywords='web wsgi pylons pyramid',
      author='Nozomu Kaneko',
      author_email='nozom.kaneko@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points=entry_points,
      )
