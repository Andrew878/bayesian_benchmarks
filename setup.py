from setuptools import find_packages, setup

requirements = [
    'numpy>=1.10.0',
    'scipy>=0.18.0',
    'xlrd>=1.1.0',
    'pandas>=0.23',
    'pytest>=4.4.0',
]

setup(name='bayesian_benchmarks',
      version='0.0.1',
      author="Hugh Salimbeni",
      author_email="hrs13@ic.ac.uk",
      description=("Bayesian benchmarking"),
      license="Apache License 2.0",
      keywords="machine-learning bayesian-methods",
      url="https://github.com/hughsalimbeni/bayesian_benchmarks",
      python_requires=">=3.6",
      packages=find_packages(include=["bayesian_benchmarks",
                                      "bayesian_benchmarks.*"]),
      install_requires=requirements,
      package_data={"":["bayesian_benchmarksrc"]},
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ])
