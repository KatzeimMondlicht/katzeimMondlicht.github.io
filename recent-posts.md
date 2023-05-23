---
layout: default
title: Recent Posts
---
<h1>Recent Posts</h1>

<ol>
  {% for post in site.posts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ol>