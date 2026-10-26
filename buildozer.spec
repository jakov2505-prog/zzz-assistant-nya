[app]
title = ZZZ Floating Assistant
package.name = zzzai
package.domain = org.yakov.zzzai
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0.0
requirements = python3,kivy,requests,urllib3,certifi,charset_normalizer,idna

orientation = portrait
fullscreen = 0
android.permissions = SYSTEM_ALERT_WINDOW, INTERNET, FOREGROUND_SERVICE

android.api = 33
android.ndk = 25b
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
