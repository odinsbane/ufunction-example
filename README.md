# ufunction-example
A Short ufunction example for numpy. With numba example for comparison.

Create an environment and install eg. go to the source directory and:  
 
    pip install -r requirements.txt .

Note that an acceptable version of llvm also needs to be installed. I had to got through the 
numba release notes to find compatible versions of python-llvm and numba.

For just numpy:

    python -m package.check
    
for ufunc example:

    python -m package.ufun_check
    
Likewise, for the numba example:

    python -m package.numba_check
    
I use `time` to time the processes, and the output has been reported on [my blog](https://orangepalantir.org/topicspace/show_110.html)
