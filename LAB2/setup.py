from setuptools import setup

setup(
    name='serial',
    version='1.0',
    description='LR2',
    packages=['serializers'],
    author='Me',
    author_email='shprexenplus@gmail.com',
    entry_points={
        'console_scripts': [
            'run = serializers.main:main'
        ]
    }
)
