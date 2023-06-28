from setuptools import setup

setup(
    name='ctafpe',
    version='1.0.0',
    author='ctaMTX',
    mail='ctamtx@gmail.com',
    description='Lets you see FPE files.',
    long_description='A library for viewing the animation keyframes for GameGuru software's FPE entities files.',
    long_description_content_type='text/markdown',
    url='https://github.com/ctaMTX/ctafpe',
    packages=['ctafpe'],
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='fpe',
    python_requires='>=3.7',
    install_requires=[
        'pygame',
        '',
    ],
)
