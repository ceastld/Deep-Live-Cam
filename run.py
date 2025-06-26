from modules import core
import subprocess

def run_video(source_img_path: str, target_video_path: str, out_video_path: str) -> None:
    core.run(source_img_path, target_video_path, out_video_path)


def concat_videos_hstack(input_video: str, output_video: str, concat_output: str) -> bool:
    """Use ffmpeg to horizontally stack two videos side by side"""
    try:
        subprocess.run([
            "ffmpeg",
            "-i", input_video,
            "-i", output_video,
            "-filter_complex", "hstack=inputs=2",
            "-c:a", "copy",
            "-y", concat_output
        ], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to concatenate {input_video} and {output_video}")
        return False


def main():
    # run_video("girl.png","p2.mp4","p2_output.mp4")
    # run_video("data/source/g2.jpg", "data/target/p1.mp4", "data/output/g2_p1.mp4")
    # run_video("data/source/g2.jpg", "data/target/p2.mp4", "data/output/g2_p2.mp4")
    
    # Concatenate input and output videos horizontally
    concat_videos_hstack("data/target/p1.mp4", "data/output/g2_p1.mp4", "data/output/g2_p1_concat.mp4")
    concat_videos_hstack("data/target/p2.mp4", "data/output/g2_p2.mp4", "data/output/g2_p2_concat.mp4")


if __name__ == "__main__":
    main()
