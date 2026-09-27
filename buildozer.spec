[app]

# (str) Title of your application
title = محل صوتيات جيولوجية

# (str) Package name
package.name = geoacoustic

# (str) Package domain (needed for android packaging)
package.domain = org.geo

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude all the files)
#source.exclude_exts = spec

# (list) List of directory to include
source.include_dirs = .

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivyMD

# (str) Custom icon (tells where the icon is located)
#icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK will support.
#android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if run as root (0 = False, 1 = Prohibit lang)
warn_on_root = 1
