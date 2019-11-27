# 计算Bit1的个数？？？
# 编写一个函数，该函数采用无符号整数并返回其具有的“ 1”位数（也称为汉明权重）。
# 范例1： 输入： 00000000000000000000000000001010
# 输出： 3
# 说明：输入二进制字符串00000000000000000000000000001011
def Solution(object):
    def hammingWeight(self, n):

        count = 0  # 定义count存储1的个数
        while n:  # 当n部位0时持续循环
            n = n & (n - 1)  # 执行一次相与，count技术加一
            count += 1
        return count