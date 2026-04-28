import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from recommender import load_songs, recommend_songs


CSV_PATH = "data/songs.csv"


def test_load_songs_returns_data():
    songs = load_songs(CSV_PATH)

    assert songs is not None
    assert len(songs) > 0


def test_recommend_songs_returns_results():
    songs = load_songs(CSV_PATH)

    user_profile = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "acoustic": False
    }

    recommendations = recommend_songs(user_profile, songs)

    assert recommendations is not None
    assert len(recommendations) > 0


def test_recommendations_are_valid():
    songs = load_songs(CSV_PATH)

    user_profile = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "acoustic": False
    }

    recommendations = recommend_songs(user_profile, songs)

    first_recommendation = recommendations[0]

    assert first_recommendation is not None