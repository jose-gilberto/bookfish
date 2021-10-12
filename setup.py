from setuptools import setup, find_packages

setup(
    name='bookfish',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    scripts=['bookfish/bin/bookfish'],
    author='Gilberto Medeiros',
    author_email='medeiros.gilberto.br@gmail.com',
    url='https://github.com/jose-gilberto/bookfish'
)