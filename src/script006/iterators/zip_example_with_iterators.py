import cProfile
from zip_example import with_iterators, process

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    result1 = with_iterators()
    for value in result1:
        process(value)

    profiler.disable()
    profiler.print_stats()



"""
/usr/bin/time -v python zip_example_with_iterators.py 
         100000003 function calls in 7.149 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 50000000    2.675    0.000    2.675    0.000 zip_example.py:20(process)
 50000001    4.474    0.000    4.474    0.000 zip_example.py:3(with_iterators)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


        Command being timed: "python zip_example_with_iterators.py"
        User time (seconds): 19.11
        System time (seconds): 0.00
        Percent of CPU this job got: 100%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:19.12
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 9648
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 1111
        Voluntary context switches: 1
        Involuntary context switches: 15
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

"""

