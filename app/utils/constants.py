"""
Poricom Constants
Copyright (C) `2021-2022` `<Alarcon Ace Belen>`

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from .types import ButtonConfigDict

# ------------------------------------- General ------------------------------------- #

IMAGE_EXTENSIONS = ["*.bmp", "*.gif", "*.jpeg", "*.jpg", "*.pbm", "*.pgm", "*.png", "*.ppm", "*.webp", "*.xbm", "*.xpm",]

# Paths
TESSERACT_LANGUAGES = "./assets/languages/"

TOOLBAR_ICONS = './assets/images/icons/'
TOOLBAR_ICON_DEFAULT = './assets/images/icons/default_icon.png'

EXPLORER_ROOT_DEFAULT = './assets/images/'

# ------------------------------------ Settings ------------------------------------- #

SETTINGS_FILE_DEFAULT = './utils/poricom-config.ini'

# View
IMAGE_VIEW_DEFAULT = {
    "viewImageMode": 0,
    "splitViewMode": "false",
    "zoomPanMode": "false"
}
IMAGE_VIEW_TYPES = {
    "viewImageMode": int,
    "splitViewMode": bool,
    "zoomPanMode": bool
}

# --------------------------------------- UI ---------------------------------------- #

# Main view
MAIN_VIEW_RATIO = [1, 9]

# Toolbar
TOOLBAR_ICON_SIZE = 0.05  # Fraction of primary screen height

NAVIGATION_FUNCTIONS: ButtonConfigDict = {
    "zoomIn": {
        "title": "Zoom in",
        "message": "Hint: Double click the image to reset zoom.",
        "path": "zoomIn.png",
        "toggle": False,
        "align": "AlignRight",
        "iconHeight": 0.45,
        "iconWidth": 0.45
    },
    "zoomOut": {
        "title": "Zoom out",
        "message": "Hint: Double click the image to reset zoom.",
        "path": "zoomOut.png",
        "toggle": False,
        "align": "AlignRight",
        "iconHeight": 0.45,
        "iconWidth": 0.45
    },
    "loadImageAtIndex": {
        "title": "",
        "message": "Jump to page",
        "path": "loadImageAtIndex.png",
        "toggle": False,
        "align": "AlignRight",
        "iconHeight": 0.45,
        "iconWidth": 1.3
    },
    "loadPrevImage": {
        "title": "",
        "message": "Show previous image",
        "path": "loadPrevImage.png",
        "toggle": False,
        "align": "AlignRight",
        "iconHeight": 0.45,
        "iconWidth": 0.6
    },
    "loadNextImage": {
        "title": "",
        "message": "Show next image",
        "path": "loadNextImage.png",
        "toggle": False,
        "align": "AlignRight",
        "iconHeight": 0.45,
        "iconWidth": 0.6
    }
}
TOOLBAR_FUNCTIONS: dict[str, ButtonConfigDict] = {
    "file": {
        "openDir": {
            "title": "Open manga directory",
            "message": "Open a directory containing images.",
            "path": "openDir.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "openManga": {
            "title": "Open manga file",
            "message": "Supports the following formats: cbr, cbz, pdf.",
            "path": "openManga.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "captureExternalHelper": {
            "title": "External capture",
            "message": "This will minimize the app and perform OCR on the current screen. Alternatively, you may use the shortcut Alt+Q.",
            "path": "captureExternalHelper.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        }
    },
    "view": {
        "toggleStylesheet": {
            "title": "Change theme",
            "message": "Switch between light and dark mode.",
            "path": "toggleStylesheet.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "hideExplorer": {
            "title": "Hide explorer",
            "message": "Hide the file explorer from view",
            "path": "hideExplorer.png",
            "toggle": True,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "modifyFontSettings": {
            "title": "Modify preview text",
            "message": "Change font style and font size of preview text.",
            "path": "modifyFontSettings.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "toggleSplitView": {
            "title": "Turn on split view",
            "message": "View two images at once.",
            "path": "toggleSplitView.png",
            "toggle": True,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "scaleImage": {
            "title": "Adjust image scaling",
            "message": "Fit an image according to the available options: fit to width, fit to height, fit to screen",
            "path": "scaleImage.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        }
    },
    "controls": {
        "toggleMouseMode": {
            "title": "Change mouse behavior",
            "message": "This will disable text detection. Turn this on only if do not want to hold CTRL key to zoom and pan on an image.",
            "path": "toggleMouseMode.png",
            "toggle": True,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "modifyHotkeys": {
            "title": "Remap hotkeys",
            "message": "Change shortcut for external captures.",
            "path": "modifyHotkeys.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        }
    },
    "misc": {
        "loadModel": {
            "title": "Switch detection model",
            "message": "Switch between MangaOCR and Tesseract models.",
            "path": "loadModel.png",
            "toggle": True,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "modifyTesseract": {
            "title": "Tesseract settings",
            "message": "Set the language and orientation for the Tesseract model.",
            "path": "modifyTesseract.png",
            "toggle": False,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        },
        "toggleLogging": {
            "title": "Enable text logging",
            "message": "Save detected text to a text file located in the current project directory.",
            "path": "toggleLogging.png",
            "toggle": True,
            "align": "AlignLeft",
            "iconHeight": 1.0,
            "iconWidth": 1.0
        }
    }
}
