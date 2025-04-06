[app]
title = HavoPosboni
package.name = havo_posboni
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf
icon.filename = icon.png
version = 1.0
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[app]
requirements = python3,kivy,kivymd,pymupdf
android.permissions = INTERNET
android.api = 33
android.build_tools_version = 34.0.0
android.minapi = 21
android.ndk = 23b
