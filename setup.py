from setuptools import find_packages, setup

setup(
    name='pyquote',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.3',
        'psycopg2==2.9.3',
        'requests==2.27.1',
        'beautifulsoup4==4.10.0'
    ],
)
