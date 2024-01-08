from setuptools import setup, find_packages

setup(
    name="your-project-name",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "django~=5.0",
        "djangorestframework~=3.14",
    ],
)
