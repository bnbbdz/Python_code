import setuptools

setuptools.setup(
    name="first_project",
    packages=setuptools.find_packages(exclude=["first_project_tests"]),
    install_requires=[
        "dagster==0.14.1",
        "dagit==0.14.1",
        "pytest",
    ],
)
