import json
from pathlib import Path
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

DATA_PATH = Path(_file_).resolve().parent.parent / "data" / "sample_jobs.json"

class TFIDFRecommender:
    def _init_(self):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            self.jobs = json.load(f)
        # create a simple corpus mixing title, description, location and language
        corpus = [f"{j['title']} {j['description']} {j.get('location','')} {j.get('language','')}" for j in self.jobs]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.job_matrix = self.vectorizer.fit_transform(corpus)

    def recommend(self, query: str, top_k: int = 5) -> List[Dict]:
        q_vec = self.vectorizer.transform([query])
        sims = linear_kernel(q_vec, self.job_matrix).flatten()
        ranked = sims.argsort()[::-1]
        results = []
        for idx in ranked[:top_k]:
            job = self.jobs[idx].copy()
            job["score"] = float(sims[idx])
            results.append(job)
        return results