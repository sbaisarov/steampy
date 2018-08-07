from distutils.core import setup

setup(name='steampy',
      version='1.0',
      description='Python Steam Library',
      author='Shamil Baysarov',
      author_email='',
      url='',
      package_dir={'steampy': 'steampy},
      install_requires=[
          'requests',
          'rsa',
          'bs4'
      ]
     )
