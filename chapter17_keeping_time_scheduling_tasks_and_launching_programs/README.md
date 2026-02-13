# Chapter 17 – Working with Time, Threads, and Processes ⏱️🧵⚙️

## Topics Covered
- Pausing execution with the time module (`sleep()`)
- Measuring and formatting time values  
- Working with dates and times using the datetime module  
- Creating threads with the threading module  
- Running functions in parallel using threads  
- Understanding the difference between threads and processes  
- Launching external programs with the subprocess module  
- Monitoring processes using `poll()` and `wait()`  
- Passing command-line arguments to external programs  
- Opening files and applications from Python  

## Goal
Automate tasks that depend on time, scheduling, or parallel execution.  
This includes creating timers, running background tasks, launching other programs, and coordinating multiple operations at once.

## Notes
Time control and concurrency are fundamental in real-world automation.  
Scripts often need to wait, schedule actions, or perform several tasks simultaneously.  
Threads allow multiple operations inside the same program, while subprocesses allow launching completely separate programs that run independently.

## Projects

stopwatch.py (a simple stopwatch program with aligned output)

cheduled_web_comic_downloader.py (periodically checks XKCD and downloads any new comics)