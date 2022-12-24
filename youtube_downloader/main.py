from pytube import YouTube, Playlist
import sys
import os
from PySide6.QtWidgets import QApplication,QFileDialog, QPushButton, QLabel
from interface import Ui_MainWindow

class Window(Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("YouTube Downloader")
        self.ui.format_mp4.toggle()
        self.ui.directory_select.clicked.connect(self.directory_select)
        self.ui.download.clicked.connect(self.download)
        self.ui.get_res.clicked.connect(self.show_res_list)

    def directory_select(self):
        self.f_name = QFileDialog.getExistingDirectory(self)
        if len(self.f_name)>40:
            f_show = self.f_name[-40:]
            f_show = '...' + f_show[f_show.index('/'):]
        else:
            f_show = self.f_name
        self.ui.label.setText(f_show)
        print(self.f_name)
        
    def show_res_list(self):
        link = self.ui.url.text()
        if link.find('/playlist?') !=-1:
            self.yt = Playlist(link)
            res_list = [stream.resolution for stream in self.yt.videos[0].streams.filter(progressive=True, file_extension='mp4')]
        else:
            self.yt = YouTube(link)
            res_list = [stream.resolution for stream in self.yt.streams.filter(progressive=True, file_extension='mp4')]
        self.ui.res_list.addItems(res_list)

    def get_audio(self, video):
        v = video.streams.filter(only_audio=True).first()
        out = v.download(output_path=self.f_name)
        base, ext = os.path.splitext(out)
        new_file = base + '.mp3'
        os.rename(out, new_file)

    def download(self):
        if type(self.yt) is Playlist:
            for video in self.yt.videos:
                if self.ui.format_mp3.isChecked():
                    self.get_audio(video)
                else:    
                    v = video.streams.get_by_resolution(self.ui.res_list.currentText())
                    print(type(v))
                    v.download(output_path=self.f_name)
                self.setWindowTitle(f"Download in progress")
        else:
            if self.ui.format_mp3.isChecked():
                self.get_audio(self.yt)
            else:
                v = self.yt.streams.get_by_resolution(self.ui.res_list.currentText())
                v.download(output_path=self.f_name)
        self.setWindowTitle(f"YouTube Downloader")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())