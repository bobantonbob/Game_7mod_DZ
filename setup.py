from setuptools import setup, find_namespace_packages

setup(
    name='Turtle Race',
    version='0.0.1',
    description='Turtle Race game by Python',
    author='antonbabenko',
    author_email='antonbabenko1983@gmail.com',
    url='',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    data_files=[('turtle_race', ['turtle_race/score.bin'])],
    include_package_data=True,
    entry_points={'console_scripts': [
        'startgame=turtle_race.main:run']}

)