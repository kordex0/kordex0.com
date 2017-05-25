from setuptools import setup

install_requires = [
    'pyramid',
]

setup(name='kordex0.com',
      install_requires=install_requires,
      entry_points="""\
      [paste.app_factory]
      main = src:main
      """
)
