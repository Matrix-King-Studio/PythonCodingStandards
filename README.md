# 1. 前言

> 这个项目主要是提供了一份 Matrix 工作室的编码风格指南，总结了几年来的项目开发经验和踩坑经验。
> 当然，本项目更多的是一种参考，也提供了一些工具，希望可以帮助到大家。

首先，关于 Python 代码的编码风格，可以直接参考 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) [[中译版](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents.html)]，Google 作为世界一流大厂，他们的 Python 风格指南写的非常的好，完整读下来绝对受益匪浅。

当然，我知道大家都不是很喜欢读文档，所以本项目更多的提供一些工具和方法论，可以拿过来直接用，在实战中规范自己的代码。

文档内容可能会与您的喜好冲突，请尽量用包容的心态来接受，如果你觉得有不合理之处，那你说的都对。

在阅读本文档之前，我们假设你已经掌握了以下知识：

1. Git
2. Github
2. Python
3. Markdown

# 2. 文档

> 程序员最讨厌的 4 件事：
> 1. 写文档
> 2. 写注释
> 3. 别人不写文档
> 4. 别人不写注释

## 需求开发文档（PRD）

> 一般一个团队要有两个负责人，产品经理负责管理和沟通，开发经理负责技术和功能实现。

对于程序员来说，一个项目确定要做是从接到 PRD 开始的，当然我们也要参加 PRD 的讨论和确定过程，建议找一个技术栈比较全面的开发经理来参与讨论，因为他可以大致判断哪些需求可以做，哪些需求不能做，可以避免参会的人会后还要再去找技术确定。

作为开发，拿到 PRD 之后，一定要先搞清楚这个项目要做什么，有哪些模块，每个模块有哪些功能，列好思维导图。这个时候，前面参会的技术大佬可以在最后做决策和补充，以及提供一些问题解决方案。

千万不要着急写代码，除非这个功能你已经开发过很多次了。在真正写代码之前，建议每个人都先说一下自己的实现方案，定好接口文档和测试用例。另外，在介绍实现方案的时候，建议找一个杠精来，作为红队疯狂挑刺，有的时候这种人的角度非常刁钻，能看到常人看不到的东西，我们可以怀着包容的心态跟他辩论。

尽量事前就把 80% 的需求和事项讨论清楚，颗粒度建议细化到核心函数级别，事前充分的讨论能够避免事后大部分问题。

一定要讨论！一定要讨论！一定要讨论！

当然，也不是所有的需求都要做，适当的时候也可以跟产品和甲方 battle。

## 系统功能图

思维导图可以用来梳理系统功能，进而可以构建系统功能图，这个一般是产品经理先定好框架，然后开发人员再细化内容，以产品经理为主。

系统功能图的重点在于功能，主要是产品经理用来对外讨论，所以千万不要太专业，功能点尽量让人一看就明白。

## 系统架构图

系统架构图跟系统功能图类似，只是系统架构图更侧重于技术实现，内容可以更专业，以开发经理为主。

系统架构图的目的是让开发人员了解整个系统的各个模块之间的调用关系，以及各个模块之间的数据交互，主要是用来内部讨论，方便快速了解是哪个模块的问题，方便定位。

![系统框架图](docs\images\系统框架图.png)

## 功能时序图

时序图的目的是为了梳理系统各个模块之间的调用顺序，主要针对的是交互比较复杂的局部，比如多轮交互，或者异步交互。

功能时序图是要交互的两个模块的开发者之前确定的，搭配接口文档和测试用例使用，可以使用 Mock 测试工具来模拟数据交互。

![功能时序图](docs\images\功能时序图.png)

> 总而言之，写代码之前，多讨论多沟通，一个文档三张图，缺一不可。产品经理和开发经理可以不写代码，但是一定要验收这三张图。

> 还有一点是，虽然我们都想事前把所有的需求和功能都 100% 确定下来，但这确实不现实，一般能确定下来 80% 就很好了，但是没关系，一旦涉及到超出自己能力范围之外的需求，一定要跟产品经理和开发经理沟通。

## 提交说明

Git 的 Commit Message（提交说明）也是一种日志。

在 commit 之前一定要想一下哪里还有不完善的地方，避免多次 commit。

在 commit 的时候多花 5 秒钟写一个有明确含义的 message 绝对能让你避免很多麻烦。

可以借助一些工具来生成 message，比如 Github Copilot 或 文心快码。

每天晚上推送最新的代码（定个闹钟），可以借助 Github 的 Webhooks 往开发群里推送消息，这样大家也能及时看见。

## 更新日志

> 更新日志不是 git 日志的堆砌物。

# 3. 质量保证工具

> Matrix 工作室编程守则
> 1. KISS原则（Keep It Stupid Simple），不要让问题复杂化，要简单易懂；
> 2. DRY原则（Don't Repeat Yourself），不要重复你的代码，抽象成函数；
> 3. CYC原则（Code is Your Child），想象每一段代码都是你的孩子，你要一直维护它。

安装代码质量检查的依赖库

```shell
pip install requirements_code_quality.txt
```

## PyLint

PyLint 可以对单个文件进行检查，并且输出代码中不符合规范的代码行，还能够给出打分。

例如对于下面这个 Python 文件：
```python
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
```

运行下面的命令：
```
> pylint main_pylint.py
************* Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 5.00/10
```

例如这里说我们的 main() 函数没有写函数文档，我们给它加上函数文档之后，再运行 PyLint 命令：
```
> pylint main_pylint.py
************* Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 5.00/10, +2.50)
```

可以发现 PyLint 给出的提示变少了，而且分数也提高了。

## pre-commit

pre-commit 框架是一个支持多语言的 pre-commit 脚本的管理器，能够简化我们的 pre-commit 脚本配置。

使用 pre-commit 框架时，在 .pre-commit-config.yaml 配置文件指定所需的linter列表（脚本列表），然后 pre-commit 框架会自动下载这些linter并运行。

创建 pre-commit 框架配置文件 .pre-commit-config.yaml：

```yaml
default_stages: [ commit ]

# Install
# 1. pip install pre-commit
# 2. pre-commit install(the first time you download the repo, it will be cached for future use)
repos:
  - repo: https://github.com/pycqa/isort
    rev: 5.11.5
    hooks:
      - id: isort
        args: [ '--profile', 'black' ]
        exclude: >-
          (?x)^(
          .*__init__\.py$
          )

  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.6.2
    hooks:
      # Run the linter.
      - id: ruff
        args: [ --fix ]
      # Run the formatter.
      - id: ruff-format

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        args: [ '--line-length', '120' ]
```

运行pre-commit框架:

```shell
pre-commit run --all-files
```

## git-pylint-commit-hook

在`.git/hooks`文件夹下创建`pre-commit`文件，并填入如下内容：
```
git-pylint-commit-hook --limit=8.0
```

git-pylint-commit-hook 有几个参数可以配置：
```
--limit LIMIT        分数限制，分数较低的文件将停止提交。默认值：8.0
--pylint PYLINT      pylint 可执行文件的路径。默认值：pylint
--pylintrc PYLINTRC  pylintrc 文件的路径，通过这个文件可以自定义检查规则。
--pylint-params      自定义要添加到pylint命令中的pylint参数
--version            打印当前版本号
```

# 参考资料

- [pylint+pre-commit+commit-msg](https://blog.csdn.net/zang_debby/article/details/126830304)
- [git和pylint结合自动检测规范 (git-pylint-commit-hook）](https://blog.csdn.net/ypgsh/article/details/110139816)
- [cannot import name 'find_pylintrc' from 'pylint.config' #444](https://github.com/microsoft/vscode-pylint/issues/444)
- [find_pylintrc removed in 3.0 #9105](https://github.com/pylint-dev/pylint/issues/9105)
- [Docs » Welcome to git-pylint-commit-hook’s documentation!](https://git-pylint-commit-hook.readthedocs.io/en/latest/)
- [好好学Git：Git pre-commit 代码质量检查](https://www.voidking.com/dev-git-pre-commit/)
- []()
- [如何维护更新日志](https://keepachangelog.com/zh-CN/1.1.0/)
- []()
