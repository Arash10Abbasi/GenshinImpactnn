# EM Scaling

## Amplifying Reactions
Melt and Vaporize are the only amplifying reactions in the game. They directly multiply the damage caused by the attack stats. Meaning, these reactions are also influenced by crit rate, crit damage, enemy defence and enemy resistance.

This is the formula for Elemental-Mastery to DMG factor conversion for Amplifying Reactions.

$$
\text{AmplifyingReaction} = \text{ReactionMultiplier} \times \displaystyle\left[  1 + \frac{2.78 \times \text{EM}}{1400 + \text{EM}} + \text{ReactionBonus}\right]
$$

Where the reaction multiplier is

$$
\begin{equation*}
\text{ReactionMultiplier} =
\begin{cases}
2 & \text{if, triggering Vaporize with \blue{Hydro} or Melt with \orange{Pyro}} \\
1.5 & \text{if, triggering Vaporize with \orange{Pyro} or Melt with {\color{Cyan} Cryo}} \\
1 & \text{otherwise}
\end{cases}
\end{equation*}
$$

### Python Code

```python
# Elemental Mastery Increased Linearly
EM = np.linspace(0, 1000, 50)

# RB - Reaction Bonus
# RM - Reaction Multiplier
# DMG - Damage scaling

DMG = RM * (1.0 + (2.78 * EM)/(1400 + EM) + RB)
```

### Intereactive Plot
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

---

## Tranformative Reactions

Transformative reactions deal a separate instance of damage on the enemy. Transformation reaction damage **_cannot crit!_**. This damage depends on the EM, character level, and the enemies' resistance multiplier.

$$
\text{TransformativeReaction} = \text{ReactionMultiplier} \times \text{LevelMultiplier} \times \displaystyle\left[  1 + \frac{16 \times \text{EM}}{2000 + \text{EM}} + \text{ReactionBonus}\right]\\ \times \text{EnemyReistanceMultiplier}
$$

Where the reaction multiplier is

$$
\begin{equation*}
\text{ReactionMultiplier} = 
\begin{cases}
3 & \text{if, triggering \orange{Burgeon} or {\color{Orchid}Hyperbloom}} \\
2 & \text{if, triggering {\color{DarkOrchid}Overloaded} or {\color{LimeGreen}Bloom}} \\
1.5 & \text{if, triggering Shattered} \\
1.2 \times \text{ECTriggers} & \text{if, triggering {\color{Orchid}Electro-Charged}} \\
0.6 & \text{if, triggering {\color{Turquoise} Swirl}} \\
0.5 & \text{if, triggering {\color{Cyan} Superconduct}} \\
0.25 & \text{if, triggering \orange{Burning}} \\
0 & \text{otherwise}
\end{cases}
\end{equation*}
$$

### Python Code

```python
# Elemental Mastery Increased Linearly
EM = np.linspace(0, 1000, 50)

# RB - Reaction Bonus
# RM - Reaction Multiplier
# LM - Level Multiplier
# ERM - Enemies' Resistance Multiplier
# DMG - Damage scaling

DMG = RM * LM * (1.0 + (16 * EM)/(2000 + EM) + RB) * ERM
```

### Interactive Plot

Note: The Level Multiplier calculation is a bit wrong. Level Multiplier is a non-linear function. Here, I am assuming it to be linear between the starting value and ending value for the plot due to the absence of exact values. I need to fetch them.

<div class="bk-root" id="a0b7554b-5849-4a76-a287-e093d5a31a42" data-root-id="1046"></div>
  
<script type="application/json" id="1179">
    {"66fe35af-9146-445f-b121-3497eccf88ef":{"defs":[],"roots":{"references":[{"attributes":{"tools":[{"id":"1020"},{"id":"1021"},{"id":"1022"},{"id":"1023"},{"id":"1024"},{"id":"1025"}]},"id":"1027","type":"Toolbar"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"coordinates":null,"group":null},"id":"1047","type":"Title"},{"attributes":{"line_alpha":0.6,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Line"},{"attributes":{"data":{"x":{"__ndarray__":"AAAAAAAAJEB00UUXXXQ+QHTRRRdddElAF1100UXXUUB00UUXXfRWQNFFF110EVxAF1100UWXYEBGF1100SVjQHTRRRddtGVAoosuuuhCaEDRRRdddNFqQAAAAAAAYG1ALrrooovub0Auuuiiiz5xQEYXXXTRhXJAXXTRRRfNc0B00UUXXRR1QIsuuuiiW3ZAoosuuuiid0C66KKLLup4QNFFF110MXpA6KKLLrp4e0AAAAAAAMB8QBdddNFFB35ALrroootOf0Ciiy666EqAQC666KKL7oBAuuiiiy6SgUBGF1100TWCQNFFF1102YJAXXTRRRd9g0DooosuuiCEQHTRRRddxIRAAAAAAABohUCLLrrooguGQBdddNFFr4ZAoosuuuhSh0Auuuiii/aHQLrooosumohARRdddNE9iUDRRRdddOGJQF100UUXhYpA6KKLLrooi0B00UUXXcyLQAAAAAAAcIxAiy666KITjUAXXXTRRbeNQKKLLrroWo5ALrrooov+jkC66KKLLqKPQKKLLrroIpBA6KKLLrp0kEAuuuiii8aQQHTRRRddGJFAuuiiiy5qkUAAAAAAALyRQEYXXXTRDZJAiy666KJfkkDRRRdddLGSQBdddNFFA5NAXXTRRRdVk0Cjiy666KaTQOiiiy66+JNALrroootKlEB00UUXXZyUQLrooosu7pRAAAAAAABAlUBFF1100ZGVQIsuuuii45VA0UUXXXQ1lkAXXXTRRYeWQF100UUX2ZZAoosuuugql0DooosuunyXQC666KKLzpdAdNFFF10gmEC66KKLLnKYQAAAAAAAxJhARRdddNEVmUCLLrroomeZQNFFF110uZlAF1100UULmkBddNFFF12aQKKLLrrorppA6KKLLroAm0Auuuiii1KbQHTRRRddpJtAuuiiiy72m0AAAAAAAEicQEUXXXTRmZxAiy666KLrnEDRRRdddD2dQBdddNFFj51AXXTRRRfhnUCiiy666DKeQOiiiy66hJ5ALrrooovWnkB00UUXXSifQLrooosuep9AAAAAAADMn0A=","dtype":"float64","order":"little","shape":[100]},"y":{"__ndarray__":"6Hme53meO0DQHCoWNAdVQJNNNtlkk2FAvoxXpy+jaEDpy3h1+rJvQIoFzaFiYXNAIKXdCEjpdkC2RO5vLXF6QEvk/tYS+X1A8MEHH3zAgEC7EZDSboSCQIZhGIZhSIRAULGgOVQMhkAbASntRtCHQOdQsaA5lIlAsaA5VCxYi0B78MEHHxyNQEZASrsR4I5ACEhpNwJSkEDuby2R+zORQNOX8er0FZJAuL+1RO73kkCe53me59mTQIQPPvjgu5RAaTcCUtqdlUBNX8ar03+WQDOHigXNYZdAGa9OX8ZDmED/1hK5vyWZQOT+1hK5B5pAySabbLLpmkCuTl/Gq8ubQJR2IyClrZxAep7neZ6PnUBexqvTl3GeQETuby2RU59AFAuaQ8UaoEAHH3zwwYugQPoyXp2+/KBA7UZASrttoUDfWiL3t96hQNJuBKS0T6JAxYLmULHAokC4lsj9rTGjQKuqqqqqoqNAnb6MV6cTpECQ0m4EpISkQILmULGg9aRAdfoyXp1mpUBoDhULmtelQFoi97eWSKZATDbZZJO5pkA/SrsRkCqnQDJenb6Mm6dAJXJ/a4kMqEAYhmEYhn2oQAuaQ8WC7qhA/a0lcn9fqUDwwQcffNCpQOPV6ct4QapA1unLeHWyqkDJ/a0lciOrQLoRkNJulKtArSVyf2sFrECgOVQsaHasQJNNNtlk56xAhmEYhmFYrUB4dfoyXsmtQGqJ3N9aOq5AXZ2+jFerrkBQsaA5VByvQEPFguZQja9ANdlkk03+r0CUdiMgpTewQI2AlHYjcLBAh4oFzaGosECAlHYjIOGwQHqe53meGbFAc6hY0BxSsUBssskmm4qxQGa8On0Zw7FAX8ar05f7sUBZ0BwqFjSyQFHajYCUbLJAS+T+1hKlskBE7m8tkd2yQD744IMPFrNANwJS2o1Os0AxDMMwDIezQCkWNIeKv7NAIyCl3Qj4s0AcKhY0hzC0QBY0h4oFabRADz744IOhtEAISGk3Atq0QAJS2o2AErVA+1tL5P5KtUD1Zbw6fYO1QO5vLZH7u7VA6Hme53n0tUA=","dtype":"float64","order":"little","shape":[100]}},"selected":{"id":"1056"},"selection_policy":{"id":"1055"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{"source":{"id":"1002"}},"id":"1039","type":"CDSView"},{"attributes":{"line_alpha":0.1,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Line"},{"attributes":{},"id":"1004","type":"DataRange1d"},{"attributes":{},"id":"1055","type":"UnionRenderers"},{"attributes":{"coordinates":null,"formatter":{"id":"1050"},"group":null,"major_label_policy":{"id":"1051"},"ticker":{"id":"1017"}},"id":"1016","type":"LinearAxis"},{"attributes":{},"id":"1056","type":"Selection"},{"attributes":{"below":[{"id":"1012"}],"center":[{"id":"1015"},{"id":"1019"}],"height":400,"left":[{"id":"1016"}],"renderers":[{"id":"1038"}],"title":{"id":"1047"},"toolbar":{"id":"1027"},"width":800,"x_range":{"id":"1004"},"x_scale":{"id":"1008"},"y_range":{"id":"1006"},"y_scale":{"id":"1010"}},"id":"1003","subtype":"Figure","type":"Plot"},{"attributes":{"axis":{"id":"1016"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"1019","type":"Grid"},{"attributes":{"line_alpha":0.2,"line_color":"#1f77b4","line_width":3,"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Line"},{"attributes":{"end":3000,"js_property_callbacks":{"change:value":[{"id":"1044"}]},"start":0.0,"step":10,"title":"Elemental Mastery","value":100},"id":"1042","type":"Slider"},{"attributes":{"coordinates":null,"data_source":{"id":"1002"},"glyph":{"id":"1035"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"1037"},"nonselection_glyph":{"id":"1036"},"view":{"id":"1039"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{"axis":{"id":"1012"},"coordinates":null,"group":null,"ticker":null},"id":"1015","type":"Grid"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{"args":{"EM":{"id":"1042"},"ERM":{"id":"1043"},"RB":{"id":"1041"},"RM":{"id":"1040"},"source":{"id":"1002"}},"code":"\n    const data = source.data;\n    const rm = RM.value;\n    const rb = RB.value;\n    const em = EM.value;\n    const erm = ERM.value;\n    const x = data['x']\n    const y = data['y']\n    for (var i = 0; i &lt; x.length; i++) {\n        y[i] = rm * x[i] * (1.0 + (16 * em)/(2000 + em)  + rb) * erm;\n    }\n    source.change.emit();\n"},"id":"1044","type":"CustomJS"},{"attributes":{"end":3,"js_property_callbacks":{"change:value":[{"id":"1044"}]},"start":0,"step":0.05,"title":"Reaction Multiplier","value":1},"id":"1040","type":"Slider"},{"attributes":{},"id":"1050","type":"BasicTickFormatter"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"end":3,"js_property_callbacks":{"change:value":[{"id":"1044"}]},"start":0.0,"step":0.1,"title":"Enemy Resistance Multiplier","value":1},"id":"1043","type":"Slider"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"overlay":{"id":"1026"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{"children":[{"id":"1040"},{"id":"1041"},{"id":"1042"},{"id":"1043"}]},"id":"1045","type":"Column"},{"attributes":{},"id":"1051","type":"AllLabels"},{"attributes":{"end":300000},"id":"1006","type":"Range1d"},{"attributes":{"coordinates":null,"formatter":{"id":"1053"},"group":null,"major_label_policy":{"id":"1054"},"ticker":{"id":"1013"}},"id":"1012","type":"LinearAxis"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"end":1.5,"js_property_callbacks":{"change:value":[{"id":"1044"}]},"start":0.0,"step":0.01,"title":"Reaction Bonus","value":0.25},"id":"1041","type":"Slider"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{},"id":"1053","type":"BasicTickFormatter"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{"children":[{"id":"1003"},{"id":"1045"}]},"id":"1046","type":"Row"},{"attributes":{},"id":"1054","type":"AllLabels"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"1026","type":"BoxAnnotation"}],"root_ids":["1046"]},"title":"Bokeh Application","version":"2.4.3"}}
</script>
<script type="text/javascript">
    (function() {
    const fn = function() {
        Bokeh.safely(function() {
        (function(root) {
            function embed_document(root) {
            const docs_json = document.getElementById('1179').textContent;
            const render_items = [{"docid":"66fe35af-9146-445f-b121-3497eccf88ef","root_ids":["1046"],"roots":{"1046":"a0b7554b-5849-4a76-a287-e093d5a31a42"}}];
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

---

## Additive Reactions
These reactions add a massive flat damage to the base damage. This damage is independent of the ATK percent. However, together with the base ATK and flat damage, this damage can scale with crit damage.

$$
\text{AmplifyingReaction} = \text{ReactionMultiplier} \times \text{LevelMultiplier} \times \displaystyle\left[  1 + \frac{5 \times \text{EM}}{1200 + \text{EM}} + \text{ReactionBonus}\right]
$$

Where the reaction multiplier is

$$
\begin{equation*}
\text{ReactionMultiplier} =
\begin{cases}
1.25 & \text{if, triggering {\color{LimeGreen}Spread}} \\
1.15 & \text{if, triggering {\color{DarkOrchid}Aggravate}}
\end{cases}
\end{equation*}
$$

### Python

```python
# Elemental Mastery Increased Linearly
EM = np.linspace(0, 1000, 50)

# RB - Reaction Bonus
# RM - Reaction Multiplier
# LM - Level Multiplier
# DMG - Damage scaling

DMG = RM * LM * (1.0 + (5 * EM)/(1200 + EM) + RB)
```


## Status
Test run successful!

## Notes

EM scaling formulae taken from [Keqing Mains](https://library.keqingmains.com/combat-mechanics/damage/damage-formula)