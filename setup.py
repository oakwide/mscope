from setuptools import setup, find_packages

setup(
    name='mscope',
    version='0.1',
    packages=find_packages(),
    author='oakwide',
    install_requires=['requests', 'dnspython'],
    description='mscope allows you to find emails by username',
    include_package_data=True,
    entry_points={
        'console_scripts': ['mscope = mscope.main:main']
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
