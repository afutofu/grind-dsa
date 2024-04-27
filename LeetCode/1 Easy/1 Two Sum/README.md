# Two Sum

DS: Map/Dictionary

- Iterate over nums array and store key value pairs of elements and their indices
- Iterate over nums again and this time find the complement of the value at the time of the loop. complement = target - nums[i]
- Check if the complement exists in the map and it is not the same index as the current index of the loop. If complement in numMap and numMap[i] != currentIdx
- If it exists, return [complement, numMap[i]]
- If not, return []
