# Best Time to Buy and Sell Stocks

Use: 2 pointers to track and update buying index and selling index

- Initialize 2 pointers to the first two indexes of the array to track buying and selling index
- Loop over the list and stop when selling index reaches end of list
- Get profit using selling index and buying index value
- If profit is not negative, check if profit is greater than max profit. - If it is, set that to the new max profit
- If the profit is negative, set the buy pointer to the new index. A negative profit indicates that the selling value is a new low in the list (so more profits going ahead)
- Increment the selling index every iteration
- After the loop finishes, return the max profit
