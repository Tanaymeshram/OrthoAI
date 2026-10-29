import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

output_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(output_dir, exist_ok=True)

fig, ax = plt.subplots(figsize=(12, 7.8), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.axis('off')

# Outer rounded rectangle
outer_card = patches.FancyBboxPatch(
    (0.02, 0.02), 0.96, 0.96,
    boxstyle='round,pad=0.03,rounding_size=0.03',
    facecolor='white',
    edgecolor='#e2e8f0',
    linewidth=1.5,
    transform=ax.transAxes
)
ax.add_patch(outer_card)

# Title & Subtitle
ax.text(0.06, 0.92, "Traditional Planning vs. Ortho-AI", 
        fontsize=18, fontweight='bold', color='#0f172a', family='sans-serif', transform=ax.transAxes)
ax.text(0.06, 0.87, "Pre-operative accuracy, biomechanics & clinical efficiency metrics comparison", 
        fontsize=11.5, color='#64748b', family='sans-serif', transform=ax.transAxes)

items = [
    {
        "title": "Pre-Op Alignment Precision",
        "trad": "Traditional: 62%",
        "ortho": "Ortho-AI: 83.5%",
        "val": 83.5,
        "c_start": "#2563eb", "c_mid": "#06b6d4", "c_end": "#10b981",
        "color": "#0d9488"
    },
    {
        "title": "Range of Motion (ROM) Prediction",
        "trad": "Traditional: 52%",
        "ortho": "Ortho-AI: 84.2%",
        "val": 84.2,
        "c_start": "#2563eb", "c_mid": "#0891b2", "c_end": "#10b981",
        "color": "#0d9488"
    },
    {
        "title": "FEA Stress Prediction Accuracy",
        "trad": "Traditional: 48%",
        "ortho": "Ortho-AI: 81.8%",
        "val": 81.8,
        "c_start": "#3b82f6", "c_mid": "#06b6d4", "c_end": "#059669",
        "color": "#0d9488"
    },
    {
        "title": "10-Year Implant Survival Rate",
        "trad": "Traditional: 88.5%",
        "ortho": "Ortho-AI: 94.8%",
        "val": 94.8,
        "c_start": "#0284c7", "c_mid": "#10b981", "c_end": "#059669",
        "color": "#059669"
    },
    {
        "title": "Surgical Planning Time Reduction",
        "trad": "Manual: 2.5 Hrs",
        "ortho": "Ortho-AI: 8.2 Sec (>94% Faster)",
        "val": 94.5,
        "c_start": "#7c3aed", "c_mid": "#9333ea", "c_end": "#4f46e5",
        "color": "#7c3aed"
    },
    {
        "title": "Patient Financial Protection (Avoided Revision)",
        "trad": "Risk: ₹3.50 Lakhs",
        "ortho": "Savings: ₹3.50 Lakhs / Patient",
        "val": 90.0,
        "c_start": "#ea580c", "c_mid": "#f59e0b", "c_end": "#10b981",
        "color": "#ea580c"
    }
]

y_positions = [0.74, 0.62, 0.50, 0.38, 0.26, 0.14]
bar_width = 0.88
bar_height = 0.022

for idx, item in enumerate(items):
    y = y_positions[idx]
    ax.text(0.06, y + 0.038, item["title"], 
            fontsize=11.5, fontweight='bold', color='#1e293b', family='sans-serif', transform=ax.transAxes)
    
    ax.text(0.66, y + 0.038, f"{item['trad']}  |  ", 
            fontsize=10.5, fontweight='bold', color='#475569', ha='right', family='sans-serif', transform=ax.transAxes)
    ax.text(0.66, y + 0.038, f"{item['ortho']}", 
            fontsize=11, fontweight='bold', color=item["color"], ha='left', family='sans-serif', transform=ax.transAxes)
    
    bg_bar = patches.FancyBboxPatch(
        (0.06, y), bar_width, bar_height,
        boxstyle='round,pad=0.004,rounding_size=0.011',
        facecolor='#f1f5f9', edgecolor='none', transform=ax.transAxes
    )
    ax.add_patch(bg_bar)
    
    fill_fraction = (item["val"] / 100.0) * bar_width
    n_pts = 200
    grad = np.linspace(0, 1, n_pts).reshape(1, -1)
    cmap = LinearSegmentedColormap.from_list(f'grad_{idx}', [item["c_start"], item["c_mid"], item["c_end"]])
    
    active_bar = patches.FancyBboxPatch(
        (0.06, y), fill_fraction, bar_height,
        boxstyle='round,pad=0.004,rounding_size=0.011',
        facecolor=item["c_mid"], edgecolor='none', transform=ax.transAxes
    )
    ax.add_patch(active_bar)
    
    im = ax.imshow(
        grad, aspect='auto', cmap=cmap,
        extent=[0.06, 0.06 + fill_fraction, y, y + bar_height],
        clip_path=active_bar, clip_on=True, transform=ax.transAxes
    )

# Bottom Key Insight Pill Box
bottom_box = patches.FancyBboxPatch(
    (0.06, 0.04), 0.88, 0.055,
    boxstyle='round,pad=0.008,rounding_size=0.012',
    facecolor='#f8fafc', edgecolor='#e2e8f0', linewidth=1.0, transform=ax.transAxes
)
ax.add_patch(bottom_box)

ax.text(0.08, 0.06, "Key Insight:", fontsize=10.5, fontweight='bold', color='#1e293b', transform=ax.transAxes)
ax.text(0.19, 0.06, "Automated 3D digital twin eliminates 2D alignment errors and protects patients from revision burden.", 
        fontsize=10, color='#475569', transform=ax.transAxes)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
out_img = os.path.join(output_dir, "traditional_vs_ortho_ai_card_expanded.png")
plt.savefig(out_img, dpi=300, bbox_inches='tight')
plt.close()
print(f"Expanded card saved: {out_img}")
