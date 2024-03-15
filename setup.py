from setuptools import setup, find_packages

setup(
    name='wild',
    version='0.1',
    packages=find_packages(),
    description="Première version d'eda globale",
    author='Michaël Tirat',
    author_email='michaeltirat@gmail.com',
    install_requires=[
        'pandas'
    ],
    py_modules=['wilder'],
)
