from setuptools import setup, find_packages

setup(
    name="pwa-create",
    version="1.0.0",
    description="Linux PWA Installer - GUI & CLI",
    author="schwarper",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "pwa-create=pwa_create.main:main",
        ],
    },
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)