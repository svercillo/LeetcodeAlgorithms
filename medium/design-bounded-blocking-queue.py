class BoundedBlockingQueue {


    Semaphore insert_semaphore;
    Semaphore remove_semaphore;
    Semaphore mutex;
    Deque<Integer> queue;

    public BoundedBlockingQueue(int capacity) {
        this.insert_semaphore = new Semaphore(capacity);
        this.remove_semaphore = new Semaphore(capacity);
        
        for (int i =0 ; i<capacity; i++){
            try {
                this.remove_semaphore.acquire();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        this.mutex = new Semaphore(1);
        this.queue = new LinkedList<>();
    }
    
    public void enqueue(int element) throws InterruptedException {
        this.insert_semaphore.acquire();
        
        this.mutex.acquire();
        this.queue.addFirst(element);
        this.mutex.release();

        this.remove_semaphore.release();
    }
    
    public int dequeue() throws InterruptedException {

        this.remove_semaphore.acquire(); 
        
        this.mutex.acquire();
        int res = this.queue.pollLast();
        this.mutex.release();

        this.insert_semaphore.release();

        return res;
    }
    
    public int size() throws InterruptedException {
        this.mutex.acquire();
        int res = this.queue.size();
        this.mutex.release();
        
        return res;
    }
}
