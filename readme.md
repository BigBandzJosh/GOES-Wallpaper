#  Dynamic GOES-19 Satellite Wallpaper (Windows)

This repo will automatically updates your Windows wallpaper with the latest **GOES-19 satellite imagery (Canada sector, geocolor composite)**.  
It fetches the newest image from NOAA’s servers, saves it locally, and applies it as your wallpaper.  
Using **Task Scheduler**, it can refresh automatically in the background. (Must implement on your own)



##  Files in this repo 
- **`goes_wallpaper.py`**  
  - Downloads the most recent GOES-19 Canada image.  
  - Saves it to your `Pictures` folder.  
  - Sets it as your wallpaper.  

- **`wallpaper_runner.vbs`**  
  A wrapper that runs the Python script **in the background** (no prompts at all).  



## How It Works
1. `wallpaper_runner.vbs` launches the Python script hidden.  
2. The Python script scrapes the NOAA site, finds the newest 9000×4500 image, downloads it, and updates your wallpaper.  
3. Task Scheduler runs the `.vbs` file on a set interval (e.g., every 30 minutes).  


## Setting Up Task Scheduler

1. Open **Task Scheduler** (`Win + R` → `taskschd.msc`).  
2. In the right panel, click **Create Task**.  
3. Name it something like **Dynamic Wallpaper** (Mine is named **Wallpaperupdater**).  
4. Decide when you want it to run:  
   - Daily, or  
   - At logon, or  
   - Set to repeat every X minutes (adjustable later) (I run mine every 15 minutes).  
5. Under **Action**, choose **Start a Program**.  
6. Fill in:  
   - **Program/script:**  
     ```
     wscript.exe
     ```  
   - **Add arguments:**  
     ```
     "C:\your\file\path\to\wallpaper_runner.vbs"
     ```  
7. Edit anything else you feel needs doing.  

### Optional: 
- Right-click the task → **Properties**:  
  - In **Triggers**, you can set *Repeat task every 15 minutes*.  
  - In **General**, check:  
    -  *Run whether user is logged on or not*  
    -  *Run with highest privileges*  


##  Notes
- Requires Python 3.11+ and the packages `requests` + `beautifulsoup4`.  
- The script overwrites the old image, so disk space won’t get crazy.  
- Resolution is 9000×4500, which looks great on 1080p and higher displays.  
- NOAA updates GOES imagery every 10–15 minutes.  



