from conans import ConanFile
import os


class FakeItConan(ConanFile):
    name = 'FakeIt'
    version = '2.0.5'
    description = 'C++ mocking made easy. A simple yet very expressive, headers only library for c++ mocking.'
    settings = None
    options = {'integration': ['boost', 'gtest', 'mstest', 'standalone', 'tpunit', 'catch', 'qtest', 'mettle', 'nunit']}
    default_options = 'integration=standalone'
    url = 'https://github.com/gasuketsu/conan-fakeit.git'
    homepage = "https://github.com/eranpeer/FakeIt"
    license = 'MIT'

    def source(self):
        git_args = ' '.join([
            'https://github.com/eranpeer/FakeIt.git',
            self.name,
        ])
        self.run('git clone %s' % git_args)
        self.run('cd %s && git checkout %s' % (self.name, self.version))

    def build(self):
        # This is a header-only library so no build step required
        pass

    def package(self):
        self.copy(pattern='*.hpp', dst='include', src='FakeIt/include')
        self.copy(pattern='*.hpp', dst='config', src='FakeIt/config')
        self.copy('license*', dst='licenses', src='FakeIt', ignore_case=True, keep_path=False)

    def package_id(self):
        # as it is header only, one package is good for everything.
        self.info.options.integration = "All"

    def package_info(self):
        config_dir = os.path.join('config', str(self.options.integration))
        self.cpp_info.includedirs = ['include', config_dir]
