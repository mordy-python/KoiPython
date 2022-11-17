from setuptools import setup

setup(
    name="Koi",
    version="2.0.0",
    description="Koi Language",
    author="Israel Waldner",
    author_email="imky171@gmail.com",
    packages=["src", "src.koi", "src.koi.std"],
    entry_points={"console_scripts": ["koi=src.__main__:main"]},
)