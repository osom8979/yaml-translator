# -*- coding: utf-8 -*-

import os
from unittest import TestCase, main

from yaml_translator import package
from yaml_translator.package.package_utils import get_module_directory


class FakeModule:
    __file__: str


class PackageUtilsTestCase(TestCase):
    def test_get_module_directory(self):
        self.assertTrue(os.path.isdir(get_module_directory(package)))

    def test_get_module_directory_with_file_attribute(self):
        fake_module = FakeModule()
        fake_module.__file__ = __file__
        module_dir = get_module_directory(fake_module)  # noqa
        self.assertEqual(os.path.dirname(__file__), module_dir)

    def test_get_module_directory_error(self):
        with self.assertRaises(RuntimeError):
            get_module_directory(object())  # noqa


if __name__ == "__main__":
    main()
