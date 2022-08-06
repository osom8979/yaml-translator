# -*- coding: utf-8 -*-

import os
from unittest import TestCase, main

from yaml_translator import package
from yaml_translator.package.package_utils import get_module_directory


class PackageUtilsTestCase(TestCase):
    def test_get_module_directory(self):
        self.assertTrue(os.path.isdir(get_module_directory(package)))


if __name__ == "__main__":
    main()
