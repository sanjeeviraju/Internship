from setuptools import setup, find_packages

setup(
    name="random-username-generator",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    author="sanjeeviraju",
    author_email="your.email@example.com",
    description="A Python GUI application for generating random creative usernames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sanjeeviraju/random-username-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
    ],
    entry_points={
        'console_scripts': [
            'random-username-generator=src.main:main',
        ],
    },
)
