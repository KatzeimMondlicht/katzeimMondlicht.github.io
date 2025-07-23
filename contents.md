---
layout: default
title: Contents
---

<ol> <b>
  {% for post in site.posts %}
    <li><span class="meta">{{ post.date | date: "%Y-%m-%d" }} <a href="{{ post.url }}">{{ post.title }}</a> <font color="#63E58A"><span class="category">{{ post.category | join: ', ' }}</span>
    </font>
  
  {% endfor %}
