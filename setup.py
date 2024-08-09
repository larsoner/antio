from setuptools import setup
from setuptools.dist import Distribution
import platform


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


# Set the platform-specific files
if platform.system() == "Linux":
    lib_files = ["*libEep.so", "*pyeep.so"]
elif platform.system() == "Windows":
    lib_files = ["*Eep.dll", "*pyeep.pyd"]
else:
    lib_files = []

setup(
    package_data={"antio.libeep": lib_files},
    include_package_data=False,
    distclass=BinaryDistribution,  # To handle binary files
)