---
layout: default
---
<!--不行啊这个标签页就直接生成到tag这个页面本身了，没有出现那种对应具体tag页面的列表呜呜，难道要一个一个单独建立吗？-->




<h1>{{ page.tag }}</h1>

<ul>
{% for post in site.posts %}
  {% if post.tags contains page.tag %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>