#!/usr/bin/env python3

import os
import sys
from modules import core
from natsort import natsorted


def get_image_paths(directory):
    image_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg")):
                image_paths.append(os.path.join(root, file))
    return natsorted(image_paths)


def get_run_pairs():
    res = []
    for line in open("exp_data/run_pair.txt").readlines():
        pair = line.strip()
        name = pair.replace(" ", "_")
        out_path = f"exp_data/deeplivecam/{name}.mp4"
        if pair and not os.path.exists(out_path) and not pair in res:
            res.append(pair)
    return res


def run_video(source_img_path, target_video_path, out_video_path):
    core.run(source_img_path, target_video_path, out_video_path)


def exp_pair(pair: str):
    source_name = pair.split(" ")[0]  # PID
    target_name = pair.split(" ")[1]  # HSID
    source_img_path = get_image_paths(f"exp_data/pids/{source_name}")[0]
    target_video_path = f"exp_data/{target_name}/face_crop.mp4"
    assert os.path.exists(target_video_path), "target video dont exists"
    name = pair.replace(" ", "_")
    out_video_path = f"exp_data/deeplivecam/{name}.mp4"
    os.makedirs(os.path.dirname(out_video_path), exist_ok=True)
    if os.path.exists(out_video_path):
        print(f"already done, see {out_video_path}")
        return

    run_video(source_img_path, target_video_path, out_video_path)


if __name__ == "__main__":
    sys.argv += ["--execution-provider", "cuda", "--max-memory", "60"]
    sys.argv.extend(['--frame-processor', 'face_swapper', 'face_enhancer'])
    pairs = get_run_pairs()
    print(pairs)
    for pair in pairs:
        print(pair)
        exp_pair(pair)
