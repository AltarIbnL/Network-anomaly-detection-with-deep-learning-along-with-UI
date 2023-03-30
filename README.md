### Network-anomaly-detection-with-deep-learning-along-with-UI

2023年3/30 更新

更改了net.py 中 在view或reshape时，输入的模型形状，不再设置为一个定值64，而是用out.size(0)代替

```
关于我项目的简要介绍可以看一下我的博客：
https://blog.csdn.net/weixin_39032619/article/details/120337693
```

项目基于pytorch，PyQt

在运行项目前，请先安装winpcap以对网络流量进行嗅探。

```
安装目录：https://www.winpcap.org/
```

# 文件夹功能

dataprocess 文件夹负责对将pacp文件进行处理为我们所需要的源文件。

UI 文件夹包含页面的图片资源。

model包含我们所训练的三个模型

NetData 中，我们将网络流量包切成多个数据流并保存在txt文件内

# 文件功能的介绍

- menu.py是项目主文件，主要是项目逻辑的运行和一些按钮功能的关联
- ui.py 是基于ui.ui，使用QTdesigner生成的文件，不能改动。如果想改动需要在ui.ui上进行改动QTdesigner的部署可以自己上网搜一下，可以通过可视化界面完成一些简要的搭建

- sniff.py负责读取当前网络流

- prepare.py 是负责读取处理后的流量数据并转换为pytorch的tensor

- net.py 是网络模型代码

这里只包含了模型结构还有训练好的模型，训练过程的代码还有数据集我之后再上传到github。

虽然代码写的稀烂，不过请大家不要吝啬自己的star，算是给我写代码的认可。



项目运行结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/c7358132a5d24132a6a00073700cb9e2.gif#pic_center#pic_center)