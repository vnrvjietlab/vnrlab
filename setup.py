from setuptools import setup

setup(
    name='vnrlab',
    version='0.1.0',
    packages=['vnrlab'],
    license='MIT',
    include_package_data=True,
    package_data={
        "": ['Data/*.bin']
    },
    install_requires=[
        'pycryptodome'
    ],
)