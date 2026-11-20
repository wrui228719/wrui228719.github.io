# 课程示例网站

首页是虚构学生王睿的中文简历。论文只作阅读参考。

在网站根目录运行 `python -m http.server 8000 --bind 127.0.0.1`，再打开 `http://127.0.0.1:8000/`。学习笔记的 JSON 源文件在 `content/knowledge/`，修改后用 `python scripts/knowledge.py build` 重新生成页面。
