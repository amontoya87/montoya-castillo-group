---
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Montoya-Castillo
        Group
      image:
        filename: welcome.jpg
      text: |
        **Theoretical Chemistry &nbsp;|&nbsp; University of Colorado Boulder**

        <br>

        We develop theoretical and computational tools to understand
        charge and energy transfer dynamics in the condensed phase —
        with applications in solar energy conversion, catalysis at
        electrode surfaces, and quantum computing.

        <br>

        {{< cta cta_link="/research" cta_text="See our research →" >}}
        &nbsp;&nbsp;
        {{< cta cta_link="/join" cta_text="Join the group →" >}}

  - block: about.avatar # about.biography
    id: about
    content:
      title: Principal Investigator
      username: admin

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: collection
    content:
      title: Featured Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title: Research
      subtitle: "Developing theory and computation to understand complex quantum and classical processes across chemistry, biology, materials, and beyond."
      text: |
        <br>

        **🧬 Biophysical Transformations** — Uncovering how slow conformational 
        changes in biomolecules drive disease, revealing principles for 
        molecular treatment design.

        **⚡ Out-of-Equilibrium Energy Flow** — Simulating and decoding 
        spectroscopies and microscopies to manipulate charge and energy 
        flow in molecular systems and next-generation energy materials.

        **🔬 Quantum Sensing** — Enabling precision measurement of temperature, 
        magnetic, and electric field fluctuations in microscopic environments 
        to advance quantum technologies and probe biological systems.

        **📐 Mori-Zwanzig Theory** — Developing bottom-up and data-driven 
        approaches to predict dynamics of complex many-body systems with 
        controllable precision, from biomolecules to climate.

        <br>

        {{< cta cta_link="/research" cta_text="Explore our research →" >}}
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{< cta cta_link="/people" cta_text="Meet the team →" >}}
    design:
      columns: '1'
---