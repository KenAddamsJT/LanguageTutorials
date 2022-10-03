-----------------------------------------------
The C++ Standard Template Library
-----------------------------------------------

1. Algorithms:

// Header file to be included
#include <algorithm>

> a) Sort

// Function syntax
sort(start_add, end_add)

Example:
#include <iostream> 
#include <algorithm> 
  
using namespace std; 
  
void show(int a[]) 
{ 
    for(int i = 0; i < 10; ++i) 
        cout << a[i] << " "; 
} 
  
int main() 
{ 
    int a[10]= {1, 5, 8, 9, 6, 7, 3, 4, 2, 0}; 
    cout << "\n The array before sorting is : "; 
    show(a); 
  
    sort(a, a+10); 
  
    cout << "\n\n The array after sorting is : "; 
    show(a); 
  
    return 0; 
  
} 

//working and theory

Sorting is one of the most basic functions applied to data. It means arranging the data in a particular 
fashion, which can be increasing or decreasing. There is a builtin function in C++ STL by the name of 
sort(). This function internally uses IntroSort. In more details it is implemented using hybrid of 
QuickSort, HeapSort and InsertionSort.By default, it uses QuickSort but if QuickSort is doing unfair 
partitioning and taking more than N*logN time, it switches to HeapSort and when the array size becomes 
really small, it switches to InsertionSort.

> b) Binary Search

// function syntax
binary_search(startaddress, endaddress, valuetofind)

Example:
#include <algorithm> 
#include <iostream> 
  
using namespace std; 
  
void show(int a[], int arraysize) 
{ 
    for (int i = 0; i < arraysize; ++i) 
        cout << a[i] << " "; 
} 
  
int main() 
{ 
    int a[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 }; 
    int asize = sizeof(a) / sizeof(a[0]); 
    cout << "\n The array is : "; 
    show(a, asize); 
  
    cout << "\n\nLet's say we want to search for 2 in the array"; 
    cout << "\n So, we first sort the array"; 
    sort(a, a + asize); 
    cout << "\n\n The array after sorting is : "; 
    show(a, asize); 
    cout << "\n\nNow, we do the binary search"; 
    if (binary_search(a, a + 10, 2)) 
        cout << "\nElement found in the array"; 
    else
        cout << "\nElement not found in the array"; 
  
    cout << "\n\nNow, say we want to search for 10"; 
    if (binary_search(a, a + 10, 10)) 
        cout << "\nElement found in the array"; 
    else
        cout << "\nElement not found in the array"; 
  
    return 0; 
}

> c) Reverse
//function syntax
//for vectors
reverse(first_iterator, last_iterator)

> d) Maximum Element
//function syntax
*max_element(first_iterator, last_iterator)

> e) Minimum Element
//function syntax
*min_element(first_iterator, last_iterator)

> f) Accumulate
//header file
#include <numeric>
//function syntax
accumulate(first_iterator, last_iterator, initial value of sum)

Example:
#include <algorithm> 
#include <iostream> 
#include <vector> 
#include <numeric> //For accumulate operation 
using namespace std; 
  
int main() 
{ 
    // Initializing vector with array values 
    int arr[] = {10, 20, 5, 23 ,42 , 15}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    vector<int> vect(arr, arr+n); 
  
    cout << "Vector is: "; 
    for (int i=0; i<n; i++) 
        cout << vect[i] << " "; 
  
    // Sorting the Vector in Ascending order 
    sort(vect.begin(), vect.end()); 
  
    cout << "\nVector after sorting is: "; 
    for (int i=0; i<n; i++) 
       cout << vect[i] << " "; 
  
    // Reversing the Vector 
    reverse(vect.begin(), vect.end()); 
  
    cout << "\nVector after reversing is: "; 
    for (int i=0; i<6; i++) 
        cout << vect[i] << " "; 
  
    cout << "\nMaximum element of vector is: "; 
    cout << *max_element(vect.begin(), vect.end()); 
  
    cout << "\nMinimum element of vector is: "; 
    cout << *min_element(vect.begin(), vect.end()); 
  
    // Starting the summation from 0 
    cout << "\nThe summation of vector elements is: "; 
    cout << accumulate(vect.begin(), vect.end(), 0); 
  
    return 0; 
} 

> g) Count
//function syntax
count(first_iterator, last_iterator,x) 

> h) find
//function syntax
find(first_iterator, last_iterator, x)

Example:
#include <algorithm> 
#include <iostream> 
#include <vector> 
using namespace std; 
  
int main() 
{ 
    // Initializing vector with array values 
    int arr[] = {10, 20, 5, 23 ,42, 20, 15}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    vector<int> vect(arr, arr+n); 
  
    cout << "Occurrences of 20 in vector : "; 
  
    // Counts the occurrences of 20 from 1st to 
    // last element 
    cout << count(vect.begin(), vect.end(), 20); 
  
    // find() returns iterator to last address if 
    // element not present 
    find(vect.begin(), vect.end(),5) != vect.end()? 
                         cout << "\nElement found": 
                     cout << "\nElement not found"; 
  
    return 0; 
}

> i) erase
//function syntax
arr.erase(position to be deleted)

> j) Remove duplicate occurences
//function syntax
arr.erase(unique(arr.begin(),arr.end()),arr.end()) 

Example:
#include <algorithm> 
#include <iostream> 
#include <vector> 
using namespace std; 
  
int main() 
{ 
    // Initializing vector with array values 
    int arr[] = {5, 10, 15, 20, 20, 23, 42, 45}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    vector<int> vect(arr, arr+n); 
  
    cout << "Vector is :"; 
    for (int i=0; i<6; i++) 
        cout << vect[i]<<" "; 
  
    // Delete second element of vector 
    vect.erase(vect.begin()+1); 
  
    cout << "\nVector after erasing the element: "; 
    for (int i=0; i<5; i++) 
        cout << vect[i] << " "; 
  
    // sorting to enable use of unique() 
    sort(vect.begin(), vect.end()); 
  
    cout << "\nVector before removing duplicate "
             " occurrences: "; 
    for (int i=0; i<5; i++) 
        cout << vect[i] << " "; 
  
    // Deletes the duplicate occurrences 
    vect.erase(unique(vect.begin(),vect.end()),vect.end()); 
  
    cout << "\nVector after deleting duplicates: "; 
    for (int i=0; i< vect.size(); i++) 
        cout << vect[i] << " "; 
  
    return 0; 
}

> k) index of an Element
//function syntax
distance(first_iterator,desired_position)
arr.erase(position to be deleted)

Example:
#include <algorithm> 
#include <iostream> 
#include <vector> 
using namespace std; 
  
int main() 
{ 
    // Initializing vector with array values 
    int arr[] = {5, 10, 15, 20, 20, 23, 42, 45}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    vector<int> vect(arr, arr+n); 
  
    // Return distance of first to maximum element 
    cout << "Distance between first to max element: ";  
    cout << distance(vect.begin(), 
                     max_element(vect.begin(), vect.end())); 
    return 0; 
} 