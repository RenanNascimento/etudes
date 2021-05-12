import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='etudes',  
     version='0.1',
     scripts=['etudes'] ,
     author="Renan Nascimento",
     author_email="renan.engcomp@gmail.com",
     description="An utility package to help build machine learning applications",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/renannascimento/etudes",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )