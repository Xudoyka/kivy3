[app]

title = HavoPosboni
package.name = havo_posboni
package.domain = org.havo.posboni
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf
version = 1.0
icon.filename = icon.png
orientation = portrait

# Window yo‘q, chunki bu Android ilova
fullscreen = 1

# Requirements
requirements = python3,kivy,kivymd,PyMuPDF

# Android sozlamalari
android.build_tools = 34.0.0
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0

# Logcat uchun
log_level = 2
