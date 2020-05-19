#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess as sp

def main(inn_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    for dirPath, _, fileList in os.walk(inn_dir):
        for filename in fileList:
            fn = os.path.basename(filename)
            fn, ext = os.path.splitext(fn)

            inn_fn = os.path.join(dirPath, filename)
            out_fn = os.path.join(out_dir, f'{fn}.mp3')
            args = ['ffmpeg', '-i', inn_fn, '-y', '-vn', '-acodec', 'libmp3lame', out_fn]
            print(f'Coverting {inn_fn}')
            err = sp.call(args, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
            if err:
                print(f'Conversion error with {inn_fn}')
            else:
                print(f'Conversion success, save to {out_fn}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('inn_dir')
    parser.add_argument('out_dir')
    args = parser.parse_args()

    main(args.inn_dir, args.out_dir)
