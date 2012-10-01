"""
pip-tools keeps your pinned dependencies fresh.
"""
import sys
from setuptools import setup


def get_dependencies():
    deps = []
    if sys.version_info < (2, 7):
        deps += ['argparse']
    return deps


setup(
    name='pip-tools',
    version='0.2',
    url='https://github.com/nvie/pip-tools/',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description=__doc__,
    #packages=[],
    scripts=['bin/pip-review', 'bin/pip-dump'],
    #include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ]
)
