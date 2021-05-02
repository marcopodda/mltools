
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mltools",
    version="0.0.1",
    author="Marco Podda",
    author_email="marcopodda1985@gmail.com",
    description="Utilities for ML experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcopodda/mltools",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scikit-learn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Lincense :: OSI Approved :: MIT License",
        "Operating System :: OS Linux"
    ]
)