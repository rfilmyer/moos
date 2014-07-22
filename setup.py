try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mississippi OpenElections OCR Scanner',
    'author': 'Roger Filmyer',
    'url': 'https://github.com/rfilmyer/moos',
    'version': '0.1',
    'install_requires': ['nose', 'PIL'], #tesseract and Wand next up!
    'scripts': [],
    'name': 'moos',
}

setup(**config)
