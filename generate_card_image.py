import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

output_dir = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(output_dir, exist_ok=True)

# --------------------------------------------------------------------------
# Exact UI Card Match: "Traditional Planning vs. Ortho-AI"
# --------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.axis('off')

# Outer rounded rectangle container card
outer_card = patches.FancyBboxPatch(
    (0.02, 0.03), 0.96, 0.94,
    boxstyle='round,pad=0.03,rounding_size=0.04',
    facecolor='white',
    edgecolor='#e2e8f0',
    linewidth=1.5,
    transform=ax.transAxes
)
ax.add_patch(outer_card)

# Title & Subtitle
ax.text(0.06, 0.90, "Traditional Planning vs. Ortho-AI", 
        fontsize=18, fontweight='bold', color='#0f172a', family='sans-serif', transform=ax.transAxes)
ax.text(0.06, 0.84, "Pre-operative accuracy & planning efficiency metrics comparison", 
        fontsize=11.5, color='#64748b', family='sans-serif', transform=ax.transAxes)

# Define items to display: (Title, Trad_label, Ortho_label, Percent_fill, Gradient_colors)
items = [
    {
        "title": "Pre-Op Alignment Precision",
        "trad": "Traditional: 62%",
        "ortho": "Ortho-AI: 83.5%",
        "val": 83.5,
        "c_start": "#2563eb",  # Blue
        "c_mid": "#06b6d4",    # Cyan
        "c_end": "#10b981",    # Emerald
    },
    {
        "title": "Range of Motion (ROM) Prediction",
        "trad": "Traditional: 52%",
        "ortho": "Ortho-AI: 84.2%",
        "val": 84.2,
        "c_start": "#2563eb",
        "c_mid": "#0891b2",
        "c_end": "#10b981",
    },
    {
        "title": "FEA Stress Prediction Accuracy",
        "trad": "Traditional: 48%",
        "ortho": "Ortho-AI: 81.8%",
        "val": 81.8,
        "c_start": "#3b82f6",
        "c_mid": "#06b6d4",
        "c_end": "#059669",
    },
    {
        "title": "Surgical Planning Time Reduction",
        "trad": "Manual: 2.5 Hrs",
        "ortho": "Ortho-AI: 8.2 Sec (94% Faster)",
        "val": 94.5,
        "c_start": "#7c3aed",  # Purple
        "c_mid": "#9333ea",
        "c_end": "#4f46e5",    # Indigo
    }
]

y_positions = [0.68, 0.52, 0.36, 0.20]
bar_width = 0.88
bar_height = 0.028

for idx, item in enumerate(items):
    y = y_positions[idx]
    
    # Left Label
    ax.text(0.06, y + 0.045, item["title"], 
            fontsize=12, fontweight='bold', color='#1e293b', family='sans-serif', transform=ax.transAxes)
    
    # Right Label (Traditional in Slate, Ortho-AI in Bold Color)
    ortho_color = '#0d9488' if 'Reduction' not in item['title'] else '#7c3aed'
    ax.text(0.68, y + 0.045, f"{item['trad']}  |  ", 
            fontsize=11, fontweight='bold', color='#475569', ha='right', family='sans-serif', transform=ax.transAxes)
    ax.text(0.68, y + 0.045, f"{item['ortho']}", 
            fontsize=11.5, fontweight='bold', color=ortho_color, ha='left', family='sans-serif', transform=ax.transAxes)
    
    # Background Track (Light Gray)
    bg_bar = patches.FancyBboxPatch(
        (0.06, y), bar_width, bar_height,
        boxstyle='round,pad=0.005,rounding_size=0.014',
        facecolor='#f1f5f9',
        edgecolor='none',
        transform=ax.transAxes
    )
    ax.add_patch(bg_bar)
    
    # Active Filled Bar
    fill_fraction = (item["val"] / 100.0) * bar_width
    
    # Create gradient inside bar using an image mesh
    n_pts = 200
    grad = np.linspace(0, 1, n_pts).reshape(1, -1)
    cmap = LinearSegmentedColormap.from_list(
        f'grad_{idx}', [item["c_start"], item["c_mid"], item["c_end"]]
    )
    
    # Draw filled rounded patch
    active_bar = patches.FancyBboxPatch(
        (0.06, y), fill_fraction, bar_height,
        boxstyle='round,pad=0.005,rounding_size=0.014',
        facecolor=item["c_mid"],
        edgecolor='none',
        transform=ax.transAxes
    )
    ax.add_patch(active_bar)
    
    # Use imshow clipped to the patch for a smooth gradient
    im = ax.imshow(
        grad, aspect='auto', cmap=cmap,
        extent=[0.06, 0.06 + fill_fraction, y, y + bar_height],
        clip_path=active_bar, clip_on=True, transform=ax.transAxes
    )

# Bottom Key Insight Pill Box
bottom_box = patches.FancyBboxPatch(
    (0.06, 0.06), 0.88, 0.065,
    boxstyle='round,pad=0.01,rounding_size=0.015',
    facecolor='#f8fafc',
    edgecolor='#e2e8f0',
    linewidth=1.0,
    transform=ax.transAxes
)
ax.add_patch(bottom_box)

ax.text(0.08, 0.09, "Key Insight:", fontsize=10.5, fontweight='bold', color='#1e293b', transform=ax.transAxes)
ax.text(0.19, 0.09, "Automated 3D modeling eliminates 2D slice-by-slice manual alignment errors.", 
        fontsize=10.5, color='#475569', transform=ax.transAxes)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
out_img = os.path.join(output_dir, "traditional_vs_ortho_ai_card.png")
plt.savefig(out_img, dpi=300, bbox_inches='tight')
plt.close()

print(f"Image successfully generated: {out_img}")
