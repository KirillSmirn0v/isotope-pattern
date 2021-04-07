import setuptools
from typing import List


def parse_description() -> str:
    with open('README.md', 'r') as file:
        description = file.read()
    return description


def parse_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements


setuptools.setup(
    name='isotope-pattern-lib',
    version='dev',
    description="a library to compute an isotope pattern of a given molecular formula",
    author='Kirill S Smirnov',
    author_email='kirill.smirnov.mail@gmail.com',
    long_description=parse_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/ksmirn0v/isotope-pattern-lib',
    packages=setuptools.find_namespace_packages(include=['isotope_pattern_lib*']),
    package_data={'isotope_pattern_lib': ['resources/config.yaml']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    keywords=['isotope pattern', 'mass spectrometry', 'molecular formula'],
    python_requires='>=3.7',
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'test': parse_requirements('requirements-test.txt'),
        'dev': parse_requirements('requirements-dev.txt')
    }
)
