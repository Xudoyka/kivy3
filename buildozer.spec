[app]
#title = My Application
title = HavoPosboni
package.name = HavoPosboni
#package.domain = org.test
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
#version = 0.1
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2



[android]
android.sdk = 36
android.build_tools = 36.0.0
android.api = 36
android.minapi = 21
android.ndk = 25b
android.ndk_path =/usr/local/lib/android/ndk-r25b
#android.sdk_path =$HOME/.buildozer/android/platform/android-sdk
android.sdk_path =/usr/local/lib/android/sdk
#android.sdk_path =/home/runner/.buildozer/android/platform/android-sdk
android.gradle_dependencies = com.android.tools.build:gradle:7.3.3
#android.archs = arm64-v8a, armeabi-v7a
android.archs = arm64-v8a, armeabi-v7a, x86, x86_64
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab
