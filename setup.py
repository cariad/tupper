"""
"tupper" package setup.
"""

from setuptools import setup

with open('README.md', 'r') as stream:
    LONG_DESCRIPTION = stream.read()

setup(
    author='Cariad Eccleston',
    author_email='cariadeccleston@icloud.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    description='Calculates plots for Tupper\'s Self-Referential Formula.',
    name='tupper',
    license='MIT',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=[
        'tupper'
    ],
    url='https://github.com/cariad/py-tupper',
    version='0.10.1')
