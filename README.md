# SyServant 🤵
SyServant is your loyal AI servant, ready to assist your system at all times.

## Environment Requirements
- `pytorch` with CUDA support
- `transformers`
- `moviepy`

## Simple Usage
- Run `capture_screenshots.py` to record your screen. Adjust the `timer = threading.Timer(3, func, [])` setting to change the frame rate (default is 0.33 fps).
- Run `analyse_pics.py` to generate descriptions for all the screenshots, and output the results to a CSV file.

## TODO
- Summarize the screen descriptions using Language Models.
- Explore the use of Video-LLMs for faster analysis.
