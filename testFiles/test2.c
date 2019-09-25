#include <stdlib.h>
#include <stdio.h>

#define OK		0
#define ERROR	1
#define TRUE	0
#define FALSE	1

typedef int Status;
typedef int ElemType;	//为了通用性，将顺序栈中存储的数据类型进行单独定义

typedef struct {
    ElemType* base;		//存储空间基址
    int top;			//栈顶位置
    int size;			//栈的容量
} SqStack;

Status InitStack(SqStack &stack, int size);				//初始化顺序栈
Status ExpandStack(SqStack &stack, int expand_size);	//扩容顺序栈
void DestroyStack(SqStack &stack);						//销毁顺序栈
Status StackIsEmpty(SqStack stack);						//判断栈是否为空
int GetStackDepth(SqStack stack);						//获取栈深度
void ClearStack(SqStack &stack);						//清空栈
Status PushElem(SqStack &stack, ElemType elem);			//将元素压入栈中
Status FetchElem(SqStack &stack, ElemType &elem);		//取出栈顶元素
Status GetTop(SqStack stack, ElemType &elem);			//仅读取而不取出栈顶元素

Status InitStack(SqStack &stack, int size) {
	stack.base = (ElemType*) malloc(sizeof(ElemType) * size);
	if (stack.base != NULL) {
		stack.size = size;
		stack.top = 0;
		printf("栈初始化成功\n");
		return OK;
	} else {
		printf("栈初始化失败\n");
		return ERROR;
	}
}

Status ExpandStack(SqStack &stack, int expand_size) {
	ElemType* newBase = (ElemType*) realloc(stack.base, sizeof(ElemType) * (stack.size + expand_size));
	if (newBase != NULL) {
		stack.base = newBase;
		stack.size += expand_size;
		printf("栈已扩容\n");
		return OK;
	} else {
		printf("栈扩容失败\n");
		return ERROR;
	}
}

void DestroyStack(SqStack &stack) {
	free(stack.base);
}

Status StackIsEmpty(SqStack &stack) {
	return (stack.top == 0)?TRUE:FALSE;
}

int GetStackDepth(SqStack stack) {
	return stack.top;
}

void ClearStack(SqStack &stack) {
	stack.top = 0;
}

Status PushElem(SqStack &stack, ElemType elem) {
	//若栈已满则进行扩容
	if (stack.top == stack.size) {
		if (ExpandStack(stack, 5) == ERROR) {
			return ERROR;
		}
	}
	stack.base[stack.top] = elem;
	stack.top++;
	return OK;
}

Status FetchElem(SqStack &stack, ElemType &elem) {
	//如果操作的栈是空的，则出错
	if (stack.top == 0) {
		return ERROR;
	}
	stack.top--;
	elem = stack.base[stack.top];
	return OK;
}

Status GetTop(SqStack stack, ElemType &elem) {
	//如果操作的栈是空的，则出错
	if (stack.top == 0) {
		return NULL;
	}
	elem = stack.base[stack.top-1];
	return OK;
}

int main(int argc, char const *argv[])
{
	SqStack stack;
	ElemType result;
	InitStack(stack, 1);
	PushElem(stack, 111);
	PushElem(stack, 1111);
	FetchElem(stack, result);
	FetchElem(stack, result);
	printf("%d\n", result);
	DestroyStack(stack);
	return 0;
}
