#include <iostream>
#include <string>
using namespace std;

bool belongs = true;
string word = "abacaba";
int i = 0;

void A();
void B();

int main() {
	if (word != "") {
		if (word[i] == 'a') A();
		else if (word[i] == 'b' || word[i] == 'c') B();
		else belongs = false;
		if (i != word.size()) belongs = false;
	}
	else belongs = false;
	if (belongs) cout << "Pertenece" << endl;
	else cout << "No Pertenece" << endl;
	return 0;
}

void A(){
	if (word.size() - i < 3) {
		belongs = false;
		return;
	}
	// A -> a B a
	if (word[i] == 'a') i++;
	else {
		belongs = false;
		return;
	}
	B();
	if (word[i] == 'a') i++;
	else {
		belongs = false;
		return;
	}
}

void B(){
	// B -> c
	if (word[i] == 'c') {
		i++;
		return;
	}
	if (word.size() - i < 3) {
		belongs = false;
		return;
	}
	// B -> b A b
	if (word[i] == 'b') i++;
	else {
		belongs = false;
		return;
	}
	A();
	if (word[i] == 'b') i++;
	else {
		belongs = false;
		return;
	}
}