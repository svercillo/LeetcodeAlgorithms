class Solution {
    public int minAbsoluteDifference(List<Integer> nums, int x) {
        TreeSet<Integer> btree = new TreeSet<Integer>();

        int min_dist = Integer.MAX_VALUE;
        for (int i = 0; i < nums.size(); i ++){
            
            if (i >= x){
                int next = nums.get(i-x);
                btree.add(next);
                Integer ceil = btree.ceiling(nums.get(i)); 
                Integer floor = btree.floor(nums.get(i));

                if (ceil == null){ 
                    ceil = Integer.MAX_VALUE;
                }

                if (floor == null){
                    floor = Integer.MIN_VALUE;
                }

                min_dist = Collections.min(List.of(min_dist, Math.abs(nums.get(i) - ceil), Math.abs(nums.get(i) - floor)));

                // System.out.println("" + nums.get(i) +  " " + next + " " +  ceil + " "  +floor);
                // System.out.println(btree);
            } 
        }

        return min_dist;
    }
}
