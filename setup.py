from setuptools import setup, find_packages

setup(
    name="ETLpipeline",
    version="0.1.0",
    description="ETL and Query",
    author="Danish Maknojia",
    author_email="d.maknojia@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
