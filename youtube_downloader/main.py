from pytube import YouTube, Playlist
import sys
import os
from PySide6.QtWidgets import QApplication,QFileDialog, QPushButton, QLabel
from PySide6.QtGui import QFont
from interface import Ui_MainWindow

class Window(Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("YouTube Downloader")
        self.ui.format_mp4.toggle()
        self.ui.res_high.toggle()
        self.ui.directory_select.clicked.connect(self.directory_select)
        self.ui.download.clicked.connect(self.download)
        self.ui.res_other.toggled.connect(self.show_res_list)
        self.ui.url.textChanged.connect(self.yt_init)
        self.ui.res_high.toggled.connect(self.clear_reslist)
        self.ui.res_low.toggled.connect(self.clear_reslist)

    def directory_select(self):
        self.f_name = QFileDialog.getExistingDirectory(self)
        if len(self.f_name)>40:
            f_show = self.f_name[-40:]
            f_show = '...' + f_show[f_show.index('/'):]
        else:
            f_show = self.f_name
        self.ui.label.setText(f_show)
    
    def yt_init(self):
        self.ui.res_high.toggle()
        link = self.ui.url.text()
        if link.find('/playlist?') !=-1:
            self.yt = Playlist(link)
        else:
            self.yt = YouTube(link)


    def show_res_list(self):
        self.ui.res_list.setEnabled(True)
        self.ui.res_list.clear()
        if type(self.yt) is Playlist:
            res_list = [stream.resolution for stream in self.yt.videos[0].streams.filter(progressive=True, file_extension='mp4')]
        else:
            res_list = [stream.resolution for stream in self.yt.streams.filter(progressive=True, file_extension='mp4')]
        self.ui.res_list.addItems(res_list)

    def get_audio(self, video):
        v = video.streams.filter(only_audio=True).first()
        fileslist = [f for f in os.listdir(self.f_name) if os.path.isfile(os.path.join(self.f_name, f))]
        if v.default_filename[:-4]+'.mp3' in fileslist:
            self.ui.download.setFont(QFont('Bahnschrift', 20))
            self.ui.download.setText('Already downloaded')
            return
        else:
            out = v.download(output_path=self.f_name)
            base, ext = os.path.splitext(out)
            new_file = base + '.mp3'
            os.rename(out, new_file)

    def clear_reslist(self):
        self.ui.res_list.clear()
        self.ui.res_list.setEnabled(False)

    def select_res(self, video):
        if self.ui.res_high.isChecked():
            v = video.streams.get_highest_resolution()
        if self.ui.res_low.isChecked():
            v = video.streams.get_lowest_resolution()
        if self.ui.res_other.isChecked():
            self.show_res_list()
            v = video.streams.get_by_resolution(self.ui.res_list.currentText())
        return v


    def download(self):
        self.ui.download.setFont(QFont('Bahnschrift', 34))
        self.ui.download.setText('Download')
        if type(self.yt) is Playlist:
            failures = []
            for video in self.yt.videos:
                video.bypass_age_gate()
                if self.ui.format_mp3.isChecked():
                    try:
                        self.get_audio(video)
                    except KeyError:
                        failures.append(video.title)
                        print(video.title)
                        continue
                    except FileExistsError:
                        continue
                if self.ui.format_mp4.isChecked():
                    v = self.select_res(video)    
                    try:
                        v.download(output_path=self.f_name)
                    except KeyError:
                        failures.append(video.title)
                    except FileExistsError:
                        continue
                self.setWindowTitle(f"Download in progress")
            if len(failures) > 0:
                with open(f'{self.f_name}/errors.txt', 'w') as errorfile:
                    for name in failures:
                        errorfile.write("%s\n" % name)
        else:
            self.yt.bypass_age_gate()
            if self.ui.format_mp3.isChecked():
                try:
                    self.get_audio(self.yt)
                except KeyError:
                    self.ui.label.setText(self.yt.title)###
                    self.ui.download.setFont(QFont('Bahnschrift', 20))
                    self.ui.download.setText('Try another video')
            if self.ui.format_mp4.isChecked():
                v = self.select_res(self.yt)
                try:
                    v.download(output_path=self.f_name)
                except KeyError:
                    self.ui.download.setFont(QFont('Bahnschrift', 20))
                    self.ui.download.setText('Try another video')
                except FileExistsError:
                    self.ui.download.setFont(QFont('Bahnschrift', 20))
                    self.ui.download.setText('Already downloaded')
        self.setWindowTitle(f"YouTube Downloader")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())