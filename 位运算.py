class Solution:
    def add(self, a: int, b: int) -> int:
        return sum([a, b])
"""
此为python函数sum()， python对于无符号整型数处理较为复杂，
两数相加可以运用位运算实现。下为cpp代码
class Solution {
public:
    int add(int a, int b) {
        int sum = 0, carry = 0;
        while (b)
        {
            sum = a ^ b;
            carry = ((unsigned int)a & b) << 1;
            a = sum;
            b = carry;
    }
    return a;

    }
};
"""