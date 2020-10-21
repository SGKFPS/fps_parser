import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fps_parser", # Replace with your own username
    version="0.0.1",
    author="FPS",
    author_email="",
    description="Parser/Cleaner/Sanitiser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SGKFPS/parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pandas',
    ],
    zip_safe=False,
    python_requires='>=3.6',
)