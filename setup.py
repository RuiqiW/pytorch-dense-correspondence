#!/usr/bin/env python

from setuptools import setup, find_packages


dependencies = [
            "configargparse",
            "imageio",
            "matplotlib",
            "numpy",
            "opencv_python",
            "scipy",
            "scikit-optimize",
            "sklearn",
            "tensorboardX",
            "torchdiffeq",
            "torchvision",
            "torchviz",
            "zarr"
        ]

setup(name='densenet',
      version="0.1",
      packages=find_packages(exclude=["notebooks", "scripts"]),
      package_dir={"":"./"},
      install_requires=dependencies)