# bad-youtube-search
## Description
See the worst of YouTube, one 30-second video mosaic at a time.

###### [GitHub Project Link](https://github.com/aymswick/bad-youtube-search/tree/development)
##### By Anthony, Robert, and Sean

## Dependency Installation
```sh
sudo pip install --upgrade google-api-python-client
sudo pip install Pillow==2.9
sudo pip install moviepy
```

## Setup
Requires a YouTube Data API Key
* [Click here to create a server key](https://console.developers.google.com/apis/credentials)
* Then create a file called ```YOURAPIKEY.py```
  with the contents:
  ```APIKEY="<Replace with your API key"```
  Save it in the same directory as ```main.py```, ```badgui.py```, and ```badrender.py```
* Your directory structure should look like this:
```
 + bad-youtube-search
 |
 |-+ badvideos
 | |- <Empty Folder>
 |
 |-+ temp
 | |- <Empty Folder>
 |
 |- .gitignore
 |- badgui.py
 |- badlayout.png
 |- badrender.py
 |- main.py
 |- README.md
 |- YOURAPIKEY.py
```
