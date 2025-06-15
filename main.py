import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from moviepy.editor import ImageSequenceClip

def create_smooth_scroll_video(
    url: str,
    duration: int = 10,
    output_video: str = "github_scroll.mp4",
    screen_width: int = 1280,
    screen_height: int = 720,
    frame_rate: int = 24
):
    screenshots_dir = "scroll_frames"
    os.makedirs(screenshots_dir, exist_ok=True)

    # Setup headless Chrome browser
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"--window-size={screen_width},{screen_height}")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)  # wait for page to load

    # Get viewport height and total scroll height dynamically from browser
    viewport_height = driver.execute_script("return window.innerHeight")
    total_scroll_height = driver.execute_script("return document.body.scrollHeight")

    print(f"Viewport height: {viewport_height}px")
    print(f"Total scroll height: {total_scroll_height}px")

    max_scroll_position = total_scroll_height - viewport_height
    total_frames = duration * frame_rate

    print(f"Max scroll position: {max_scroll_position}px")
    print(f"Total frames: {total_frames}")

    # Calculate pixels to scroll per frame for smooth full scroll
    scroll_step = max_scroll_position / total_frames
    print(f"Scroll step per frame: {scroll_step:.2f}px")

    frames = []

    for frame_idx in range(total_frames):
        y_pos = int(frame_idx * scroll_step)
        driver.execute_script(f"window.scrollTo(0, {y_pos});")
        time.sleep(1 / frame_rate)  # keep framerate steady

        screenshot_path = os.path.join(screenshots_dir, f"frame_{frame_idx:04}.png")
        driver.save_screenshot(screenshot_path)
        frames.append(screenshot_path)

        print(f"Captured frame {frame_idx + 1}/{total_frames} at scroll {y_pos}px")

    driver.quit()

    # Create video clip from screenshots
    clip = ImageSequenceClip(frames, fps=frame_rate)
    clip.write_videofile(output_video, fps=frame_rate)

    print(f"Video created successfully: {output_video}")


if __name__ == "__main__":
    create_smooth_scroll_video(
        url="https://github.com/black-forest-labs/flux",
        duration=40,  # seconds
        output_video="flux_repo_scroll2.mp4",
    )
