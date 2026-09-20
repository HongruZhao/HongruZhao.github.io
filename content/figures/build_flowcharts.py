"""Generate the two editable, accessible SVG dependency diagrams for the GBS post."""
from html import escape
from pathlib import Path

from matplotlib.font_manager import FontProperties
from matplotlib.path import Path as VectorPath
from matplotlib.textpath import TextPath

ASSETS = Path(__file__).resolve().parents[2] / 'dist/assets'


def latex_label_rows(x, y, width, height, lines):
    """Embed LaTeX math as vector outlines so it also renders inside an SVG image."""
    rows = []
    for i, line in enumerate(lines):
        font = FontProperties(family='DejaVu Sans', weight='semibold' if i == 0 else 'normal',
                              math_fontfamily='cm')
        path = TextPath((0, 0), line, size=19, prop=font)
        bounds = path.get_extents()
        if bounds.width > width - 24:
            size = 19 * (width - 24) / bounds.width
            if size < 16:
                raise ValueError(f'Label needs a wider box: {line}')
            path = TextPath((0, 0), line, size=size, prop=font)
            bounds = path.get_extents()
        rows.append((line, path, bounds))
    gap = 12
    total_height = sum(bounds.height for _, _, bounds in rows) + gap * (len(rows) - 1)
    if total_height > height - 16:
        raise ValueError(f'Labels need a taller box: {lines}')
    top = y + (height - total_height) / 2
    result = []
    commands = {VectorPath.MOVETO: 'M', VectorPath.LINETO: 'L',
                VectorPath.CURVE3: 'Q', VectorPath.CURVE4: 'C'}
    for line, path, bounds in rows:
        data = []
        for vertices, code in path.iter_segments(curves=True, simplify=False):
            if code == VectorPath.CLOSEPOLY:
                data.append('Z')
            elif code in commands:
                data.append(commands[code] + ' '.join(f'{value:.4f}' for value in vertices))
        left = x + width / 2 - (bounds.x0 + bounds.x1) / 2
        baseline = top + bounds.y1
        result.append(f'<g role="img" aria-label="{escape(line, quote=True)}" '
                      f'transform="translate({left:.4f} {baseline:.4f}) scale(1 -1)" '
                      f'fill="#172d47"><title>{escape(line)}</title>'
                      f'<path d="{" ".join(data)}"/></g>')
        top += bounds.height + gap
    return result


def diagram(filename, height, title, description, nodes, edges, footer):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="{height}" viewBox="0 0 800 {height}" role="img" aria-labelledby="title description">',
             f'<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>',
             '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#51667c"/></marker></defs>',
             f'<rect width="800" height="{height}" fill="#ffffff"/>']
    if any(kind == 'unpublished' for _, kind in edges):
        parts.append('<defs><marker id="unpublished-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#7b51a3"/></marker></defs>')
    for path, conditional in edges:
        dash = ' stroke-dasharray="7 5"' if conditional else ''
        color, marker = ('#7b51a3', 'unpublished-arrow') if conditional == 'unpublished' else ('#51667c', 'arrow')
        parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2"{dash} marker-end="url(#{marker})"/>')
    for x, y, width, box_height, kind, lines in nodes:
        fill, stroke = {'known': ('#eff5fc','#6285ad'), 'result': ('#e5f4fb','#2174a5'), 'assumption': ('#fff5df','#a87a2c'), 'unpublished': ('#f4efff','#7b51a3')}[kind]
        dash = ' stroke-dasharray="7 5"' if kind == 'unpublished' else ''
        parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{box_height}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"{dash}/>')
        if any('$' in line for line in lines):
            parts.extend(latex_label_rows(x, y, width, box_height, lines))
            continue
        line_height = 25
        start = y + (box_height - (len(lines)-1)*line_height)/2 + 7
        for i, line in enumerate(lines):
            weight = '600' if i == 0 else '400'
            parts.append(f'<text x="{x+width/2}" y="{start+i*line_height}" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="{weight}" fill="#172d47" text-anchor="middle">{escape(line)}</text>')
    for i, line in enumerate(footer):
        parts.append(f'<text x="24" y="{height-28-18*max(0,len(footer)-2)+(i*18)}" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#51667c">{escape(line)}</text>')
    parts.append('</svg>')
    (ASSETS/filename).write_text('\n'.join(parts))


diagram('boson-sampling-hardness.svg',770,
        'Ordinary boson sampling: the conditional hardness argument',
        'The assumed classical sampler and a side box containing the proved Gaussian hiding and approximate counting reduction both point to additive squared-permanent estimates. The reduction uses an NP oracle. Anticoncentration and the AA conversion give relative permanent estimates. Average-case hardness then implies a collapse of the polynomial hierarchy.',
        [
            (24,24,440,126,'assumption',['Hypothetical efficient classical','approximate boson sampler']),
            (490,24,285,126,'known',['Proved reduction [1,15]','Gaussian hiding','+ approximate counting','Using an NP oracle']),
            (24,194,440,82,'known',['Additive estimate of |Per(X)|²','Error ≤ ε N!','For most Gaussian matrices X']),
            (24,316,440,94,'known',['AA conversion [1, Theorem 1.7]','Includes the complex-phase reduction']),
            (24,450,440,90,'known',['Relative estimation of Per(X)','using an NP oracle']),
            (24,600,440,120,'known',['Polynomial hierarchy collapses','to its third level','Contradicts the noncollapse assumption']),
            (490,307,285,114,'result',['Permanent anticoncentration','Koehler–Leung [2]','2026 preprint result']),
            (490,585,285,135,'assumption',['Gaussian permanent','average-case #P-hardness','AA Conjecture 1.5','Separate assumption'])
        ],
        [('M244,150 V188',False),('M632.5,150 V235 H470',False),('M244,276 V310',False),('M244,410 V444',False),('M244,540 V594',False),('M490,364 H470',False),('M490,654 H470',False)],
        ['The reductions require the stated accuracy, hiding regime, and finite-precision model.'])

diagram('gbs-hardness.svg',1360,
        'Gaussian boson sampling: manuscript results and an unpublished implication',
        'Uniform matrix-law hiding and normalization are results of the hiding manuscript. Stockmeyer counting is an established external tool. The purple box and dashed arrow mark the additional unpublished implication from an assumed efficient classical GBS sampler to estimation on supplied Gaussian-factor inputs; its proof is omitted. Local anticoncentration supplies the analytic additive-to-relative conversion. The lower complexity conclusions are conditional on that unpublished implication and matching average-case hardness.',
        [
            (180,24,440,85,'known',['Ideal GBS with equal squeezing',r'Fixed collision-free event, $N=2n$']),
            (24,155,360,165,'result',['My uniform matrix-law hiding [10]',r'Error $\leq\min\left\{1,615172\,\dfrac{N^2}{M}\right\}$',r'$1\leq N\leq M,\quad 1\leq K\leq M$','Finite Gaussian Gram reference']),
            (416,155,360,165,'result',['Normalization and sampling bounds','Proposition 4.1; Corollary 4.2 [10]','TV error gives an additive tail','At a random circuit and label']),
            (24,370,360,130,'assumption',['Hypothetical efficient classical','approximate ideal GBS sampler','With a finite circuit description']),
            (416,370,360,130,'known',['Stockmeyer counting [1,15]',"Estimates the sampler's probabilities",'Using an NP oracle']),
            (24,550,752,140,'unpublished',['Unpublished implication: sampler to Gaussian estimator','Conditional instance generation and finite-precision transfer','Beyond the two manuscripts [10,11]; proof omitted here','See the one-paragraph hint in the post']),
            (24,760,440,110,'known',['Additive squared-hafnian estimation',r'$|\operatorname{haf}(GG^{\mathsf{T}})|^2$','On supplied Gaussian-factor inputs']),
            (24,940,440,110,'known',['Relative squared-hafnian estimation','Analytic additive-to-relative conversion','Corollary 7.2 [11]']),
            (490,910,285,165,'result',['My local','anticoncentration [11]',r'$K\geq4n$',r'Polynomial $B_{K,n}$ when',r'$n^2/K=O(\log n)$']),
            (490,1145,285,145,'assumption',[r'Average-case $\#\mathrm{P}$-hardness','Matching finite-Gram problem,','precision, accuracy, and regime']),
            (24,1170,440,120,'known',['Polynomial hierarchy collapses','to its third level','Contradicts the noncollapse assumption'])
        ],
        [('M400,109 V130 H204 V149',False),('M400,130 H596 V149',False),
         ('M204,320 V342 H12 V620 H18',False),('M596,320 V342 H790 V620 H782',False),
         ('M384,435 H410',False),('M204,500 V544',False),('M596,500 V544',False),
         ('M400,690 V725 H244 V754','unpublished'),('M244,870 V934',False),
         ('M490,995 H470',False),('M244,1050 V1164',False),('M490,1230 H470',False)],
        ['Blue: manuscript results and established tools; lower conclusions are conditional.',
         'Purple and dashed: unpublished implication; proof omitted.',
         'Amber: assumed sampler and matching average-case hardness.'])
