"""Простой drift-репорт через KS-test и pandas. Без evidently — оно ломается между версиями."""
import pandas as pd
from scipy.stats import ks_2samp
from sklearn.datasets import load_iris

df = load_iris(as_frame=True).frame.drop(columns=["target"])
ref = df.iloc[:75]
cur = df.iloc[75:] * 1000  # искусственный дрифт

rows = []
for col in df.columns:
    s, p = ks_2samp(ref[col], cur[col])
    rows.append({
        "feature": col,
        "ref_mean": round(ref[col].mean(), 3),
        "cur_mean": round(cur[col].mean(), 3),
        "ks_stat": round(s, 3),
        "p_value": round(p, 5),
        "drift": "YES" if p < 0.05 else "no",
    })

res = pd.DataFrame(rows)
print(res.to_string(index=False))

html = f"""<html><head><meta charset='utf-8'><title>Drift report</title>
<style>body{{font-family:sans-serif;padding:20px}} table{{border-collapse:collapse}} td,th{{border:1px solid #ccc;padding:6px}} .yes{{background:#ffcccc}}</style>
</head><body>
<h1>Data drift report (KS-test)</h1>
<p>Reference: первые 75 строк iris. Current: остальные × 1000.</p>
{res.to_html(index=False, classes='t')}
<p><b>Drift найден</b> там где p-value &lt; 0.05.</p>
</body></html>"""
open("drift_report.html", "w").write(html)
print("saved drift_report.html")
