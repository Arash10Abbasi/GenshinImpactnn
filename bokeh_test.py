import numpy as np

from bokeh.layouts import row, column
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource

from bokeh.embed import components

EM = np.linspace(0, 1000, 50)
DMG = 2.0 * (1.0 + (2.78 * EM)/(1400 * EM) + 0.0)

source = ColumnDataSource(data=dict(x=EM, y=DMG))

plot = figure(y_range=(0, 8), plot_width=800, plot_height=400)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

ReactionMultiplier_slider = Slider(start=1, end=2, value=1, step=0.5, title="Reaction Multiplier")
ReactionBonus_slider = Slider(start=0.0, end=1.5, value=0.25, step=0.01, title="Reaction Bonus")

callback = CustomJS(args=dict(source=source, RM=ReactionMultiplier_slider, RB=ReactionBonus_slider),
                    code="""
    const data = source.data;
    const rm = RM.value;
    const rb = RB.value;
    const x = data['x']
    const y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = rm * (1.0 + (2.78 * x[i])/(1400 + x[i])  + rb);
    }
    source.change.emit();
""")

ReactionMultiplier_slider.js_on_change('value', callback)
ReactionBonus_slider.js_on_change('value', callback)

layout = row(
    plot,
    column(ReactionMultiplier_slider, ReactionBonus_slider),
)

output_file("Interactive_EM.html", title="Interactive EM example")

# show(layout)
# Extract components
script, div = components(plot)
print(script)
print(div)