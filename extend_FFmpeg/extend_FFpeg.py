import ffmpeg


# V 4.1.2 Needed 

# input = ffmpeg.input('IMG_4743.MP4')
in_file = ffmpeg.input('input.mp4')

def main():
    # in_file = ffmpeg.input('input.mp4')
    # sel_frame = in_file.trim(start_frame=1, end_frame=2)
    # print(sel_frame)
    # ext_interval = [sel_frame for i in range(25)]
    # ext_interval.append(in_file)
    # # (
    # #     ffmpeg
    # #     .input('IMG_4743.MP4')
    # #     .trim(start_frame=1, end_frame=2)
    # #     .output('output.mp4')
    # #     .run()
    # # )
    # (
    #     ffmpeg
    #     .concat(
    #             sel_frame,
    #             sel_frame,
    #             sel_frame,
    #             sel_frame,
    #             in_file
    #         )
    #     .output('output.mp4')
    #     .run()
    # )


if __name__ == '__main__':
    main()
