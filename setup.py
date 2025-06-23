from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r', encoding='utf-8') as f:
    return f.read()


version = '0.1.0'


setup(
    name='itertols',
    version=version,
    packages=find_packages(),
    description='Functions creating iterators for efficient looping',
    author='Eth33r',
    author_email='ztncrypted@gmail.com',
    url='https://github.com/e-th3r/itertols',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in or package_data
    # spackage_data=package_data,
    install_requires=[
        "inspect",
        "random",
        "math",
        "numpy",
        "fractions",
        "itertools",
        "scipy",
        "sympy"
    ],
    license='LICENSE.txt'
)