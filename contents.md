---
layout: default
title: Contents
---

<ol>
  {% for post in site.posts %}
    <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <red><span class="tag">{{ post.tags | join: ', ' }}</span></red>
    <span class="meta">{{ post.date | date: "%Y-%m-%d" }}</span>
    </li>
  {% endfor %}
</ol>