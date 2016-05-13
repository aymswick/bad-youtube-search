# Bad YouTube Search
## Description
See the worst of YouTube, one 30-second video mosaic at a time.

*Built and tested on Ubuntu & Xubuntu*

###### [GitHub Project Link](https://github.com/aymswick/bad-youtube-search/tree/development)
##### By Anthony, Robert, and Sean

## Usage
1. Run `python main.py`
2. Enter your desired search term into the text box.
3. Wait while the magic happens.
4. The resulting video should open and play on its own.
   - **Note:** *If the video does not open on its own after the console indicates that moviepy has finished, then browse to the folder `badvideos` and open the file matching the search terms you entered.*


## Dependencies
 * [Python 2.7](https://www.python.org/)
 * [TkInter](https://wiki.python.org/moin/TkInter)
 * [youtube-dl](https://rg3.github.io/youtube-dl/)
 * [Pillow *Version: 2.9*](https://python-pillow.org/)
 * [moviepy](https://zulko.github.io/moviepy/)

 ### Installation
```bash
sudo pip install --upgrade google-api-python-client
sudo pip install youtube-dl
sudo pip install Pillow==2.9
sudo pip install moviepy
```

## Setup
Requires a YouTube Data API Key
* [Click here to create a server key](https://console.developers.google.com/apis/credentials)
* Then create a file called `YOURAPIKEY.py` in the same directory as `main.py`, `badgui.py`, and `badrender.py`
  with the contents:
  ```python
  APIKEY="<Replace with your API key"
  ```
#### Your directory structure should look like this:

 * `bad-youtube-search`
   * `badvideos/`
   * `temp/`
   * `.gitignore`
   * `badgui.py`
   * `badlayout.png`
   * `badrender.py`
   * `main.py`
   * `README.md`
   * `YOURAPIKEY.py`
