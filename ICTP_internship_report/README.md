# ICTP Internship Report

This repository accompanies the ICTP PWF: Physics for Bangladesh summer internship. It documents the complete workflow we used to port Quantum ESPRESSO 7.4.1 to macOS 15 (Apple M4), reproduce the Path A/Path B "stretching" exercises on both local and remote infrastructure, and compare performance across platforms.

## Contents

- `main.tex` – LaTeX source for the report.
- `ICTP_internship_report.pdf` – precompiled PDF for quick reading.
- `figs/` – figures imported into the manuscript (copied from the workflow repositories).
- `code/`, `data/` – helper assets referenced in the text.
- `build/` – ignored LaTeX build directory (use `latexmk` locally instead).

## Reproducing the PDF

```bash
latexmk -pdf main.tex
```

The build products are written to `build/`. The provided `.gitignore` keeps auxiliary files out of version control.

## Related Repositories

- [qe_macm4_build](https://github.com/shahpoll/qe_macm4_build) – macOS build scripts.
- [QE_stretching_macm4](https://github.com/shahpoll/QE_stretching_macm4) – Mac mini Path A and Path B workflows.
- [QE_stretching_server](https://github.com/shahpoll/QE_stretching_server) – Stretching server Path A and Path B workflows.
- [qe_comparison_macm4_v_server](https://github.com/shahpoll/qe_comparison_macm4_v_server) – performance comparison data and plots.

## License

Unless stated otherwise in the subdirectories, the prose in this repository is released under the MIT License. See `LICENSE` for details.
