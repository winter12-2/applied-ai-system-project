# 🎵 Music Recommender Simulation

## Project Summary

This project implements a simple content-based music recommendation system. It uses song features such as genre, mood, energy, and acousticness to compare each song with a user’s preferences. Based on this comparison, each song is assigned a score, and the system recommends the top matching songs. The goal of this project is to understand how recommendation systems convert user preferences into ranked suggestions.

---

## How The System Works

This recommendation system works by comparing a user’s preferences with the features of each song in the dataset. Features such as genre, mood, energy, and tempo are used to determine how similar a song is to what the user likes. Each song is given a score based on this similarity. Songs that are closer to the user’s preferences receive higher scores. After scoring all songs, they are ranked from highest to lowest score, and the top results are recommended to the user. This system focuses on content-based filtering, meaning it recommends songs based on their attributes rather than other users’ behavior.

### Song Features:
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

### User Preferences:
- favorite genre
- favorite mood
- target energy
- acoustic preference

---

## Scoring Logic

- +2 points if the song genre matches the user's favorite genre  
- +1 point if the mood matches  
- Energy similarity is calculated using:  
  `1 - |song_energy - target_energy|`  
- Acoustic preference is considered based on whether the user prefers acoustic songs  

Songs are scored using these rules and then ranked from highest to lowest score.

---

## Data Flow

Input: User preferences (genre, mood, energy, acoustic preference)  
→ Process: Each song is compared using scoring logic  
→ Output: Ranked list of top recommended songs  

---

## Getting Started

### Setup

1. Create a virtual environment (optional):

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows