# 🎵 Applied AI Music Recommender System

## Project Summary

This project is an improved version of my original Module 1–3 project, **Music Recommender Simulation**. The original project was a simple content-based music recommendation system that recommended songs based on user preferences such as genre, mood, energy, and acoustic preference.

For the final project, I improved the system by adding a **reliability and testing layer** using `pytest`. This makes the project easier to evaluate because the system is not only producing recommendations, but also proving that important parts of the code work correctly.

---

## Original Project

The original project was named **Music Recommender Simulation**. Its goal was to simulate how a basic recommendation system works by comparing user preferences with song features from a dataset.

The system used features such as:

- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

Based on these features, each song received a score. The songs with the highest scores were shown as the top recommendations.

---

## What This System Does

This system recommends music based on a user preference profile. It compares the user’s preferred genre, mood, target energy, and acoustic preference with the available songs in the dataset.

The system then ranks the songs and prints the top recommendations with scores and reasons.

Example output:

```text
Top recommendations:

Sunrise City - Score: 3.98
Because: genre match, mood match, similar energy, non-acoustic preference

Gym Hero - Score: 2.87
Because: genre match, similar energy, non-acoustic preference

Rooftop Lights - Score: 1.96
Because: mood match, similar energy, non-acoustic preference
AI Feature Added for Final Project

For the final project, I added a Reliability and Testing System.

This feature tests whether the recommender system works correctly and consistently. Instead of only running the program manually, I added automated tests to check important parts of the system.

The tests check that:

the song dataset loads successfully
the recommender returns results
the recommendation output is valid

This improves the project because the system can now be tested in a repeatable way.

System Architecture

The system follows this simple flow:

User Input
   ↓
Music Preference Profile
   ↓
Song Dataset
   ↓
Recommendation Logic
   ↓
Ranked Song Recommendations
   ↓
Reliability Tests
Architecture Explanation

The user preference profile contains information such as genre, mood, energy level, and acoustic preference. The system loads songs from the dataset and compares each song with the user profile. Each song gets a score based on how closely it matches the user preferences. Finally, the system prints the highest-ranked recommendations.

The reliability tests check whether this process works correctly.

Folder Structure
applied-ai-system-project/
│
├── assets/
│   └── system_architecture.txt
│
├── data/
│   └── songs.csv
│
├── src/
│   ├── main.py
│   └── recommender.py
│
├── tests/
│   └── test_recommender.py
│
├── README.md
├── requirements.txt
└── model_card.md
Setup Instructions
1. Clone the repository
git clone https://github.com/winter12-2/applied-ai-system-project.git
2. Go into the project folder
cd applied-ai-system-project
3. Install requirements
pip install -r requirements.txt

If pytest is not already installed, install it using:

pip install pytest
How to Run the Project

Run the main program with:

py src/main.py

The program will print the top music recommendations.

How to Run the Tests

Run the reliability tests with:

py -m pytest

Current test result:

3 passed in 0.05s
Reliability and Evaluation

I added automated tests using pytest to measure whether the system works correctly. The tests are located in:

tests/test_recommender.py

The test cases check three main things:

The song dataset loads correctly.
The recommender returns recommendations.
The recommendation output is valid.

Testing result:

3 passed

This shows that the main recommender functions are working and can be checked again in the future if the project changes.

Sample Interactions
Sample Run 1
Input: User prefers pop, happy mood, high energy, and non-acoustic music.

Output:
Sunrise City - Score: 3.98
Because: genre match, mood match, similar energy, non-acoustic preference
Sample Run 2
Input: User prefers energetic music.

Output:
Gym Hero - Score: 2.87
Because: genre match, similar energy, non-acoustic preference
Sample Run 3
Input: User prefers songs with a matching mood.

Output:
Rooftop Lights - Score: 1.96
Because: mood match, similar energy, non-acoustic preference
Design Decisions

I used a content-based recommendation approach because it is simple, explainable, and easy to test. Each song is scored based on how well it matches the user’s preferences.

A trade-off is that this system does not learn from real user behavior. It does not use listening history, likes, skips, or ratings. However, it is easier to understand because the recommendation reasons are clearly shown.

Limitations and Ethics

This system has some limitations. It uses a small dataset, so the recommendations may be repetitive or limited. It also depends on the features available in the dataset. If the song data is incomplete or biased toward certain genres, the recommendations may also be biased.

This system could be improved by using a larger and more diverse dataset. It could also include user feedback so the recommendations become more personalized over time.

A possible misuse is over-personalization, where users only receive similar songs and do not discover new types of music. To reduce this, future versions could include some variety in the recommendations.

Reflection

This project taught me that building an AI system is not only about getting an output. It is also important to test the system and explain how it works. Adding reliability tests helped me understand how to check whether the recommender is working correctly.

I also learned that documentation is important because another person should be able to understand, run, and evaluate the project without guessing.

Portfolio Reflection

This project shows that I can take an existing AI project and improve it into a more complete system. I added testing, clearer documentation, and an architecture explanation. This project also shows my understanding of recommendation systems, reliability checks, and responsible AI design.

Demo Video

Loom video walkthrough:

Add Loom video link here
GitHub Repository
https://github.com/winter12-2/applied-ai-system-project