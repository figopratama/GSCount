# Metode AND
# def soal5_metode1(n):
#     return "Genap" if (n & 1) == 0 else "Ganjil"

# number = int(input("Masukkan angka: "))
# print(f"Angka {number} adalah {soal5_metode1(number)}")

# # Metode perkalian dan pembagian
# def soal5_metode2(n):
#     return "Genap" if (n // 2) * 2 == n else "Ganjil"
# number = int(input("Masukkan angka: "))
# print(f"Angka {number} adalah {soal5_metode2(number)}")

# # Metode Kurang dari 1
# def soal5_metode3(n):
#     return "Genap" if (n >> 1) << 1 == n else "Ganjil"
# number = int(input("Masukkan angka: "))
# print(f"Angka {number} adalah {soal5_metode3(number)}")

# # Metode looping
# def soal5_metode4(n):
#     while n > 1:
#         n -= 2
#     return "Genap" if n == 0 else "Ganjil"
# number = int(input("Masukkan angka: "))
# print(f"Angka {number} adalah {soal5_metode4(number)}")




# def soal6_metode1(n):
#     return "Genap" if (n & 1) == 0 else "Ganjil"
# print(soal6_metode1(5))

# def soal6_metode2(n):
#     return "Genap" if (n // 2) * 2 == n else "Ganjil"
# print(soal6_metode2(5)) 

# def soal6_metode3(n):
#     return "Genap" if (n >> 1) << 1 == n else "Ganjil"
# print(soal6_metode3(5))

# def soal6_metode4(n):
#     while n > 1:
#         n -= 2
#     return "Genap" if n == 0 else "Ganjil"
# print(soal6_metode4(5))



# def rekursif(awal, akhir):
#     if awal > akhir:
#         return 0
#     if awal % 2 == 0:
#         return awal + rekursif(awal + 1, akhir)
#     else:
#         return rekursif(awal + 1, akhir)

# # Example usage
# awal = 2
# akhir = 7
# hasil = rekursif(awal, akhir)
# print(f"Input angka awal = {awal}")
# print(f"Input angka akhir = {akhir}")
# print(f"Output = {hasil}")

# output deret angka 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))

    




