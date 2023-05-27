---
layout: default
title: tag
---

<section class="tag">
  <1 class="tag-title">{{ page.title | capitalize }}</h1>
  <div class="tag-description">{{ page.description }}</div>
  
  <!-- List of posts with this tag -->
  < class="tag-posts">
    {% for post in site.tags[page.tag] %}
      <><a href="{{ post.url }}">{{ post.title }}</ali>
    {% endfor %}
  </ul>