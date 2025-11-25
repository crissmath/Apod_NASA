import requests
import streamlit as st
from io import BytesIO
from datetime import date

# --- API CONFIG --
API_KEY = st.secrets["NASA_API_KEY"]
APOD_URL = "https://api.nasa.gov/planetary/apod"

# --- STREAMLIT CONFIG ---
st.set_page_config(page_title="NASA Astronomy Picture of the Day", layout="wide")


def get_apod_data(date_str):
    params = {"api_key": API_KEY, "date": date_str}
    try:
        responce = requests.get(APOD_URL, params=params)
        responce.raise_for_status()
        return responce.json()
    except requests.RequestException as e:
        # the problem with this line is that show personal key
        # st.error(f"Error fetching APOD: {e}")
        st.error("⚠️ Could not retrieve the image. Please try a different date.")
        print(e)
        return None


def main():
    st.title("📸 NASA Astronomy Picture of the Day")

    # Date Selector
    selected_date = st.date_input(
        "Select date",
        value=date.today(),
        min_value=date(1995, 6, 16),
        max_value=date.today(),
    )

    # call Api data
    content = get_apod_data(str(selected_date))
    if not content:
        return

    # Get the data use secure metho
    image_url = content.get("hdurl") or content.get("url", "")
    media_type = content.get("media_type", "image")
    title = content.get("title", "No Title")
    apod_date = content.get("date", "No Date")
    copyright_ = content.get("copyright", "No copyright")
    explanation = content.get("explanation", "No explanation available")

    # Show content
    st.markdown(f"## {title}")
    st.markdown(f"*📅 {apod_date}*")

    with st.container():
        st.markdown(
            f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='text-align: center; color: #aaa;'>📅 {apod_date}</p>",
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if media_type == "image" and image_url:
                st.image(content["hdurl"], width=800)

                # --- Option download image ---
                img_responce = requests.get(image_url)
                if img_responce.status_code == 200:
                    img_bytes = BytesIO(img_responce.content)
                    # Download button
                    st.download_button(
                        label="📥 Download Image",
                        data=img_bytes,
                        file_name=f"apod_{apod_date}.jpg",
                        mime="image/jpeg",
                    )
                else:
                    st.warning("⚠️ Image could not be loaded for download")

            elif media_type == "video":
                st.video(image_url)
                st.info("🎥 This is a video. Download not available.")
            else:
                st.warning("⚠️ No media available for today")

            if copyright_:
                st.markdown(
                    f"<p style='text-align: center; color: #888;'>© {copyright_}</p>",
                    unsafe_allow_html=True,
                )

            # Explicación a pantalla completa
        st.markdown("---")
        st.markdown(
            f"<div style='text-align: justify; font-size: 16px;'>{explanation}</div>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()


# Get the image from metadata
# img = requests.get(content["hdurl"])
# print(img)
# with open("apod.jpg", "wb") as file:
#    file.write(img.content)
