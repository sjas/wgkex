from setuptools import setup, find_packages

setup(
    name="wgkex",
    version="0.1.0",
    author="Freifunk München",
    author_email="hilfe@ffmuc.net",
    description="WireGuard Key Exchange",
    license="",
    url="https://github.com/freifunkMUC/wgkex",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    zip_safe=False,
    install_requires=["Flask", "flask-mqtt", "PyYAML", "voluptuous"],
    setup_requires=["wheel"],
)
