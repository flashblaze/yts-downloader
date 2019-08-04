from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup(author="Neeraj Lagwankar",
      author_email='neerajlagwankar@gmail.com',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      name='yts_downloader',
      url="https://github.com/FlashBlaze/yts-downloader/",
      version='0.1.2',
      description="A simple python CLI to download movies from yts or formerly yify",
      long_description=readme + '\n\n' + history,
      long_description_content_type='text/markdown',
      license='MIT license',
      keywords='yts_downloader yts torrent download',
      install_requires=['requests', 'beautifulsoup4'],
      entry_points={
          'console_scripts': [
              'yts-downloader=yts_downloader.yts_downloader:main'
          ]
      },
      zip_safe=False,
      packages=find_packages(include=['yts_downloader']))
