---
- 描述：修复 Targeting COVID-19 Portal 的部分问题
- 作者：Qi Liu <qi.liu@ghddi.org>
- 创建：2022年9月14日
- 更新：2022年9月14日
---

# 问题


[TOC]



# git相关问题

## 账号权限

原wxy的账号目前无法进行提交，获取项目权限后，修改本账号的`.ssh`。


<details>
  <summary>原先的git config</summary>
  
```
# https://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent
eval `ssh-agent -s`
ssh-add

ssh-add ~/.ssh/id_rsa

git remote set-url origin git@github.com:GHDDI-AILab/Targeting2019-nCoV.git
```


```
(covid19) ghddiai@ai_server02:~/Targeting2019-nCoV$ git config -l
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
user.name=wxy0810500
user.email=newman_wang@sina.com
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@github.com:GHDDI-AILab/Targeting2019-nCoV.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
lfs.repositoryformatversion=0
```
</details>


## 超大文件

出现超大的文件无法上传的问题。

<details>


```text
Total 224 (delta 143), reused 212 (delta 135)
remote: Resolving deltas: 100% (143/143), completed with 7 local objects.
remote: error: Trace: e7bd1de6045197fe739092925ac6bf9cc19a9c49749e7c7093ba5b267229cf4c
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File file/outputs/dimensions-covid19-export-2021-03-27-h06-27-04_publications.csv is 632.97 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To github.com:GHDDI-AILab/Targeting2019-nCoV.git
 ! [remote rejected] gh-pages -> gh-pages (pre-receive hook declined)
error: failed to push some refs to 'git@github.com:GHDDI-AILab/Targeting2019-nCoV.git'
Traceback (most recent call last):
  File "/home/ghddiai/anaconda3/envs/covid19/bin/mkdocs", line 8, in <module>
    sys.exit(cli())
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/click/core.py", line 1259, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/mkdocs/__main__.py", line 216, in gh_deploy_command
    gh_deploy.gh_deploy(
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/mkdocs/commands/gh_deploy.py", line 108, in gh_deploy
    ghp_import.ghp_import(
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/ghp_import.py", line 285, in ghp_import
    git.check_call('push', opts['remote'], opts['branch'])
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/site-packages/ghp_import.py", line 119, in check_call
    sp.check_call(['git'] + list(args), **kwargs)
  File "/home/ghddiai/anaconda3/envs/covid19/lib/python3.8/subprocess.py", line 364, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['git', 'push', 'origin', 'gh-pages']' returned non-zero exit status 1.
```


```
git rm --cached --ignore-unmatch file/outputs/dimensions-covid19-export-2021-03-27-h06-27-04_publications.csv
```

</details>


# 文件缺失

## 总览

- `http://aidd.ghddi.org/covid19/`是在哪里进行域名解析的
- 原先`http://aidd-common.oss-cn-hangzhou.aliyuncs.com` 下的文件都需要重新下载
  - `computational.md` x27
  - `contact_us.md` x4
  - `review_paper.md`, `CN_review_paper.md`中的文献需要重新下载 x8
  - `Data_analytics.md` x1
- `CN_contact_us.md` 中`http://aidd-common.oss-cn-hangzhou.aliyuncs.com`相关文件缺失


## drugs biologics vaccines

- 在**drugs_biologics_vaccines.py**中

  ```
  df = pd.read_csv('https://docs.google.com/spreadsheets/d/1-kTZJZ1GAhJ2m4GAIhw1ZdlgO46JpvX0ZQa232VWRmw/export?format=csv&id=1-kTZJZ1GAhJ2m4GAIhw1ZdlgO46JpvX0ZQa232VWRmw&gid=1410737911')
  ```
  Google到[这个](https://docs.google.com/spreadsheets/u/0/d/10t3vtULr3nTz7mrlKj0rldUys47wsIfOVReHnx3Xu18/htmlview)，其中含有路径相似的，但是同样失效了。
  搜索关键词，找到[这个](https://dimensions.figshare.com/articles/dataset/Dimensions_COVID-19_publications_datasets_and_clinical_trials/11961063)，可能是最新的链接。




## 自动翻译

下面这两个脚本找不到。
```
targeting_covid_translation.py
targeting_covid19_automation.sh
```

## 结构

位于`/data01/ghddi_public` 下有关于蛋白质结构的文件。


# html文件嵌入到markdown中

- `research_progress`和`CN_research_progress.md` 通过 `<iframe>` 嵌入了`ldatopics.html`
- `preclinical.md`和`CN_preclinical.md` 通过 `<iframe>` 嵌入了`list.html`

原先是放在阿里云上，如今进行了清理。本地发现了这两个文件，但是无法通过`<iframe>`进行加载。

**改为直接方位github raw文件**

  ```html
  <iframe src="https://raw.githubusercontent.com/GHDDI-AILab/Targeting2019-nCoV/gh-pages/file/list.html" style="border:0px #ffffff none;" name="preclinical" frameborder="1" marginheight="0px" marginwidth="0px" height="500px" width="700px" scrolling="yes" allowfullscreen></iframe>

  <iframe src="https://raw.githubusercontent.com/GHDDI-AILab/Targeting2019-nCoV/gh-pages/file/ldatopics.html" style="border:0px #ffffff none;" name="preclinical" frameborder="1" marginheight="0px" marginwidth="0px" height="500px" width="700px" scrolling="yes" allowfullscreen></iframe>
  ```

会出现`raw.githubusercontent.com 已拒绝连接`的问题。



# 运行和调试

```
mkdocs serve -a 127.0.0.1:8003  # 本地预览
mkdocs gh-deploy  # 提交
```



