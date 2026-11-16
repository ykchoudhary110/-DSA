class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1]) # sorting the interval wiht the end time 
        removal=0
        pre_end= intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start<pre_end: # if the current that i start will start befroe our chosen pre_end which is first one then it overlaps and then we need to add remval by one and remove hte ucrent one since we set the pre-end already to best case 
                removal = removal+1
            else:
                pre_end = end
        return removal

        