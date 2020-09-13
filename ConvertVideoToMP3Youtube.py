#from __future__ import unicide_literals
import youtube_dl
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd
from _datetime import datetime
#-------------------Class-----------------------
class Downloader():
    def __init__(self,master):
        self.master=master
        self.frame = ttk.Frame(self.master)
        self.frame.grid()
        self.tabControl = ttk.Notebook(self.master)
        self.tabControl.config(width=305, height=300)

        self.download_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.download_tab, text='Download')
        self.tabControl.grid()
        self.about_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.about_tab, text='About')

        self.options = IntVar()
        self.options.set(value=0)
        self.quality=StringVar()
        self.format=StringVar()
        self.quality_opts = ['320', '1411', '320', '128']
        self.format_opts = ['mp3', 'm4a', 'flac', 'wav', 'best', 'aac', 'opus', 'vorbis']
        self.save_path = os.path.join(os.path.expanduser('~'),'Downloads')
        os.chdir(self.save_path)
        self.download_page()
        self.about_page()
    def download_page(self):
        self.url_label = ttk.Label(self.download_tab, text = 'Video / Playlist / URL:')
        self.url_label.grid(row = 0, column= 1)

        self.url_entry= ttk.Entry(self.download_tab, width=48)
        self.url_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.option= ttk.LabelFrame(self.download_tab, text = 'Download as ', width=250, height=50)
        self.option.grid(row=2, column=1)

        self.video_option=ttk.Radiobutton(self.option, text = 'Video', variable=self.options, value=0)
        self.video_option.grid(row=0, column=0, padx=10)

        self.song_option = ttk.Radiobutton(self.option, text='Song', variable=self.options, value=1)
        self.song_option.grid(row=1, column=0, padx=10)

        self.audioQ_label= ttk.Label(self.option, text= 'Audio Quality')
        self.audioQ_label.grid(row=1, column=0, padx=5)
        self.audioQ_drop = ttk.OptionMenu(self.option, self.quality, *self.quality_opts)
        self.audioQ_drop.grid(row=1, column=1)

        self.audioF_label=ttk.Label(self.option, text= 'Audio Format')
        self.audioF_label.grid(row=2, column=0)
        self.audioF_drop = ttk.OptionMenu(self.option, self.format, *self.format_opts)
        self.audioF_drop.grid(row=2, column=1)
        self.location_label = ttk.Label(self.download_tab, text ='Location')
        self.location_label.grid(row=3, column=0)
        self.location_entry = ttk.Entry(self.download_tab, width=35)
        self.location_entry.grid(row=4, column=0, columnspan=2)
        self.location_entry.insert(0, str(self.save_path))
        self.location_button= ttk.Button(self.download_tab, text='Set', command=self.set_path)
        self.location_button.grid(row=4, column=2)

        self.download_button=ttk.Button(self.download_tab, text = 'Download', command=self.download)
        self.download_button.grid(row=5, column=1, pady=15)
        tk.Label(self.download_tab, text=datetime.now().strftime('%A, %d %B %Y'), font='Montserrat 8', bg='#CDD1D1',
                 fg='#1A2121').grid(row=7, column = 1)

    def about_page(self):
        pass
    def download(self):
            self.url = self.url_entry.get()
            self.ydl = youtube_dl.YoutubeDL(self.get_opts())
            self.ydl.download([self.url])

    def set_path(self):
            self.path =fd.askdirectory()
            self.location_entry.delete(0,END)
            self.location_entry.insert(0, str(self.path))
    def get_opts(self):
        self.save= self.location_entry.get()
        self.filetype = self.options.get()
        self.quality = self.quality.get()
        self.file_format = self.format.get()

        if self.filetype == 0:
            self.opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'}],
                'outtmpl': self.save + '/%(title)s.%(ext)s',
                'noplaylist': True
            }
        elif self.filetype == 1:
            self.opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferedcodec': self.file_format,
                    'preferedformat': self.quality}],
                'extractaudio': True,
                'outtmpl': save + '/%(title)s.%(ext)s',
                'noplaylist': True
            }
        return self.opts

if __name__ == '__main__':
    root=Tk()
    root.title('MP3 Youtube Downloader')
    Downloader(root)
    root.mainloop()