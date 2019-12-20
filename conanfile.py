from conans import ConanFile, CMake, tools


class EasyprofilerConan(ConanFile):
    name = "easy_profiler"
    version = "2.1.0"
    license = "MIT"
    author = "Edgar Edgar@AnotherFoxGuy.com"
    url = "https://github.com/AnotherFoxGuy/conan-easy_profiler"
    description = "Lightweight cross-platform profiler library for c++"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/yse/easy_profiler.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions['EASY_PROFILER_NO_GUI'] = 'ON'
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = tools.collect_libs(self)
