from setuptools import setup, find_packages


setup(
    name = 'flask-crafter',
    version = '0.1.0',
    url = 'https://github.com/rdp-jr/crafter',
    download_url = 'https://github.com/rdp-jr/crafter/archive/refs/tags/0.1.0.tar.gz',
    author = 'Obee Principio',
    author_email = 'rdprincipio.jr@gmail.com',
    description = 'A CLI tool for the FlaskMVC Starter Kit',
    long_description=open('README.md').read(),
    py_modules = ['main', 'crafter'],
    packages=find_packages(),
    install_requires = ['Click',
        'inflect'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'crafter = main:cli'
        ]
    },
    include_package_data=True,
    package_data={'': ['templates/*.tpl']},
    

)