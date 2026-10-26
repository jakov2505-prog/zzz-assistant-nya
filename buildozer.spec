[app]

# (str) Title of your application
title = ZZZ Floating Assistant

# (str) Package name
package.name = zzzai

# (str) Package domain (needed for android packaging)
package.domain = org.yakov.zzzai

# (str) Source files where the include files are stored
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv

# (list) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = SYSTEM_ALERT_WINDOW, INTERNET, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) NDK version to use
android.ndk = 25b

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Use --private-storage by default (str)
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = warn, 1 = allow, 2 = ignore)
warn_on_root = 1
