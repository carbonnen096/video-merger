from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

def merge_videos(video_paths, output_path):
    clips = [VideoFileClip(v) for v in video_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)

if __name__ == "__main__":
    output = sys.argv[1]
    videos = sys.argv[2:]
    merge_videos(videos, output)
