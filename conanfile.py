import os

from conans import ConanFile, CMake, tools


class Issue6305Conan(ConanFile):
    name = "issue6305"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "example.cpp",

    requires = "boost/1.70.0@conan/stable",
    generators = "cmake_paths"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
