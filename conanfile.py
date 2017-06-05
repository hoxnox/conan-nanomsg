from nxtools import NxConanFile
from conans import tools, CMake

class NanomsgConan(NxConanFile):
    name = "nanomsg"
    description = "A socket library that provides several common communication patterns."
    version = "1.0.0"
    options = {"shared":[True, False]}
    default_options = "shared=False"
    url = "https://github.com/hoxnox/conan-nanomsg.git"
    license = "https://github.com/nanomsg/nanomsg/blob/master/COPYING"
    settings = "os", "compiler", "build_type", "arch"

    def do_source(self):
        self.retrieve("24afdeb71b2e362e8a003a7ecc906e1b84fd9f56ce15ec567481d1bb33132cc7",
            [
                'vendor://nanomsg/nanomsg/nanomsg-{version}.tar.gz'.format(version=self.version),
                'https://github.com/nanomsg/nanomsg/archive/{version}.tar.gz'.format(version=self.version)
            ], "nanomsg-{v}.tar.gz".format(v = self.version))

    def do_build(self):
        cmake = CMake(self)
        tools.untargz("nanomsg-{v}.tar.gz".format(v=self.version))
        cmake_defs = {"CMAKE_INSTALL_PREFIX": self.staging_dir,
                      "CMAKE_INSTALL_LIBDIR": "lib",
                      "NN_ENABLE_DOC": "0",
                      "NN_ENABLE_GETADDRINFO": "0",
                      "NN_TESTS": "0",
                      "NN_TOOLS": "0",
                      "NN_ENABLE_NANOCAT": "0",
                      "NN_STATIC_LIB": "0" if self.options.shared else "0"}
        cmake_defs.update(self.cmake_crt_linking_flags())
        cmake.configure(defs=cmake_defs, source_dir="nanomsg-{v}".format(v=self.version))
        cmake.build(target="install")

    def do_package_info(self):
        self.cpp_info.libs = ["nanomsg"]

