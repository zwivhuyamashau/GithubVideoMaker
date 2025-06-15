# GithubVideoMaker
creates videos based of a github repo.
# 📹 GitHub Page Scroller Video Generator

This Python script captures a smooth, scrolling video of a GitHub repository's main page. It's ideal for showcasing project documentation, README files, or any content displayed on the GitHub interface.

---

## 🛠️ Features

- **Smooth Scrolling**: Emulates natural mouse scrolling.
- **Customizable Duration**: Set the video length in seconds.
- **Full Page Capture**: Scrolls through the entire visible content.
- **Frame Rate Control**: Adjust frames per second for desired smoothness.

---

## 📦 Dependencies

To ensure compatibility and avoid issues with newer versions, we recommend using **MoviePy 1.0.3**. This version is stable and works well with the script.

Install the required dependencies using the following commands:

```bash
pip install moviepy==1.0.3
pip install selenium
```

⚙️ Usage
Clone the Repository:

git clone https://github.com/yourusername/github-scroller.git
cd github-scroller

Run the Script:
python scroller.py

-------
from scroller import create_smooth_scroll_video
create_smooth_scroll_video(
    url="https://github.com/black-forest-labs/flux",
    duration=40,  # Total video length in seconds
    output_video="flux_repo_scroll.mp4",
)
-----
