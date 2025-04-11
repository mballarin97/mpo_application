from setuptools import find_packages, setup

setup(
    name="mpo_application",
    version="0.1",
    description="Way to apply an MPO to an MPS",
    packages=find_packages(exclude=("tests", ".github")),
    install_requires=[
        "numpy",
        "scipy",
    ],
    include_package_data=True,
    platforms="any",
)
