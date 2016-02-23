# conan-fakeit [![Build Status](https://travis-ci.org/hinrikg/conan-fakeit.svg?branch=master)](https://travis-ci.org/hinrikg/conan-fakeit)

[Conan.io](https://conan.io) package for [FakeIt](https://github.com/eranpeer/FakeIt)

FakeIt is a simple mocking framework for C++. It supports GCC, Clang and MS Visual C++.

## Building the package

Install the Conan package manager and the Conan package tools with pip

    $ pip install conan_package_tools

Then build the package with

    $ python build.py

## Uploading the package

    $ conan upload FakeIt/2.0.2@hinrikg/stable

## Using the package

### Installation

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

### Options

#### `integration`

FakeIt can be pre-configured to work with some of the major unit testing frameworks. A pre-configured
version will use the assertions mechanism of the unit testing framework to integrate the generated
error messages into the unit testing framework output.

The following frameworks are supported:

- [Boost Test](http://www.boost.org/doc/libs/release/libs/test) using `FakeIt:integration=boost`
- [Google Test](https://github.com/google/googletest) using `FakeIt:integration=gtest`
- [MSTest](http://en.wikipedia.org/wiki/Visual_Studio_Unit_Testing_Framework) using `FakeIt:integration=mstest`
- [tpunit++](https://github.com/tpounds/tpunitpp) using `FakeIt:integration=tpunit`

By default FakeIt is configured without any framework integration using `FakeIt:integration=standalone`.
