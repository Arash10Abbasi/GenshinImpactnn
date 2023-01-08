# EM Scaling

This is the formula for Elemental-Mastery to DMG conversion.

$$
\text{AmplifyingReaction} = \text{ReactionMultiplier} \times \displaystyle\left[  1 + \frac{2.78 \times EM}{1400 + EM} + \text{ReactionBonus}\right]
$$

Where the reaction multiplier is

$$
\begin{equation*}
\text{ReactionMultiplier} = \left\{ 
\begin{array}{ll}
2 && \text{if, triggering Vaporize with \blue{Hydro} or Melt with \orange{Pyro}} \\
1.5 && \text{if, triggering Vaporize with \orange{Pyro} or Melt with \blue{Cryo}} \\
1 && \text{otherwise}
\end{array}
\right.
\end{equation*}
$$

## Python Code

```python
# Elemental Mastery Increased Linearly
EM = np.linspace(0, 1000, 50)

# RB - Reaction Bonus
# RM - Reaction Multiplier
# DMG - Damage scaling

DMG = RM * (1.0 + (2.78 * EM)/(1400 * EM) + RB)
```

## Intereactive Plot
<div class="bk-root" id="8784d752-5113-422a-93d3-405da356cb82" data-root-id="1044"></div>
  
<script type="application/json" id="1177">
{"fb9c9960-d8e0-4833-8973-bed26124e7e4":{"defs":[],"roots":{"references":[{"attributes":{"end":1.5,"js_property_callbacks":{"change:value":[{"id":"1042"}]},"start":0.0,"step":0.01,"title":"Reaction Bonus","value":0.25},"id":"1041","type":"Slider"},{"attributes":{"args":{"RB":{"id":"1041"},"RM":{"id":"1040"},"source":{"id":"1002"}},"code":"\n    const data = source.data;\n    const rm = RM.value;\n    const rb = RB.value;\n    const x = data['x']\n    const y = data['y']\n    for (var i = 0; i &lt; x.length; i++) {\n        y[i] = rm * (1.0 + (2.78 * x[i])/(1400 + x[i])  + rb);\n    }\n    source.change.emit();\n"},"id":"1042","type":"CustomJS"},{"attributes":{"children":[{"id":"1040"},{"id":"1041"}]},"id":"1043","type":"Column"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"end":2,"js_property_callbacks":{"change:value":[{"id":"1042"}]},"start":1,"step":0.5,"title":"Reaction Multiplier","value":1},"id":"1040","type":"Slider"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{"children":[{"id":"1003"},{"id":"1043"}]},"id":"1044","type":"Row"},{"attributes":{"coordinates":null,"data_source":{"id":"1002"},"glyph":{"id":"1035"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"1037"},"nonselection_glyph":{"id":"1036"},"view":{"id":"1039"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{"line_alpha":0.2,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Line"},{"attributes":{},"id":"1053","type":"UnionRenderers"},{"attributes":{},"id":"1054","type":"Selection"},{"attributes":{"end":8},"id":"1006","type":"Range1d"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"axis":{"id":"1016"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"1019","type":"Grid"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"coordinates":null,"formatter":{"id":"1048"},"group":null,"major_label_policy":{"id":"1049"},"ticker":{"id":"1017"}},"id":"1016","type":"LinearAxis"},{"attributes":{"data":{"x":{"__ndarray__":"AAAAAAAAAAAa60NjfWg0QBrrQ2N9aERAp+DlFLycTkAa60NjfWhUQODlFLycgllAp+DlFLycXkC3bdu2bdthQBrrQ2N9aGRAfWisD431ZkDg5RS8nIJpQERjfWisD2xAp+DlFLycbkAFL6fg5ZRwQLdt27Zt23FAaKwPjfUhc0Aa60NjfWh0QMwpeDkFr3VAfWisD431dkAvp+DlFDx4QODlFLycgnlAkiRJkiTJekBEY31orA98QPWhsT40Vn1Ap+DlFLycfkBZHxrrQ+N/QAUvp+DllIBAXk7Byyk4gUC3bdu2bduBQBCN9aGxfoJAaKwPjfUhg0DByyl4OcWDQBrrQ2N9aIRAcwpeTsELhUDMKXg5Ba+FQCRJkiRJUoZAfWisD431hkDWh8b60JiHQC+n4OUUPIhAiMb60FjfiEDg5RS8nIKJQDkFL6fgJYpAkiRJkiTJikDrQ2N9aGyLQERjfWisD4xAnYKXU/CyjED1obE+NFaNQE7Byyl4+Y1Ap+DlFLycjkAAAAAAAECPQA==","dtype":"float64","order":"little","shape":[50]},"y":{"__ndarray__":"AAAAAAAA+P9XqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQFepHiwiCABAV6keLCIIAEBXqR4sIggAQA==","dtype":"float64","order":"little","shape":[50]}},"selected":{"id":"1054"},"selection_policy":{"id":"1053"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{"overlay":{"id":"1026"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{"source":{"id":"1002"}},"id":"1039","type":"CDSView"},{"attributes":{},"id":"1048","type":"BasicTickFormatter"},{"attributes":{"axis":{"id":"1012"},"coordinates":null,"group":null,"ticker":null},"id":"1015","type":"Grid"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{},"id":"1049","type":"AllLabels"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{"coordinates":null,"formatter":{"id":"1051"},"group":null,"major_label_policy":{"id":"1052"},"ticker":{"id":"1013"}},"id":"1012","type":"LinearAxis"},{"attributes":{},"id":"1051","type":"BasicTickFormatter"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Line"},{"attributes":{},"id":"1052","type":"AllLabels"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"1026","type":"BoxAnnotation"},{"attributes":{"below":[{"id":"1012"}],"center":[{"id":"1015"},{"id":"1019"}],"height":400,"left":[{"id":"1016"}],"renderers":[{"id":"1038"}],"title":{"id":"1045"},"toolbar":{"id":"1027"},"width":800,"x_range":{"id":"1004"},"x_scale":{"id":"1008"},"y_range":{"id":"1006"},"y_scale":{"id":"1010"}},"id":"1003","subtype":"Figure","type":"Plot"},{"attributes":{"coordinates":null,"group":null},"id":"1045","type":"Title"},{"attributes":{"tools":[{"id":"1020"},{"id":"1021"},{"id":"1022"},{"id":"1023"},{"id":"1024"},{"id":"1025"}]},"id":"1027","type":"Toolbar"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"line_alpha":0.6,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Line"},{"attributes":{},"id":"1004","type":"DataRange1d"}],"root_ids":["1044"]},"title":"Bokeh Application","version":"2.4.3"}}
</script>
<script type="text/javascript">
    (function() {
    const fn = function() {
        Bokeh.safely(function() {
        (function(root) {
            function embed_document(root) {
            const docs_json = document.getElementById('1177').textContent;
            const render_items = [{"docid":"fb9c9960-d8e0-4833-8973-bed26124e7e4","root_ids":["1044"],"roots":{"1044":"8784d752-5113-422a-93d3-405da356cb82"}}];
            root.Bokeh.embed.embed_items(docs_json, render_items);
            }
            if (root.Bokeh !== undefined) {
            embed_document(root);
            } else {
            let attempts = 0;
            const timer = setInterval(function(root) {
                if (root.Bokeh !== undefined) {
                clearInterval(timer);
                embed_document(root);
                } else {
                attempts++;
                if (attempts > 100) {
                    clearInterval(timer);
                    console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                }
                }
            }, 10, root)
            }
        })(window);
        });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
    })();
</script>

<!-- BokehJS -->
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js"></script>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.3.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>

## Status
Test run successful!