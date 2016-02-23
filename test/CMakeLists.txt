cmake_minimum_required(VERSION 2.8)
project(conan_fakeit_test)

include(conanbuildinfo.cmake)
conan_basic_setup()

# Enable C++11 support
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif()

add_executable(conan_fakeit_test main.cpp)
