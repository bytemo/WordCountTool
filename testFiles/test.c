#include <stdlib.h>
#include <stdio.h>

#define OK		0
#define ERROR	1
#define TRUE	0
#define FALSE	1

typedef int Status;
typedef int ElemType;	//为了通用性，将循环队列中存储的数据类型进行单独定义

typedef struct {
	ElemType* base;		//存储空间基址
	int head;			//队头位标
	int end;			//队尾位标
	int size;			//队列容量
	int length;			//队列长度
} SqQueue;

Status InitQueue(SqQueue &queue, int size);				//初始化循环队列
Status ExpandQueue(SqQueue &queue, int expand_size);	//扩容循环队列
void DestroyQueue(SqQueue &queue);						//销毁循环队列
Status QueueIsEmpty(SqQueue queue);						//判断队列否为空
int GetQueueLength(SqQueue queue);						//获取队列长度
void ClearQueue(SqQueue &queue);						//清空队列
Status EnQueue(SqQueue &queue, ElemType elem);			//将元素加入队尾
Status DeQueue(SqQueue &queue, ElemType &elem);			//取出队头元素
Status GetHeadElem(SqQueue queue, ElemType &elem);		//仅读取而不取出队尾元素

Status InitQueue(SqQueue &queue, int size) {
	queue.base = (ElemType*) malloc(sizeof(ElemType) * size);
	if (queue.base == NULL) {
		printf("队列初始化失败\n");
		return ERROR;
	} else {
		queue.head = 0;
		queue.end = 0;
		queue.size = size;
		queue.length = 0;
		printf("队列初始化成功\n");
		return OK;
	}
}

Status ExpandQueue(SqQueue &queue, int expand_size) {
	ElemType* newBase = (ElemType*) realloc(queue.base, sizeof(ElemType) * (queue.size + expand_size));
	if (newBase == NULL) {
		printf("队列扩容失败\n");
		return ERROR;
	} else {
		queue.base = newBase;
		//如果队列的尾部已经折叠到队头之前，则需要将队头部分后移
		if (queue.end <= queue.head) {
			for (int i = (queue.size - queue.head); i > 0 ; i--) {
				queue.base[queue.head + i - 1 + expand_size] = queue.base[queue.head + i - 1];
			}
			queue.head += expand_size;
			printf("队列头部已迁移\n");
		}
		queue.size += expand_size;
		printf("队列已扩容\n");
		return OK;
	}
}

void DestroyQueue(SqQueue &queue) {
	free(queue.base);
}

Status QueueIsEmpty(SqQueue queue) {
	return (queue.length == 0)?TRUE:FALSE;
}

int GetQueueLength(SqQueue queue) {
	return queue.length;
}

void ClearQueue(SqQueue &queue) {
	queue.head = 0;
	queue.end = 0;
	queue.length = 0;
}

Status EnQueue(SqQueue &queue, ElemType elem) {
	//如果队列已满则进行扩容
	if (queue.length == queue.size) {
		if (ExpandQueue(queue, 5) == ERROR) {
			return ERROR;
		}
	}
	queue.base[queue.end] = elem;
	queue.end = (queue.end + 1) % queue.size;
	queue.length++;
	return OK;
}

Status DeQueue(SqQueue &queue, ElemType &elem) {
	//如果操作的队列为空，则出错
	if (queue.length == 0) {
		elem = -1;
		return ERROR;
	}
	elem = queue.base[queue.head];
	queue.head = (queue.head + 1) % queue.size;
	queue.length--;
	return OK;
}

Status GetHeadElem(SqQueue queue, ElemType &elem) {
	//如果操作的队列为空，则出错
	if (queue.length == 0) {
		return ERROR;
	}
	elem = queue.base[queue.head];
	return OK;
}

int main(int argc, char const *argv[])
{
	SqQueue queue;
	ElemType result;
	int len;
	while(1);
	InitQueue(queue, 3);
	EnQueue(queue, 11);
	EnQueue(queue, 11);
	EnQueue(queue, 111);
	DeQueue(queue, result);
	EnQueue(queue, 4);
	EnQueue(queue, 5);
	len = GetQueueLength(queue);
	for (int i = 0; i < len; i++)
	{
		printf("%d,%d\n", DeQueue(queue, result), result);
	}
	DestroyQueue(queue);
	return 0;
}
