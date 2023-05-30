---
layout: default
title: Contents
---

<ol>
  {% for post in site.posts %}
    <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <font color="#63E58A"><span class="tag">{{ post.tags | join: ', ' }}</span></red>
    <b><span class="meta">{{ post.date | date: "%Y-%m-%d" }}</b></font>
    </li>
  {% endfor %}
</ol>