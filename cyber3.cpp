#include<bits/stdc++.h>
using namespace std;
int main()
{ int a,b,c=0;
 cin>>a>>b;
 cout<<"prime no are"<<endl;
 for(int i=a;i<=b;i++)
 { c=0;
 for(int j=2;j<=i;j++)
     { if(i%j==0)
           { c++;
           }
     }
 	if(c<2)
 	     { cout<<i<<endl;
	     }
 	
  }
return 0;	
}
