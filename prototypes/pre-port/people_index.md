---
title: Team
date: 2024-01-01
type: landing

sections:
  - block: people
    content:
      title: Team
      user_groups:
        - Principal Investigator
        - Postdoctoral Researchers
        - Graduate Students
        - Undergraduate Researchers
    design:
      show_interests: false
      show_role: true
      show_social: true
      show_organizations: false

  - block: markdown
    content:
      title: ""
      subtitle: ""
      text: |
        {{< cta cta_link="/alumni" cta_text="See group alumni & collaborators →" >}}

        <!-- Team page layout: hide the per-group section headings so every
             member renders in one flat, continuous, horizontally-organized
             grid. Inline here so it always applies, independent of the
             SCSS build pipeline. -->
        <style>
          .people-widget .col-md-12 { display: none !important; }
          .people-widget .people-person { margin-bottom: 2rem; }
        </style>
    design:
      columns: '1'
---