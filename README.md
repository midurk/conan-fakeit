# conan-fakeit

[Conan.io](https://conan.io) package for FakeIt

FakeIt is a simple mocking framework for C++. It supports GCC, Clang and MS Visual C++.

## Building the package

Install the Conan package manager and the conan package tools with pip

    $ pip install conan_package_tools

Then build the package with

    $ python build.py

## Uploading the package

    $ conan upload FakeIt/2.0.2@hinrikg/stable

## Using the package

You can manually install this package to your local cache by running

    $ conan install FakeIt/2.0.2@hinrikg/stable

If you handle multiple dependencies in your project it's better to add a *conanfile.txt*

    [requires]
    FakeIt/2.0.2@hinrikg/stable

    [options]
    FakeIt:integration=standalone

    [generators]
    cmake

Then you can install all requirements for your project by running

    $ conan install .

For further information on how to use Conan packages see the [Conan documentation](http://docs.conan.io/)
