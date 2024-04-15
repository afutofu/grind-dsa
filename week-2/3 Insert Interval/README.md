# Insert Interval

Use: left and right of sorted list

- Understand that we can segregate the problem by dividing the new interval list into three parts: the left of the new interval, the new interval, and the right of the new interval
- To get the intervals to the left of the new interval, we simply need to compare whether the end of the interval is lesser than the start of the new interval
- To get the interval to the right of the new interval, we compare the start of the interval being greater than the end of the new interval
- To get the new interval, we make sure the above two cases are false and set the start of the new interval = the min of the start of the new interval or the start of the current interval, and the same with the end of the new interval.
- Finally return the left, the new interval, and the right lists
