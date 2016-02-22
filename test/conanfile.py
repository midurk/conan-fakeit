from conans import ConanFile, CMake
import os

class RunFakeItConanTest(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def requirements(self):
        conan_user = os.getenv('CONAN_USERNAME', 'hinrikg')
        conan_channel = os.getenv('CONAN_CHANNEL', 'testing')
        self.requires('FakeIt/2.0.2@%s/%s' % (conan_user, conan_channel))

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run('cmake --build . %s' % cmake.build_config)

    def test(self):
        self.run(os.path.join('.', 'bin', 'conan_fakeit_test'))
