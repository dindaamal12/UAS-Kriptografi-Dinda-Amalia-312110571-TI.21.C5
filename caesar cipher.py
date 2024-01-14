def caesar_cipher(text, shift):
  result = ""
  for char in text:
      if char.isalpha():
          if char.islower():
              shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
          else:
              shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
          result += shifted_char
      else:
          result += char
  return result

def main():
  while True:
      print("Menu:")
      print("1. Kita Lakukan Enkripsi")
      print("2. Kita Lakukan Dekripsi")
      print("3. Keluar")

      choice = input("silahkan Pilih kebutuhan anda (1/2/3): ")

      if choice == '1':
          plaintext = input("Masukkan teks untuk dienkripsi: ")
          shift = int(input("Masukkan jumlah pergeseran (angka bulat): "))
          ciphertext = caesar_cipher(plaintext, shift)
          print("Teks yang dienkripsi:", ciphertext)
      elif choice == '2':
          ciphertext = input("Masukkan teks untuk didekripsi: ")
          shift = int(input("Masukkan jumlah pergeseran (angka bulat): "))
          plaintext = caesar_cipher(ciphertext, -shift)
          print("Teks yang didekripsi:", plaintext)
      elif choice == '3':
          print("Terima kasih!")
          break
      else:
          print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
  main()