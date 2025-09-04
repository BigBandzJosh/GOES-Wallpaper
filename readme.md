"# GOES Wallpaper

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Automatically download and set the latest GOES-19 satellite imagery of Canada as your Windows desktop wallpaper.

## Overview

This Python script fetches the most recent GOES-19 satellite image of Canada from NOAA's STAR (Center for Satellite Applications and Research) and automatically sets it as your Windows desktop wallpaper. The images are high-resolution (9000x4500) GEOCOLOR imagery that provides stunning real-time views of Canada from space.

## Features

- 🛰️ Downloads latest GOES-19 satellite imagery of Canada
- 🖼️ Automatically sets image as Windows desktop wallpaper
- 📁 Saves images to `Pictures` folder for easy access
- 🎨 Configures wallpaper to "Fill" style for optimal display
- 🔄 Perfect for automation with Windows Task Scheduler

## Requirements

- **Operating System**: Windows (uses Windows Registry and Win32 API)
- **Python**: 3.6 or higher
- **Dependencies**:
  - `requests` - HTTP library for downloading images
  - `beautifulsoup4` - HTML parsing for finding latest images

## Installation

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/BigBandzJosh/GOES-Wallpaper.git
   cd GOES-Wallpaper
   ```

2. **Install required Python packages:**
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### Manual Execution

Run the script directly to update your wallpaper immediately:

```bash
python goes_wallpaper.py
```

The script will:
1. Connect to NOAA's GOES-19 image directory
2. Find the latest Canada satellite image
3. Download the image to `%USERPROFILE%\Pictures\goes_canada.jpg`
4. Set it as your desktop wallpaper

### Automated Execution

For regular updates, set up a scheduled task using Windows Task Scheduler:

1. Open **Task Scheduler** (search in Start menu)
2. Click **Create Basic Task**
3. Name: "GOES Wallpaper Update"
4. Trigger: **Daily** (or your preferred frequency)
5. Action: **Start a program**
   - Program: `python` (or full path to python.exe)
   - Arguments: `goes_wallpaper.py`
   - Start in: `C:\path\to\GOES-Wallpaper` (your script directory)

## How It Works

1. **Web Scraping**: The script fetches the HTML directory listing from NOAA's GOES-19 Canada sector
2. **Image Selection**: Parses the page to find all high-resolution (9000x4500) JPEG files
3. **Latest Image**: Sorts by filename to get the most recent timestamp
4. **Download**: Downloads the latest image using HTTP requests
5. **Wallpaper Setup**: Uses Windows Registry to set wallpaper style and Win32 API to apply the image

## Data Source

Images are sourced from:
- **Provider**: NOAA STAR (Center for Satellite Applications and Research)
- **Satellite**: GOES-19 (GOES East)
- **Sector**: Canada (CAN)
- **Product**: GEOCOLOR
- **Resolution**: 9000x4500 pixels
- **Update Frequency**: Every 10-15 minutes

**URL**: `https://cdn.star.nesdis.noaa.gov/GOES19/ABI/SECTOR/can/GEOCOLOR/`

## Troubleshooting

### Common Issues

**"No JPG links found" error:**
- Check your internet connection
- NOAA servers may be temporarily unavailable
- Try running the script again in a few minutes

**Permission errors:**
- Ensure Python has permission to write to the Pictures folder
- Run as administrator if necessary

**Import errors:**
- Install missing dependencies: `pip install requests beautifulsoup4`
- Verify Python 3.6+ is installed

**Wallpaper not updating:**
- Check that the image was downloaded to `Pictures\goes_canada.jpg`
- Windows may cache wallpaper changes; try refreshing desktop (F5)
- Ensure Windows user has permission to change wallpaper

### Debug Mode

Add print statements or logging to see detailed execution steps:

```python
print(f"Found {len(jpg_links)} images")
print(f"Latest image: {latest_image}")
print(f"Saved to: {local_path}")
```

## Contributing

Contributions are welcome! Here are some ideas for improvements:

- Add support for other GOES-19 sectors (CONUS, Mesoscale, etc.)
- Add Linux/macOS support
- Create a GUI interface
- Add image enhancement options
- Implement error logging
- Add configuration file support

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **NOAA STAR** for providing free access to GOES-19 satellite imagery
- **GOES-19 Satellite** for capturing these amazing views of Earth
- The Python community for excellent libraries like `requests` and `BeautifulSoup`

---

*Enjoy your real-time satellite view of Canada! 🇨🇦 🛰️*" 
