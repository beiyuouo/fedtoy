from setuptools import setup, find_packages
from os import path as os_path

__version__ = "0.0.1a1"

this_directory = os_path.abspath(os_path.dirname(__file__))

setup(
    name="fedtoy",
    version=__version__,
    keywords=[
        "federated learning",
        "deep learning",
        "pytorch",
        "asynchronous federated learning",
        "wandb",
    ],
    author="Bingjie Yan",
    author_email="bj.yan.pa@qq.com",
    maintainer="Bingjie Yan",
    maintainer_email="bj.yan.pa@qq.com",
    description="🧸FedToy: A robust deterministic federated learning simulator.",
    long_description=open(os_path.join(this_directory, "README.md")).read(),
    long_description_content_type="text/markdown",
    license="Apache-2.0 License",
    url="https://github.com/beiyuouo/fedtoy",
    packages=find_packages(include=["fedtoy", "fedtoy.*", "LICENSE"]),
    package_data={"": ["*.yaml"]},
    install_requires=[
        "torch>=1.8.2",
        "torchvision>=0.9.2",
        "numpy",
        "ezkfg",
        "pyyaml",
        "urllib3==1.25.3",
        "click",
        "loguru",
    ],
    extras_require={
        "dev": ["pytest", "pytest-order", "mkdocs"],
        "test": ["pytest", "pytest-order"],
        "docs": ["mkdocs"],
    },
    python_requires=">=3.6",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        # "console_scripts": [
        #     "fedtoyplot=fedtoy.cli.toolkits.plot:plot",
        #     "fedtoy=fedtoy.cli.toolkits.cli:cli",
        # ]
    },
)
