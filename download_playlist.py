import os
import time
import pytube
import argparse
import threading
import pickle as pk
import pytube as pt

def main(url, out_dir):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    playlist = pt.Playlist(url)
    playlist = [link for link in playlist.parse_links()]

    threads = []
    for link in playlist:
        t = threading.Thread(target=downlaod, args=(link,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Done!')

def downlaod(link):
    while True:
        try:
            url = f'https://www.youtube.com{link}'
            print(f'Downloading {url}')
            yt = pt.YouTube(url)
            yt.streams.filter(only_audio=True, subtype='mp4').first().download('audio/')
            print(f'{url} done.')
            break
        except pytube.exceptions.RegexMatchError as e:
            print(f'Error: {e}')
            print(f'This might be a private video, aborted.')
            return
        except Exception as e:
            print(f'Error: {e}')
            print(f'Will retry in 5 seconds')
            time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--playlist-url', help='url of the youtube playlist')
    parser.add_argument('-o', '--output-dir', help='output directory')
    args = parser.parse_args()

    main(args.playlist_url, args.output_dir)
