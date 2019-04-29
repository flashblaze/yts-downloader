from setuptools import setup, find_packages

setup(name='yts', version='0.1.0', description='Download any movie from yts.am',
      long_description='A Python package developed to try yts.am API and download any movie from it.', author='Neeraj Lagwankar', author_email='neerajlagwankar@gmail.com', license='MIT', classifiers=[
          'Programming Language :: Python :: 3',
          "License :: OSI Approved :: MIT License",
          'Programming Language :: Python :: 3.6',
      ], keywords='yts torrent download', install_requires=['requests', 'beautifulsoup4'], entry_points={
          'console_scripts': [
              'yts=yts:main',
          ]
      })
