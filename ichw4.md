## 概论作业4
**1.解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？**
- 概念解释：
  1. 作业：从一个程序被选中执行，到其运行结束并再次成为一个程序的这段过程中，这个程序称为作业，即用户向计算机提交的任务实体；
  1. 进程：是一个驻留在内存中运行的作业，是计算机为了完成用户任务实体而设置的执行实体；
  1. 线程：是操作系统能够进行运算调度的最小单位。被包含在进程中，是进程中的实际运作单位。
- 新概念提出解决的问题：
  1. 进程：从是对正在运行的程序过程的抽象，能清晰地刻画动态系统的内在规律，有效管理和调度进入计算机系统主存储器运行的程序。
  2. 线程：线程的创建与撤销，线程之间的切换所占用的资源要比进程少很多，从而进一步提高系统的并发性，提高CPU利用率。

**2. 调研虚拟存储器的概念，描述其工作原理和作用.**
- 概念：虚拟存储器是计算机系统内存管理的一种技术。
- 工作原理为以下6个步骤: 
  1. CPU访问主存的逻辑地址分解成组号a和组内地址b，并对组号a进行地址变换，以确定该组信息是否存放在主存内； 
  1. 如该组号已在主存内，则转而执行iv；如果该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往辅存，以便将这组信息调入主存； 
  1. 从辅存读出所要的组，并送到主存空闲区，然后将那个空闲的物理组号a和逻辑组号a登录在地址变换表中；
  1. 从地址变换表读出与逻辑组号a对应的物理组号a；
  1. 从物理组号a和组内字节地址b得到物理地址；
  1. 根据物理地址从主存中存取必要的信息。
- 作用：程序的大小可以超过可用的物理内存大小，由操作系统自动决定哪些部分保留在内存，哪些保存在磁盘。
