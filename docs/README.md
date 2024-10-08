## 安装依赖

```
pip install mkdocs-git-revision-date-localized-plugin
sudo apt-get install git-lfs
git lfs install
```


## 更新文档

```
conda activate covid19
mkdocs serve -a 127.0.0.1:8003  # 本地预览
mkdocs gh-deploy  # 提交
```
