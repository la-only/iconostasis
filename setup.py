from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    _long_description = fh.read()

setup(
    name='iconostasis',
    version='0.0.1',    
    description='Make app icon for store simple. Again and again. And Again',
    long_description=_long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/la-only/iconostasis',
    project_urls={
        "Bug Tracker": "https://github.com/la-only/iconostasis/issues",
    },
    author='la-only',
    author_email='i@0ls.ru',
    license='MIT',
    install_requires=['Pillow>=8.4.0',
                      'tqdm>=4.62.3',                     
                      'click>=8.0.3',                     
                      ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.10',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points = {
        "console_scripts": "iconostasis=iconostasis.__main__:cmain"
    },
)
