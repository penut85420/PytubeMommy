# Pytube Mommy

## Introduction
+ When your mom told you that she want to put some video of YouTube into her mp3 player, and there are hundreds of videos to download..., this project may be helpful to you!

## Requirement
+ `pytube3` package
  ```
  $ pip install pytube3
  ```
+ (Optional) If the mp3 player is not support playing mp4 audio file, you may need `ffmpeg` to do batch conversion.
  + [Download FFmpeg](https://www.ffmpeg.org/download.html)
  + If you are using Ubuntu, get FFmpeg from `sudo apt install ffmpeg`.

## Usage
+ First of all, train your mom how to add youtube video into playlist.
+ [`download_playlist.py`](download_playlist.py) can download all videos in a YouTube playlist.
  ```
  $ python download_playlist.py -u [playlist-url] -o [output-dir]
  ```
+ (Optional) If you need to convert `.mp4` into `.mp3`, then you can use [`to_mp3.py`](to_mp3.py).
  ```
  $ python to_mp3.py [input_dir] [output_dir]
  ```

## License
+ Licensed under the MIT license.