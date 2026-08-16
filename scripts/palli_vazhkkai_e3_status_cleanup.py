from pathlib import Path

root = Path('speeches/palli-vazhkkai')
review_path = root / 'translation-review.md'
handover_path = root / 'HANDOVER.md'

review = review_path.read_text(encoding='utf-8')
old = '''- The English layer is now **fidelity-corrections-consolidated**, but **not yet verified-complete**.
- E3 final end-to-end Tamil→English verification remains mandatory.'''
new = '''- The English layer passed E3 and is now **verified-complete**.
- Final archival synchronization remains the only pending gate.'''
assert old in review
review = review.replace(old, new, 1)
review_path.write_text(review, encoding='utf-8')

handover = handover_path.read_text(encoding='utf-8')
handover = handover.replace('`translation-en.md` preserves PDF/printed-page headings and paragraph sequence throughout the full body. E1 is complete, E2 review/correction consolidation is complete, and E3 final verification remains mandatory.', '`translation-en.md` preserves PDF/printed-page headings and paragraph sequence throughout the full body. E1, E2 and E3 are complete; the English layer is verified-complete.', 1)
handover = handover.replace('All **76/76 body pages, PDF 6-81 / printed 5-80**, have undergone independent Tamil→English fidelity review. Every confirmed E2 correction has been consolidated into `translation-en.md`; `translation-review.md` contains the full Batch 1-16 audit. The English layer state is now **fidelity-corrections-consolidated**.', 'All **76/76 body pages, PDF 6-81 / printed 5-80**, underwent independent Tamil→English fidelity review. Every confirmed E2 correction was consolidated into `translation-en.md`; `translation-review.md` contains the full Batch 1-16 audit. E3 subsequently passed, so the English layer is now **verified-complete**.', 1)
handover_path.write_text(handover, encoding='utf-8')

print('PASS: E3 status prose synchronized')
