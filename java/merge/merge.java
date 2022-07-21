
// Work backwards since we know the arrays are sorted
//

class Solution2 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
    int p1 = m-1 , p2 = n-1 ,i = m+n-1;
        while(p2 >=0 ){
            if(p1 >=0 && nums1[p1] > nums2[p2]){
                nums1[i--] = nums1[p1--];
            } 
            else{
                nums1[i--] = nums2[p2--];
            }
        }
    }

    }
}

class Solution1 {
    
    public void merge(int[] nums1, int m, int[] nums2, int n) {
         if (n == 0) {
            return; 
        }
        
        if (m == 0) {
            for(int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
            return;
        }
       
        int i = 0;
        int j = 0;
        int [] merge = new int[nums1.length];
        
        for (int k = 0; k < nums1.length; k++) {
            if (j == n) {
                while (i < m) {
                    merge[k++] = nums1[i++];
                 }
                break;
            }
            if (i == m || nums1[i] > nums2[j]) {
                merge[k] = nums2[j++];
            }
            else if (nums1[i] < nums2[j]) {
                merge[k] = nums1[i++];
            }
            else {
                merge[k] = nums1[i++];
                merge[k+1] = nums2[j++];
                k++;
            }
        }
        
        for (int k = 0; k < nums1.length; k++) {
            nums1[k] = merge[k];
        }
    }
}

class Solution3 {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            for (int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
            return;
        }
        if (n == 0) {
            return;
        }

        int end_idx = nums1.length - 1;
        int i = m - 1;
        int j = n - 1;

        for (int k = end_idx; k >= 0; k--) {

            if (i < 0) {
                nums1[k] = nums2[j--];
                continue;
            }

            if (j < 0) {
                nums1[k] = nums1[i--];
                continue;
            }

            if (nums1[i] >= nums2[j]) {
                nums1[k] = nums1[i--];
            }
            else {
                nums1[k] = nums2[j--];
            }
        }
    }
}

