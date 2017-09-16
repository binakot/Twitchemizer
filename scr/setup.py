from setuptools import setup, find_packages

setup(
    name='twitchemizer',
    version='0.0.1',
    url='https://github.com/binakot/twitchemizer',
    license='MIT',
    author='binakot',
    author_email='binakot@gmail.com',
    description='',
    packages=find_packages(),
    install_requires=[
        'livestreamer>=1.12.2',
        'streamlink>=0.8.1'
    ]
)
