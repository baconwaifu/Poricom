"""
Poricom Windows

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

from shutil import rmtree
from time import sleep

from manga_ocr import MangaOcr
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QApplication, QPushButton

from .external import ExternalWindow
from components.popups import BasePopup, CheckboxPopup
from components.settings import (
    BaseSettings,
    PreviewOptions,
    OptionsContainer,
    ShortcutOptions,
    TesseractOptions,
)
from components.toolbar import BaseToolbar
from components.views import WorkspaceView
from services import BaseWorker, State
from utils.constants import (
    LOAD_MODEL_MESSAGE,
    MAIN_WINDOW_DEFAULTS,
    MAIN_WINDOW_TYPES,
    STYLESHEET_DARK,
    STYLESHEET_LIGHT,
)


class MainWindow(QMainWindow, BaseSettings):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.state = State()

        self.vLayout = QVBoxLayout()

        self.mainView = WorkspaceView(self, self.state)
        self.toolbar = BaseToolbar(self)
        self.vLayout.addWidget(self.toolbar)

        self.vLayout.addWidget(self.mainView)
        mainWidget = QWidget()
        mainWidget.setLayout(self.vLayout)
        self.setCentralWidget(mainWidget)

        self.setDefaults(MAIN_WINDOW_DEFAULTS)
        self.setTypes(MAIN_WINDOW_TYPES)
        self.loadSettings()

        self.threadpool = QThreadPool()

    @property
    def canvas(self):
        return self.mainView.canvas

    @property
    def explorer(self):
        return self.mainView.explorer

    def closeEvent(self, event):
        try:
            rmtree("./poricom_cache")
        except FileNotFoundError:
            pass
        self.saveSettings(False)
        self.mainView.saveSettings(False)
        return super().closeEvent(event)

    def noop(self):
        BasePopup("Not Implemented", "This function is not yet implemented.").exec()

    # ------------------------------ File Functions ------------------------------ #

    def captureExternalHelper(self):
        self.showMinimized()
        sleep(0.5)
        if self.isMinimized():
            self.captureExternal()

    def captureExternal(self):
        ExternalWindow(self).showFullScreen()

    # ------------------------------ View Functions ------------------------------ #

    def toggleStylesheet(self):
        if self.stylesheetPath == STYLESHEET_LIGHT:
            self.stylesheetPath = STYLESHEET_DARK
        elif self.stylesheetPath == STYLESHEET_DARK:
            self.stylesheetPath = STYLESHEET_LIGHT

        app = QApplication.instance()
        if app is None:
            raise RuntimeError("No Qt Application found.")

        with open(self.stylesheetPath, "r") as fh:
            app.setStyleSheet(fh.read())

    def modifyFontSettings(self):
        confirmation = OptionsContainer(PreviewOptions(self))
        ret = confirmation.exec()

        if ret:
            app = QApplication.instance()
            if app is None:
                raise RuntimeError("No Qt Application found.")

            with open(self.stylesheetPath, "r") as fh:
                app.setStyleSheet(fh.read())

    # ----------------------------- Control Functions ---------------------------- #

    def modifyHotkeys(self):
        OptionsContainer(ShortcutOptions(self)).exec()

    # ------------------------------ Misc Functions ------------------------------ #

    def loadModel(self):
        loadModelButton = self.toolbar.findChild(QPushButton, "loadModel")
        loadModelButton.setChecked(not self.state.ocrModel)

        if loadModelButton.isChecked() and self.hasLoadModelPopup:
            ret = CheckboxPopup(
                "hasLoadModelPopup",
                "Load the MangaOCR model?",
                LOAD_MODEL_MESSAGE,
                CheckboxPopup.Ok | CheckboxPopup.Cancel,
            ).exec()
            if ret == CheckboxPopup.Cancel:
                loadModelButton.setChecked(False)
                return

        def loadModelHelper(state: State):
            betterOCR = state.switchOCRMode()
            if betterOCR:
                try:
                    state.ocrModel = MangaOcr()
                    return "success"
                except Exception as e:
                    state.switchOCRMode()
                    return str(e)
            else:
                state.ocrModel = None
                return "success"

        def loadModelConfirm(message: str):
            modelName = "MangaOCR" if self.state.ocrModel else "Tesseract"
            if message == "success":
                BasePopup(
                    f"{modelName} model loaded",
                    f"You are now using the {modelName} model for Japanese text detection.",
                ).exec()
            else:
                BasePopup("Load Model Error", message).exec()
                loadModelButton.setChecked(False)

        worker = BaseWorker(loadModelHelper, self.state)
        worker.signals.result.connect(loadModelConfirm)
        worker.signals.finished.connect(lambda: loadModelButton.setEnabled(True))

        self.threadpool.start(worker)
        loadModelButton.setEnabled(False)

    def modifyTesseract(self):
        confirmation = OptionsContainer(TesseractOptions(self))
        confirmation.exec()
        if confirmation:
            self.canvas.loadSettings()

    def toggleLogging(self):
        self.logToFile = not self.logToFile
        self.canvas.loadSettings()