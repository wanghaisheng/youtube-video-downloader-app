import streamlit as st
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable


def validate_url(url):  # Check to ensure that the url is valid or not
    try:
        return YouTube(url)
    except RegexMatchError:
        st.error('Invalid URL.')
    except VideoUnavailable:
        st.error('This video is unavailable')


st.set_page_config(page_title="Simple Youtube Downloader",
                   page_icon="⚡")  # page configuration
st.title("Youtube Video Downloader")
st.subheader("Enter the URL:")
resolution_list = set()
url = st.text_input(label="URL")  # url from the user

# This block executes if the URL is not None
if url:
    yt = validate_url(url)  # checks the given url is valid or not
    if yt is not None:
        st.image(yt.thumbnail_url, use_column_width=True)
        st.write(
            """
                {}
                ###### Length: {} seconds
                ###### Rating: {} out of 5
            """.format(yt.title, yt.length, yt.rating)
        )

        # adds all available resolutions to a set object
        for stream in yt.streams.filter(progressive=True, file_extension='mp4'):
            resolution_list.add(stream.resolution)
        resolution = st.selectbox("Resolution List", list(
            resolution_list))  # displays resolutions selectbox

        if len(yt.streams) > 0:
            download_video = st.button("Process")  # process button
            if download_video:
                with st.spinner(
                    f'Downloading {yt.title}... ***Please wait to open any files until the download has finished***'
                ):
                    yt.streams.filter(res=resolution).first().download(
                        filename="video.mp4")
                    file_name = yt.title + '.mp4'
                    with open("video.mp4", "rb") as fp:  # downloader button
                        button = st.download_button(
                            label="Download Video",
                            data=fp,
                            file_name=file_name
                        )

# Displays a info message when the URL is empty
else:
    st.info("Please, Enter the URL to continue ⏩")
