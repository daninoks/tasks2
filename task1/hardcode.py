#!/usr/bin/env python
import argparse
import os
import re
from moviepy.editor import *
from moviepy.video.fx.all import freeze

# task execution time = 03:09 [HH:MM]


# Arguments for terminal ussage:
parser = argparse.ArgumentParser(description=format(
        'This program extends the given frame of the video to first 15 seconds'
    ),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-ptf', '--path-to-file',
    required=True,
    type=str,
    help='Path to video file to be extended (can be relative or absolute)'
)
parser.add_argument('-pre', '--prefix',
    default='_extended',
    type=str,
    help='Edited video file name prefix'
)
parser.add_argument('-ft', '--frame',
    default='0',
    type=float,
    help='Select frame that will be extended to first 15 seconds.'
        'By default 1st frame of second selected.'
        'Second can be provided as float to select exact frame needed'
)
args = parser.parse_args()
config = vars(args)
print(config)

def main():
    """Load selected video and freeze the frame by t1 (00:00:00:00)"""
    """Then create a new video with 1st 15 seconds extended by selected frame"""
    if os.path.exists(config['path_to_file']):
        t1 = float(config['frame'])
        try:
            # max frame value check:
            clip = VideoFileClip(
                config['path_to_file'],
                audio=False
            ).subclip(t1,t1+1)
            # creating 15 sec long clip with selected frame:
            input_clip = VideoFileClip(
                config['path_to_file'],
                audio=False
            )
            new_clip = input_clip.fx(
                vfx.freeze,
                t=t1,
                freeze_duration=15
            ).subclip(t1, t1+15)

        except (Exception, ValueError) as e:
            digits_re = re.findall('\d{2}.\d{2}', str(e))
            max_frame = float(digits_re[1]) - 1
            print(f'ValueError: Selected frame should be smalle then the {max_frame}')
            sys.exit(os.EX_DATAERR)
        # creating new video file:
        video = CompositeVideoClip([new_clip.set_start(0), input_clip.set_start(15)])
        file_name = re.split('\.', re.split('/', config['path_to_file'])[-1])[0]
        video.write_videofile(f"{file_name}{config['prefix']}.webm")

    else:
        print('Error: File given in --path-to-file does not exists')
        sys.exit(os.EX_DATAERR)


if __name__=='__main__':
    main()
