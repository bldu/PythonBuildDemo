import setuptools

def get_long_description():
    with open("README.md", "r") as f:
        long_desc = f.read()
    return long_desc      

setuptools.setup(
    name="mypkg",
    version="0.0.1",
    author="bldu",
    description="python build demo",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="",
    install_requires=["opencv-python"],
    packages=setuptools.find_packages(exclude=("tests"))
)