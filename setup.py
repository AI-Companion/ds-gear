import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


INSTALL_REQUIREMENTS = [
    'numpy==1.19.0rc2',
    'pandas==1.0.4',
    'scikit-learn==0.23.1',
    'matplotlib',
    'pylint',
    'doxypypy',
    'pycodestyle',
    'nltk==3.5',
    'keras==2.3.1',
    'tensorflow==2.2.0']


class InstallCommand(install):
    """
    will call activate githooks for install mode
    """
    def run(self):
        subprocess.call("git config core.hooksPath .githooks/", shell=True)
        install.run(self)


setup(name='mlp',
      packages=find_packages(),
      author='Marouen Azzouz, Youssef Azzouz',
      author_email='azzouz.marouen@gmail.com, youssef.azzouz1512@gmail.com',
      version='0.1.0',
      zip_safe=False,
      dependency_links=['git+https://www.github.com/keras-team/keras-contrib.git#egg=keras-contrib'],
      install_requires=INSTALL_REQUIREMENTS,
      package_data={},
      include_package_data=True,
      cmdClass={
          'install': InstallCommand
      })
