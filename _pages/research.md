---
permalink: /Research/
title: "Research"
layout: single
author_profile: true
---

## Research interests
- High-dimensional statistics
- Generative AI and reinforcement learning
- Adaptive design and sequential estimation
- Astrostatistics
- Random matrix theory
- PDEs and dynamical systems

{% assign ordered_pubs = site.publications | sort: 'date' | reverse %}

## Preprints
{% assign preprints = ordered_pubs | where: 'research_section', 'preprints' %}
{% if preprints.size > 0 %}
<ul>
  {% for pub in preprints %}
  <li>
    <strong>{{ pub.title }}</strong>. {{ pub.citation }}
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">Paper</a>
    {% elsif pub.url %}
      <a href="{{ pub.url | relative_url }}">Details</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No preprints available at this time.</p>
{% endif %}

## Publications: Theory and Methodology
{% assign theory_pubs = ordered_pubs | where: 'research_section', 'theory-methodology' %}
{% if theory_pubs.size > 0 %}
<ul>
  {% for pub in theory_pubs %}
  <li>
    <strong>{{ pub.title }}</strong>. {{ pub.citation }}
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">Paper</a>
    {% elsif pub.url %}
      <a href="{{ pub.url | relative_url }}">Details</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No theory or methodology publications available at this time.</p>
{% endif %}

## Publications: Applications
{% assign application_pubs = ordered_pubs | where: 'research_section', 'applications' %}
{% if application_pubs.size > 0 %}
<ul>
  {% for pub in application_pubs %}
  <li>
    <strong>{{ pub.title }}</strong>. {{ pub.citation }}
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">Paper</a>
    {% elsif pub.url %}
      <a href="{{ pub.url | relative_url }}">Details</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No application-focused publications available at this time.</p>
{% endif %}
