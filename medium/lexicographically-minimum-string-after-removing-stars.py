class Solution {
    public String clearStars(String s) {
        Set<Integer> to_remove = new HashSet<>();
        TreeMap<Character, LinkedList<Integer>> stack = new TreeMap<>();

        for (int i =0; i < s.length(); i++){ 
            if (s.charAt(i) == '*'){
                char c = stack.firstKey();
                LinkedList<Integer> indexes = stack.get(c);
                to_remove.add(indexes.pollLast());
                to_remove.add(i);
        
                if (indexes.size() == 0){
                    stack.remove(c);
                }
            } else {
                char c = s.charAt(i);
                if (!stack.containsKey(c)){
                    stack.put(c, new LinkedList<Integer>());
                }
                stack.get(c).add(i);
            }
        }

        StringBuilder str = new StringBuilder();
        for (int i = s.length()- 1; i >= 0; i--){ 
            if (!to_remove.contains(i))
                str.append(s.charAt(i));
        }

        str.reverse();
        return str.toString();
    }
    public void print(Object obj){ 
        System.out.println(obj);
        return;
    }
}
