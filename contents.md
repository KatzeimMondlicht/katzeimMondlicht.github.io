---
layout: default
title: Contents
---

<ol>
  {% for post in site.posts %}
    <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="tag">{{ post.tags | join: ', ' }}</span>
    </li>
  {% endfor %}
</ol>