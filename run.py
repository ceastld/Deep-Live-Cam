from modules import core

def run_video(source_img_path, target_video_path, out_video_path):
    core.run(source_img_path, target_video_path, out_video_path)


def main():
    run_video("girl.png","p2.mp4","p2_output.mp4")


if __name__ == "__main__":
    main()
