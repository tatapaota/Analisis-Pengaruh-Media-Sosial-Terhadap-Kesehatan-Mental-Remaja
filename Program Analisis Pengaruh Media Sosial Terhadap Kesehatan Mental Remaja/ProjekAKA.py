import sys
import time
import matplotlib.pyplot as plt

# Menambah batas rekursi
sys.setrecursionlimit(10000)

# Fungsi iteratif untuk menghitung rata-rata waktu yang dihabiskan dan rata-rata skor kesehatan mental
def average_iterative(data):
    total_time = 0
    total_health = 0
    for time_spent, health_score in data:
        total_time += time_spent
        total_health += health_score
    return total_time / len(data), total_health / len(data)

# Fungsi rekursif untuk menghitung rata-rata waktu yang dihabiskan dan rata-rata skor kesehatan mental
def average_recursive(data, n):
    if n == 1:
        return data[0][0], data[0][1] 
    prev_time, prev_health = average_recursive(data, n - 1)
    current_time, current_health = data[n - 1]
    return (prev_time * (n - 1) + current_time) / n, (prev_health * (n - 1) + current_health) / n

# Fungsi untuk menerima input data dari pengguna
def get_input_data():
    data = []
    print("Masukkan data dalam format waktu_spend (jam) dan skor_health (0-100).")
    
    while True:
        try:
            input_data = input("Masukkan data (waktu_spend, skor_health) atau ketik 'done' untuk selesai: ")
            if input_data.lower() == 'done':
                break
            time_spent, health_score = map(int, input_data.split(','))
            data.append((time_spent, health_score))
        except ValueError:
            print("Format input salah. Pastikan memasukkan data dalam format waktu_spend, skor_health (misalnya 2, 80).")
    return data

# Fungsi utama
def main():
    data = get_input_data()

    if len(data) == 0:
        print("Tidak ada data yang dimasukkan. Program dihentikan.")
        return

    # Menghitung rata-rata menggunakan fungsi iteratif
    start = time.time()
    iterative_avg_time, iterative_avg_health = average_iterative(data)
    iter_time = time.time() - start
    print(f"\nHasil Iteratif: Rata-rata Waktu = {iterative_avg_time}, Rata-rata Skor Kesehatan = {iterative_avg_health}")

    # Menghitung rata-rata menggunakan fungsi rekursif
    start = time.time()
    recursive_avg_time, recursive_avg_health = average_recursive(data, len(data))
    recur_time = time.time() - start
    print(f"Hasil Rekursif: Rata-rata Waktu = {recursive_avg_time}, Rata-rata Skor Kesehatan = {recursive_avg_health}")

    print("\nMenampilkan grafik running time...")
    input_sizes = [len(data), len(data) * 2, len(data) * 5]
    iterative_times = []
    recursive_times = []

    for size in input_sizes:
        dummy_data = [(i % 24, (i % 100) + 1) for i in range(1, size + 1)]
        
        # Waktu iteratif
        start = time.time()
        average_iterative(dummy_data)
        end = time.time()
        iterative_times.append(end - start)

        # Waktu rekursif
        if size <= 1000:
            start = time.time()
            average_recursive(dummy_data, len(dummy_data))
            end = time.time()
            recursive_times.append(end - start)
        else:
            recursive_times.append(None)  

    valid_recursive_sizes = [size for size, time in zip(input_sizes, recursive_times) if time is not None]
    valid_recursive_times = [time for time in recursive_times if time is not None]

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, iterative_times, label="Iteratif (Waktu Media Sosial)", marker='o', color='blue')
    if valid_recursive_sizes:
        plt.plot(valid_recursive_sizes, valid_recursive_times, label="Rekursif (Skor Kesehatan Mental)", marker='s', color='red')
    plt.title("Perbandingan Running Time Algoritma Iteratif dan Rekursif Pengaruh Media Sosial Terhadap Kesehatan Mental Remaja")
    plt.xlabel("Ukuran data yang diinput")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

   
    print("\nAnalisis Kompleksitas dan Performa Berdasarkan Data:")

    # Analisis ukuran data
    if len(data) <= 100:
        print("- Ukuran data kecil (<= 100), baik iteratif maupun rekursif sangat efisien.")
    elif 100 < len(data) <= 1000:
        print("- Ukuran data sedang (101-1000), iteratif lebih stabil, tetapi rekursif masih dapat digunakan.")
    else:
        print("- Ukuran data besar (> 1000), rekursif dapat gagal karena batas stack memori, disarankan menggunakan iteratif.")

    # Analisis waktu eksekusi
    if iter_time < recur_time:
        print(f"- Dari waktu eksekusi: Iteratif lebih cepat ({iter_time:.6f} detik) dibandingkan rekursif ({recur_time:.6f} detik).")
    elif recur_time < iter_time:
        print(f"- Dari waktu eksekusi: Rekursif lebih cepat ({recur_time:.6f} detik) dibandingkan iteratif ({iter_time:.6f} detik).")
    else:
        print("- Dari waktu eksekusi: Iteratif dan rekursif memiliki waktu yang hampir sama.")

  # Kompleksitas berdasarkan hasil
    if len(data) > 1000:
        print("- Kompleksitas: Iteratif O(n) karena setiap elemen dalam data diakses satu per satu menggunakan perulangan.")
        print("- Kompleksitas: Rekursif O(n) karena setiap pemanggilan fungsi rekursif memproses satu elemen data hingga seluruh elemen selesai diproses. Namun, pada data besar, terdapat risiko stack overflow karena jumlah pemanggilan fungsi yang berlapis-lapis.")
    else:
        print("- Kompleksitas: Iteratif O(n) karena setiap elemen dalam data diakses satu per satu menggunakan perulangan.")
        print("- Kompleksitas: Rekursif O(n) karena setiap pemanggilan fungsi rekursif memproses satu elemen data hingga seluruh elemen selesai diproses. Pada ukuran data ini, baik iteratif maupun rekursif tetap dapat diandalkan.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
