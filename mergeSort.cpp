#include <iostream>

using namespace std;

void printing(int a[]){
    for(int i=0;i<6;i++){
        cout<<a[i]<<" ";
    }
}

void merge(int a[],int si,int mid,int ei){
    int *la=new int[mid-si+1];
    int *ua=new int[ei-mid];
    for(int i=0;i<mid-si+1;i++){
        la[i]=a[si+i];
    }
    for(int i=0;i<=ei-mid;i++){
        ua[i]=a[mid+1+i];
    }
    int j=mid-si+1,k=ei-mid,i1=0,i2=0,me=si;
    while(i1<j and i2<k){
        if(la[i1]<=ua[i2]){
            a[me]=la[i1];
            i1++;
        }
        else{
            a[me]=ua[i2];
            i2++;
        }
        me++;
    }
    while(i1<j){
        a[me]=la[i1];
        i1++;
        me++;
    }
    while(i2<k){
        a[me]=ua[i2];
        me++;
        i2++;
    }
}

void mergeSort(int a[],int si,int ei){
    if(si>=ei)
    return;
    int mid=(si+ei)/2;
    mergeSort(a,si,mid);
    mergeSort(a,mid+1,ei);
    merge(a,si,mid,ei);
}
int main()
{
    int arr[]={2,8,4,9,12,5};
    mergeSort(arr,0,5);
    printing(arr);
    return 0;
}
