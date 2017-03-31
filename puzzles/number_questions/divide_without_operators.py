#Divide two integers without using multiplication, division and mod operator.
#
#If it is overflow, return MAX_INT
#

class Solution(object):

    def divide_till_remainder_more_than_divisor(self, dividend, divisor):
        count = 1
        if dividend - divisor >= divisor:
            while divisor < dividend:
                divisor = divisor << 1
                count = count << 1
        return count, divisor

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0
        if divisor == 1:
            return dividend
        count = 1
        orig_divisor = divisor
        orig_divisor2 = divisor
        Negative = False
        if dividend < 0:
            dividend =  -dividend
            Negative = True

        while divisor < dividend:
            divisor = divisor << 1
            count = count << 1

        print("divisor", divisor)
        print("count", count)
        if divisor != dividend:
            divisor = divisor >> 1
            count = count >>  1
            print("divsor after right shift", divisor)
            print("count after right shift", count)
            remainder = dividend - divisor
            print("remainder", remainder)
            remain_count = 0
            while remainder >= orig_divisor:
                print("remainder", remainder)
                #if remainder - orig_divisor >= orig_divisor:
                remain_count, divisor = self.divide_till_remainder_more_than_divisor(remainder,orig_divisor)
                print("After function call remaini_count", remain_count, "divisor", divisor)
                divisor = divisor >> 1
                print("Reduced divisor", divisor)
                if  (remainder - divisor) >= orig_divisor:
                    remain_count = remain_count >> 1
                    print("Reduced remain_count ", remain_count )
                remainder = remainder - divisor
                divisor = orig_divisor2
                count = count + remain_count
                print("count after adding remain_count", count)
        return count

    def divide_slow(self, dividend, divisor):
            """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
            if divisor == 0:
                return 0
            count = 0
            orig_divisor = divisor
            if dividend < 0:
                temp = -dividend
            else:
                temp = dividend
            while temp > 0 and temp >= divisor:
                temp -= divisor
                print("temp=",temp)
                count += 1
            if dividend < 0 and divisor < 0:
                return count
            elif dividend < 0 or divisor < 0:
                return 0-count
            return count


c = Solution()
#print("Answer", c.divide(100000000, 10))
#print("Answer", c.divide(1300000, 2))
print("Answer", c.divide(130299999, 1001))
#print(c.divide(3333333333333333, 1))
#print(c.divide(3333333333333333, 2))
#print(c.divide_slow(3333333333333333, 3))
