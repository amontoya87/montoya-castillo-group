import os

publications = [
    # --- PREPRINTS (Independent career) ---
    {
        "slug": "laskowski-2026-semiclassical",
        "title": "How to improve the accuracy of semiclassical and quasiclassical dynamics with and without generalized quantum master equations",
        "authors": "M. R. Laskowski, S. Bhattacharyya, A. Montoya-Castillo",
        "date": "2026-01-01",
        "pub_type": "preprint",
        "publication": "arXiv:2603.04563",
        "url": "https://arxiv.org/abs/2603.04563",
        "doi": "",
        "note": ""
    },
    {
        "slug": "sayer-2026-weather",
        "title": "Data-driven, non-Markovian modelling of weather in the presence of non-stationary, non-Gaussian, and heteroskedastic climate dynamics",
        "authors": "T. Sayer, A. Montoya-Castillo",
        "date": "2026-01-02",
        "pub_type": "preprint",
        "publication": "arXiv:2603.00259",
        "url": "https://arxiv.org/abs/2603.00259",
        "doi": "",
        "note": ""
    },
    {
        "slug": "canestraight-2026-stochastic",
        "title": "A Stochastic Cluster Expansion for Electronic Correlation in Large Systems",
        "authors": "A. Canestraight, A. J. Dominic, A. Montoya-Castillo, L. Veis, V. Vlcek",
        "date": "2026-01-03",
        "pub_type": "preprint",
        "publication": "arXiv:2602.12254",
        "url": "https://arxiv.org/abs/2602.12254",
        "doi": "",
        "note": ""
    },
    {
        "slug": "tubman-2025-downfolding",
        "title": "Theory of ab initio downfolding with arbitrary range electron-phonon coupling",
        "authors": "N. M. Tubman, C. J. N. Coveney, C.-E. Hsu, A. Montoya-Castillo, M. R. Filip, J. B. Neaton, Z. Li, V. Vlcek, A. M. Alvertis",
        "date": "2025-01-02",
        "pub_type": "preprint",
        "publication": "arXiv:2502.00103",
        "url": "https://arxiv.org/abs/2502.00103",
        "doi": "",
        "note": ""
    },
    {
        "slug": "tubman-2025-srtio3",
        "title": "Phonon-mediated electron attraction in SrTiO3 via the generalized Fröhlich and deformation potential mechanisms",
        "authors": "N. M. Tubman, C. J. N. Coveney, C.-E. Hsu, A. Montoya-Castillo, M. R. Filip, J. B. Neaton, Z. Li, V. Vlcek, A. M. Alvertis",
        "date": "2025-01-03",
        "pub_type": "preprint",
        "publication": "arXiv:2501.17230",
        "url": "https://arxiv.org/abs/2501.17230",
        "doi": "",
        "note": ""
    },
    {
        "slug": "wiethorn-2024-porphyrin",
        "title": "Symmetry breaking fluctuations split the porphyrin Q bands",
        "authors": "Z. R. Wiethorn, K. Hunter, A. Montoya-Castillo, T. Zuehlsdorff",
        "date": "2024-11-01",
        "pub_type": "preprint",
        "publication": "arXiv:2411.02687",
        "url": "https://arxiv.org/abs/2411.02687",
        "doi": "",
        "note": ""
    },
    # --- PUBLISHED (Independent career) ---
    {
        "slug": "li-2026-tensor-networks",
        "title": "Numerically exact quantum dynamics with tensor networks: Predicting the decoherence of interacting spin systems",
        "authors": "T. Li, P. Venkatesh, N. Shitara, A. Montoya-Castillo",
        "date": "2026-03-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 164, 091103",
        "url": "https://pubs.aip.org/aip/jcp/article/164/9/091103/3382073/",
        "doi": "",
        "note": ""
    },
    {
        "slug": "shitara-2026-noise",
        "title": "Fast, accurate, and error-resilient noise spectroscopy via basis optimization",
        "authors": "N. Shitara, A. Montoya-Castillo",
        "date": "2026-02-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 164, 061101",
        "url": "https://pubs.aip.org/aip/jcp/article/164/6/061101/3379373",
        "doi": "",
        "note": ""
    },
    {
        "slug": "mendes-2026-polaron",
        "title": "Coherent and Dynamic Small Polaron Delocalization in CuFeO2",
        "authors": "J. L. Mendes, S. Bhattacharyya, C. Huang, J. M. Michelson, F. Babbe, I. M. Klein, T. Sayer, T. Li, J. K. Cooper, H. Liu, N. Ginsberg, A. Montoya-Castillo, S. K. Cushing",
        "date": "2026-01-10",
        "pub_type": "article",
        "publication": "Journal of Physical Chemistry Letters, 17, 656",
        "url": "https://doi.org/10.1021/acs.jpclett.5c03430",
        "doi": "10.1021/acs.jpclett.5c03430",
        "note": ""
    },
    {
        "slug": "sambur-2026-gerischer",
        "title": "Gerischer Electrochemistry Today",
        "authors": "J. B. Sambur et al., A. Montoya-Castillo",
        "date": "2026-01-11",
        "pub_type": "article",
        "publication": "ACS Energy Letters, 11, 1",
        "url": "https://pubs.acs.org/doi/full/10.1021/acsenergylett.5c02966",
        "doi": "10.1021/acsenergylett.5c02966",
        "note": ""
    },
    {
        "slug": "kelly-2025-2des",
        "title": "Two-dimensional electronic spectroscopy in the condensed phase using equivariant transformer accelerated molecular dynamics simulations",
        "authors": "J. Kelly, F. Hu, A. Damiani, M. S. Chen, A. Snider, M. Son, A. Lee, P. Gupta, A. Montoya-Castillo, T. J. Zuehlsdorff, G. S. Schlau-Cohen, C. M. Isborn, T. E. Markland",
        "date": "2025-06-01",
        "pub_type": "article",
        "publication": "Journal of Physical Chemistry Letters, 16, 5561",
        "url": "https://pubs.acs.org/doi/10.1021/acs.jpclett.5c00911",
        "doi": "10.1021/acs.jpclett.5c00911",
        "note": ""
    },
    {
        "slug": "bhattacharyya-2025-nonequilibrium",
        "title": "Nonequilibrium relaxation exponentially delays the onset of quantum diffusion",
        "authors": "S. Bhattacharyya, T. Sayer, A. Montoya-Castillo",
        "date": "2025-05-01",
        "pub_type": "article",
        "publication": "Proceedings of the National Academy of Sciences, 122, e2424582122",
        "url": "https://www.pnas.org/doi/10.1073/pnas.2424582122",
        "doi": "10.1073/pnas.2424582122",
        "note": ""
    },
    {
        "slug": "dominic-2025-fourier",
        "title": "A pedagogical tour of the Fourier transform with applications to NMR and IR spectroscopy",
        "authors": "A. J. Dominic, N. L. Cipolla, W. C. Pfalzgraff, J. A. Jankowski, R. J. Rapf, A. Montoya-Castillo",
        "date": "2025-04-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Education, 102, 1972",
        "url": "https://pubs.acs.org/doi/full/10.1021/acs.jchemed.4c01439",
        "doi": "10.1021/acs.jchemed.4c01439",
        "note": ""
    },
    {
        "slug": "bhattacharyya-2025-space-local",
        "title": "Space-local memory in generalized master equations: Reaching the thermodynamic limit for the cost of a small lattice simulation",
        "authors": "S. Bhattacharyya, T. Sayer, A. Montoya-Castillo",
        "date": "2025-03-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 162, 091102",
        "url": "https://pubs.aip.org/aip/jcp/article/162/9/091102/3338405/",
        "doi": "10.1063/5.0249145",
        "note": "Accepted as a Communication & selected as an Editor's Pick"
    },
    {
        "slug": "austin-2024-trions",
        "title": "Hiding in plain sight: The prevalence and impact of trions and Fermi polarons in transient absorption spectroscopy experiments of 2D semiconductors",
        "authors": "R. Austin, T. Sayer, Y. Farrah, A. Montoya-Castillo, A. Krummel, J. B. Sambur",
        "date": "2024-11-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 161, 190901",
        "url": "https://pubs.aip.org/aip/jcp/article/161/19/190901/3320834",
        "doi": "",
        "note": "Selected as a Featured Article & Cover"
    },
    {
        "slug": "bhattacharyya-2024-mori-polaron",
        "title": "Mori generalized master equations offer an efficient route to predict and interpret polaron transport",
        "authors": "S. Bhattacharyya, T. Sayer, A. Montoya-Castillo",
        "date": "2024-10-01",
        "pub_type": "article",
        "publication": "Chemical Science, 15, 16715",
        "url": "https://pubs.rsc.org/en/content/articlelanding/2024/sc/d4sc03144j",
        "doi": "",
        "note": ""
    },
    {
        "slug": "sayer-2024-semiclassical-multitime",
        "title": "Generalized quantum master equations can improve the accuracy of semiclassical predictions of multitime correlation functions",
        "authors": "T. Sayer, A. Montoya-Castillo",
        "date": "2024-07-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 161, 011101",
        "url": "https://doi.org/10.1063/5.0219205",
        "doi": "10.1063/5.0219205",
        "note": "Accepted as a Rapid Communication"
    },
    {
        "slug": "vezvaee-2024-fourier-noise",
        "title": "Fourier Transform Noise Spectroscopy",
        "authors": "A. Vezvaee, N. Shitara, S. Sun, A. Montoya-Castillo",
        "date": "2024-06-01",
        "pub_type": "article",
        "publication": "npj Quantum Information, 10, 52",
        "url": "https://www.nature.com/articles/s41534-024-00841-w",
        "doi": "",
        "note": "Highlighted by JILA Research Highlights & phys.org"
    },
    {
        "slug": "bhattacharyya-2024-anomalous",
        "title": "Anomalous transport of small polarons arises from transient lattice relaxation or immovable boundaries",
        "authors": "S. Bhattacharyya, T. Sayer, A. Montoya-Castillo",
        "date": "2024-02-01",
        "pub_type": "article",
        "publication": "Journal of Physical Chemistry Letters, 15, 1382",
        "url": "https://pubs.acs.org/doi/10.1021/acs.jpclett.3c03380",
        "doi": "",
        "note": ""
    },
    {
        "slug": "sayer-2024-multitime-gqme",
        "title": "Efficient formulation of multitime generalized quantum master equations: Taming the cost of simulating 2D spectra",
        "authors": "T. Sayer, A. Montoya-Castillo",
        "date": "2024-01-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 160, 044108",
        "url": "https://pubs.aip.org/aip/jcp/article/160/4/044108/3105995/",
        "doi": "10.1063/5.0185578",
        "note": "Selected as an Editor's Pick"
    },
    {
        "slug": "wiethorn-2023-condon",
        "title": "Beyond the Condon limit: Condensed phase optical spectra from atomistic simulations",
        "authors": "Z. R. Wiethorn, K. Hunter, T. Zuehlsdorff, A. Montoya-Castillo",
        "date": "2023-12-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 159, 244114",
        "url": "https://pubs.aip.org/aip/jcp/article/159/24/244114/2931601/",
        "doi": "",
        "note": ""
    },
    {
        "slug": "almaraz-2023-interfacial",
        "title": "Quantifying interfacial energetics of 2D semiconductor electrodes using in situ spectroelectrochemistry and many-body theory",
        "authors": "R. Almaraz, T. Sayer, J. Toole, R. Austin, Y. Farah, J. M. Redwing, N. Trainor, A. Krummel, A. Montoya-Castillo, J. B. Sambur",
        "date": "2023-11-01",
        "pub_type": "article",
        "publication": "Energy & Environmental Science, 16, 4522",
        "url": "https://pubs.rsc.org/en/content/articlehtml/2023/ee/d3ee01165h",
        "doi": "",
        "note": ""
    },
    {
        "slug": "sayer-2023-trion",
        "title": "Trion formation resolves observed peak shifts in the optical spectra of transition metal dichalcogenides",
        "authors": "T. Sayer, Y. R. Farah, R. Austin, J. Sambur, A. T. Krummel, A. Montoya-Castillo",
        "date": "2023-10-01",
        "pub_type": "article",
        "publication": "Nano Letters, 13, 6035",
        "url": "https://pubs.acs.org/doi/full/10.1021/acs.nanolett.3c01342",
        "doi": "10.1021/acs.nanolett.3c01342",
        "note": ""
    },
    {
        "slug": "dominic-2023-memory",
        "title": "Memory unlocks the future of biomolecular dynamics: Transformative tools to uncover physical insights accurately and efficiently",
        "authors": "A. J. Dominic, S. Cao, A. Montoya-Castillo, X. Huang",
        "date": "2023-05-01",
        "pub_type": "article",
        "publication": "Journal of the American Chemical Society, 145, 9916",
        "url": "https://pubs.acs.org/doi/full/10.1021/jacs.3c01095",
        "doi": "10.1021/jacs.3c01095",
        "note": ""
    },
    {
        "slug": "austin-2023-hot-carrier",
        "title": "Hot carrier extraction from 2D semiconductor photoelectrodes",
        "authors": "R. Austin, Y. R. Farah, T. Sayer, B. M. Luther, A. Montoya-Castillo, A. T. Krummel, J. B. Sambur",
        "date": "2023-04-01",
        "pub_type": "article",
        "publication": "Proceedings of the National Academy of Sciences, 120, e2220333120",
        "url": "https://www.pnas.org/doi/abs/10.1073/pnas.2220333120",
        "doi": "10.1073/pnas.2220333120",
        "note": "Highlighted by CSU College News & Materials Today"
    },
    {
        "slug": "dominic-2023-building",
        "title": "Building insightful, memory-enriched models to capture long-time biochemical processes from short-time simulations",
        "authors": "A. J. Dominic, T. Sayer, S. Cao, T. E. Markland, X. Huang, A. Montoya-Castillo",
        "date": "2023-03-01",
        "pub_type": "article",
        "publication": "Proceedings of the National Academy of Sciences, 120, e2221048120",
        "url": "https://www.pnas.org/doi/10.1073/pnas.2221048120",
        "doi": "10.1073/pnas.2221048120",
        "note": ""
    },
    {
        "slug": "sayer-2023-compact",
        "title": "Compact and complete description of non-Markovian dynamics",
        "authors": "T. Sayer, A. Montoya-Castillo",
        "date": "2023-01-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 158, 014105",
        "url": "https://aip.scitation.org/doi/10.1063/5.0132614",
        "doi": "10.1063/5.0132614",
        "note": "Selected as an Editor's Pick"
    },
    # --- DOCTORAL & POSTDOCTORAL WORK ---
    {
        "slug": "chen-2023-gfp",
        "title": "Elucidating the role of hydrogen bonding in the optical spectroscopy of the solvated green fluorescent protein chromophore",
        "authors": "M. S. Chen, Y. Mao, A. Snider, P. Gupta, A. Montoya-Castillo, T. J. Zuehlsdorff, C. M. Isborn, T. E. Markland",
        "date": "2023-07-01",
        "pub_type": "article",
        "publication": "Journal of Physical Chemistry Letters, 14, 6610",
        "url": "https://pubs.acs.org/doi/10.1021/acs.jpclett.3c01444",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2023-bosonic",
        "title": "A derivation of the conditions under which bosonic operators exactly capture fermionic structure and dynamics",
        "authors": "A. Montoya-Castillo, T. E. Markland",
        "date": "2023-02-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 158, 094112",
        "url": "https://aip.scitation.org/doi/10.1063/5.0138664",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "atsango-2023-ehrenfest",
        "title": "An accurate and efficient Ehrenfest dynamics approach for calculating linear and nonlinear electronic spectra",
        "authors": "A. O. Atsango, A. Montoya-Castillo, T. E. Markland",
        "date": "2023-02-02",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 158, 074107",
        "url": "https://aip.scitation.org/doi/10.1063/5.0138671",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2022-anisotropy",
        "title": "Optically induced anisotropy in time-resolved scattering: Imaging molecular scale structure and dynamics in disordered media with experiment and theory",
        "authors": "A. Montoya-Castillo, M. S. Chen, S. L. Raj, K. A. Jung, K. S. Kjaer, T. Morawietz, K. J. Gaffney, T. B. van Driel, T. E. Markland",
        "date": "2022-07-01",
        "pub_type": "article",
        "publication": "Physical Review Letters, 129, 056001",
        "url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.056001",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "mao-2020-diabatization",
        "title": "Excited state diabatization on the cheap using DFT: Photoinduced electron and hole transfer",
        "authors": "Y. Mao, A. Montoya-Castillo, T. E. Markland",
        "date": "2020-12-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 153, 244111",
        "url": "https://aip.scitation.org/doi/full/10.1063/5.0035593",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "cao-2020-markov",
        "title": "On the advantages of exploiting memory in Markov state models for biomolecular dynamics",
        "authors": "S. Cao, A. Montoya-Castillo, W. Wang, T. E. Markland, X. Huang",
        "date": "2020-07-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 153, 014105",
        "url": "https://aip.scitation.org/doi/10.1063/5.0010787",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "mao-2019-dft-diabatization",
        "title": "Accurate and efficient DFT-based diabatization for hole and electron transfer using absolutely localized molecular orbitals",
        "authors": "Y. Mao, A. Montoya-Castillo, T. E. Markland",
        "date": "2019-10-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 151, 164114",
        "url": "https://aip.scitation.org/doi/10.1063/1.5125275",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "zuehlsdorff-2019-optical",
        "title": "Optical spectra in the condensed phase: Capturing anharmonic and vibronic features using dynamic and static approaches",
        "authors": "T. J. Zuehlsdorff, A. Montoya-Castillo, J. A. Napoli, T. E. Markland, C. M. Isborn",
        "date": "2019-08-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 151, 074111",
        "url": "https://aip.scitation.org/doi/10.1063/1.5114818",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "pfalzgraff-2019-gqme",
        "title": "Efficient construction of generalized master equation memory kernels for multi-state systems from nonadiabatic quantum-classical dynamics",
        "authors": "W. C. Pfalzgraff, A. Montoya-Castillo, A. Kelly, T. E. Markland",
        "date": "2019-06-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 150, 244109",
        "url": "https://aip.scitation.org/doi/full/10.1063/1.5095715",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2018-fermions",
        "title": "On the exact continuous mapping of fermions",
        "authors": "A. Montoya-Castillo, T. E. Markland",
        "date": "2018-08-01",
        "pub_type": "article",
        "publication": "Scientific Reports, 8, 12929",
        "url": "https://www.nature.com/articles/s41598-018-31162-6",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2017-mori-ii",
        "title": "Approximate but accurate dynamics from the Mori formalism: II. Equilibrium correlation functions",
        "authors": "A. Montoya-Castillo, D. R. Reichman",
        "date": "2017-02-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 146, 084110",
        "url": "https://aip.scitation.org/doi/abs/10.1063/1.4975388",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2017-path-integral",
        "title": "Path integral approach to the Wigner representation of canonical density operators for discrete systems coupled to harmonic baths",
        "authors": "A. Montoya-Castillo, D. R. Reichman",
        "date": "2017-01-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 146, 024107",
        "url": "https://aip.scitation.org/doi/abs/10.1063/1.4973646",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "kelly-2016-gqme",
        "title": "Generalized quantum master equations in and out of equilibrium: How can one win?",
        "authors": "A. Kelly, A. Montoya-Castillo, L. Wang, T. E. Markland",
        "date": "2016-05-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 144, 184105",
        "url": "https://aip.scitation.org/doi/abs/10.1063/1.4948612",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2016-mori-i",
        "title": "Approximate but accurate dynamics from the Mori formalism: I. Nonequilibrium dynamics",
        "authors": "A. Montoya-Castillo, D. R. Reichman",
        "date": "2016-05-02",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 144, 184104",
        "url": "https://aip.scitation.org/doi/full/10.1063/1.4948408",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "raja-2016-energy-transfer",
        "title": "Energy transfer from quantum dots to graphene and MoS2: screening vs. absorption",
        "authors": "A. Raja, A. Montoya-Castillo, J. Zultak, X.-X. Zhang, Z. Ye, C. Roquelet, D. A. Chenet, A. M. van der Zande, P. Huang, S. Jockusch, J. Hone, D. R. Reichman, L. E. Brus, T. F. Heinz",
        "date": "2016-03-01",
        "pub_type": "article",
        "publication": "Nano Letters, 16, 2328",
        "url": "https://pubs.acs.org/doi/abs/10.1021/acs.nanolett.5b05012",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "blackwell-2016-esr",
        "title": "ESR in the 21st century: From buried valleys and deserts to the deep ocean and tectonic uplift",
        "authors": "B. A. B. Blackwell, A. R. Skinner, J. I. B. Blickstein, A. Montoya-Castillo, J. A. Florentin, S. M. Baboumian, I. J. Ahmed, A. E. Deely",
        "date": "2016-01-01",
        "pub_type": "article",
        "publication": "Earth-Science Reviews, 158, 125",
        "url": "https://www.sciencedirect.com/science/article/pii/S0012825216300010",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "montoya-castillo-2015-redfield",
        "title": "Extending the applicability of Redfield theories into highly non-Markovian regimes",
        "authors": "A. Montoya-Castillo, T. C. Berkelbach, D. R. Reichman",
        "date": "2015-11-01",
        "pub_type": "article",
        "publication": "Journal of Chemical Physics, 143, 194108",
        "url": "https://aip.scitation.org/doi/full/10.1063/1.4935443",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "jang-2015-charge-hopping",
        "title": "Charge hopping dynamics along a disordered chain in quantum environments: Comparative study of different rate kernels",
        "authors": "S. Jang, A. Montoya-Castillo",
        "date": "2015-04-01",
        "pub_type": "article",
        "publication": "Journal of Physical Chemistry B, 119, 7659",
        "url": "https://pubs.acs.org/doi/abs/10.1021/jp511933m",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
    {
        "slug": "blackwell-2007-esr-india",
        "title": "ESR analyses for teeth from the open-air site at Attirampakkam, India: Clues to complex U uptake and paleoenvironmental change",
        "authors": "B. A. B. Blackwell, A. Montoya-Castillo, J. I. B. Blickstein, A. R. Skinner, S. Pappu, Y. Gunnell, M. Taieb, A. Kumar, J. A. Lundberg",
        "date": "2007-01-01",
        "pub_type": "article",
        "publication": "Radiation Measurements, 42, 1243",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S1350448707002132",
        "doi": "",
        "note": "Doctoral & postdoctoral work"
    },
]

def make_pub_md(pub):
    pub_type_map = {
        "article": "article-journal",
        "preprint": "article"
    }
    hugoblox_type = pub_type_map.get(pub["pub_type"], "article-journal")

    note_section = ""
    if pub["note"]:
        note_section = f'\nsummary: "{pub["note"]}"\n'

    doi_section = ""
    if pub["doi"]:
        doi_section = f'doi: "{pub["doi"]}"\n'

    content = f"""---
title: "{pub['title'].replace('"', "'")}"
authors:
  - {pub['authors']}
date: "{pub['date']}"
publishDate: "{pub['date']}"
publication_types:
  - "{hugoblox_type}"
publication: "{pub['publication']}"
url_pdf: ""
url_source: "{pub['url']}"
{doi_section}{note_section}---
"""
    return content

base_dir = "content/publication"
os.makedirs(base_dir, exist_ok=True)

for pub in publications:
    folder = os.path.join(base_dir, pub["slug"])
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "index.md")
    with open(filepath, "w") as f:
        f.write(make_pub_md(pub))
    print(f"Created: {filepath}")

print(f"\nDone! Created {len(publications)} publication files.")
