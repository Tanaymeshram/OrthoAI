import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure results directory exists
output_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------------
# GRAPH 1: Head-to-Head Clinical Performance (Traditional vs. Ortho-AI)
# -------------------------------------------------------------------------
metrics = [
    'Alignment\nPrecision',
    'ROM\nPrediction',
    'Stress/Wear\nDetection',
    '10-Yr Implant\nSurvival',
    '10-Yr Revision\nRate (Lower is better)'
]
traditional = [62.0, 52.0, 48.0, 88.5, 11.5]
ortho_ai = [83.5, 84.2, 81.8, 94.8, 4.2]

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
rects1 = ax.bar(x - width/2, traditional, width, label='Traditional Method (2D CT/X-Ray)', color='#94a3b8', edgecolor='#64748b', linewidth=1)
rects2 = ax.bar(x + width/2, ortho_ai, width, label='Ortho-AI Platform (3D Digital Twin)', color='#0284c7', edgecolor='#0369a1', linewidth=1)

ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Clinical Performance Comparison: Traditional Planning vs. Ortho-AI', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=10.5, fontweight='bold')
ax.legend(frameon=True, facecolor='white', edgecolor='#cbd5e1', fontsize=11, loc='upper left')
ax.set_ylim(0, 115)
ax.grid(axis='y', linestyle='--', alpha=0.35)

for rect in rects1:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width() / 2, h),
                xytext=(0, 4), textcoords='offset points', ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#475569')

for rect in rects2:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width() / 2, h),
                xytext=(0, 4), textcoords='offset points', ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#0284c7')

plt.tight_layout()
p1 = os.path.join(output_dir, "graph_clinical_comparison.png")
plt.savefig(p1, dpi=300)
plt.close()

# -------------------------------------------------------------------------
# GRAPH 2: Planning Time & Economic Protection (Indian Context in ₹ Lakhs)
# -------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=300)

# 1. Time Comparison
cats_time = ['Traditional\n(Manual Doctor Tracing)', 'Ortho-AI\n(Automated Pipeline)']
vals_time = [150.0, 0.14]  # 150 min (2.5 hrs) vs 8.2 sec (0.14 min)
bars_time = ax1.bar(cats_time, vals_time, color=['#f43f5e', '#10b981'], width=0.45, edgecolor=['#be123c', '#047857'], linewidth=1.2)
ax1.set_ylabel('Planning Time (Minutes)', fontsize=11, fontweight='bold')
ax1.set_title('Surgical Planning Time\n(2.5 Hours vs. 8.2 Seconds)', fontsize=12.5, fontweight='bold', pad=10)
ax1.set_ylim(0, 180)
ax1.grid(axis='y', linestyle='--', alpha=0.35)
for b in bars_time:
    val = b.get_height()
    txt = f'150 mins\n(2.5 Hours)' if val > 1 else '8.2 Seconds\n(>94% Faster)'
    ax1.annotate(txt, xy=(b.get_x() + b.get_width() / 2, val),
                 xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10.5, fontweight='bold')

# 2. Cost Avoidance (INR in Lakhs)
cats_cost = ['Revision Surgery Risk\n(Traditional Failure)', 'Pre-Op AI Prevention\n(Savings for Patient)']
bars_cost = ax2.bar(cats_cost, [3.5, 3.5], color=['#ef4444', '#06b6d4'], width=0.45, edgecolor=['#b91c1c', '#0891b2'], linewidth=1.2)
ax2.set_ylabel('Cost per Patient (₹ in Lakhs)', fontsize=11, fontweight='bold')
ax2.set_title('Financial Protection (Indian Healthcare)\nAvoided Revision Burden', fontsize=12.5, fontweight='bold', pad=10)
ax2.set_ylim(0, 4.5)
ax2.grid(axis='y', linestyle='--', alpha=0.35)
ax2.annotate('₹3.50 Lakhs\n(Patient Risk Burden)', xy=(0, 3.5), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#b91c1c')
ax2.annotate('₹3.50 Lakhs Saved\n(Direct Cost Protection)', xy=(1, 3.5), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#0891b2')

plt.tight_layout()
p2 = os.path.join(output_dir, "graph_time_and_cost.png")
plt.savefig(p2, dpi=300)
plt.close()

# -------------------------------------------------------------------------
# GRAPH 3: Machine Learning Model Benchmarks
# -------------------------------------------------------------------------
models = ['Logistic\nRegression', 'Support Vector\nMachine (SVM)', 'Random\nForest', 'Gradient\nBoosting', 'Ortho-AI\nPipeline']
accuracy = [79.5, 83.7, 86.1, 88.4, 88.4]
f1_scores = [79.1, 83.2, 85.9, 88.1, 88.1]
roc_auc = [82.0, 86.0, 89.0, 91.0, 91.0]

x = np.arange(len(models))
width = 0.25

fig, ax = plt.subplots(figsize=(10.5, 5), dpi=300)
r1 = ax.bar(x - width, accuracy, width, label='Accuracy (%)', color='#6366f1')
r2 = ax.bar(x, f1_scores, width, label='F1-Score (%)', color='#14b8a6')
r3 = ax.bar(x + width, roc_auc, width, label='ROC-AUC (%)', color='#f59e0b')

ax.set_ylabel('Score (%)', fontsize=11, fontweight='bold')
ax.set_title('AI Classifier Evaluation Metrics (Accuracy, F1, ROC-AUC)', fontsize=13, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=10, fontweight='bold')
ax.legend(loc='lower right', frameon=True, fontsize=10.5)
ax.set_ylim(65, 100)
ax.grid(axis='y', linestyle='--', alpha=0.35)

for rects in [r1, r2, r3]:
    for r in rects:
        h = r.get_height()
        ax.annotate(f'{h:.1f}', xy=(r.get_x() + r.get_width() / 2, h),
                    xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=8.5, fontweight='bold')

plt.tight_layout()
p3 = os.path.join(output_dir, "graph_ml_models.png")
plt.savefig(p3, dpi=300)
plt.close()

print(f"SUCCESS: Generated:\n1) {p1}\n2) {p2}\n3) {p3}")
