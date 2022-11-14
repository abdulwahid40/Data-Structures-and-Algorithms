# include "Stacks_Templates.cpp"

using namespace std;

int main(){
	
	Stack<int> intStack;
	Stack<char> charStack;
	
	int x = 10, y = 20;
	char c = 'C', d = 'D';
	

	intStack.push(x);
	intStack.push(y);
	
	cout << "Elements in Stacks\n";
	intStack.display();
	cout << "\n\n";
	
	cout << "Size of Stack: " << intStack.sizeStack() + 1 << "\n";

	cout << "Element at top of Stack: " << intStack.peek() << "\n";
	
	cout << "inStack pop method: " << intStack.pop() << " , " << intStack.pop() << "\n";
	
	charStack.push(c);
	charStack.push(d);
	cout << "charStack pop method: " << charStack.pop() << " , " << charStack.pop() << "\n";
	
	getche();
	return 0;
}