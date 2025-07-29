# website
https://toolbox.lukemech.org

## Translations helper

- Update sketch
```
pybabel extract -F babel.cfg -o translations/messages.pot .
```

- Init translation strings
- Update translation strings
```
pybabel init -i translations/messages.pot -d translations -l en
pybabel update -i translations/messages.pot -d translations
```

- Compile
```
pybabel compile -d translations
```