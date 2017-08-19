#include <iostream>
using namespace std;

class array{

	int a[100],i,n,data,index_no,no;

public:

	void arrinpt(){
		cout<<"Enter Number Of Elements You Want To Enter : ";
		cin>>n;
		for(i=0;i<n;i++)
		{
			cout<<"a["<<i<<"] : ";
			cin>>data;
			a[i]=data;

		}
	}

	void arrdsply(){
		for(i=0;i<n;i++){
			cout<<a[i]<<"\t";
		}
		cout<<endl;
	}

	void addarr(){
		cout<<"How Many Elements Do You Want To Enter : ";
		cin>>no;
		cout<<"Enter The Index Number Where You Want To Start Adding The New Data From : ";
		cin>>index_no;
		
		for(i=n;i>=index_no;i--){
			a[i+no]=a[i];
		}
		for(i=index_no;i<index_no+no;i++){
			cout<<"Enter The New Data You Want To Enter At The a["<<i<<"]'th Position : ";
			cin>>data;
			a[i]=data;
		}
		n=n+no;
	}

	void dltearr(){
		cout<<"Enter The Index Number That You Want To Delete The Entry For : ";
		cin>>index_no;
		for(i=index_no;i<n;i++){
			a[i]=a[i+1];
		}
		n--;
	}

};

int main(){
	array arr;
	int c;

	do{

		cout<<"==============================MENU==============================\n1. input\t2. display\t3. add\t4. delete\t5. exit\nEnter Your Choice : ";
		cin>>c;


		switch(c){
			case 1: arr.arrinpt();
					break;

			case 2: arr.arrdsply();
					break;

			case 3: arr.addarr();
					break;

			case 4: arr.dltearr();
					break;
		}
	}while(c!=5);

	return 0;
}