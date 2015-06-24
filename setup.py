from setuptools import setup, find_packages
import os

version = '2.0.1.dev0'

setup(name='rer.al.mcorevideoportlet',
      version=version,
      description="This package is used to show mediacore video into a portlet",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://rersvn.ente.regione.emr.it/svn/plone/prodotti/rer.al.mcorevideoportlet/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rer', 'rer.al'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.rtvideo.mediacore',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
