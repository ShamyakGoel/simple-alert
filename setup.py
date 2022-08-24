from setuptools import setup
setup(
  name = 'simple-alert',
  packages = ['simple-alert'],
  version = '1.0.2',
  license='MIT',
  description = 'This is a library that give alerts on terminal',
  author = 'Shamyak',
  author_email = 'sj907822@gmail.com',
  url = 'https://github.com/ShamyakGoel/simple-alert',
  download_url = 'https://github.com/ShamyakGoel/simple-alert/archive/refs/tags/v_11.tar.gz',
  keywords = ['simple-alert', 'ShamyakGoel', 'codewithshamyak', 'coding with shamyak', 'alert', 'alerts'],
  long_description=open('README', 'r').read(),
  install_requires=[
          'termcolor'
      ],
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)