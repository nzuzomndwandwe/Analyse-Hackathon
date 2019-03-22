from setuptools import setup, find_packages

setup(
    name='Analse-Hackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/nzuzomndwandwe/Analyse-Hackathon.git',
    author='Nzuzo Ndwandwe',
    author_email='nzuzo.ndwandwe@gmail.com'
)
