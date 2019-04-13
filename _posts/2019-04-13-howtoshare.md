---
layout: post
title:  "Hotpot分享者指南"
excerpt: "本文写给Hotpot计划的分享者，包括如何贡献自己的选校和录取信息(不透露个人联系方式)、如何给学弟学妹分享交流、暑研、申请心得……"
categories: Hotpot
tags: 建站
author: cooks
top: true
typora-copy-images-to: ipic
---

* content
{:toc}
>  注：这是一份简明的使用指南，我们预设您懂得如何使用[Markdown](http://support.typora.io/Markdown-Reference/)和[Github](https://guides.github.com/activities/hello-world/)，如果需要学习相关知识，可以进入我们提供的超链接。

本文写给*Hotpot计划* 的分享者，包括如何贡献自己的选校和录取信息(不透露个人联系方式)、如何上传自己的交流、暑研、申请心得，希望我们能够促进跨年级信息交流，一起帮助学弟学妹们在申请时少走弯路。

## 分享动机与原则：

可参见建站的[卷首语](https://fdu-cooks.github.io/fdu-gradhotpot/2019/04/10/hellohotpot/#%E8%87%B4%E5%88%86%E4%BA%AB%E8%80%85)中提到的公益动机和分享原则：

>  -  **分享自由：** 期待分享者能够尽可能填写完整的资料，为学弟学妹们提供全面完善的信息。我们以及学弟学妹对此表示**真诚的感谢（×100）！**同时，分享者可以隐藏不想透露的信息。
>  -  **隐私保护：** 分享者的真实姓名、联系方式等隐私信息将被保护。并且只有在分享者允许的情况下，学弟学妹们才能通过学号邮件请求到分享者的个人联系方式。
>  -  **公益性质：** 该项目依靠我旦学长学姐的善意分享而建立，希望分享者不要填写虚假信息，同时也不要出现广告等商业信息，感谢！

## 分享的具体流程：

#### 选校定位[(Collections)](https://fdu-cooks.github.io/fdu-gradhotpot/collections/)：

-  我旦的学长学姐的选校与录取，能够为学弟学妹提供直接的定位和比较，信息分享包括两大块：**录取情况**和**个人背景**，两者兼备才能给学弟学妹提供参考。
-  **完成该问卷即可添加您的选校定位信息：<https://wj.qq.com/s2/3492415/6902/>  (注：电脑端填写更方便)**
-  问卷中有一道题询问联系方式，联系方式不会直接暴露在网上，学弟学妹需要通过学号邮箱进行请求才能获得联系方式，避免网络其他信息对您生活的干扰。

#### 申请心得[(Categories)](https://fdu-cooks.github.io/fdu-gradhotpot/category/)：

##### 写作前：

-  您可以将自己在申请过程中的心得、教训、建议在这里分享，您可以写申请全程回顾、详细而全面（例：[这一篇](https://fdu-cooks.github.io/fdu-gradhotpot/2019/04/11/%E6%9D%B0%E5%B0%BC%E9%BE%9F%E7%9A%84%E7%94%B3%E8%AF%B7%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB/)），您也可以有所侧重、精简干练（例：[这一篇](https://fdu-cooks.github.io/fdu-gradhotpot/2019/04/12/%E7%94%B3%E8%AF%B7%E5%89%8D%E5%87%86%E5%A4%87-%E8%BD%AC%E7%A0%81%E5%90%91/)），只要您认为能够帮助他人即可。
-  您可通过向Github提交Markdown文件添加申请心得，相信 CS / DS 的你能够很快搞定这些，我们的文章存放在[此处](https://github.com/fdu-cooks/fdu-gradhotpot/tree/master/_posts/%E7%94%B3%E8%AF%B7%E7%BB%8F%E9%AA%8C)，可作为您写作前的参考。

##### 写作时：

-  您需要注意两点要求，以便文章顺利地显示在Hotpot网站上：

   1. **Markdown文件名：**` YYYY-MM-DD - TITLE.md` 格式。

      >  例：2019-04-11 - 杰尼龟的申请经验分享.md

   2. **Markdown文件抬头：** 其中`toc`部分是为了能够在网站上加载目录内容，完成抬头后就可以在Markdown中自由地写作啦。

       ```markdown
       ---
       layout: post
       title:  "请输入标题"
       excerpt: "请输入摘要"
       categories: 申请经验
       tags: 您打算输入的标签，请用空格隔开
       author: 请输入您的昵称
       ---
       * content
       {:toc}
       ```

       >  例：[2019-04-12 - 申请前准备 - 转码向.md](https://raw.githubusercontent.com/fdu-cooks/fdu-gradhotpot/master/_posts/%E7%94%B3%E8%AF%B7%E7%BB%8F%E9%AA%8C/2019-04-12-%E7%94%B3%E8%AF%B7%E5%89%8D%E5%87%86%E5%A4%87-%E8%BD%AC%E7%A0%81%E5%90%91.md) 的抬头：
       >
       >  ```markdown
       >  ---
       >  layout: post
       >  title:  "转码之路，道阻且长"
       >  excerpt: "这是来自妙蛙种子的申请经验分享~ 我主要讲讲申请前准备（GT、实习、科研、简历）几个方面说一说自己的看法"
       >  categories: 申请经验
       >  tags: 申请准备
       >  author: 妙蛙种子
       >  ---
       >  * content
       >  {:toc}
       >  ```


##### 写作后：


-  当您完成写作之后，您可以选择其中一种方式上传：
   -  创建Pull Request推送到我们的代码仓库中，这种方式能够使您纳入到我们的Github贡献者名单中，如果您不担心真实姓名被透露，我们推荐您采取这种方法(文章存放位置：[代码仓库](https://github.com/fdu-cooks/fdu-gradhotpot)的 `fdu-gradhotpot/_posts/申请经验/` 文件夹中)。
   -  将您的Markdown文件发送至Hotpot公邮<fdu-hotpot@outlook.com>中，我们将尽快帮您上传。
-  注：如果您需要插入图片，我们推荐您使用在线图床。

## 写在最后

感谢您的无私分享，让我们一起打造通畅且非盈利的复旦留学信息渠道，希望您在我们的[代码仓库](https://github.com/fdu-cooks/fdu-gradhotpot)中提交意见和建议，以及如果有可能的话，欢迎加入我们！诚挚感谢！

