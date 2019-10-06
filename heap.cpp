#include <iostream>
#include <cmath>
#include <vector>
#include <random>
using namespace std;

int random(int start, int end)
{
    random_device rd;
    mt19937 eng(rd());
    uniform_int_distribution<> distr(start, end); 
    return distr(eng);
}

class Heap
{
    public:
        static void heapify(vector<int>& v, int i)
        {
            int min = v[i];
            int orig = i;
            auto left = Heap::_leftChildIdx(i);
            auto right = Heap::_rightChildIdx(i);
            if (left < v.size())
            {
                auto leftV = v[left];
                if (leftV < min)
                {
                    min = leftV;
                    i =  left;
                } 
            }
            if (right < v.size())
            {
                auto rightV = v[right];
                if (rightV < min)
                {
                    min = rightV;
                    i =  right;
                } 
            }
            if (orig != i)
            {
                swap(v[orig],v[i]);
                Heap::heapify(v,i);
            }
        }
        static int peek(vector<int>& v)
        {
            if (v.size() == 0) throw "Heap empty cannot peek";
            return v[0];
        }
        static int pop(vector<int>&v)
        {
            if (v.size() == 0) throw "Heap empty cannot pop";
            swap(v[v.size() - 1], v[0]);
            auto ret = v.back();
            v.pop_back();
            Heap::heapify(v, 0);
            return ret;
        }
        static int pushpop(vector<int>& v, int val)
        {
            v.push_back(val);
            swap(v[v.size() - 1], v[0]);
            auto ret = v.back();
            v.pop_back();
            Heap::heapify(v, 0);
            return ret;
        }
        static void push(vector<int>&v, int val)
        {
            v.push_back(val);
            Heap::_siftUp(v, v.size() - 1);
        }
        static void makeMinHeap(vector<int>& v)
        {
            if (v.size() == 0 || v.size() == 1) return;
            int idx = pow(2,((int)floor(log2(v.size())))) - 2;
            for (;idx >= 0; idx--) Heap::heapify(v, idx);
        } 
    private:
        Heap();
        static void _siftUp(vector<int>& v, int i)
        {
            while (Heap::_parentIdx(i) >= 0 && v[Heap::_parentIdx(i)] > v[i])
            {
                swap(v[i], v[Heap::_parentIdx(i)]);
                i = Heap::_parentIdx(i);
            }
        }
        static int _parentIdx(int i)
        {
            if (i % 2 == 0)
                return (int)(((double)i / 2) - 1);
            else
                return i/2;
        }

        static inline int _leftChildIdx(int i)
        {
            return 2*i + 1;
        }

        static inline int _rightChildIdx(int i)
        {
            return 2*i + 2;
        }
};

void heapSort(vector<int>& v)
{
    Heap::makeMinHeap(v);
    vector<int> sorted;
    while (v.size() > 0)
    {
        sorted.push_back(Heap::pop(v));
    }
    v = sorted;
}

void printvec(vector<int> v)
{
    cout << "[";
    for (auto i: v)
    {
       cout << i << ", "; 
    }
    cout << "]\n";
}

int main()
{
    vector<int> rands;
    for (int i = 0; i < 8; ++i)
    {
        rands.push_back(random(0,100));
    }
    cout << "Testing make min heap:\n";
    printvec(rands);
    Heap::makeMinHeap(rands);
    printvec(rands);


    cout << "Testing heapsort:\n";
    rands.clear();
    for (int i = 0; i < 8; ++i)
    {
        rands.push_back(random(0,100));
    }
    printvec(rands);
    heapSort(rands);
    printvec(rands);

    cout << "Testing stuff:\n";
    rands.clear();
    for (int i = 0; i < 8; ++i)
    {
        Heap::push(rands,random(0,100));
    }
    printvec(rands);
    while(rands.size() > 0)
    {
        auto i = Heap::pop(rands);
        cout << i << " ";
    }
    cout << "\n";

    cout << "Testing pushpop:\n";
    for (int i = 0; i < 4; ++i)
    {
        rands.push_back(random(0,10));
    }
    Heap::makeMinHeap(rands);
    while (rands.size() > 0)
    {
        printvec(rands);
        auto randVal = random(0,100);
        cout << "Random val is: " << randVal << "\n";
        cout << "Popped: " << Heap::pushpop(rands, randVal) << "\n";
        printvec(rands);
        cout << "Popped: " << Heap::pop(rands) << "\n";
        printvec(rands);
    }
    return 0;
}