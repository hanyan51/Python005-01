学习笔记
使用 socket 可以进行基于套接字的底层网络编程。

socket 对象是网络通信的基础，相当于一个管道连接了发送端和接收端，并在两者之间相互传递数据。

对于 TCP，首先服务器启动，服务器和客户端都必须调用 socket() 建立一个套接字 socket，服务器调用 bind() 将套接字与本机指定端口绑定在一起，再调用 listen() 使套接字处于一种被动的准备接收状态。然后客户端建立套接字便可以通过调用 connect() 与服务器建立连接，服务器可以调用accept() 来接收客户端连接，然后继续监听指定端口，并发出阻塞，直到下一个请求出现，从而实现连接多个客户端。建立连接后，客户端和服务器之间就可以发送和接收数据。数据结束传送后，双方调用 close() 关闭套接字。

对于 UDP，客户端通过 sendto() 给服务器发送数据，服务器调用 revcfrom()，等待客户端传来的数据。服务器根据 recvfrom() 给客户机应答。

创建 TCP socket 的语法如下：

```python
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

创建 UDP socket 的语法如下：

```python
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
```

实例：TCP 连接豆瓣网

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建 socket 对象，TCP 协议
s.connect(('www.douban.com', 80)) # 主动建立豆瓣网连接，一般格式为元组(hostname, post)
# send 发送括号中的请求
s.send(b'GET / HTTP/1.1\r\nHOST:www.douban.com\r\nConnection:close\r\n\r\n')

buffer = []
while True:
		data = s.recv(1024) # 每次最多接收服务器 1k 的数据
		if data:
				buffer.append(data) # 加入到 buffer 列表
		else:
				break # 返回空数据，接收完毕退出循环
response = b''.join(buffer)
s.close()

header, html = response.split(b'\r\n\r\n', 1)
print(header.encode('utf-8'))

with open('douban.html', 'wb') as f:
		f.write(html)
```

如果想访问 https 安全协议的网站如新浪，需要 ssl 协议，将上述代码改为

```python
import socket
import ssl  # ssl协议需要ssl模块

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象，tcp
sock = ssl.wrap_socket(socket.socket())  # 使用https的socket对象
sock.connect(('www.sina.com.cn', 443))  # https端口为443

sock.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  # send发送括号中的请求

buffer = []
while True:
    d = sock.recv(1024)  # 每次最多接收服务器端1k的数据
    if d:
        buffer.append(d)  # 加入到buffer列表
    else:
        break  # 返回空数据，接收完毕退出循环
data = b''.join(buffer)  # b表示空字节，join()是连接列表的函数，buffer是一个字节串列表，这句就是是用空字节把buffer字节列表连接在一起成为新字符串
sock.close()  # 关闭连接

header, html = data.split(b'\r\n\r\n', 1)  # 以\r\n\r\n分隔一次，
print(header.decode('utf-8'))  # 打印头内容

with open('sina.html', 'wb') as f:
    f.write(html)  # 具体html文件写入文档中
```

TCP **服务端程序**

TCP 服务端相比 TCP 客户端程序要复杂一些。服务端首先要绑定一个端口用于监听其他客户端的连接。同时服务器还要相应多个客户端的请求，因此每个连接都需要一个新的进程或线程来处理。

编写一个简单的 TCP 服务端程序，接收客户端请求，将客户端发过来的字符加上 Hello 再发送回去。

```python
import socket
import time
import threading

def tcplink(sock, addr):
		print("接受一个来自%s：%s的连接请求" % addr)
    sock.send(b'Welcome!')  # 发送给客户端welcome信息
    while True:
        data = sock.recv(1024)  # 接收客户端信息
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break  # 如果没有数据或者接受到exit，则终止接受
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  # 收到的信息加上hello在发回去
    sock.close()
    print("来自%s:%s的连接关闭了" % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))  # 绑定并监听本机8888端口，只有本机客户端才能连接
s.listen(5)  # 连接最大数量为5
print("等待客户连接：")
while True:
    sock, addr = s.accept()  # 接受一个新链接，accpet()会等待并返回一个客户端的连接
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 创建新线程处理tcp连接
    t.start()
```

测试程序

```python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888)) #建立链接
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```


# **一 、with 语句的原理**

- 上下文管理协议（Context Management Protocol）：包含方法 `__enter__()`和`__exit__()`，支持该协议的对象要实现这两个方法。
- 上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了`__enter__()`和`__exit__()`方法。上下文管理器定义执行`with`语句时要建立的运行时上下文，负责执行`with`语句块上下文中的进入与退出操作。通常使用`with`语句调用上下文管理器，也可以通过直接调用其方法来使用。

说完上面两个概念，我们再从`with`语句的常用表达式入手，一段基本的`with`表达式，其结构是这样的：

```python
1 with EXPR as VAR:
2
3 BLOCK
```

其中EXPR可以是任意表达式；as VAR是可选的。其一般的执行过程是这样的：

1. 执行EXPR，生成上下文管理器context_manager；
2. 获取上下文管理器的`__exit()__`方法，并保存起来用于之后的调用；
3. 调用上下文管理器的`__enter__()`方法；如果使用了`as`子句，则将`__enter__()`方法的返回值赋值给`as`子句中的VAR；
4. 执行BLOCK中的表达式；
5. 不管是否执行过程中是否发生了异常，执行上下文管理器的`__exit__()`方法，`__exit__()`方法负责执行“清理”工作，如释放资源等。如果执行过程中没有出现异常，或者语句体中执行了语句`break/continue/return`，则以`None`作为参数调用`__exit__(None, None, None)`；如果执行过程中出现异常，则使用`sys.exc_info`得到的异常信息为参数调用`__exit__(exc_type, exc_value, exc_traceback)`；
6. 出现异常时，如果`__exit__(type, value, traceback)`返回False，则会重新抛出异常，让`with`之外的语句逻辑来处理异常，这也是通用做法；如果返回True，则忽略异常，不再对异常进行处理。

# **二、自定义上下文管理器**

`Python`的`with`语句是提供一个有效的机制，让代码更简练，同时在异常产生时，清理工作更简单。

```
 1 # coding = utf-8
 2 # 2019/7/19  Luckyxxt：有趣的事，Python永远不会缺席！
 3 #!/usr/bin/env python
 4 
 5 class DBManager(object):
 6     def __init__(self):
 7         pass
 8 
 9     def __enter__(self):
10         print('__enter__')
11         return self
12 
13     def __exit__(self, exc_type, exc_val, exc_tb):
14         print('__exit__')
15         return True
16 
17 def getInstance():
18         return DBManager()
19 
20 with getInstance() as dbManagerIns:
21     print('with demo')
```

**with后面必须跟一个上下文管理器，如果使用了as，则是把上下文管理器的 __enter__() 方法的返回值赋值给 target，target 可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“,”分隔的变量列表，必须加“()”）**

代码运行结果如下：

```
1 '''
2 __enter__
3 with demo
4 __exit__
5 
6 '''
```

结果分析：当我们使用with的时候,__enter__方法被调用，并且将返回值赋值给as后面的变量，并且在退出with的时候自动执行__exit__方法

```
 1 class With_work(object):
 2     def __enter__(self):
 3         """进入with语句的时候被调用"""
 4         print('enter called')
 5         return "xxt"
 6 
 7     def __exit__(self, exc_type, exc_val, exc_tb):
 8         """离开with的时候被with调用"""
 9         print('exit called')
10 
11 
12 with With_work() as f:
13     print(f)
14     print('hello with')
```

```
1 '''
2 enter called
3 xxt
4 hello with
5 exit called
6 
7 '''
```