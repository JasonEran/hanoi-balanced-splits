# Balanced Frame--Stewart Data

This folder mirrors the artefacts referenced in the Bulletin submission and the reproducibility link https://github.com/JasonEran/hanoi-balanced-splits.

Contents:

- `hanoi_bulletin_final.tex` / `hanoi_bulletin_final.pdf`: latest manuscript (9-page version).
- `balanced_fs_solver.py`: memoised solver used to regenerate Table 1 and the ratios for $4 \le n \le 30$.

Example usage:

```bash
python balanced_fs_solver.py > ratios.txt
```
