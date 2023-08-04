class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        result = 0

        boxTypes = sorted(boxTypes,key=lambda x:x[1],reverse = True)
        print(boxTypes)

        for box_type in boxTypes:
            boxes = min (truckSize, box_type[0])
            print(boxes)
            result += (boxes*box_type[1])
            truckSize -= box_type[0]
            if truckSize <= 0:
                break
        return result