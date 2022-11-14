# include <iostream>
# include <conio.h>

using namespace std;

// Node Class
class Node {
	private:
		int object;
		Node *nextNode;
		Node *prevNode;
	public:
		int get(){
			return object;
		}
		void set(int object){
			this -> object = object;
		}
		Node *getNext(){
			return nextNode;
		}
		void setNext(Node *nextNode){
			this->nextNode = nextNode;
		}
		Node *getPrev(){
			return prevNode;
		}
		void setPrev(Node *prevNode){
			this->prevNode = prevNode;
		}

};

// Linked-List Class
class List{
	private:
		int size;
		Node *headNode;
		Node *currentNode;
		Node *lastCurrentNode;
	public:
		List();
		void addStart(int addObject);
		void add(int addObject);
		void remove();
		int get();
		bool next();
		void start();
		int length();
		friend void traverse(List list);
		friend List addNodes();
};

List::List(){
	headNode = new Node();
	headNode->setNext(NULL);
	headNode->setPrev(NULL);
	currentNode = NULL;
	lastCurrentNode = NULL;
	size = 0;
}

void List::addStart(int addObject){
	Node *newNode = new Node();
	newNode->set(addObject);
	newNode->setNext(currentNode);
	newNode->setPrev(headNode);
	if(currentNode != NULL){
		currentNode->setPrev(newNode);
	}
	lastCurrentNode = headNode;
	currentNode = headNode;	
	size++;
}

// add method for class List
void List::add(int addObject){
	Node *newNode = new Node();
	newNode->set(addObject);
	if (currentNode != NULL){
		newNode->setNext(currentNode->getNext());
		newNode->setPrev(currentNode);
		(currentNode->getNext())->setPrev(newNode);
		currentNode->setNext(newNode);
		lastCurrentNode = currentNode;
		currentNode = newNode;
	}
	else{
		newNode->setNext(NULL);
		newNode->setPrev(headNode);
		headNode->setNext(newNode);
		headNode->setPrev(NULL);
		lastCurrentNode = headNode;
		currentNode = newNode;
	}
	size++;
}

//// remove method of class List
//// remove currentNode element
//void List::remove(){
//	if (currentNode != NULL && currentNode != headNode){
//		lastCurrentNode->setNext(currentNode->getNext());
//		delete currentNode;
//		currentNode = lastCurrentNode->getNext();
//		size--; 	
//	}
//}

// get method for class List
int List::get(){
	if (currentNode != NULL){
		return currentNode->get();
	}
}

//// next method for class List
bool List::next(){
	if (currentNode == NULL){
		return false;
	}
	
	lastCurrentNode = currentNode;
	currentNode = currentNode->getNext();
	if (currentNode == NULL || size == 0){
		return false;
	}
	else{
		return true;
	}
} 

// start method of class List
void List::start(){
	lastCurrentNode = headNode;
	currentNode = headNode;
}

int List::length(){
	return size;
}

// Friend function to traverse linked list
//void traverse(List list){
//	Node *savedCurrentNode = list.currentNode;
//	list.currentNode = list.headNode;
//	for(int i=1; list.next(); i++){
//		cout << "\nElement " << i << " " << list.get();
//	}
//	list.currentNode = savedCurrentNode;
//}


// Friend function to add Nodes in the list
//List addNodes(){
//	List list;
//	
//	list.add(2);
//	list.add(6);
//	list.add(8);
//	list.add(7);
//	list.add(1);
//	
//	cout << "\nList Size: " << list.length();
//	return list;
//}

//int main(){
//	
//	List list = addNodes();
//	traverse(list);
//	
//	getche();
//	return 0;
//}

// another way to add data in linked lists
int main(){
	
	List list;
	
	list.add(5);
	list.addStart(7);
	//cout << "Element: " << list.get();	
//	list.start();
//	cout << list.get();
	while(list.next()){
		cout << "List element: " << list.get() << endl;
	}
	
	cout << "\nList Size: " << list.length();
	
	getche();
	return 0;
}
