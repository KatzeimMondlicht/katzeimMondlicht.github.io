// load.js
const main   = document.querySelector('main');
const tpl    = document.getElementById('loader');
main.appendChild(tpl.content);

const button = main.querySelector('#load');
const client = new XMLHttpRequest();
let   next   = 2;                       // 下一页页码
const total  = Number(button.dataset.total);

button.addEventListener('click', () => {
  if (client.readyState !== 0) return;  // 防止并发
  client.open('GET', `/page/${next}/`);
  client.responseType = 'document';
  client.send();
});

client.addEventListener('load', () => {
  if (client.status === 200) {
    const doc = client.response;
    main.append(...doc.querySelectorAll('article.post'));
    history.pushState(null, doc.title, client.responseURL);

    if (++next > total) button.hidden = true;
  } else {
    console.error('Load failed:', client.status);
  }
});