# Machine Learning-Based Loan Approval Automation: Enhancing Efficiency, Accuracy, and Fairness in Credit Decision-Making

## Abstract

Traditional loan approval processes are manual, time-consuming, and susceptible to human bias. This research develops a machine learning-based system to automate loan eligibility assessment while enhancing efficiency, accuracy, and fairness in credit decision-making. We developed and compared multiple supervised ML models---including Random Forest, XGBoost, stacking, and voting ensembles---on a publicly available loan dataset (614 instances, 13 features). To address class imbalance (68.7\% approved, 31.3\% rejected), we applied the Synthetic Minority Over-sampling Technique (SMOTE). Hyperparameter tuning was performed using GridSearchCV with 5-fold cross-validation, optimising for F1-score. Model performance was evaluated using accuracy, precision, recall, F1-score, and Area Under the Curve (AUC). Local Interpretable Model-Agnostic Explanations (LIME) were applied to ensure transparency. A tuned Random Forest classifier achieved the best performance with an accuracy of 85.96\%, F1-score of 87.17\%, and recall of 95.32\%, outperforming XGBoost and ensemble methods. The high recall ensures effective identification of loan approvals and minimises false negatives. LIME provided instance-level interpretability, enabling stakeholders to understand prediction rationale. This study demonstrates that a systematic framework combining rigorous hyperparameter tuning, class imbalance handling, and explainable AI can create accurate, transparent, and equitable loan approval systems, providing a practical blueprint for responsible AI deployment in credit decision-making.

---

## Project Structure

```
src/
  hellen_paper.ipynb   # Main notebook: preprocessing, modelling, evaluation, explainability
  loans_data.csv       # Dataset (614 instances, 13 features)

documents/
  figs/                # Generated figures (confusion matrices, ROC curves, SHAP/LIME plots)
```

---

## Setup

```bash
pip install -r requirements.txt
```

Then open `src/hellen_paper.ipynb` in Jupyter and run all cells.

---

## Citation

*This paper is currently under review. Citation details will be updated upon publication.*
 
If you use this work, please contact the corresponding author at `mani.ghahremani@port.ac.uk` for citation details until the paper is published.

