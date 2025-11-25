# 🌌 Astronomy Picture of the Day (APOD)

### Author: [crissmath](https://github.com/crissmath)

---

## 📖 Description

This project is a **Streamlit web application** that connects to NASA’s **Astronomy Picture of the Day (APOD) API** to display breathtaking daily imagery of our universe, accompanied by scientific explanations written by astronomers.

Users can:
- 📅 Select any date to retrieve the image or video of that day.
- 📥 Download the full-resolution image if available.
- 🎥 Watch the video if the content is not an image.
- 🧠 Read the corresponding explanation with metadata.

---

## 🚀 Technologies Used

- **Python 3.10+**
- **[Streamlit](https://streamlit.io/)** for UI and layout
- **[Requests](https://docs.python-requests.org/)** for handling HTTP requests
- **[NASA APOD API](https://api.nasa.gov/)** for fetching astronomy data
- **Pillow** (optional) for advanced image handling

---

## 🔧 How It Works

1. The user selects a date from a calendar input.
2. The app fetches data using the NASA APOD API (API key required).
3. If the media is an image:
   - It is displayed in a centered layout.
   - A download button is offered.
4. If the media is a video:
   - It is embedded via Streamlit’s `st.video()`.
5. Additional metadata such as title, copyright, and explanation are shown.

---

## ⚠️ Prerequisites

- Python installed locally
- A valid **NASA API Key** (Free – get it [here](https://api.nasa.gov))

---

## 🧪 Installation & Run Locally

```bash
# Clone this repository
git clone https://github.com/yourusername/apod-streamlit.git
cd apod-streamlit

# (Optional) Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
