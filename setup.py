import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'project',
  packages=['project'],
  version = '0.0.1',
  description = 'python sample project starter',
  long_description_content_type="text/markdown",
  author = 'Brent Ray',
  author_email = 'brentlrayjr@gmail.com',
  url = 'https://github.com/shocknode/python-project-starter',
  keywords = ['python', 'project', 'starter', 'bootstrap','template'],
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'project = project.main:main',
        ],
    },
)