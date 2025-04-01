[app]
title = HavoPosboni
package.name = HavoPosboni
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
#requirements = python3,kivy,pillow
requirements = python3,kivy==2.3.1
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
android.sdk = 34
android.build_tools = 34.0.0
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk_path = /usr/local/lib/android/sdk
android.gradle_dependencies = com.android.tools.build:gradle:8.1.0
android.archs = arm64-v8a, armeabi-v7a, x86, x86_64
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab
android.accept_sdk_license = True
