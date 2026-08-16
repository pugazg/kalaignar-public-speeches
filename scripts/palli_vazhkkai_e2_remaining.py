from pathlib import Path

p = Path('speeches/palli-vazhkkai/translation-review.md')
text = p.read_text(encoding='utf-8')
old = 'E1 is complete for all 76 body pages. E2 is now active. E3 remains blocked until all 76 pages have been independently reviewed and all confirmed E2 corrections have been consolidated.'
new = 'E1 is complete for all 76 body pages. E2 is review-complete and all confirmed corrections are consolidated. E3 remains the mandatory final release gate.'
assert text.count(old) == 1
text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
