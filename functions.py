class Functions:
    def getIndexs(self, content, value):
        result = []
        valueIndex = 0
        for i in content:
            if i in value:
                result.append(valueIndex)
            valueIndex+=1
        return result

