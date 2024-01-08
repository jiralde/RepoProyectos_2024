//
//
//
//
#include<iostream>
using namespace std;

class cordenada{
	private:
		int x,y,z;
	public:
		cordenada();
		void setPunto(int,int);
		int getPuntoX();
		int getPuntoY();
		int getPuntoZ();
}

void cordenada::setPunto(int _x, int _y, int _z){
	x = _x;
	z = _z;
	y = _y;
}

int cordenada::getPuntoX(){
	return x;
}
int cordenada::getPuntoZ(){
	return z;
}
int cordenada::getPuntoY(){
	return y;
}

int main(){
	
	cout << "hola Mundo" << "\n";
}


