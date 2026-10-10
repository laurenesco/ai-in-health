Generate a NLP tutorial using MIMIC-III or MIMIC-IV data.
Note: You may not use demo data or synthetic data for this assignment.

## Learning Outcomes

After finishing this assignment, you should be able to say: 

    I know how to apply Spacy, SciSpacy and MedSpacy on medical notes.
    I know how to apply NLP tools, word embedding, and dimensionality reduction (t-SNE, plus optionally UMAP) on medical notes

## Rationale

The goal of this assignment is to get familiar with the latest NLP technologies and know how to apply them to process EHR data, especially medical notes. Medical notes are important parts of EHR data, but often ignored due to a lack of sufficient analyses and the big learning curve associated with understanding and applying NLP technologies. In this tutorial, you will demonstrate how you apply NLP technologies to process medical notes. These extracted entities and their embeddings can become new features for your machine learning algorithms.

## Instructions

Use NLP technologies to extract entities from medical notes data. To receive full credit, your project should yield Spacy,  SciSpacy and Medspacy <https://github.com/medspacy/medspacy> extracted entities, word2vec, and tuned t-SNE plots for all three Python libraries. Compare and contrast the results you achieve. The incorporation of DisplaCy is encouraged but not required. See the rubric below for more information. 

How to get medical notes: MIMIC NOTEEVENTS Table contains different kinds of medical reports. It is a file over >1 GB in size, so it might take 30 mins for you to load it to Google Colab. For this reason, you may want to subscribe to Colab Pro to speed up the process. This is optional. 

We have provided python code that can help you extract a set of medical notes from NOTEEVENTS table. The example here shows how to extract discharge notes for patients diagnosed with ICD9 code 430 (Subarachnoid hemorrhage), which is also available with our lecture series resources. 

The NLP assignment features t-SNE, and you may run into a lot of confusion working with it for the first time. So please have a look at How to Use t-SNE Effectively. Tune your t-SNE plots. The addition of UMAP is encouraged but not required.

## Bonus 1 pt

To receive a bonus point for this assignment, you can introduce a new NLP tool such as cTakes, BERT, BlueBERT, ClinicalBERT, BioBERT or BioClinicalBERT. and apply it on MIMIC dataset. 

> Please highlight any work intended for bonus credit.

## Submission

- Your Python code file as a Jupyter notebook (.ipynb) -- with executed code blocks.
- For each of spaCy, scispaCy and medspaCy, perform the entity extraction, word2vec and a tuned t-SNE. Show each of these results for each model in your slide presentation (not just a t-SNE). The use of displaCy is encouraged although not required. You are also encouraged to try UMAP in addition to (not instead of) t-SNE. Compare and contrast your results.
- Slides (.pptx or .pdf), including your interpretation and comparison of your results.

Both your presentation and code notebook are required for full credit.