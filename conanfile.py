from conans import ConanFile
import os


class FakeItConan(ConanFile):
    name = 'FakeIt'
    version = 'master'
    settings = None
    options = {'integration': ['boost', 'gtest', 'mstest', 'standalone', 'tpunit', 'catch', 'qtest', 'mettle']}
    default_options = 'integration=standalone'
    url = 'https://github.com/gasuketsu/conan-fakeit.git'
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

    def package_info(self):
        config_dir = os.path.join('config', str(self.options.integration))
        self.cpp_info.includedirs = ['include', config_dir]
