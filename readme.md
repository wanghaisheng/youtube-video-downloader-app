## Youtube Video Downloader App
![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![python](https://img.shields.io/badge/Python-0078D4?style=flat-square&logo=python&logoColor=white)
![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?style=flat-square&logo=Windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat-square&logo=visual%20studio%20code&logoColor=white)

- `pytube` is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
- Youtube video downloader app gets the URL from the User using streamlit's `text_input`.
- If the URL is empty then app will displays a info message `Please, Enter the URL to continue`.
- If the URL is Invalid then app will displays a warning message `Invalid URL`.
- If the URL is valid then app will displays a resolution list and `process` button to continue.
- After user selected a resolution and clicked the `process` button it will download the file and store it in a temporary location.
- Finally When the user click the `download` button the file is downloaded to their local machine.

### Installation
To install all necessary requirement packages for the app 👇
```
pip install -r requirements.txt
```

simple function to validate if the given URL is valid or not
```python
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
def validate_url(url):  # Check to ensure that the url is valid or not
    try:
        return YouTube(url)
    except RegexMatchError:
        st.error('Invalid URL.')
    except VideoUnavailable:
        st.error('This video is unavailable')
```
If you like this work hit a star to my github repository and fork this repository.

### If the URL is invalid
![If the URL is invalid](images/out1.gif)

### If the URL is empty
![If the URL is empty](images/out2.gif)

### If the URL is valid
![If the URL is valid](images/out3.gif)
