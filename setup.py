from setuptools import setup
from setuptools import find_packages

setup(
    name='base_page',
    version='4.2.7',
    author='Kristoffer Snabb, Pratik Hublikar',
    url='https://github.com/geonition/base_page',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "base_page": [
            "templates/*.html",
            "templates/analytics.js",
            "templates/admin/*.html",
            "static/css/*.css",
            "static/img/*.png",
            "static/img/*.gif",
            "static/js/*.js",
            "static/js/libs/*.js",
            "static/js/libs/i18n/*.js",
            "locale/*/LC_MESSAGES/*.mo",
            "locale/*/LC_MESSAGES/*.po",
        ],
    },
    zip_safe=False,
    install_requires=['django',
                      'django-modeltranslation'],
)
