/* /assets/load.js */
(() => {
  /* 1. 基本配置 ----------------------------------------------------------- */
  const btn       = document.getElementById('load-more');
  if (!btn) return;                 // 防呆：页面上没有按钮就直接退出
  const total     = Number(btn.dataset.total);
  const container = document.querySelector('main'); // 你的文章列表容器
  let   nextPage  = 2;              // 从第 2 页开始加载
  let   loading   = false;          // 并发锁

  /* 2. 工具函数 ----------------------------------------------------------- */
  const hideBtn = () => (btn.hidden = true);
  const disableBtn = (flag = true) => (btn.disabled = flag);
  const insertPosts = doc => {
    const posts = doc.querySelectorAll('article.post');
    container.append(...posts);
    history.pushState(null, doc.title, doc.URL);
  };

  /* 3. 主加载逻辑 --------------------------------------------------------- */
  btn.addEventListener('click', () => {
    if (loading || nextPage > total) return;

    loading = true;
    disableBtn(true);

    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/page/${nextPage}/`);
    xhr.responseType = 'document';
    xhr.onload = () => {
      if (xhr.status === 200) {
        insertPosts(xhr.response);
        if (++nextPage > total) hideBtn();
      } else {
        console.error(`[load-more] 请求失败：${xhr.status}`);
      }
    };
    xhr.onerror = () => console.error('[load-more] 网络异常');
    xhr.onloadend = () => {
      loading = false;
      disableBtn(false);
    };
    xhr.send();
  });
})();