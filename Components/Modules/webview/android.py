import sys
import os
import logging
import threading
from webview import OPEN_DIALOG, FOLDER_DIALOG, SAVE_DIALOG

logger = logging.getLogger(__name__)

try:
    import androidhelper
    droid = androidhelper.Android()

except ImportError as e:
    logger.warn("androidhelper is not found")
    _import_error = True
else:
    _import_error = False

if _import_error:
    try:
        import android
        droid = android.Android()
    except ImportError as e:
        logger.warn("android is not found")
        _import_error = True
    else:
        _import_error = False


def create_window(title, url, width, height, resizable, fullscreen, min_size):

    droid.webViewShow(url = url)#...

