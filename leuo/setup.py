from setuptools import setup, find_packages

setup(
    name="leuo",
    version="0.1",
    packages=find_packages(),
    install_requires=["fake-useragent"],
    description="A simple library to generate User Agents and UUIDs",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/hasneenn/leuo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
