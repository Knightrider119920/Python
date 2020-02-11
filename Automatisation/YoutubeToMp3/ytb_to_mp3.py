#!/usr/bin/env python

# Credit: https://www.youtube.com/watch?v=eZUpOY8mcRY
from __future__ import unicode_literals
import youtube_dl


def download_ytb_as_mp3(video_adress):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_adress])


video_adress = input('Place video adress: ')
download_ytb_as_mp3(video_adress)
