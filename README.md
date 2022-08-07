# yaml-translator

![PyPI](https://img.shields.io/pypi/v/yaml-translator?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yaml-translator?style=flat-square)
![GitHub](https://img.shields.io/github/license/osom8979/yaml-translator?style=flat-square)

A simple translator using Yaml 

## Usage

Create a translation file in your package.

```
your_package
your_package/__init__.py
your_package/translator/__init__.py
your_package/translator/en.yaml
your_package/translator/ko.yaml
```

``your_package/translator/en.yaml`` file:
```.yaml
menu:
  title: "Title"
  subtitle: "{sub} Subtitle"
```

``your_package/translator/ko.yaml`` file:
```.yaml
menu:
  title: "제목"
  subtitle: "소제목 {sub}"
```

- <i>See "[Installing Package Data](https://docs.python.org/3/distutils/setupscript.html#distutils-installing-package-data)"
for how to add a yaml file to your deployment package.<i>


Import package:
```.python
from yaml_translator import Translator
from your_package import translations
```

Create ``Translator`` instance:
```.python
t = Translator.from_module_dir(translations, "ko")
```

Get translated text:
```.python
t("menu.title")
t("menu.subtitle", sub="TEMP")
```

Change language code:
```.python
t.lang = "ko"
```

## License

See the [LICENSE](./LICENSE) file for details. In summary,
**yaml-translator** is licensed under the **MIT license**.
