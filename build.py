from conan.packager import ConanMultiPackager
import os
import sys

if __name__ == '__main__':
    channel = os.getenv('CONAN_CHANNEL', 'testing')
    username = os.getenv('CONAN_USERNAME', 'hinrikg')
    upload = os.getenv('CONAN_UPLOAD', False)
    reference = os.getenv('CONAN_REFERENCE')
    password = os.getenv('CONAN_PASSWORD')

    args_list = sys.argv[1:]
    args_list.append('--build=missing')
    args = ' '.join(args_list)
    builder = ConanMultiPackager(args, username, channel)

    builder.add()

    builder.pack()

    if upload and reference and password:
        builder.upload_packages(reference, password)
