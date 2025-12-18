---
permalink: /research-by-topic/
title: "Research by topic"
layout: single
author_profile: true
topics:
  - title: "High-dimensional statistics"
    id: high-dimensional-statistics
  - title: "Generative AI and Reiforcement Learning"
    id: generative-ai-and-reiforcement-learning
  - title: "Adaptive design and sequential estimation"
    id: adaptive-design-and-sequential-estimation
  - title: "Astrostatistics"
    id: astrostatistics
  - title: "Random matrix theory"
    id: random-matrix-theory
  - title: "PDEs and dynamical systems"
    id: pdes-and-dynamical-systems
---

<!-- The sections below automatically gather every publication and preprint, grouped by the research threads that colleagues most often ask about. As you add new papers to the `_publications/` collection with the appropriate `topics` tag, they will appear in the relevant section without further editing. -->

{% assign ordered_pubs = site.publications | sort: 'date' | reverse %}

{% for topic in page.topics %}
### {{ topic.title }}

{% assign topic_pubs = ordered_pubs | where_exp: 'pub', 'pub.topics contains topic.id' %}
{% if topic_pubs.size > 0 %}
<ul class="research-topic-list">
  {% for pub in topic_pubs %}
  <li>
    <strong>{{ pub.title }}</strong>. {{ pub.citation | replace: 'Hongru Zhao', '<u>Hongru Zhao</u>' }}
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">Paper</a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No publications available for this topic yet.</p>
{% endif %}

{% endfor %}
