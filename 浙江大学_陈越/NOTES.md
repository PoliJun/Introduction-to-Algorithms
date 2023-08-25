# 图书摆放

## 循环与递归

![print](img/printN.pic.jpg)

## 多项式定点求和

![alt](img/多项式求和.pic.jpg)
从内向外

## `clock()`

`#include <time.h>`
![alt](<img/clock().pic.jpg>)

## 什么是数据结构？

-   **数据对象**在计算机中的组织方式
-   数据对象必定与一系列加载其上的**操作**相关联
-   完成这些操作所用的方法就是**算法**

## 抽象数据类型(Abstract Data Type)

-   数据类型
    -   数据的对象集
    -   数据集合相关联的操作集
-   抽象：描述数据类型的方法不依赖于具体实现
    -   与存放数据的机器无关
    -   与数据存储的物理结构无关
    -   与实现操作的算法和编程语言无关

### 矩阵例子

![alt](img/矩阵.pic.jpg)

## 什么是算法

-   算法
    -   一个有限的指令集
    -   接受一些输入
    -   产生输出
    -   一定在有限步骤之后终止
    -   每一条指令必须
        -   有充分明确的目标， 不可以有歧义
        -   计算机能处理的范围之内
        -   描述应不依赖于任何一种计算机语言以及具体的实现手段

### 例： 选择排序算法的 pseudocode

![alt](img/选择排序pseudo.pic.jpg)

## 什么是好的算法

-   空间复杂度 S(n)
    > 根据算法写成的程序在执行时占用存储单元的长度。
-   时间复杂度 T(n)
    > 根据算法写成的程序在执行时耗费时间的长度。

### 分析算法效率

-   最坏情况复杂度 Tworst(n)
-   平均复杂度 Tavg(n)

### 复杂度的渐进表示法

![alt](img/复杂度的渐进表示法.jpg)

-   增长率曲线图
    ![alt](img/曲线.jpg)

### 复杂度分析小窍门

![alt](img/xiaoqiaomen.jpg)

### 例：最大子列和问题

intuition:
improve a `O(n^2)` to `O(n log n)`  
**分而治之**  
![分而治之数学分析](img/fenzhimath.jpg)
**在线处理**  
![O(n) 在线处理](img/在线处理.jpg)

# 2 线性结构

## 2.1 线性表及其表现

### 分析： 多项式的表示

先找关键数据

![alt](img/多项式的表示.jpg)

-   方法
    1. 连续数组
    2. 数对数组
    3. 链表

### 线性表

-   线性表的抽象数据类型描述

    > ![Alt text](img/线性表的抽象数据类型描述.png)

-   操作
    -   建立
    -   查找
    -   插入
        1. 先移动
        2. 插入
    -   删除
        1. 后面的元素依次前移

### 线性表的链式存储实现

**不要求逻辑上相邻的两个物理元素物理上也相邻， 插入、删除不需要移动数据元素，只需要修改“链”。**

-   操作
    -   求表长
        > ![alt](img/求表长.png)
    -   查找
        -   按序号查找
        -   按值查找
            > ![alt](img/查找.png)
    -   插入
        节点操作顺序固定
        ![插入](img/charu.png)
    -   删除
        ![alt](img/删除.png删除)

### 广义表

-   展示
    ![alt](img/广义表展示.png)
-   定义
    ![alt](img/广义表定义.png)

### 多重链表

-   定义
    -   指针域会有多个，例如包含 Next 和 SubList 两个指针域
    -   但有多个指针域的不一定是多重链表，比如双向链表
        > ![alt](img/多重链表定义.png)
-   数图等多重用途

### 矩阵

二维数组表示
![alt](img/矩阵.png)

-   分析
    -   数据域:
        > `Row`, `Col`, `Value`
    -   每个节点通过两个指针域，把同行、同列串起来；
        -   行指针： Right
        -   列指针： Down
-   矩阵 A 的多重链表图
    > ![alt](img/矩阵A.png)  
    > ![节点结构](img/矩阵A节点结构.png)
    -   Term 节点： 入口。 非零项 7 项

## 堆栈

### 后缀表达式

> ![后缀表达式](img/houzhui.png)
> Time: Ο(n)

### 堆栈的抽象数据类型描述

-   push
-   pop
-   **LIFO**
    > ![alt](img/dzchx.png)

### 栈的顺序存储实现

**栈的顺序存储结构通常由一个一堆数组和一个记录栈顶元素位置的变量组成**

1. push 判断 stack 满不满
2. pop 判断空不空

#### 例：用一个数组实现两个堆栈

从两边向中间
![alt](img/clbxzj.png)

### 堆栈的链式存储实现

Top 在堆栈的头节点
![alt](img/dzdlscch.png)

1. push 不需要判断满不满
2. pop 判断空不空

### 堆栈应用：表达式求值

#### 中缀表达式求值

转换为后缀表达式  
Top 永远是当前最高优先级

#### 中缀表达式如何转换为后缀表达式

> ![alt](img/zzbdsrhzhwhzbds.png)

### 堆栈的其他应用

-   函数调用及递归实现
-   深度优先搜索
-   回溯算法
-   ...
    **按顺序保存状态，然后按顺序调用**

## 队列及实现

**FIFO**

### 什么是队列

-   插入和删除操作：一端插入，另一端删除

### 队列的抽象数据类型描述

![alt](img/dldcxsjlxms.png)

### 队列的顺序存储实现

-   循环队列
    > ![alt](img/xhdl.png)
    -   解决 front == rear
        1. 使用额外标记
        2. 仅使用 n-1 个空间
    -   (rear+1) % MaxSeze == 0, 则满
    -   front == rear， 则空

### 队列的链式存储实现

队列的链式存储结构也可以用一个单链表实现。插入和删除操作分别在链表的两头进行。 front 在头部，rear 在尾部。  
定义 Qnode，里面有两个指针，分别指向 Front 节点和 rear 节点。

-   front == null : 空

![dldlsccsx](img/dldlsccsx.png)

#### 不带头节点的链式队列出队操作

![bdtjddlsdlcdcz](img/bdtjddlsdlcdcz.png)

## 一元多项式的加乘法实现

### 多项式加法运算

-   the structure of the
    1. 系数
    2. 指数
    3. 指向下一个节点的指针

### 程序框架搭建

指针的指针：rear 初始指向一个空节点

> ![cxkjdj](img/cxkjdj.png))

### 如何将两个多项式相乘

转换为加法运算
![rhjlgdxsxc](img/rhjlgdxsxc.png)

# 树

### 什么是树

like a family tree

### 查找

定义：根据某个给定关键字 K， 从集合 R 中找出关键字与 K 相同的记录

-   静态查找
    > 没有插入和删除的操作
    -   哨兵
        > ![jtcz,sxcz](img/jtczsxcz.png)
    -   二分查找
        -   数据必须有序排列
        -   必须连续存放(数组)
-   动态查找
    > 可以发生插入和删除

### 树的定义

-   树(Tree): n(n>=0) 个结点构成的有限集合。
    -   当 n=0 时，称为空树
    -   根(Root)
    -   互不相交的子树
        > ![sddy](img/sddy.png)

#### 树的一些基本术语

![sdysjbsy1](img/sdyxjbsy1.png)
![sdyxjbsy2](img/sdyxjbsy2.png)

### 树的表示

-   儿子-兄弟表示法

    -   节点结构统一
    -   同时空间浪费不大

    > ![ezxdbsf](img/ezxdbsf.png)

-   儿子-兄弟结构是一个**_二叉树_**
    > ![ezxdecs](img/ezxdecs.png)

#### 二叉树的定义

-   可以为空
-   根节点
-   左子树
-   右子树

#### 特殊二叉树

-   斜二叉树
-   完美二叉树/满二叉树
-   完全二叉树

> ![tsecs](img/tsecs.png)

#### 二叉树的几个重要性质

![ecsdjgzyxz](img/ecsdjgzyxz.png)

#### 二叉树的抽象数据类型定义

最主要的操作是遍历  
![ecsdcxsjlxdy](img/ecsdcxsjlxdy.png)

### 二叉树的存储结构

-   使用完全二叉树,数组存储
    ![ecsdszcc](img/ecsdszcc.png)
-   链表存储
    ![ecsdlbcc](img/ecsdlbcc.png)

### 二叉树的遍历

-   先序遍历

    1. 访问根节点
    2. 先序遍历左子树
    3. 先序遍历右子树

    > 递归实现
    > ![alt](img/xxbl.png)

-   中序遍历

    1. 中序遍历左子树
    2. 访问根节点
    3. 中序遍历右子树

    ![alt](img/zxbl.png)

-   后序遍历

    1. 后序遍历左子树
    2. 后序遍历右子树
    3. 访问根节点

    ![alt](img/hxbl.png)

### 二叉树的非递归遍历

中序遍历：  
![zxbldfdgbl](img/zxbldfdgbl.png)  
也可先序遍历和后序遍历。移动 print 位置即可。

### 层序遍历

-   核心问题：**二维结构的线性化**
-   从节点访问其左右儿子节点 - 保存节点
-   需要一个存储结构保存暂时不访问的节点
-   存储结构：堆栈、队列
    > 堆栈保存自己，队列保存未访问的儿子节点
    > ![cxjbgc](img/cxbldjbgc.png)

### 二叉树遍历的应用

求树的高度
【例】求二叉树的高度。

```c
// 求左子树深度，求右子树深度。 二者去大，+1
int PostOrderGetHeight( BinTree BT ) { int HL, HR, MaxH;
if( BT ) {
HL = PostOrderGetHeight(BT->Left); /*求左子树的深度*/
HR = PostOrderGetHeight(BT->Right); /*求右子树的深度*/
MaxH = （HL > HR）? HL : HR; /*取左右子树较大的深度*/
return ( MaxH + 1 ); /*返回树的深度*/ }
else return 0; /* 空树深度为0 */
}
```

### 树的同构

-   求解思路
    1. 二叉树表示
        > 结构数组
    2. 建二叉树
    3. 同构判断
-   结构数组
    > 没有指向的是根节点
    > 是静态数组
    > ![结构数组表示二叉树](img/jgszbsecs.png)
-   如何判断二叉树同构
    ![如何判断二叉树同构1](img/rhpdecssstg2.png)
    ![如何判断二叉树同构2](img/rhpdecssstg1.png)

    ```c
    int Isomorphic ( Tree R1, Tree R2 )
    {
    if ( (R1==Null )&& (R2==Null) ) /* both empty */
    return 1;
    if ( ((R1==Null)&&(R2!=Null)) || ((R1!=Null)&&(R2==Null)) )
    return 0; /* one of them is empty */
    if ( T1[R1].Element != T2[R2].Element )
    return 0; /* roots are different */
    if ( ( T1[R1].Left == Null )&&( T2[R2].Left == Null ) )
    /* both have no left subtree */
    return Isomorphic( T1[R1].Right, T2[R2].Right );
    ……
    }
    ```

    ```c
    int Isomorphic ( Tree R1, Tree R2 )
    { ……
    if ( ((T1[R1].Left!=Null)&&(T2[R2].Left!=Null))&&
    ((T1[T1[R1].Left].Element)==(T2[T2[R2].Left].Element)) )
    /* no need to swap the left and the right */
    return ( Isomorphic( T1[R1].Left, T2[R2].Left ) &&
    Isomorphic( T1[R1].Right, T2[R2].Right ) );
    else /* need to swap the left and the right */
    return ( Isomorphic( T1[R1].Left, T2[R2].Right) &&
    Isomorphic( T1[R1].Right, T2[R2].Left ) );
    }
    ```

## 二叉搜索树

-   查找问题
    -   静态查找与动态查找
    -   针对动态查找， 数据如何组织

### 查找最大值和最小值

-   最大元素一定是在树的最右分枝的端结点上
    ```c
    Position FindMax( BinTree BST )
    { if(BST )
    while( BST->Right ) BST = BST->Right;
    /*沿右分支继续查找，直到最右叶结点*/
    return BST;
    }
    ```
-   最小元素一定是在树的最左分枝的端结点上
    ```c
    Position FindMin( BinTree BST )
    { if( !BST ) return NULL; /*空的二叉搜索树，返回NULL*/
    else if( !BST->Left )
    return BST; /*找到最左叶结点并返回*/
    elsereturn FindMin( BST->Left ); /*沿左分支继续查找*/
    }
    ```

### 二叉搜索树的插入

-   关键是要找到元素应该插入的位置，可以采用与 Find 类似的方法

```c
BinTree Insert( ElementType X, BinTree BST )
{
if( !BST ){
/*若原树为空，生成并返回一个结点的二叉搜索树*/
BST = malloc(sizeof(struct TreeNode));
BST->Data = X;
BST->Left = BST->Right = NULL;
}else /*开始找要插入元素的位置*/
if( X < BST->Data )
BST->Left = Insert( X, BST->Left);
/*递归插入左子树*/
else if( X > BST->Data )
BST->Right = Insert( X, BST->Right);
/*递归插入右子树*/
/* else X已经存在，什么都不做 */
return BST;
}
```

### 二叉搜索树的删除

-   考虑三种情况
    1. 要删除的是叶节点
    2. 要删除的节点有左、右两棵子树
        - 用另一节点替代别删除的节点：**右子树的最小**或**左子树的最大**
        ```c
        BinTree Delete( ElementType X, BinTree BST )
        { Position Tmp;
        if( !BST ) printf("要删除的元素未找到");
        else if( X < BST->Data )
        BST->Left = Delete( X, BST->Left); /* 左子树递归删除 */
        else if( X > BST->Data )
        BST->Right = Delete( X, BST->Right); /* 右子树递归删除 */
        else /*找到要删除的结点 */
        if( BST->Left && BST->Right ) { /*被删除结点有左右两个子结点 */
        Tmp = FindMin( BST->Right );
        /*在右子树中找最小的元素填充删除结点*/
        BST->Data = Tmp->Data;
        BST->Right = Delete( BST->Data, BST->Right);
        /*在删除结点的右子树中删除最小元素*/
        } else { /*被删除结点有一个或无子结点*/
        Tmp = BST;
        if( !BST->Left ) /* 有右孩子或无子结点*/
        BST = BST->Right;
        else if( !BST->Right ) /*有左孩子或无子结点*/
        BST = BST->Left;
        free( Tmp );
        }
        return BST;
        }
        ```
    3.

### 平衡二叉树

-   **平衡因子**
    > Balance Factor, BF. BF(T) = hl - hr.
-   平衡二叉树
    > Balance Binary Tree, AVL
    > 空树， 或者任一节点左、右子树高度差的绝对值不超过 1，即`｜BF(T)｜ <= 1`
-   平衡二叉树
    > 满足 Time: `Ο(log n)`.

### 平衡二叉树的调整

-   右旋
    > 插在发现者的右子树的右子树上  
    >  ![rr rotate](img/RR.png)
-   左旋
    > 插在发现者的左子树的左子树上
    > ![左旋](img/LL.png)
-   左右旋
    > 插在发现者的左子树的右子树上
    > ![LR](img/LR.png)
-   右左旋
    > 插在发现者的右子树的左子树上
    > ![RL](img/RL.png)

### 是否是同一棵二叉搜索树

-   两个序列是否对应相同搜索树的判别
    1. 分别建两棵树的判别方法

```c
// 使用flag
```

    2. 不建树的判别方法

### Reverse Linked List

#### 什么是抽象的链表

节点构成，每个节点有两个域，一个是值，另一个指向下一个节点的位置。

#### 单链表的逆转

1. create a temp node to hold current node.next
2. redirect
3. head.next.next = &(K+1 node)

#### 测试数据

-   有尾巴不反转
-   地址取到上下界
-   正好全反转
-   K=N 全反转
-   K=1 不用反转
-   最大（最后剩 K-1 不反转）、最小 N
-   有多余节点

# 第五讲 树（下）

## 5.1 堆

### 5.1.1 什么是堆

-   优先队列(priority queue):取出元素按**优先权（关键字）**大小。
-   最大堆(MaxHeap)和最小堆(MinHeap)
-   堆的抽象数据类型描述
    ![堆的抽象数据类型描述]()

### 5.1.2 堆的插入

![alt](https://)

### 5.1.3 最大堆，删除根节点

1. 移除根节点
2. 将最后节点放置到根节点
3. 从上至下 matain 这个 Heap， 通过置换父子节点 if Element[Child] > Element[Parent]

### 5.1.4 建立最大堆

`Ο(n)`

1. 先将元素按顺序建立完全二叉树
2. 从下至上建堆

## 5.2 哈夫曼树

-   哈夫曼树的定义
    -   ![哈夫曼树的定义](img/)
    -   最优二叉树或哈夫曼树：WPL 最小的二叉树。

###### my own experience

To build a data structure, build an Object or use key value pairs.

## 5.3

### 5.3.1 集合的表示及查找

![集合的表示](img/)

-   集合运算
    > 交、并、补、差，判定一个元素是否属于某一集合
-   查并集
    > 集合并、查某元素属于什么集合
-   并查集问题中集合存储如何实现？
    > Root 节点表示这个集合，双亲节点为 parent，寻找节点属于哪个集合，从下向上循环访问父节点

### 5.3.2 集合的并运算

![集合的并运算](img/)

### 堆的路径

-   数组表示堆
-   “岗哨”方便判断下标是否越界
### 伪递归
编译器将递归转换成优化的循环，实际上执行的是一个循环。
# 6 图
### 6.1.1 什么是图
- 表示多对多的关系
线性表和树可以看作是图的一种特殊情况
### 图的抽象数据类型
- 抽象数据类型三要素
    1. 名称
    2. 抽象对象集合
    3. 操作集
    