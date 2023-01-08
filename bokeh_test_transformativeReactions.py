import numpy as np

from bokeh.layouts import row, column
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource

from bokeh.embed import components

RM = 1.0
LM = 1.0
RB = 1.0
ERM = 1.0

# Elemental Mastery Increased Linearly
EM = 100.0
LM = np.linspace(10, 2035, 100)

# RB - Reaction Bonus
# RM - Reaction Multiplier
# LM - Level Multiplier
# ERM - Enemies' Resistance Multiplier
# DMG - Damage scaling

DMG = RM * LM * (1.0 + (16 * EM)/(2000 + EM) + RB) * ERM

print(LM)

source = ColumnDataSource(data=dict(x=LM, y=DMG))

plot = figure(y_range=(0, 300000), plot_width=800, plot_height=400)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

ReactionMultiplier_slider = Slider(start=0, end=3, value=1, step=0.05, title="Reaction Multiplier")
ReactionBonus_slider = Slider(start=0.0, end=1.5, value=0.25, step=0.01, title="Reaction Bonus")
ElementalMastery_slider = Slider(start=0.0, end=3000, value=100, step=10, title="Elemental Mastery")
EnemyResistanceMultiplier_slider = Slider(start=0.0, end=3, value=1, step=0.1, title="Enemy Resistance Multiplier")

callback = CustomJS(args=dict(source=source, RM=ReactionMultiplier_slider, RB=ReactionBonus_slider, EM=ElementalMastery_slider, ERM=EnemyResistanceMultiplier_slider),
                    code="""
    const data = source.data;
    const rm = RM.value;
    const rb = RB.value;
    const em = EM.value;
    const erm = ERM.value;
    const x = data['x']
    const y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = rm * x[i] * (1.0 + (16 * em)/(2000 + em)  + rb) * erm;
    }
    source.change.emit();
""")

ReactionMultiplier_slider.js_on_change('value', callback)
ReactionBonus_slider.js_on_change('value', callback)
ElementalMastery_slider.js_on_change('value', callback)
EnemyResistanceMultiplier_slider.js_on_change('value', callback)

layout = row(
    plot,
    column(ReactionMultiplier_slider, ReactionBonus_slider, ElementalMastery_slider, EnemyResistanceMultiplier_slider),
)

output_file("Transformative_EM.html", title="Transformative EM example")

show(layout)
# Extract components
script, div = components(plot)
print(script)
print(div)