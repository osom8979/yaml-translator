# -*- coding: utf-8 -*-

from unittest import TestCase, main

from tester import translations
from yaml_translator.translator import Translator, TranslatorLangMapper


class YamlTranslatorPackageTestCase(TestCase):
    def test_default(self):
        trans = Translator.from_module_dir(translations, "en")
        self.assertEqual("en-title", trans.t("menu.title"))

        trans.lang = "ko"
        self.assertEqual("ko-title", trans.t("menu.title"))

    def test_lang_mapper(self):
        t = TranslatorLangMapper.from_module_dir(translations)
        result = {"en": "en-title", "ko": "ko-title"}

        t.lang = "en"
        self.assertDictEqual(result, t("menu.title"))

        t.lang = "ko"
        self.assertDictEqual(result, t("menu.title"))


if __name__ == "__main__":
    main()
