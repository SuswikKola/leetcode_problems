class Solution {
    public int findMin(int[] a) {
        int l=0,h=a.length-1;
        if(a[l]<a[h])return a[l];
        while(l<h){
            int m=(l+h)/2;
            if(a[m]<a[h])h=m;
            else if(a[m]>a[h])l=m+1;
            else h--;
        }
        return a[h];
    }
}