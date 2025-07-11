# 🎬 Movie Recommender System

A fast, interactive movie recommendation engine using the TMDB reviews dataset and cosine similarity. Get personalized top-5 movie suggestions and discover new favorites through an intuitive Streamlit web app.

---

## 🚀 Features

- **Personalized Recommendations:**  
  Instantly receive the top 5 movie recommendations based on your selection.

- **Visual Experience:**  
  See movie posters alongside recommendations for a richer experience.

- **User-Friendly Web App:**  
  Built with [Streamlit](https://streamlit.io/) for easy and responsive interaction.

- **Efficient Processing:**  
  Preprocessed data and optimized similarity search for fast results.

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```


### 2. Install Dependencies

```bash
pip install -r requirements.txt
```


### 3. Prepare the Data

- Download the TMDB reviews dataset from [Kaggle](https://www.kaggle.com/).
- Run the data preprocessing notebook to generate:
  - `similarity.pkl`
  - `movies_dict.pkl`
- Place these files in your project directory.

### 4. Launch the App

```bash
streamlit run app1.py
```


- Open the provided local URL in your browser.
- Select a movie and view your recommendations!

---

## 📁 Project Structure

```bash
movie-recommender/
│
├── app1.py # Streamlit app main script
├── notebook.ipynb # Data preprocessing and model building
├── requirements.txt # List of dependencies
├── similarity.pkl # Precomputed similarity matrix
├── movies_dict.pkl # Movie metadata dictionary
└── README.md # Project documentation
```

---

## 🧑‍💻 Skills & Technologies

- Python, Pandas, NumPy
- Scikit-learn (cosine similarity)
- Streamlit (web app development)
- Data preprocessing & feature engineering
- Model serialization (pickle)

---

## 💡 Example Usage

1. **Select a Movie:**  
   Use the dropdown to choose any movie.

2. **Get Recommendations:**  
   Instantly see the top 5 similar movies, complete with posters.

---

## ❓ Troubleshooting

- **Missing Pickle Files:**  
  Ensure `similarity.pkl` and `movies_dict.pkl` are in the project directory.

- **Dependency Errors:**  
  Check that all packages in `requirements.txt` are installed.

---

## 📜 License

Open-source for personal and academic use. Please cite if used in research.

---

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for the dataset
- [Kaggle](https://www.kaggle.com/) for data hosting
- [Streamlit](https://streamlit.io/) for the web framework

---

Enjoy discovering your next favorite movie! 🍿
