# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- v0.0.3 引入 debug Agent
- v0.0.3 引入 RAG 检索相关文档

### Changed

- Use frontmatter title & description in each language version template
- Replace broken OpenGraph image with an appropriately-sized Keep a Changelog 
  image that will render properly (although in English for all languages)
- Fix OpenGraph title & description for all languages so the title and 
description when links are shared are language-appropriate

### Removed

- Trademark sign previously shown after the project description in version 


## [0.0.2] - 2024-08-24【0.1850】

### Added

- 没有输入文件的题目，通过生成数据运行脚本。

### Analyze

1. 有些问题是把结果写入文件，这些需要将写入的文件内容读取出来作为答案。

例如第 186 题：

```
As a cinematographer, you have been hired to document the growth of a 2-ary tree in a forest over time. The tree has 5 vertices and is a simple structure. Using your expertise in visualizing structures, you need to create a visual representation of the tree graph in DOT format and save it to a file named 'tree_graph.dot' for further analysis and documentation.
```

需要把 tree_graph.dot 文件的内容读取出来作为答案。

2. 有些比较简单的报错，可以通过 RAG 找到正确的内容。

```text
Traceback (most recent call last):
  File "/Users/liuzhaofeng01/PycharmProjects/SMP-2024-LLM-Graph/submit/2024-08-24/code/3.py", line 13, in <module>
    spanning_trees = list(nx.minimum_spanning_trees(G))
AttributeError: module 'networkx' has no attribute 'minimum_spanning_trees'
```

引入一个 debug Agent。

## [0.0.1] - 2024-08-21【0.1737】

### Added

- 直接通过 GPT-40 mini 生成代码，执行然后再 refine 答案。

### Analyze

代码执行错误类型统计

| 错误类型 | 出现次数 |
| --- |------|
|  ModuleNotFoundError  | 21   |
|  FileNotFoundError  | 102  |
|  AttributeError  | 121  |
|  ImportError  | 38   |
|  TypeError  | 60   |
|  KeyError  | 13   |
|  NetworkXError  | 33   |
