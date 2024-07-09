import calendar
import locale

locale.setlocale(locale.LC_ALL, 'de_de')

print(calendar.calendar(2022))
print(locale.getlocale())
# Get-WinSystemLocale

local = locale.locale_alias
for key in local:
    print(key)

for lang in locale.locale_alias.values():
    print(lang)