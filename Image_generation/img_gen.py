import cv2
from PIL import Image
import os

def extract_frames_per_second(video_path, output_folder, target_fps=10, start_time=0, end_time=None):
    # Load the video
    video = cv2.VideoCapture(video_path)
    
    # Get the frame rate (fps) of the video
    video_fps = video.get(cv2.CAP_PROP_FPS)
    
    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate the start and end frame numbers
    start_frame = int(start_time * video_fps)
    end_frame = int(end_time * video_fps) if end_time else total_frames
    
    # Calculate the interval in frames
    interval = int(video_fps / target_fps)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame_number = 0
    success, frame = video.read()
    while success and frame_number <= end_frame:
        if frame_number >= start_frame:
            # Only save the frame if it is on the interval
            if frame_number % interval == 0:
                # Convert the frame from BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Convert the frame to a PIL image
                img = Image.fromarray(frame_rgb)
                
                # Calculate time in seconds
                time_in_seconds = frame_number / video_fps

                # Save the image
                img.save(f"{output_folder}/frame_at_e{time_in_seconds:.2f}s.png")
        
        # Move to the next frame
        success, frame = video.read()
        frame_number += 1
    
    # Release the video
    video.release()

# Example usage
video_path = 'C:\\Users\\ravib\\Videos\\Captures\\5.mp4'
output_folder_nothing = 'C:\\Users\\ravib\\Downloads\\Nothing'


extract_frames_per_second(video_path, output_folder_nothing, target_fps=10, start_time=9, end_time=11)










