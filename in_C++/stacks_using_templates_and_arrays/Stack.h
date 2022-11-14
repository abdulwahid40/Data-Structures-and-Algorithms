template<class T>
class Stack{
	private:
		int top;
		T *nodes;
	
	public:
		Stack();
		~Stack();
		int isEmpty();
		int push(T &);
		T pop();
		T peek();
		void display();	
		int sizeStack();	
};