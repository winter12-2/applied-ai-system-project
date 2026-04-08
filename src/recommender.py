from typing import List, Dict, Tuple
import csv

# -------------------------
# LOAD SONGS
# -------------------------

def load_songs(csv_path: str) -> List[Dict]:
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)

    return songs


# -------------------------
# SCORE SONG
# -------------------------

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match")

    # Mood match
    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match")

    # Energy similarity
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0, 1.0 - energy_diff)
    score += energy_score
    reasons.append("similar energy")

    # Acoustic preference (simple explanation)
    if song["acousticness"] > 0.5:
        reasons.append("more acoustic")
    else:
        reasons.append("non-acoustic preference")

    return score, reasons


# -------------------------
# RECOMMEND SONGS
# -------------------------

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    # Sort by highest score
    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:k]