Analysis

Reproducible pipeline for the paper: data prep → descriptives → inferential stats → figures.
All steps run locally with Python; no external services are required.

Folder layout

```
analysis/
├─ data/
│  ├─ tidy_data.csv
│  ├─ survey_responses.csv
│  └─ trial_logs.csv
├─ notebooks/
│  ├─ 01_prepare_data.ipynb
│  ├─ 02_descriptives.ipynb
│  ├─ 03_inferential_stats.ipynb
│  └─ 04_figures.ipynb
├─ scripts/               # optional helpers (preprocess.py, stats_tests.py, plotting.py)
├─ figures/               # auto-saved by 04_figures.ipynb
│  ├─ trust_boxplot.png
│  ├─ decision_time.png
│  └─ acceptance_rate.png
└─ README.md

```
Quick start
1) Create environment
```
# from repo root
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip

# core deps
pip install numpy pandas scipy matplotlib seaborn jupyter ipykernel
# optional: for headless runs
pip install nbconvert papermill
```
2) Launch Jupyter
Open the notebooks in analysis/notebooks/ and run in order:

1) 01_prepare_data.ipynb
2) 02_descriptives.ipynb
3) 03_inferential_stats.ipynb
4) 04_figures.ipynb

Each notebook assumes relative paths from the repo root (as committed). No edits needed.

What each notebook does

01_prepare_data.ipynb
Loads raw tables from analysis/data/ (trial_logs.csv, survey_responses.csv).
Merges/cleans into tidy_data.csv (if not already present).
Ensures typed columns: participant_id, condition ∈ {A,B}, decision_time_s (float), accepted (0/1), investigate (0/1), trust_post (1–5).
Saves clean dataset to analysis/data/tidy_data.csv.

02_descriptives.ipynb
Computes group means/SDs by condition for: trust (post), decision time (s), acceptance rate (%), investigate (%).
Outputs a Descriptives table that matches the paper’s Table 1.

03_inferential_stats.ipynb
Assumption checks: Shapiro–Wilk (normality), Levene (homogeneity).
If assumptions hold: independent‐samples t tests + Cohen’s d.
Otherwise: Mann–Whitney U + rank‐biserial r.
Correlations (Pearson or Spearman) for trust–behavior links.
Writes a compact results summary (stats + effect sizes + CIs).

04_figures.ipynb
Generates paper figures and saves them to analysis/figures/:
* trust_boxplot.png
* decision_time.png
* acceptance_rate.png

Data dictionary
survey_responses.csv
participant_id — anonymized ID (string)
condition — “A” (Standard AI) or “B” (Explainable AI)
trust_pre — baseline trust (1–5)
trust_post — post‐task trust (1–5)
nasa_tlx_short — workload (0–100)

trial_logs.csv
participant_id — as above
trial_id — 1–10
condition — “A”/“B”
decision — {accept, reject, investigate}
decision_time_s — seconds to decision (float)
accepted — 1 if “accept”, else 0
investigate — 1 if “investigate”, else 0

tidy_data.csv (analysis-ready; one row per participant)
participant_id, condition
trust_post — post‐task trust (1–5)
decision_time_s_mean — mean across trials
acceptance_rate — proportion accepted (0–1)
investigate_rate — proportion investigate (0–1)
nasa_tlx_short — workload

Reproducing the paper numbers
Run notebooks in order (or use headless commands).
Verify analysis/figures/ contains all three PNGs named exactly as in the LaTeX.
Copy the Descriptives table and stats summary from 02_* and 03_* into the manuscript (or let your LaTeX pull from CSV).

Randomness & seeds
Analyses are deterministic. If any resampling/bootstrapping is used in the future, set a fixed seed (e.g., np.random.seed(42)) at the top of the notebook.

Troubleshooting
File not found: run from the repo root so relative paths resolve.
Package errors: make sure the virtualenv is active and packages are installed.
Figures not saving: ensure analysis/figures/ exists (notebook will attempt to create it).
