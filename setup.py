import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'pretty_talib'

setuptools.setup(
    name="pretty_talib",
    version="0.0.7",
    author="Kristof",
    description="prettified interface for TA-Lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/pretty-TA-Lib",
    packages=setuptools.find_packages(),
    install_requires=["jsoncodable", "numpy", "TA-Lib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)