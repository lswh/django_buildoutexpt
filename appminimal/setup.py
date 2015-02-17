from setuptools import setup, find_packages

setup(
    name='plex',
    version='0.1.24',
    packages=find_packages(),
    url='channelfix.com',
    license='commercial property',
    author='Helen Mary Samonte Labao-Barrameda',
    author_email='helenmarylabao@live.com',
    description='The PLEX video funding platform.',
    install_requires=['django==1.6.8',
                      'anyjson==0.3.3',
                      'python-social-auth==0.2.1',
                      'South==1.0.2',
                      'celery==3.1.11',
                      'kombu==3.0.16',
                      'django-celery==3.1.10',
                      'Pillow==2.7.0'],
)
