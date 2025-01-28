import sys
from modules import core
from expdataloader import ExpDataLoader


def run_video(source_img_path, target_video_path, out_video_path):
    core.run(source_img_path, target_video_path, out_video_path)


def main():
    sys.argv += ["--execution-provider", "cuda", "--max-memory", "60"]
    sys.argv.extend(["--frame-processor", "face_swapper", "face_enhancer"])
    loader = ExpDataLoader("deeplivecam")
    loader.run_video = run_video
    loader.print_run_pairs()
    loader.run_all()


if __name__ == "__main__":
    main()
