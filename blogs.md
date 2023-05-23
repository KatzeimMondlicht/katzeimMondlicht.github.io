---
layout: default
title: Blogs
---
<h1>Blogs</h1>

<ol>
  {% for post in site.posts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ol>