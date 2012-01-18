from setuptools import setup
from setuptools import find_packages

setup(
    name='base_page',
    version='1.0.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/base_page',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "base_page": [
            "templates/*.html",
            "static/css/*.css"
        ],
    },
    zip_safe=False,
    install_requires=['django'],
)
