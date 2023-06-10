class H2O {
    Semaphore hydro = new Semaphore(2);
    Semaphore oxy = new Semaphore(1);



    Semaphore oxy_start = new Semaphore(1);
    Semaphore oxy_ready = new Semaphore(1);
    Semaphore second_h_signal = new Semaphore(1);


    Semaphore hydro_released = new Semaphore(1);

    Integer num_h = new Integer(0);
    public H2O() {
        try{ 
            second_h_signal.acquire();
            oxy.acquire();
            oxy_ready.acquire();
            oxy_start.acquire();
            hydro_released.acquire();
        } catch (Exception ex){
        }

    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hydro.acquire();
            boolean first = false;
            synchronized(num_h){
                if (num_h == 0){
                    first = true;
                }
                num_h += 1;
            }

            
            
            if (first){
                second_h_signal.acquire(); // if first, wait for second H
                
                oxy_start.release(); // after both H's have arrived, signal oxygen that hydrogens are ready
                oxy_ready.acquire();

                // release 2 hydrogens
                releaseHydrogen.run();
                releaseHydrogen.run();

                synchronized(num_h){
                    num_h = 0; // reset hydrogen counter
                }
        
                hydro_released.release(); // signal to other hyd thread that it can exit safely 
            } else {
                second_h_signal.release(); // signal first thread

                hydro_released.acquire(); // wait for all the hydrogen to be released
            }
        hydro.release();

    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxy_start.acquire(); // wait for both hydrogens to be done
        oxy_ready.release(); // signal that oxygen is ready to send
        
        releaseOxygen.run();
    }
}
