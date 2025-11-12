1. package引入package_status_logger, 记录package build时的git rev-parse HEAD和git status。

2. Package(path), Module(path)替代Package(name), Module(name)，因为我们总是先打开文件才知道'.'或':'，且Source没有'.'。另外，不要用executable，会混淆。

3. 对编译错误的parse，写在Compiler类里面。