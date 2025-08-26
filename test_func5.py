def main():
    import subprocess
    import psutil
    import time
    import threading
    import os

    # Sample workload: compute primes up to N
    def compute_primes(n):
        primes = []
        for i in range(2, n):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes

    # Measure traits
    start_time = time.time()
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss // 1024
    cpu_before = process.cpu_times().user

    # Run workload
    N = 10000
    primes = compute_primes(N)

    exec_time = (time.time() - start_time) * 1000  # ms
    mem_after = process.memory_info().rss // 1024
    cpu_after = process.cpu_times().user
    memory_used = mem_after - mem_before
    cpu_used = cpu_after - cpu_before
    reliability = 1 if len(primes) > 0 else 0
    thread_count = threading.active_count()
    uptime = time.time() - start_time
    error_count = 0
    success_rate = 1.0
    latency = exec_time / N
    peak_memory = mem_after

    traits = {
        'Speed': exec_time,
        'Memory': memory_used,
        'Reliability': reliability,
        'CPU_Usage': cpu_used,
        'Disk_IO': 0,
        'Network_Usage': 0,
        'Error_Count': error_count,
        'Uptime': uptime,
        'Thread_Count': thread_count,
        'Peak_Memory': peak_memory,
        'Success_Rate': success_rate,
        'Latency': latency,
    }

    args = [f'{k}={v}' for k, v in traits.items()]
    # Build command to run in new PowerShell window and keep it open
    cmd = f'python math_art_display.py {' '.join(args)}; pause'
    powershell_cmd = [
        'powershell', '-NoExit', '-Command', cmd
    ]
    subprocess.Popen(powershell_cmd)

if __name__ == "__main__":
    main()
