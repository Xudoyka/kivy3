# buildozer.spec faylining asosiy qismi
[app]
title = HavoPosboni
package.name = havo_posboni
package.domain = org.example
source.dir = .
source.include_exts = py,png,kv,jpg,atlas,pdf
version = 1.0
icon.filename = icon.png
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.build_tools_version = 34.0.0
# Internet kerak bo‘lmasa:
android.permissions = 

[buildozer]
log_level = 2
warn_on_root = 1

# .py faylingiz
entrypoint = main.py
