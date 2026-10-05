import os, pickle
from tqdm.auto import tqdm
import pandas as pd
import medspacy
from medspacy.ner import TargetRule

PE = "medspacy_entities.pkl"
PC = "medspacy_corpus_entities.pkl"
SAMPLE_FRAC = 0.05
MAX_CHARS = 20000

TERMS = {
    "PROBLEM": [
        "hyperkalemia", "hyperpotassemia", "hypokalemia", "hyponatremia", "hypernatremia",
        "acute kidney injury", "acute renal failure", "renal failure", "chronic kidney disease",
        "ckd", "esrd", "acidosis", "metabolic acidosis", "diabetic ketoacidosis", "dka",
        "congestive heart failure", "chf", "atrial fibrillation", "arrhythmia", "bradycardia",
        "hypertension", "hypotension", "diabetes", "sepsis", "pneumonia", "rhabdomyolysis",
        "dehydration", "hemolysis", "peaked t waves", "wide qrs",
    ],
    "MEDICATION": [
        "kayexalate", "sodium polystyrene sulfonate", "insulin", "calcium gluconate",
        "calcium chloride", "furosemide", "lasix", "sodium bicarbonate", "albuterol",
        "dextrose", "lisinopril", "spironolactone", "potassium chloride", "heparin",
        "metoprolol", "lovenox",
    ],
    "LAB": [
        "potassium", "creatinine", "bun", "sodium", "bicarbonate", "glucose", "magnesium",
        "calcium", "phosphate", "lactate", "hematocrit", "hemoglobin", "wbc", "troponin",
    ],
    "PROCEDURE": [
        "dialysis", "hemodialysis", "ekg", "ecg", "intubation", "central line", "foley",
    ],
}

def main():
    noteevents_df = pd.read_pickle("noteevents_df.pkl")

    if os.path.exists(PE) and os.path.exists(PC):
        medspacy_entities = pickle.load(open(PE, "rb"))
        medspacy_corpus = pickle.load(open(PC, "rb"))
    else:
        nlp = medspacy.load()
        target_matcher = nlp.get_pipe("medspacy_target_matcher")
        rules = [TargetRule(term, category)
                for category, terms in TERMS.items()
                for term in terms]
        target_matcher.add(rules) # type: ignore

        text = noteevents_df['text'].dropna().sample(frac=SAMPLE_FRAC, random_state=42)
        text = text.str.slice(0, MAX_CHARS)

        medspacy_entities = {}
        medspacy_corpus = []
        n_total = n_negated = 0

        for doc in tqdm(nlp.pipe(text, batch_size=32, n_process=1), total=len(text), desc="Extracting entities"):
            kept = []

            for e in doc.ents:
                n_total += 1

                # Ignore negated entities
                if e._.is_negated:
                    n_negated += 1
                    continue
                kept.append(e)

            medspacy_corpus.append([e.text.lower() for e in kept])

            for e in kept:
                medspacy_entities.setdefault(e.text.lower(), e.label_)

        pickle.dump(medspacy_entities, open(PE, "wb"))
        pickle.dump(medspacy_corpus, open(PC, "wb"))


if __name__ == "__main__":
    main()