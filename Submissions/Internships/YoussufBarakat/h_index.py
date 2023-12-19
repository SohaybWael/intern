#The h-index is a metric that measures the productivity and impact of a scientist's research.
#Number of Papers: This is the total number of papers a scientist has published.
#Citations: Each paper has a certain number of citations, which represents how many times other researchers have referenced that paper in their work.
#H-index Definition: A scientist has an h-index if they have h papers with at least h citations. The remaining (n - h) papers have no more than h citations each.
#Choosing the Maximum h: If multiple values of h satisfy the conditions, the highest possible h is taken as the h-index.
#In simpler terms, the h-index is a balance between the quantity and impact of a scientist's work. It's a way to measure both the number of papers they've published and how often others cite those papers. The higher the h-index, the more influential and impactful the scientist's body of work is considered to be.


def hIndex(citations):
    n = len(citations)
    h = []
    for i in range(n):
        print(citations[i], n, i + 1, n - i - 1)
        if citations[i] >= n - i - 1:
            h.append( n - i - 1 )
            #break
    print(h)
    return max(h)

print(hIndex([3,0,6,1,5]))
