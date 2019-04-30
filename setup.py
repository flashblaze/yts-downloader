from setuptools import setup, find_packages

setup(name='yts-downloader', version='0.1.1', description='Download any movie from yts.am',
      long_description='A Python package developed to try yts.am API and download any movie from it.', author='Neeraj Lagwankar', author_email='neerajlagwankar@gmail.com', license='MIT', classifiers=[
          'Development Status :: 3 - Alpha',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          "License :: OSI Approved :: MIT License",
      ], keywords='yts torrent download', install_requires=['requests', 'beautifulsoup4'], entry_points={
          'console_scripts': [
              'yts=yts:main',
          ]
      })
