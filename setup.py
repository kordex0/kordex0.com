from setuptools import setup

install_requires = [
    'pyramid',
    'pyramid_mako'
]

setup(name='kordex0',
      install_requires=install_requires,
      entry_points="""\
      [paste.app_factory]
      main = kordex0:main
      """
)
