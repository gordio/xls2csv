from setuptools import setup, find_packages


setup(
    name='xls2csv',
    version=0.1,
    description='Simple xls to csv convertor',
    author='Oleh Hordiienko',
    author_email='oleh.hordiienko@gmail.com',
    url='https://github.com/gordio/xls2csv',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
    install_requires="""
    xlrd
    """,
    entry_points="""
        [console_scripts]
        xls2csv = xls2csv:main
    """,
)
