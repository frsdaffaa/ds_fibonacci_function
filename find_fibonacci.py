def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    FibSeries = [0,1]
    for n in range(2,100): 
        new_series = FibSeries[n-1] + FibSeries[n-2]
        FibSeries.append(new_series)
    if x in FibSeries:
        return True
    else:
        return False   

if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
