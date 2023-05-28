---
layout: default
---

<h1>{{ page.tags }}</h1>

<ul>
{% for post in site.posts %}
  {% if post.tags contains page.tags %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}"> {{ post.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>