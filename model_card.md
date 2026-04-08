# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch Recommender 1.0  

---

## 2. Goal / Task  

This system recommends songs based on a user’s preferences such as genre, mood, and energy level. It tries to find songs that best match the user’s “vibe” using these features.

---

## 3. Data Used  

The dataset contains a small number of songs stored in a CSV file. Each song includes features like genre, mood, energy, tempo, valence, danceability, and acousticness.  

Additional songs were added to increase diversity across genres such as pop, rock, jazz, lofi, hip-hop, classical, and electronic. However, the dataset is still small and does not fully represent all music preferences.

---

## 4. Algorithm Summary  

The system assigns a score to each song based on how well it matches the user’s preferences.  

- A genre match gives the highest score  
- A mood match gives additional points  
- Energy is compared numerically, and songs closer to the user’s preferred energy get higher scores  
- Acousticness slightly adjusts the score depending on whether the user prefers acoustic or non-acoustic songs  

The final score is used to rank songs, and the top results are recommended.

---

## 5. Observed Behavior / Biases  

The system tends to prioritize songs that match genre and energy strongly. This means songs with similar energy but different genres may still appear in the recommendations.  

Because the dataset is small, some genres are underrepresented, which can bias the recommendations. The system also assumes simple user preferences and does not handle more complex tastes.

---

## 6. Evaluation Process  

I tested the recommender using different user profiles, such as a “happy pop” listener and a “low-energy acoustic” listener.  

I also ran an experiment by increasing the importance of energy compared to genre. This caused the system to recommend songs with similar energy even when the genre did not match exactly.  

These tests showed that the system behaves as expected but is sensitive to changes in scoring weights.

---

## 7. Intended Use and Non-Intended Use  

This system is designed for educational purposes to demonstrate how recommendation systems work.  

It should not be used in real-world applications because it uses a small dataset and does not consider important factors like user history, lyrics, or personalization.

---

## 8. Ideas for Improvement  

- Add more data to improve recommendation diversity  
- Include features like lyrics, artist similarity, or user listening history  
- Improve the scoring system to balance multiple features better  
- Add diversity so recommendations are not too similar  

---

## 9. Personal Reflection  

Through this project, I learned how recommendation systems convert user preferences into numerical scores and rank items accordingly. I also realized how small changes in weights can significantly affect recommendations.  

One interesting insight was how simple algorithms can still produce realistic recommendations, but they can also introduce bias depending on which features are prioritized.