# MIMIC ML/DL Assignment

#### Details
Create a tutorial about applying ML/DL using MIMIC-III or MIMIC-IV data.
Note: You may not use demo data or synthetic data for this assignment.

## Learning Outcomes

After finishing this assignment, you should be able to say: 

- I can apply ML/DL to EHR data.
- I can apply ML/DL to identify basic problems in healthcare.

## Rationale

The goal of this assignment is to get familiar with the machine learning and deep learning technologies and know how to apply them to analyze EHR data and derive insights. In this tutorial, you will demonstrate how you extract features and how to fit your features to the existing machine learning models that can provide predictions for risk management in healthcare. Or you can apply deep learning methods on multimodality data, temporal data, or other kinds of data to provide evidence-based understandings of diseases and delivered healthcare. 

## Instructions

For this project, you will create a project that uses Machine Learning and/or Deep Learning methods to execute a task on existing data, specifically MIMIC-III or MIMIC-IV. At a minimum, you should be able to recreate the tutorial from Lecture Series 11.  For full credit, you will need to use different ML/DL methods from our examples for different downstream tasks (e.g., not readmission or length of stay) and evaluate your results.

If you employ ML models, it is not sufficient merely to apply simple regression (e.g., linear, logistic or regularized) regression. Consider also Survival Models, Decision Trees, Random Forest, Gradient Boosting, Clustering, SVM, Graph-based etc. Dimension Reduction (PCA, t-SNE, UMAP) may also help simplify your modeling. Among DL models, FCN, RNN (LSTM, GRU), Transformers (e.g., BERT-style) have been popular choices, but you are not limited to these. Test multiple models, and assess and compare your results.

For the bonus point, develop your own custom DL model. Train it, test it. Apply it to new data or a new research question. Alternatively, apply GridSearch (or similar hyperparameter tuning) to your ML models to systematically optimize parameters within or across models. Compare your results.

Once you have completed your project, create a slide deck that goes through your process step-by-step—and that includes at least one slide with your thorough evaluation, interpretation and key takeaways of your results. What did you learn from this analysis? 

- Please highlight any work intended for bonus credit.

See the rubric below for more information.  

## Submission

- Your Python code file as a Jupyter notebook (.ipynb) -- with executed code blocks.
- Slides (.pptx or .pdf) that explain the steps you used to create your project and an evaluation of your results.

Both your presentation and code notebook are required for full credit.

## Rubric

| Criteria | Full Marks | Level 3 | Level 2 | Level 1 | Points |
|---|---|---|---|---|---|
| **ML/DL methods** | **Full Marks (6 pts):** You used different ML/DL methods for different downstream tasks (e.g., not readmission or length of stay), and have thorough evaluation. | **Level 3 (4 pts):** You used similar ML/DL methods for different downstream tasks (e.g., not readmission or length of stay). | **Level 2 (2 pts):** You used different ML/DL methods for the similar downstream tasks (e.g., readmission or length of stay). | **Level 1 (1 pt):** You repeated the ML/DL tutorials in lectures, but added extra features. | /6 pts |

| Criteria | Meets | Partial | No Credit | Points |
|---|---|---|---|---|
| **Presentation Slides** | **Meets (2 pts):** Your presentation was legible, well-organized--and compared and contrasted the results of your ML/DL models. | **Partial (1 pt):** Your presentation was illegible, poorly-organized, or failed to compare and contrast the results of your ML/DL models. | **No Credit (0 pts)** | /2 pts |

| Criteria | Near | Below | No Evidence | Points |
|---|---|---|---|---|
| **Code notebook** | **Near (2 pts):** Code notebook with executed code blocks that support the presentation. | **Below (1 pt):** Code notebook lacks executed code blocks that support the presentation. | **No Evidence (0 pts)** | /2 pts |

| Criteria | Full Bonus | No Marks | Points |
|---|---|---|---|
| **Bonus Point** | **Full Bonus (1 pt):** You designed a deep learning method (such as CNN, LSTM, Transformer, or on a more difficult level contrastive learning, knowledge graph-based methods) or apply it on new datasets (such as eICU, or other publicly available datasets). Alternatively, you applied GridSearch (or similar hyperparameter tuning) to your ML models to systematically optimize within or across models and compared your results. | **No Marks (0 pts)** | /1 pts |
