import cProfile
from zip_example import with_generators, process

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    result1 = with_generators()
    for value in result1:
        process(value)

    profiler.disable()
    profiler.print_stats()





"""
(venv) [11:59:16]mkoshel@Mkoshel-lws ~/BACKUPSFROMMINT/home/mkoshel/dev/script006.git/src/script006/iterators [master]$ /usr/bin/time -v python zip_example_with_generators.py 
         100000003 function calls in 12.746 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 zip_example.py:12(with_generators)
 50000001   10.003    0.000   10.003    0.000 zip_example.py:14(<genexpr>)
 50000000    2.743    0.000    2.743    0.000 zip_example.py:20(process)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


        Command being timed: "python zip_example_with_generators.py"
        User time (seconds): 24.91
        System time (seconds): 0.09
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:25.03
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 9792
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 1163
        Voluntary context switches: 1
        Involuntary context switches: 1040
        Swaps: 0
        File system inputs: 0
        File system outputs: 8
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""